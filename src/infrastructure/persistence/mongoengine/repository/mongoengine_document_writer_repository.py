from typing import Dict
from typing import List
from typing import Union

from src.domain.model.repository.document_writer_repository import DocumentWriterRepository
from src.infrastructure.persistence.mongoengine.model.patent_document import PatentDocument
from src.infrastructure.persistence.mongoengine.model.patent_document_application import PatentDocumentApplication


class MongoengineDocumentWriterRepository(DocumentWriterRepository):
    def add(self, document_details: Dict[str, Union[str, int]]):
        PatentDocument(
            abstract=document_details["abstract"],
            title=document_details["title"],
            year=document_details["year"],
            claims=document_details["claims"],
            description=document_details["description"],
            application=PatentDocumentApplication(
                country=document_details["application_country"],
                doc_number=document_details["application_document_number"],
                kind=document_details["application_kind"],
                date=document_details["application_date"],
            ),
            processed=False,
        ).save()

    def bulk_add(self, document_dicts: List[Dict[str, Union[str, int]]]):
        patent_document_instances = []
        for d in document_dicts:
            patent_document_instances.append(
                PatentDocument(
                    abstract=d["abstract"],
                    title=d["title"],
                    year=d["year"],
                    claims=d["claims"],
                    description=d["description"],
                    application=PatentDocumentApplication(
                        country=d["application_country"],
                        doc_number=d["application_document_number"],
                        kind=d["application_kind"],
                        date=d["application_date"],
                    ),
                    processed=False,
                )
            )
        return PatentDocument.objects.insert(patent_document_instances, load_bulk=False)

    def update(self, document_id: str, entities: List[str]):
        pd = PatentDocument.objects.get(id=document_id)
        pd.update(set__entities=entities)
