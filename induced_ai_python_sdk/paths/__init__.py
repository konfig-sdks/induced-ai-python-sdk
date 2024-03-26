# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from induced_ai_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    AUTONOMOUS = "/autonomous"
    AUTONOMOUS_ID = "/autonomous/{id}"
    AUTONOMOUS_ID_STOP = "/autonomous/{id}/stop"
    AUTONOMOUS_ID_FEEDBACK = "/autonomous/{id}/feedback"
    EXTRACT = "/extract"
    EXTRACT_ID = "/extract/{id}"
