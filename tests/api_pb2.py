# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapi.proto\"\x1b\n\nApiRequest\x12\r\n\x05value\x18\x01 \x01(\x03\"\x1b\n\x08\x41piReply\x12\x0f\n\x07message\x18\x01 \x02(\t\"\x1d\n\x0c\x43ounterReply\x12\r\n\x05value\x18\x01 \x02(\x03\x32\x8b\x01\n\x03\x41pi\x12.\n\x0eTriggerCounter\x12\x0b.ApiRequest\x1a\r.CounterReply\"\x00\x12*\n\nGetCounter\x12\x0b.ApiRequest\x1a\r.CounterReply\"\x00\x12(\n\x0cResetCounter\x12\x0b.ApiRequest\x1a\t.ApiReply\"\x00\x42\x0bZ\t./service')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\t./service'
  _globals['_APIREQUEST']._serialized_start=13
  _globals['_APIREQUEST']._serialized_end=40
  _globals['_APIREPLY']._serialized_start=42
  _globals['_APIREPLY']._serialized_end=69
  _globals['_COUNTERREPLY']._serialized_start=71
  _globals['_COUNTERREPLY']._serialized_end=100
  _globals['_API']._serialized_start=103
  _globals['_API']._serialized_end=242
# @@protoc_insertion_point(module_scope)
