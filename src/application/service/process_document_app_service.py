from typing import List

import spacy

from src.infrastructure.persistence.mongoengine.model.patent_document import PatentDocument


def process_document_app_service(batch: List[str]):
    print("Work")
    documents = PatentDocument.objects.filter(refs__in=batch)
    text_by_document_id = {}

    nlp = spacy.load("en_core_web_sm")
    for doc in nlp.pipe(texts, disable=["tagger", "parser"]):
        # Do something with the doc here
        print([(ent.text, ent.label_) for ent in doc.ents])
    return
