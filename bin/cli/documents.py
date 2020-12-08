from datetime import datetime
from os import listdir
from os.path import isfile
from os.path import join
from pathlib import Path

from flask import Blueprint

from config.di_container import container
from src.infrastructure.parsing.lxml_document_abstract_parser import LxmlDocumentAbstractParser
from src.infrastructure.parsing.lxml_document_claims_parser import LxmlDocumentClaimsParser
from src.infrastructure.parsing.lxml_document_description_parser import LxmlDocumentDescriptionParser
from src.infrastructure.parsing.lxml_document_metadata_parser import LxmlDocumentMetadataParser
from src.infrastructure.parsing.lxml_document_title_parser import LxmlDocumentTitleParser
from src.infrastructure.persistence.mongoengine.model.patent_document import PatentDocument
from src.infrastructure.persistence.mongoengine.model.patent_document_application import PatentDocumentApplication
from src.infrastructure.persistence.mongoengine.repository.mongoengine_document_writer_repository import \
    MongoengineDocumentWriterRepository

documents_blueprint = Blueprint("documents", __name__)

PATENTS_FOLDER = f"{Path(__file__).parents[2]}/resources"


@documents_blueprint.cli.command("persist")
def persist_document():
    patent_abstract_text = (
        """A three-piece thread wound golf ball including a central solid core portion """
        """composed mainly of polybutadiene having a Shore D hardness of 55-75 and increased """
        """diameter (34.3-38.1 mm) and reduced specific gravity (1.20-1.25) compared """
        """to traditional three-piece wound golf balls. """
        """The solid core portion is wound with an elastomeric thread material """
        """to achieve a core and winding layer diameter of 39.1-40.6 mm. """
        """A dimpled cover portion formed of a thermoplastic material """
        """overlies the winding layer. """
        """The three-piece thread wound golf ball construction provides desirable increased """
        """moment of inertia and spin characteristics for the ball. """
        """The resulting golf ball characteristics are such that when hit with a driver, """
        """other woods or the longer iron clubs it performs like a """
        """distance two-piece golf ball; when hit with """
        """mid-iron clubs it performs like a two-piece Hi-spin or """
        """a soft covered multi layered golf """
        """ball; and when hit with short iron clubs it performs much """
        """like a Balata wound golf ball."""
    )
    patent_application_year = 1998
    title = "Three-piece wound golf ball"

    pd = PatentDocument(
        abstract=patent_abstract_text,
        title=title,
        year=patent_application_year,
        application=PatentDocumentApplication(
            country="US",
            doc_number="09103061",
            kind="A",
            date=datetime.strptime("19980623", "%Y%m%d"),
        ),
    )
    pd.save()


@documents_blueprint.cli.command("list-all")
def list_all_documents():
    for o in PatentDocument.objects.all():
        print(o.id)
        print(o.title)
        print(o.year)
        print(o.abstract)
        print(o.application)


@documents_blueprint.cli.command("delete-all")
def delete_all_documents():
    PatentDocument.objects.delete()


@documents_blueprint.cli.command("process-batches")
def process_batches():
    # DistributeDocumentBatchesAppService()
    container.get("get_distribute_document_batches_service").execute()


@documents_blueprint.cli.command("bulk-load")
def bulk_load():
    BULK_LOAD_DOCUMENT_NUMBER = 1000
    document_writer_repository = MongoengineDocumentWriterRepository()

    xml_files = [f for f in listdir(PATENTS_FOLDER) if isfile(join(PATENTS_FOLDER, f))]

    abstract_parser = LxmlDocumentAbstractParser()
    metadata_parser = LxmlDocumentMetadataParser()
    title_parser = LxmlDocumentTitleParser()
    claims_parser = LxmlDocumentClaimsParser()
    description_parser = LxmlDocumentDescriptionParser()

    patents = []
    for xml_file_name in xml_files:
        with open(join(PATENTS_FOLDER, xml_file_name), "r") as fd:
            text = fd.read()
            try:
                abstract = abstract_parser.parse(text)
                metadata = metadata_parser.parse(text)
                title = title_parser.parse(text)
                metadata.title = title
                claims = claims_parser.parse(text)
                description = description_parser.parse(text)
            except Exception as e:
                import traceback;traceback.print_exc()
                print(e)
                continue

            patents.append(dict(
                abstract=abstract,
                title=title,
                year=metadata.year,
                claims=claims,
                description=description,
                application_country=metadata.application_country,
                application_document_number=metadata.application_document_number,
                application_kind=metadata.application_kind,
                application_date=metadata.application_date,
            ))

        if len(patents) == BULK_LOAD_DOCUMENT_NUMBER:
            document_writer_repository.bulk_add(patents)
            patents = []
            print(f"writing {BULK_LOAD_DOCUMENT_NUMBER} documents")

    print(f"writing {len(patents)} documents")
    document_writer_repository.bulk_add(patents)
