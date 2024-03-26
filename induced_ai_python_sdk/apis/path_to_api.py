import typing_extensions

from induced_ai_python_sdk.paths import PathValues
from induced_ai_python_sdk.apis.paths.autonomous import Autonomous
from induced_ai_python_sdk.apis.paths.autonomous_id import AutonomousId
from induced_ai_python_sdk.apis.paths.autonomous_id_stop import AutonomousIdStop
from induced_ai_python_sdk.apis.paths.autonomous_id_feedback import AutonomousIdFeedback
from induced_ai_python_sdk.apis.paths.extract import Extract
from induced_ai_python_sdk.apis.paths.extract_id import ExtractId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTONOMOUS: Autonomous,
        PathValues.AUTONOMOUS_ID: AutonomousId,
        PathValues.AUTONOMOUS_ID_STOP: AutonomousIdStop,
        PathValues.AUTONOMOUS_ID_FEEDBACK: AutonomousIdFeedback,
        PathValues.EXTRACT: Extract,
        PathValues.EXTRACT_ID: ExtractId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTONOMOUS: Autonomous,
        PathValues.AUTONOMOUS_ID: AutonomousId,
        PathValues.AUTONOMOUS_ID_STOP: AutonomousIdStop,
        PathValues.AUTONOMOUS_ID_FEEDBACK: AutonomousIdFeedback,
        PathValues.EXTRACT: Extract,
        PathValues.EXTRACT_ID: ExtractId,
    }
)
