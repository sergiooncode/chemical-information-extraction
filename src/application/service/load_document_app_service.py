from src.application.interaction.command.load_document_command import LoadDocumentCommand
from src.application.parsing.document_abstract_parser import DocumentAbstractParser
from src.application.parsing.document_claims_parser import DocumentClaimsParser
from src.application.parsing.document_description_parser import DocumentDescriptionParser
from src.application.parsing.document_metadata_parser import DocumentMetadataParser
from src.application.parsing.document_title_parser import DocumentTitleParser
from src.application.service.application_service import ApplicationService
from src.domain.model.repository.document_writer_repository import DocumentWriterRepository


class LoadDocumentAppService(ApplicationService):
    def __init__(
        self,
        document_writer_repository: DocumentWriterRepository,
        document_abstract_parser: DocumentAbstractParser,
        document_title_parser: DocumentTitleParser,
        document_metadata_parser: DocumentMetadataParser,
        document_claims_parser: DocumentClaimsParser,
        document_description_parser: DocumentDescriptionParser,
    ):
        self.__document_writer_repository = document_writer_repository
        self.__document_abstract_parser = document_abstract_parser
        self.__document_title_parser = document_title_parser
        self.__document_metadata_parser = document_metadata_parser
        self.__document_claims_parser = document_claims_parser
        self.__document_description_parser = document_description_parser

    def execute(self, command: LoadDocumentCommand):
        abstract = self.__document_abstract_parser.parse(command.document_text)
        metadata = self.__document_metadata_parser.parse(command.document_text)
        title = self.__document_title_parser.parse(command.document_text)
        metadata.title = title
        claims = self.__document_claims_parser.parse(command.document_text)
        description = self.__document_description_parser.parse(command.document_text)

        self.__document_writer_repository.add(
            document_details=dict(
                abstract=abstract,
                title=title,
                year=metadata.year,
                claims=claims,
                description=description,
                application_country=metadata.application_country,
                application_document_number=metadata.application_document_number,
                application_kind=metadata.application_kind,
                application_date=metadata.application_date,
            )
        )
