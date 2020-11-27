from mongoengine import EmbeddedDocument
from mongoengine import ListField
from mongoengine import StringField


class ExtractionDetails(EmbeddedDocument):
    entities = ListField(StringField)
