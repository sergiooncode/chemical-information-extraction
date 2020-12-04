from typing import List

import spacy

from src.infrastructure.persistence.mongoengine.model.patent_document import PatentDocument


def process_document_batch_app_service(batch: List[str]):
    print("Work")
    documents = PatentDocument.objects.filter(id__in=batch).all()

    all_entities_by_document_id = {}

    nlp = spacy.load("en_core_web_sm")
    for d in documents:
        texts = [d.abstract, d.claims, d.description]
        all_entities_by_document_id[str(d.id)] = {"entities": []}
        for doc in nlp.pipe(texts, disable=["tagger", "parser"]):
            # Do something with the doc here
            all_entities_by_document_id[str(d.id)]["entities"].extend((ent.text, ent.label_) for ent in doc.ents)

    for did in all_entities_by_document_id:
        relevant_entities = []
        for entity_tuple in all_entities_by_document_id[did]["entities"]:
            if entity_tuple[1] == "PRODUCT":
                relevant_entities.append(entity_tuple[0])
        PatentDocument.objects(id=did).update(set__entities=relevant_entities,
                                              set__processed=True)

    return
