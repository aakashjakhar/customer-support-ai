import os
from pathlib import Path
from langchain_community.document_loaders import TextLoader

def load_documents():

    folder_path = Path("knowledge_base")

    documents = []

    for file in os.listdir(folder_path):

        if file.endswith(".txt"):

            loader = TextLoader(
                folder_path / file,
                encoding="utf-8"
            )

            documents.extend(loader.load())

    return documents