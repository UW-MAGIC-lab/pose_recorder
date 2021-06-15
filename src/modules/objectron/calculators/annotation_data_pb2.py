# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/modules/objectron/calculators/annotation_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.modules.objectron.calculators import a_r_capture_metadata_pb2 as mediapipe_dot_modules_dot_objectron_dot_calculators_dot_a__r__capture__metadata__pb2
from mediapipe.modules.objectron.calculators import object_pb2 as mediapipe_dot_modules_dot_objectron_dot_calculators_dot_object__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/modules/objectron/calculators/annotation_data.proto',
  package='mediapipe',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=mediapipe/modules/objectron/calculators/annotation_data.proto\x12\tmediapipe\x1a\x42mediapipe/modules/objectron/calculators/a_r_capture_metadata.proto\x1a\x34mediapipe/modules/objectron/calculators/object.proto\"8\n\x11NormalizedPoint2D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05\x64\x65pth\x18\x03 \x01(\x02\"*\n\x07Point3D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"u\n\x11\x41nnotatedKeyPoint\x12\n\n\x02id\x18\x01 \x01(\x05\x12$\n\x08point_3d\x18\x02 \x01(\x0b\x32\x12.mediapipe.Point3D\x12.\n\x08point_2d\x18\x03 \x01(\x0b\x32\x1c.mediapipe.NormalizedPoint2D\"\xa0\x01\n\x10ObjectAnnotation\x12\x11\n\tobject_id\x18\x01 \x01(\x05\x12/\n\tkeypoints\x18\x02 \x03(\x0b\x32\x1c.mediapipe.AnnotatedKeyPoint\x12\x12\n\nvisibility\x18\x03 \x01(\x02\x12\x10\n\x08rotation\x18\x04 \x03(\x02\x12\x13\n\x0btranslation\x18\x05 \x03(\x02\x12\r\n\x05scale\x18\x06 \x03(\x02\"\xb9\x01\n\x0f\x46rameAnnotation\x12\x10\n\x08\x66rame_id\x18\x01 \x01(\x05\x12\x30\n\x0b\x61nnotations\x18\x02 \x03(\x0b\x32\x1b.mediapipe.ObjectAnnotation\x12#\n\x06\x63\x61mera\x18\x03 \x01(\x0b\x32\x13.mediapipe.ARCamera\x12\x11\n\ttimestamp\x18\x04 \x01(\x01\x12\x14\n\x0cplane_center\x18\x05 \x03(\x02\x12\x14\n\x0cplane_normal\x18\x06 \x03(\x02\"e\n\x08Sequence\x12\"\n\x07objects\x18\x01 \x03(\x0b\x32\x11.mediapipe.Object\x12\x35\n\x11\x66rame_annotations\x18\x02 \x03(\x0b\x32\x1a.mediapipe.FrameAnnotationb\x06proto3'
  ,
  dependencies=[mediapipe_dot_modules_dot_objectron_dot_calculators_dot_a__r__capture__metadata__pb2.DESCRIPTOR,mediapipe_dot_modules_dot_objectron_dot_calculators_dot_object__pb2.DESCRIPTOR,])




_NORMALIZEDPOINT2D = _descriptor.Descriptor(
  name='NormalizedPoint2D',
  full_name='mediapipe.NormalizedPoint2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='mediapipe.NormalizedPoint2D.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='mediapipe.NormalizedPoint2D.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='depth', full_name='mediapipe.NormalizedPoint2D.depth', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=254,
)


_POINT3D = _descriptor.Descriptor(
  name='Point3D',
  full_name='mediapipe.Point3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='mediapipe.Point3D.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='mediapipe.Point3D.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='mediapipe.Point3D.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=298,
)


_ANNOTATEDKEYPOINT = _descriptor.Descriptor(
  name='AnnotatedKeyPoint',
  full_name='mediapipe.AnnotatedKeyPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mediapipe.AnnotatedKeyPoint.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='point_3d', full_name='mediapipe.AnnotatedKeyPoint.point_3d', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='point_2d', full_name='mediapipe.AnnotatedKeyPoint.point_2d', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=417,
)


_OBJECTANNOTATION = _descriptor.Descriptor(
  name='ObjectAnnotation',
  full_name='mediapipe.ObjectAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='mediapipe.ObjectAnnotation.object_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keypoints', full_name='mediapipe.ObjectAnnotation.keypoints', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visibility', full_name='mediapipe.ObjectAnnotation.visibility', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='mediapipe.ObjectAnnotation.rotation', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='translation', full_name='mediapipe.ObjectAnnotation.translation', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scale', full_name='mediapipe.ObjectAnnotation.scale', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=580,
)


_FRAMEANNOTATION = _descriptor.Descriptor(
  name='FrameAnnotation',
  full_name='mediapipe.FrameAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_id', full_name='mediapipe.FrameAnnotation.frame_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='mediapipe.FrameAnnotation.annotations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='camera', full_name='mediapipe.FrameAnnotation.camera', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='mediapipe.FrameAnnotation.timestamp', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plane_center', full_name='mediapipe.FrameAnnotation.plane_center', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plane_normal', full_name='mediapipe.FrameAnnotation.plane_normal', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=583,
  serialized_end=768,
)


_SEQUENCE = _descriptor.Descriptor(
  name='Sequence',
  full_name='mediapipe.Sequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='objects', full_name='mediapipe.Sequence.objects', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame_annotations', full_name='mediapipe.Sequence.frame_annotations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=770,
  serialized_end=871,
)

_ANNOTATEDKEYPOINT.fields_by_name['point_3d'].message_type = _POINT3D
_ANNOTATEDKEYPOINT.fields_by_name['point_2d'].message_type = _NORMALIZEDPOINT2D
_OBJECTANNOTATION.fields_by_name['keypoints'].message_type = _ANNOTATEDKEYPOINT
_FRAMEANNOTATION.fields_by_name['annotations'].message_type = _OBJECTANNOTATION
_FRAMEANNOTATION.fields_by_name['camera'].message_type = mediapipe_dot_modules_dot_objectron_dot_calculators_dot_a__r__capture__metadata__pb2._ARCAMERA
_SEQUENCE.fields_by_name['objects'].message_type = mediapipe_dot_modules_dot_objectron_dot_calculators_dot_object__pb2._OBJECT
_SEQUENCE.fields_by_name['frame_annotations'].message_type = _FRAMEANNOTATION
DESCRIPTOR.message_types_by_name['NormalizedPoint2D'] = _NORMALIZEDPOINT2D
DESCRIPTOR.message_types_by_name['Point3D'] = _POINT3D
DESCRIPTOR.message_types_by_name['AnnotatedKeyPoint'] = _ANNOTATEDKEYPOINT
DESCRIPTOR.message_types_by_name['ObjectAnnotation'] = _OBJECTANNOTATION
DESCRIPTOR.message_types_by_name['FrameAnnotation'] = _FRAMEANNOTATION
DESCRIPTOR.message_types_by_name['Sequence'] = _SEQUENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NormalizedPoint2D = _reflection.GeneratedProtocolMessageType('NormalizedPoint2D', (_message.Message,), {
  'DESCRIPTOR' : _NORMALIZEDPOINT2D,
  '__module__' : 'mediapipe.modules.objectron.calculators.annotation_data_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.NormalizedPoint2D)
  })
_sym_db.RegisterMessage(NormalizedPoint2D)

Point3D = _reflection.GeneratedProtocolMessageType('Point3D', (_message.Message,), {
  'DESCRIPTOR' : _POINT3D,
  '__module__' : 'mediapipe.modules.objectron.calculators.annotation_data_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Point3D)
  })
_sym_db.RegisterMessage(Point3D)

AnnotatedKeyPoint = _reflection.GeneratedProtocolMessageType('AnnotatedKeyPoint', (_message.Message,), {
  'DESCRIPTOR' : _ANNOTATEDKEYPOINT,
  '__module__' : 'mediapipe.modules.objectron.calculators.annotation_data_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.AnnotatedKeyPoint)
  })
_sym_db.RegisterMessage(AnnotatedKeyPoint)

ObjectAnnotation = _reflection.GeneratedProtocolMessageType('ObjectAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTANNOTATION,
  '__module__' : 'mediapipe.modules.objectron.calculators.annotation_data_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ObjectAnnotation)
  })
_sym_db.RegisterMessage(ObjectAnnotation)

FrameAnnotation = _reflection.GeneratedProtocolMessageType('FrameAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _FRAMEANNOTATION,
  '__module__' : 'mediapipe.modules.objectron.calculators.annotation_data_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FrameAnnotation)
  })
_sym_db.RegisterMessage(FrameAnnotation)

Sequence = _reflection.GeneratedProtocolMessageType('Sequence', (_message.Message,), {
  'DESCRIPTOR' : _SEQUENCE,
  '__module__' : 'mediapipe.modules.objectron.calculators.annotation_data_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Sequence)
  })
_sym_db.RegisterMessage(Sequence)


# @@protoc_insertion_point(module_scope)
