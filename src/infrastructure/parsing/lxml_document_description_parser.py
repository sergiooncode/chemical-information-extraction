from lxml import etree

from src.application.parsing.document_description_parser import DocumentDescriptionParser
from src.infrastructure.parsing.utils import stringify_children

DESCRIPTION_POSITION_IN_FULL_DOCUMENT = 11


class LxmlDocumentDescriptionParser(DocumentDescriptionParser):
    def parse(self, document_text: str):
        tree = etree.fromstring(document_text.encode("utf8"))
        return stringify_children(tree)[DESCRIPTION_POSITION_IN_FULL_DOCUMENT]
