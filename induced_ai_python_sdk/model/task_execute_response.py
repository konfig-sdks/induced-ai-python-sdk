# coding: utf-8

"""
    Autonomous API

    Building the next evolution of actionable AI.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from induced_ai_python_sdk import schemas  # noqa: F401


class TaskExecuteResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            success = schemas.BoolSchema
        
            @staticmethod
            def data() -> typing.Type['TaskExecuteResponseData']:
                return TaskExecuteResponseData
            requestId = schemas.StrSchema
            timeTaken = schemas.IntSchema
            __annotations__ = {
                "success": success,
                "data": data,
                "requestId": requestId,
                "timeTaken": timeTaken,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'TaskExecuteResponseData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestId"]) -> MetaOapg.properties.requestId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeTaken"]) -> MetaOapg.properties.timeTaken: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["success", "data", "requestId", "timeTaken", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["success"]) -> typing.Union[MetaOapg.properties.success, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['TaskExecuteResponseData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestId"]) -> typing.Union[MetaOapg.properties.requestId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeTaken"]) -> typing.Union[MetaOapg.properties.timeTaken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["success", "data", "requestId", "timeTaken", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        success: typing.Union[MetaOapg.properties.success, bool, schemas.Unset] = schemas.unset,
        data: typing.Union['TaskExecuteResponseData', schemas.Unset] = schemas.unset,
        requestId: typing.Union[MetaOapg.properties.requestId, str, schemas.Unset] = schemas.unset,
        timeTaken: typing.Union[MetaOapg.properties.timeTaken, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaskExecuteResponse':
        return super().__new__(
            cls,
            *args,
            success=success,
            data=data,
            requestId=requestId,
            timeTaken=timeTaken,
            _configuration=_configuration,
            **kwargs,
        )

from induced_ai_python_sdk.model.task_execute_response_data import TaskExecuteResponseData
