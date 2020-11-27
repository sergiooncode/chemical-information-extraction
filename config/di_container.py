from dependency_injector import containers
from dependency_injector import providers

from src.application.service.distribute_document_batches_app_service import DistributeDocumentBatchesAppService
from src.application.service.load_document_app_service import LoadDocumentAppService
from src.common.app_container import AppContainer
from src.common.logging.logging_adapter import LoggingAdapter
from src.infrastructure.parsing.lxml_document_abstract_parser import LxmlDocumentAbstractParser
from src.infrastructure.parsing.lxml_document_claims_parser import LxmlDocumentClaimsParser
from src.infrastructure.parsing.lxml_document_description_parser import LxmlDocumentDescriptionParser
from src.infrastructure.parsing.lxml_document_metadata_parser import LxmlDocumentMetadataParser
from src.infrastructure.parsing.lxml_document_title_parser import LxmlDocumentTitleParser
from src.infrastructure.persistence.mongoengine.repository.mongoengine_document_reader_repository import (
    MongoengineDocumentReaderRepository,
)
from src.infrastructure.persistence.mongoengine.repository.mongoengine_document_writer_repository import (
    MongoengineDocumentWriterRepository,
)
from src.user_interface.action.api.health_check import HealthCheckAction
from src.user_interface.action.api.v1.load_document_api_action import LoadDocumentApiAction


class ApiCommonContainer(containers.DeclarativeContainer):
    get_logger = providers.Factory(LoggingAdapter)


class RepositoryContainer(containers.DeclarativeContainer):
    document_writer_repository = providers.Factory(
        MongoengineDocumentWriterRepository,
    )
    document_reader_repository = providers.Factory(
        MongoengineDocumentReaderRepository,
    )


class ServicesContainer(containers.DeclarativeContainer):
    get_load_document_service = providers.Factory(
        LoadDocumentAppService,
        document_writer_repository=RepositoryContainer.document_writer_repository(),
        document_abstract_parser=LxmlDocumentAbstractParser(),
        document_title_parser=LxmlDocumentTitleParser(),
        document_metadata_parser=LxmlDocumentMetadataParser(),
        document_claims_parser=LxmlDocumentClaimsParser(),
        document_description_parser=LxmlDocumentDescriptionParser(),
    )
    distribute_document_batches_service = providers.Factory(
        DistributeDocumentBatchesAppService,
        document_reader_repository=RepositoryContainer.document_reader_repository(),
    )


class ActionsContainer(containers.DeclarativeContainer):
    health_check_api_action = providers.Factory(HealthCheckAction, logger=ApiCommonContainer.get_logger)

    document_load_api_action = providers.Factory(
        LoadDocumentApiAction,
        service=ServicesContainer.get_load_document_service(),
        logger=ApiCommonContainer.get_logger,
    )


container = AppContainer.get_instance()
container.bind("get_health_check_api_action", ActionsContainer.health_check_api_action())
container.bind("get_load_document_api_action", ActionsContainer.document_load_api_action())
container.bind("get_distribute_document_batches_service",
               ServicesContainer.distribute_document_batches_service())
