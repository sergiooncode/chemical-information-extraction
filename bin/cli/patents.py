from datetime import datetime
from itertools import chain
from os import listdir
from os.path import isfile
from os.path import join
from pathlib import Path

from flask import Blueprint
from lxml import etree
from lxml.etree import tostring

from src.infrastructure.parsing.lxml_document_abstract_parser import LxmlDocumentAbstractParser

patents_blueprint = Blueprint("patents", __name__)

PATENTS_FOLDER = f"{Path(__file__).parents[2]}/resources"


def stringify_children(node):
    parts = [node.text] + list(chain(*([c.text, tostring(c), c.tail] for c in node.getchildren()))) + [node.tail]
    parts = [str(p) for p in parts]
    return parts


@patents_blueprint.cli.command("parse-abstract")
def parse_patent_abstract():
    xml_files = [f for f in listdir(PATENTS_FOLDER) if isfile(join(PATENTS_FOLDER, f))]
    print(xml_files[1])

    with open(join(PATENTS_FOLDER, xml_files[1]), "rb") as fd:
        print(LxmlDocumentAbstractParser().parse(fd.read()))


@patents_blueprint.cli.command("parse-metadata")
def parse_patent_metadata():
    xml_files = [f for f in listdir(PATENTS_FOLDER) if isfile(join(PATENTS_FOLDER, f))]
    print(xml_files[0])
    tree = etree.parse(join(PATENTS_FOLDER, xml_files[0]))

    title = tree.findall(".//invention-title")[0].text
    print(title)

    patent_date = tree.findall(".//application-reference/document-id/date")[0].text
    patent_year = datetime.strptime(patent_date, "%Y%m%d").year

    doc_number = tree.findall(".//publication-reference/document-id/doc-number")[0].text

    return {"title": title, "year": patent_year, "doc_number": doc_number}


@patents_blueprint.cli.command("parse-patent-full-text")
def parse_patent_full_text():
    xml_files = [f for f in listdir(PATENTS_FOLDER) if isfile(join(PATENTS_FOLDER, f))]
    print(xml_files[0])
    tree = etree.parse(join(PATENTS_FOLDER, xml_files[0]))

    # description
    print(stringify_children(tree.getroot())[8])

    # claims
    print(stringify_children(tree.getroot())[11])
