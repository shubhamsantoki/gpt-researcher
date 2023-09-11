import base64
import streamlit as st

from io import BytesIO
from reportlab.pdfgen import canvas

def streamlit_sidebar():
    with st.sidebar:
  
        st.sidebar.image("img/simform-logo.png")
        st.markdown("### FriendGPT")
        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "This tool is a work in progress. "
            "it may take a while to generate the answer as we are scraping the internet for searching answer"
        )
        st.markdown("---")

def set_streamlit_ui():
    st.set_page_config(page_title="FriendGPT Researcher", page_icon="🔍")
    streamlit_sidebar()
    st.header("`Web Intelligence, Answered in Simplicity`")
    st.info(
        "`Explore, extract, and explain with confidence. Experience the future of web research with FriendGPT. Start your journey today!`"
    )



def create_downloadable_pdf(content, filename):
    pdf_data = BytesIO()
    # Create a PDF document
    c = canvas.Canvas(pdf_data)
    # Add content to the PDF 
    c.drawString(100, 750, content)
    c.save()
    pdf_data.seek(0)
    # Encode the PDF data as base64
    b64 = base64.b64encode(pdf_data.getvalue()).decode()
    # Generate the download link
    href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}.pdf">Download {filename}.pdf</a>'
    return href