from lxml.etree import fromstring
from lxml.etree import tostring

from src.application.parsing.document_abstract_parser import DocumentAbstractParser

CHARACTERS_TO_DISCARD = ["<", ">", "\n", "\\n", "=", "'"]
ABSTRACT_PATH = ".//abstract[@id='abstr_en']/p"


class LxmlDocumentAbstractParser(DocumentAbstractParser):
    def parse(self, document_text: str):
        clean_word_list = []
        tree = fromstring(document_text.encode("utf8"))
        for e in str(tostring(tree.findall(ABSTRACT_PATH)[0])).replace("<br/>", "").split():
            if not any(x in e for x in CHARACTERS_TO_DISCARD):
                clean_word_list.append(e.replace("\n", "").strip())
        return " ".join(clean_word_list)
