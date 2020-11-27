from lxml import etree

from src.application.parsing.document_claims_parser import DocumentClaimsParser
from src.infrastructure.parsing.utils import stringify_children

CLAIMS_POSITION_IN_FULL_DOCUMENT = 8


class LxmlDocumentClaimsParser(DocumentClaimsParser):
    def parse(self, document_text: str):
        tree = etree.fromstring(document_text.encode("utf8"))
        return stringify_children(tree)[CLAIMS_POSITION_IN_FULL_DOCUMENT]
