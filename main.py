import streamlit as st
import pyperclip

from dotenv import load_dotenv
from langchain.chains import RetrievalQAWithSourcesChain

from src.settings import settings
from src.callbacks import PrintRetrievalHandler, StreamHandler
from src.utils import create_downloadable_pdf, set_streamlit_ui


# Load variables from .env file
load_dotenv()

#set the streamlit ui
set_streamlit_ui()


# Make retriever and llm
if "retriever" not in st.session_state:
    st.session_state["retriever"], st.session_state["llm"],st.session_state["memory"] = settings()

web_retriever = st.session_state.retriever
llm = st.session_state.llm
memory = st.session_state.memory

# User input
question = st.text_input("`Ask a question:`")

if question:

    # Generate answer
    import logging

    logging.basicConfig()
    logging.getLogger("langchain.retrievers.web_research").setLevel(logging.INFO)

    qa_chain = RetrievalQAWithSourcesChain.from_chain_type(llm, retriever=web_retriever, memory= memory)

    # Write answer and sources
    retrieval_streamer_cb = PrintRetrievalHandler(st.container())
    answer = st.empty()
    stream_handler = StreamHandler(answer, initial_text="`Answer:`\n\n")
    result = qa_chain(
        {"question": question}, callbacks=[retrieval_streamer_cb, stream_handler]
    )
    answer.info("`Answer:`\n\n" + result["answer"])
    st.info("`Sources:`\n\n" + result["sources"])

    complete_answer = result["answer"] + "\n" + result["sources"]

    # Copy to Clipboard button
    if st.button("Copy Answer to Clipboard"):
        pyperclip.copy(complete_answer)
        st.success("Answer copied to clipboard!")

    # Download as PDF button
    if st.button("Download Answer as PDF"):
        pdf_link = create_downloadable_pdf(complete_answer, "answer.pdf")
        st.markdown(pdf_link, unsafe_allow_html=True)
