# coding: utf-8

"""
    Autonomous API

    Building the next evolution of actionable AI.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from induced_ai_python_sdk.paths.extract.post import FromUrl
from induced_ai_python_sdk.paths.extract_id.get import GetResult
from induced_ai_python_sdk.apis.tags.extraction_api_raw import ExtractionApiRaw


class ExtractionApi(
    FromUrl,
    GetResult,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ExtractionApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ExtractionApiRaw(api_client)
