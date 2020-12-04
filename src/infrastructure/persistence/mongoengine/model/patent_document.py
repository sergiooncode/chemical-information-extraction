from mongoengine import BooleanField
from mongoengine import Document
from mongoengine import EmbeddedDocumentField
from mongoengine import IntField
from mongoengine import ListField
from mongoengine import StringField

from src.infrastructure.persistence.mongoengine.model.patent_document_application import (
    PatentDocumentApplication,
)  # noqa


class PatentDocument(Document):
    abstract = StringField(max_length=50000)
    year = IntField()
    title = StringField(max_length=500)
    claims = StringField(max_length=200000)
    description = StringField(max_length=50000)
    application = EmbeddedDocumentField("PatentDocumentApplication")
    entities = ListField(StringField())
    processed = BooleanField()
