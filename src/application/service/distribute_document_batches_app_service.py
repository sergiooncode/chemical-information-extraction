import multiprocessing

from config.constants import NUMBER_OF_DOCUMENT_PROCESSING_WORKERS
from src.application.service.application_service import ApplicationService
from src.application.service.process_document_app_service import process_document_batch_app_service
from src.application.service.util import chunk_it
from src.domain.model.repository.document_reader_repository import DocumentReaderRepository


class DistributeDocumentBatchesAppService(ApplicationService):
    def __init__(self, document_reader_repository: DocumentReaderRepository):
        self.__document_reader_repository = document_reader_repository

    def execute(self):
        unprocessed_documents = self.__document_reader_repository.list_by_processed(processed_filter=False)
        unprocessed_document_ids = [str(ud.id) for ud in unprocessed_documents]

        document_id_batches = chunk_it(unprocessed_document_ids, NUMBER_OF_DOCUMENT_PROCESSING_WORKERS)

        jobs = []
        for batch in document_id_batches:
            p = multiprocessing.Process(target=process_document_batch_app_service, args=(batch,))
            jobs.append(p)
            p.start()
