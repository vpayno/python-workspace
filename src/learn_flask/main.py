"""Flask Module Demo"""

from typing import Literal

from flask import Flask, Response, jsonify, request
from icecream import ic  # type: ignore[import-untyped]
from rich import traceback

traceback.install(show_locals=True)


app: Flask = Flask(__name__)
ic(app)


# curl -sS http://127.0.0.1:5000/
@app.route("/")
def route_home() -> str:
    """Default route"""

    return "Home"


# GET - request data
# POST - create resource
# PUT - update resource
# DELETE - delete resource

type user_data_t = dict[str, str]  # type: ignore[valid-type]
type response_t = tuple[Response, Literal[int]]  # type: ignore[valid-type]


# curl -sS http://127.0.0.1:5000/get-user/1234
@app.route("/get-user/<user_id>")
def route_get_user(user_id: str) -> response_t:
    user_data: user_data_t = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com",
    }

    # curl -sS http://127.0.0.1:5000/get-user/1234?extra="hello"
    extra = request.args.get("extra")

    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


# $ curl -sS -X POST -H "Content-Type: application/json" -d '{"username":"janedoe"}' http://127.0.0.1:5000/create-user
@app.route("/create-user", methods=["POST"])
def create_user() -> response_t:
    if not request.method == "POST":
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        return jsonify({"error": "wrong method"}), 501

    data = request.get_json()

    return jsonify(data), 201


def main() -> None:
    """Main Function"""

    app.run(debug=True)  # nosec


if __name__ == "__main__":  # pragma: no cover
    main()
