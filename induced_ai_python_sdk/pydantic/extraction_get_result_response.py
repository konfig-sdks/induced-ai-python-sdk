# coding: utf-8

"""
    Autonomous API

    Building the next evolution of actionable AI.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from induced_ai_python_sdk.pydantic.extraction_get_result_response_data import ExtractionGetResultResponseData

class ExtractionGetResultResponse(BaseModel):
    success: typing.Optional[bool] = Field(None, alias='success')

    data: typing.Optional[ExtractionGetResultResponseData] = Field(None, alias='data')

    request_id: typing.Optional[str] = Field(None, alias='requestId')

    time_taken: typing.Optional[int] = Field(None, alias='timeTaken')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
