import spacy
from flask import Blueprint

entities_blueprint = Blueprint("entities", __name__)


@entities_blueprint.cli.command("recognize")
def recognize_entities():
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

    texts = [patent_abstract_text]

    nlp = spacy.load("en_core_web_sm")
    for doc in nlp.pipe(texts, disable=["tagger", "parser"]):
        # Do something with the doc here
        print([(ent.text, ent.label_) for ent in doc.ents])
