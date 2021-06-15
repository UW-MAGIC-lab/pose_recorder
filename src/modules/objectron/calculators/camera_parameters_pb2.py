# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/modules/objectron/calculators/camera_parameters.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/modules/objectron/calculators/camera_parameters.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?mediapipe/modules/objectron/calculators/camera_parameters.proto\x12\tmediapipe\"\xe7\x03\n\x15\x43\x61meraParametersProto\x12 \n\x13height_above_ground\x18\x01 \x01(\x02:\x03\x31\x30\x30\x12\x1e\n\x0eportrait_width\x18\x02 \x01(\x02:\x06\x31.0103\x12\x1f\n\x0fportrait_height\x18\x03 \x01(\x02:\x06\x31.3435\x12\x62\n\x11image_orientation\x18\x04 \x01(\x0e\x32\x31.mediapipe.CameraParametersProto.ImageOrientation:\x14PORTRAIT_ORIENTATION\x12V\n\x0fprojection_mode\x18\x05 \x01(\x0e\x32/.mediapipe.CameraParametersProto.ProjectionMode:\x0cGROUND_PLANE\x12%\n\x18projection_sphere_radius\x18\x06 \x01(\x02:\x03\x31\x30\x30\"G\n\x10ImageOrientation\x12\x18\n\x14PORTRAIT_ORIENTATION\x10\x00\x12\x19\n\x15LANDSCAPE_ORIENTATION\x10\x01\"?\n\x0eProjectionMode\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x10\n\x0cGROUND_PLANE\x10\x01\x12\n\n\x06SPHERE\x10\x02'
)



_CAMERAPARAMETERSPROTO_IMAGEORIENTATION = _descriptor.EnumDescriptor(
  name='ImageOrientation',
  full_name='mediapipe.CameraParametersProto.ImageOrientation',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PORTRAIT_ORIENTATION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANDSCAPE_ORIENTATION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=430,
  serialized_end=501,
)
_sym_db.RegisterEnumDescriptor(_CAMERAPARAMETERSPROTO_IMAGEORIENTATION)

_CAMERAPARAMETERSPROTO_PROJECTIONMODE = _descriptor.EnumDescriptor(
  name='ProjectionMode',
  full_name='mediapipe.CameraParametersProto.ProjectionMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GROUND_PLANE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPHERE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=503,
  serialized_end=566,
)
_sym_db.RegisterEnumDescriptor(_CAMERAPARAMETERSPROTO_PROJECTIONMODE)


_CAMERAPARAMETERSPROTO = _descriptor.Descriptor(
  name='CameraParametersProto',
  full_name='mediapipe.CameraParametersProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height_above_ground', full_name='mediapipe.CameraParametersProto.height_above_ground', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(100),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='portrait_width', full_name='mediapipe.CameraParametersProto.portrait_width', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1.0103),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='portrait_height', full_name='mediapipe.CameraParametersProto.portrait_height', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1.3435),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_orientation', full_name='mediapipe.CameraParametersProto.image_orientation', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='projection_mode', full_name='mediapipe.CameraParametersProto.projection_mode', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='projection_sphere_radius', full_name='mediapipe.CameraParametersProto.projection_sphere_radius', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(100),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CAMERAPARAMETERSPROTO_IMAGEORIENTATION,
    _CAMERAPARAMETERSPROTO_PROJECTIONMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=566,
)

_CAMERAPARAMETERSPROTO.fields_by_name['image_orientation'].enum_type = _CAMERAPARAMETERSPROTO_IMAGEORIENTATION
_CAMERAPARAMETERSPROTO.fields_by_name['projection_mode'].enum_type = _CAMERAPARAMETERSPROTO_PROJECTIONMODE
_CAMERAPARAMETERSPROTO_IMAGEORIENTATION.containing_type = _CAMERAPARAMETERSPROTO
_CAMERAPARAMETERSPROTO_PROJECTIONMODE.containing_type = _CAMERAPARAMETERSPROTO
DESCRIPTOR.message_types_by_name['CameraParametersProto'] = _CAMERAPARAMETERSPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CameraParametersProto = _reflection.GeneratedProtocolMessageType('CameraParametersProto', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAPARAMETERSPROTO,
  '__module__' : 'mediapipe.modules.objectron.calculators.camera_parameters_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.CameraParametersProto)
  })
_sym_db.RegisterMessage(CameraParametersProto)


# @@protoc_insertion_point(module_scope)
