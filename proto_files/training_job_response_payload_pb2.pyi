"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from text_classifier_pb2 import (
    TextClassifierFrozenModel as text_classifier_pb2___TextClassifierFrozenModel,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class TrainingJobResponsePayload(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class JobResult(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        job_id: typing___Text = ...

        @property
        def text_classifier(self) -> text_classifier_pb2___TextClassifierFrozenModel: ...

        def __init__(self,
            *,
            job_id : typing___Optional[typing___Text] = None,
            text_classifier : typing___Optional[text_classifier_pb2___TextClassifierFrozenModel] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"classifier_frozen_model",b"classifier_frozen_model",u"text_classifier",b"text_classifier"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"classifier_frozen_model",b"classifier_frozen_model",u"job_id",b"job_id",u"text_classifier",b"text_classifier"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions___Literal[u"classifier_frozen_model",b"classifier_frozen_model"]) -> typing_extensions___Literal["text_classifier"]: ...
    type___JobResult = JobResult

    vm_id: typing___Text = ...
    signature: typing___Text = ...

    @property
    def job_result(self) -> type___TrainingJobResponsePayload.JobResult: ...

    def __init__(self,
        *,
        job_result : typing___Optional[type___TrainingJobResponsePayload.JobResult] = None,
        vm_id : typing___Optional[typing___Text] = None,
        signature : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"job_result",b"job_result"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"job_result",b"job_result",u"signature",b"signature",u"vm_id",b"vm_id"]) -> None: ...
type___TrainingJobResponsePayload = TrainingJobResponsePayload
