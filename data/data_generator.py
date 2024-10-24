import enum
import json


@enum.unique
class DataTypes(enum.StrEnum):
    INVALID_EMAIL = "INVALID_EMAIL"
    INVALID_PASSWORD = "INVALID_PASSWORD"


def get_credential_data(data_type: DataTypes):
    """
    Filter the test data dictionary by data type
    """
    with open("data\\credentials.json", "r") as cred_file:
        credentials = json.loads(cred_file.read())

    return list(filter(lambda x: x["type"] == data_type, credentials))
