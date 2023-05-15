import argparse
import logging
import os
import sys
import tempfile
import time
import io
from typing import List

from pdfminer.high_level import extract_text
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager

def extract_pdf_text(file_path: str, password: str = None, maxpages: int = 0) -> str:
    with open(file_path, "rb") as f:
        parser = PDFParser(f)
        document = PDFResourceManager()
        out = io.StringIO()
        params = LAParams()
        device = TextConverter(document, out, laparams=params)
        interpreter = PDFPageInterpreter(document, device)
        extracted_text = ""

        for page in PDFPage.get_pages(f, maxpages=maxpages, password=password, caching=True, check_extractable=True):
            interpreter.process_page(page)
            layout = out.getvalue()

            extracted_text += layout
            out.seek(0)
            out.truncate(0)

        out.close()

    return extracted_text.strip()


def main(argv: List[str]) -> int:


    parser = argparse.ArgumentParser(description="Extract text from a PDF file.")
    parser.add_argument("file_path", metavar="FILE", help="the path to the PDF file to extract text from")
    parser.add_argument("-p", "--password", metavar="PASSWORD", help="the password to use if the PDF file is password-protected")
    parser.add_argument("-m", "--maxpages", metavar="MAXPAGES", type=int, default=0, help="the maximum number of pages to extract text from (0 for all pages)")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose logging")

    args = parser.parse_args(argv)

    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    start_time = time.monotonic()

    extracted_text = extract_pdf_text(args.file_path, args.password, args.maxpages)

    end_time = time.monotonic()

    print(extracted_text)

    logging.info("Extraction completed in %s seconds.", end_time - start_time)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))