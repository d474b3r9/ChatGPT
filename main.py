import pdfplumber
# import numpy as np
from functions import getPaper, showPaperSummary

paper_url = "https://what_you_want"


def resume_pdf(paper_url):
    local_pdf = getPaper(paper_url)
    paperContent = pdfplumber.open(local_pdf).pages
    results = showPaperSummary(paperContent)

    return results
