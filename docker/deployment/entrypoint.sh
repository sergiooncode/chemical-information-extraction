#!/bin/sh

PYTHONPATH=/chemical-extraction-backend python -m spacy download en_core_web_sm

# Hand off to the CMD
exec "$@"