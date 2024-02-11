from cerberus import Validator


def tag_creator_validator(request: any) -> None:
    body_validator = Validator(
        {
            "product_code": {"type": "string", "required": True, "empty": False}
        }
    )

    response = body_validator.validate(request.json)
    if response is False:
        raise Exception(body_validator.errors)
