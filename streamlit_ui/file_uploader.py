from typing import Optional

import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile


def get_uploaded_file() -> Optional[UploadedFile]:
    """
    Get the uploaded file from the user.
    """

    uploaded_file = st.file_uploader(
        "Upload a pdf, docx, or txt file",
        type=["pdf", "docx", "txt"],
        help="Scanned documents are not supported yet!",
    )

    return uploaded_file
