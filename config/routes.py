from flask_restx import Api
from flask_restx import Resource
from flask_restx import fields

from config.di_container import container

HEALTH_CHECK = "/_health-check"
ROOT = ""

api = Api(
    version="1.0",
    title="Chemical Information Extraction API",
    description="API for simple information extraction pipeline to extract chemicals from patents",
    default="API",
    default_label="",
    doc="/apidocs/",
)

documents_ns = api.namespace("v1/documents", description="Chemical Information Extraction - Documents")


document_load = api.model(
    "DocumentLoad", {"text": fields.String(required=True, description="A document text", example="A document text")}
)


@api.route(HEALTH_CHECK, endpoint="health-check")
class HealthCheck(Resource):
    def get(self):
        return container.get("get_health_check_api_action").handle()


@documents_ns.route(ROOT, endpoint="load-documents")
class DocumentsLoad(Resource):
    @documents_ns.expect(document_load)
    @documents_ns.response(201, "Accepted")
    def post(self):
        return container.get("get_load_document_api_action").handle()
