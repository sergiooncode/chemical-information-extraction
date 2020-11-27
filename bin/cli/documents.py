from datetime import datetime

from flask import Blueprint

from config.di_container import container
from src.application.service.distribute_document_batches_app_service import DistributeDocumentBatchesAppService
from src.infrastructure.persistence.mongoengine.model.patent_document import PatentDocument
from src.infrastructure.persistence.mongoengine.model.patent_document_application import PatentDocumentApplication

documents_blueprint = Blueprint("documents", __name__)


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


@documents_blueprint.cli.command("persist-many")
def persist_many_documents():
    from .patents import parse_patent_abstract
    from .patents import parse_patent_metadata
    from .patents import parse_patent_full_text

    print(parse_patent_abstract())
    print(parse_patent_metadata())
    print(parse_patent_full_text())


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
