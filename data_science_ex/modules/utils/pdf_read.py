import spacy
import os
from PyPDF2 import PdfFileReader
import logging

en_nlp = spacy.load("en_core_web_sm")
BASE_PATH = os.path.join(os.getcwd(), "..", "datasets", "research-papers")

# Logging configuration
logging.root.   setLevel(logging.NOTSET)


# Return array with content of multiple research papers
# TODO: currently reads all files, but needs to only read content of pdf files, all other ignored
def load_files(path = None):
    global BASE_PATH

    path = path if not path == None else BASE_PATH
    file_names = os.listdir(path)
    file_contents = []


    # Iterate over files all research papers in the directory
    for file_name in file_names:
        logging.info("Read file: " + file_name)
        file_content = ""
        full_file_name = os.path.join(path, file_name)

        # Open file
        with open(full_file_name, "rb") as pdf_file:
            pdf_file_reader = PdfFileReader(pdf_file)

            # Iterate over pages            
            for num_page in range(pdf_file_reader.getNumPages()):
                page = pdf_file_reader.getPage(num_page)
                content = page.extractText()
                file_content += content

            # Append to array
            file_contents.append(file_content)

    return file_contents


if __name__ == "__main__":
    contents = load_files() 
    