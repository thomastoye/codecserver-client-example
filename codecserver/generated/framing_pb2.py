# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: framing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="framing.proto",
    package="CodecServer.proto",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\rframing.proto\x12\x11\x43odecServer.proto"b\n\x0b\x46ramingHint\x12\x13\n\x0b\x63hannelBits\x18\x01 \x01(\r\x12\x14\n\x0c\x63hannelBytes\x18\x02 \x01(\r\x12\x14\n\x0c\x61udioSamples\x18\x03 \x01(\r\x12\x12\n\naudioBytes\x18\x04 \x01(\rb\x06proto3',
)


_FRAMINGHINT = _descriptor.Descriptor(
    name="FramingHint",
    full_name="CodecServer.proto.FramingHint",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="channelBits",
            full_name="CodecServer.proto.FramingHint.channelBits",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="channelBytes",
            full_name="CodecServer.proto.FramingHint.channelBytes",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="audioSamples",
            full_name="CodecServer.proto.FramingHint.audioSamples",
            index=2,
            number=3,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="audioBytes",
            full_name="CodecServer.proto.FramingHint.audioBytes",
            index=3,
            number=4,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=36,
    serialized_end=134,
)

DESCRIPTOR.message_types_by_name["FramingHint"] = _FRAMINGHINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FramingHint = _reflection.GeneratedProtocolMessageType(
    "FramingHint",
    (_message.Message,),
    {
        "DESCRIPTOR": _FRAMINGHINT,
        "__module__": "framing_pb2"
        # @@protoc_insertion_point(class_scope:CodecServer.proto.FramingHint)
    },
)
_sym_db.RegisterMessage(FramingHint)


# @@protoc_insertion_point(module_scope)
