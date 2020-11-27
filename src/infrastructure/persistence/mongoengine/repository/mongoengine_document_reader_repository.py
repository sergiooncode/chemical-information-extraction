from src.domain.model.repository.document_reader_repository import DocumentReaderRepository
from src.infrastructure.persistence.mongoengine.model.patent_document import PatentDocument


class MongoengineDocumentReaderRepository(DocumentReaderRepository):
    def list_by_processed(self, processed_filter: bool):
        return PatentDocument.objects(processed=processed_filter).all()
