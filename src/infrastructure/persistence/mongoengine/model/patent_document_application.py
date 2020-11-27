from mongoengine import DateTimeField
from mongoengine import EmbeddedDocument
from mongoengine import StringField


class PatentDocumentApplication(EmbeddedDocument):
    country = StringField(max_length=3)
    doc_number = StringField(max_length=20)
    kind = StringField(max_length=3)
    date = DateTimeField()
