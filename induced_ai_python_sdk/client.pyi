# coding: utf-8
"""
    Autonomous API

    Building the next evolution of actionable AI.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from induced_ai_python_sdk.client_custom import ClientCustom
from induced_ai_python_sdk.configuration import Configuration
from induced_ai_python_sdk.api_client import ApiClient
from induced_ai_python_sdk.type_util import copy_signature
from induced_ai_python_sdk.apis.tags.autonomous_api import AutonomousApi
from induced_ai_python_sdk.apis.tags.extraction_api import ExtractionApi
from induced_ai_python_sdk.apis.tags.feedback_api import FeedbackApi
from induced_ai_python_sdk.apis.tags.task_api import TaskApi



class InducedAi(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.autonomous: AutonomousApi = AutonomousApi(api_client)
        self.extraction: ExtractionApi = ExtractionApi(api_client)
        self.feedback: FeedbackApi = FeedbackApi(api_client)
        self.task: TaskApi = TaskApi(api_client)
