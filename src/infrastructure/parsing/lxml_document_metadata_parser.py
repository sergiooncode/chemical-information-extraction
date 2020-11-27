from datetime import datetime

from lxml.etree import fromstring

from src.application.parsing.document_metadata_parser import DocumentMetadataParser
from src.domain.model.metadata import Metadata

APPLICATION_DATE_PATH = ".//application-reference/document-id/date"
APPLICATION_DOCUMENT_NUMBER_PATH = ".//publication-reference/document-id/doc-number"
APPLICATION_KIND_PATH = ".//publication-reference/document-id/kind"
APPLICATION_COUNTRY_PATH = ".//publication-reference/document-id/country"


class LxmlDocumentMetadataParser(DocumentMetadataParser):
    def parse(self, document_text: str) -> Metadata:
        tree = fromstring(document_text.encode("utf8"))
        date_text = tree.findall(APPLICATION_DATE_PATH)[0].text
        date = datetime.strptime(date_text, "%Y%m%d")
        document_year = date.year
        document_number = tree.findall(APPLICATION_DOCUMENT_NUMBER_PATH)[0].text
        kind = tree.findall(APPLICATION_KIND_PATH)[0].text
        country = tree.findall(APPLICATION_COUNTRY_PATH)[0].text

        return Metadata(
            year=document_year,
            application_document_number=document_number,
            application_country=country,
            application_kind=kind,
            application_date=date,
        )
