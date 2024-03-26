import typing_extensions

from induced_ai_python_sdk.apis.tags import TagValues
from induced_ai_python_sdk.apis.tags.extraction_api import ExtractionApi
from induced_ai_python_sdk.apis.tags.autonomous_api import AutonomousApi
from induced_ai_python_sdk.apis.tags.task_api import TaskApi
from induced_ai_python_sdk.apis.tags.feedback_api import FeedbackApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EXTRACTION: ExtractionApi,
        TagValues.AUTONOMOUS: AutonomousApi,
        TagValues.TASK: TaskApi,
        TagValues.FEEDBACK: FeedbackApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EXTRACTION: ExtractionApi,
        TagValues.AUTONOMOUS: AutonomousApi,
        TagValues.TASK: TaskApi,
        TagValues.FEEDBACK: FeedbackApi,
    }
)
