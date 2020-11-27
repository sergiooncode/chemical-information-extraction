from functools import partial
from http import HTTPStatus
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from flask import Response
from flask import jsonify
from flask import make_response


def _generate_response(
    data: Optional[object] = None,
    message: str = "ok",
    status_code: int = HTTPStatus.OK,
) -> Response:
    """
    Generate full responses.

    :param List data: list with the data
    :param String message: text
    :param Integer status_code: status code of the response
    :return Response: response
    """
    # full body at response
    body = _generate_body(data, message, status_code)

    # create response
    if isinstance(body, str):
        serialized_body = ""
    if isinstance(body, dict):
        serialized_body = jsonify(body)
    response = make_response(serialized_body)
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE, PATCH"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.status_code = status_code
    return response


def _generate_body(
    data: Optional[Any] = None,
    message: str = "ok",
    status_code: int = HTTPStatus.OK,
) -> Dict[str, Union[Dict[str, str], Dict[str, int], List[Any]]]:
    """
    Generate a body response as API documentation.

    :param List data: data
    :param String message: message
    :return Dict: body
    """
    if message is None:
        message = "ok"

    body = ""
    if status_code not in (HTTPStatus.NO_CONTENT, HTTPStatus.CREATED):
        body = dict(status=dict(text=message), meta={}, data=[])

    # check data
    if data is not None or data == []:
        data = [data] if type(data) != list else data
        body["data"] = data
        body["meta"] = dict(page=1, pages=1, results=len(data), showing=len(data))
    return body


def json_error(
    message: str = None,
    status_code: int = HTTPStatus.NOT_FOUND,
):
    data = {
        "status": {"text": message},
    }
    response = make_response(jsonify(data))
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE, PATCH"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.status_code = status_code
    return response


generate_get = partial(_generate_response, status_code=HTTPStatus.OK)
generate_post = partial(_generate_response, status_code=HTTPStatus.CREATED)
