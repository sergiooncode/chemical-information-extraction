from lxml.etree import fromstring

from src.application.parsing.document_title_parser import DocumentTitleParser

TITLE_PATH = ".//invention-title"


class LxmlDocumentTitleParser(DocumentTitleParser):
    def parse(self, document_text: str):
        tree = fromstring(document_text.encode("utf8"))
        return tree.findall(TITLE_PATH)[0].text
