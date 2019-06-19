# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/app_url_operating_system_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/enums/app_url_operating_system_type.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\036AppUrlOperatingSystemTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\nGgoogle/ads/googleads_v1/proto/enums/app_url_operating_system_type.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"p\n\x1d\x41ppUrlOperatingSystemTypeEnum\"O\n\x19\x41ppUrlOperatingSystemType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x07\n\x03IOS\x10\x02\x12\x0b\n\x07\x41NDROID\x10\x03\x42\xf3\x01\n!com.google.ads.googleads.v1.enumsB\x1e\x41ppUrlOperatingSystemTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_APPURLOPERATINGSYSTEMTYPEENUM_APPURLOPERATINGSYSTEMTYPE = _descriptor.EnumDescriptor(
  name='AppUrlOperatingSystemType',
  full_name='google.ads.googleads.v1.enums.AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANDROID', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=169,
  serialized_end=248,
)
_sym_db.RegisterEnumDescriptor(_APPURLOPERATINGSYSTEMTYPEENUM_APPURLOPERATINGSYSTEMTYPE)


_APPURLOPERATINGSYSTEMTYPEENUM = _descriptor.Descriptor(
  name='AppUrlOperatingSystemTypeEnum',
  full_name='google.ads.googleads.v1.enums.AppUrlOperatingSystemTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _APPURLOPERATINGSYSTEMTYPEENUM_APPURLOPERATINGSYSTEMTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=248,
)

_APPURLOPERATINGSYSTEMTYPEENUM_APPURLOPERATINGSYSTEMTYPE.containing_type = _APPURLOPERATINGSYSTEMTYPEENUM
DESCRIPTOR.message_types_by_name['AppUrlOperatingSystemTypeEnum'] = _APPURLOPERATINGSYSTEMTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppUrlOperatingSystemTypeEnum = _reflection.GeneratedProtocolMessageType('AppUrlOperatingSystemTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _APPURLOPERATINGSYSTEMTYPEENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.app_url_operating_system_type_pb2'
  ,
  __doc__ = """The possible OS types for a deeplink AppUrl.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.AppUrlOperatingSystemTypeEnum)
  ))
_sym_db.RegisterMessage(AppUrlOperatingSystemTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
