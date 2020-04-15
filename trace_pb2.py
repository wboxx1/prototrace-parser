# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trace.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trace.proto',
  package='prototrace',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0btrace.proto\x12\nprototrace\"\xd4\x04\n\x05Trace\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x11\x12\x11\n\tscan_name\x18\x02 \x01(\t\x12\x17\n\x0fstart_frequency\x18\x03 \x01(\x01\x12\x16\n\x0estop_frequency\x18\x04 \x01(\x01\x12\x1c\n\x14resolution_bandwidth\x18\x05 \x01(\x01\x12\x17\n\x0fvideo_bandwidth\x18\x06 \x01(\x01\x12\x17\n\x0freference_level\x18\x07 \x01(\x11\x12\x14\n\x0csweep_points\x18\x08 \x01(\x05\x12\x17\n\x0f\x61uto_sweep_time\x18\t \x01(\x05\x12\x12\n\nsweep_time\x18\n \x01(\x05\x12\x19\n\x11single_sweep_mode\x18\x0b \x01(\x05\x12\x18\n\x10number_of_sweeps\x18\x0c \x01(\x05\x12\x12\n\ndwell_time\x18\r \x01(\x05\x12\x10\n\x08\x63oupling\x18\x0e \x01(\x05\x12\x15\n\rpre_amp_state\x18\x0f \x01(\x05\x12\x13\n\x0b\x61ttenuation\x18\x10 \x01(\x05\x12\x18\n\x10\x61uto_attenuation\x18\x11 \x01(\x05\x12\x16\n\x0e\x61ntenna_offset\x18\x12 \x01(\x05\x12\x15\n\rdetector_type\x18\x13 \x01(\x05\x12\x12\n\ntrace_type\x18\x14 \x01(\x05\x12\x10\n\x08latitude\x18\x15 \x01(\x01\x12\x11\n\tlongitude\x18\x16 \x01(\x01\x12\x0f\n\x07\x61zimuth\x18\x17 \x01(\x05\x12\x11\n\televation\x18\x18 \x01(\x05\x12\x1d\n\x15measurement_date_time\x18\x19 \x01(\t\x12\x1a\n\x12significant_digits\x18\x1a \x01(\tb\x06proto3'
)




_TRACE = _descriptor.Descriptor(
  name='Trace',
  full_name='prototrace.Trace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='prototrace.Trace.data', index=0,
      number=1, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_name', full_name='prototrace.Trace.scan_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_frequency', full_name='prototrace.Trace.start_frequency', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_frequency', full_name='prototrace.Trace.stop_frequency', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resolution_bandwidth', full_name='prototrace.Trace.resolution_bandwidth', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_bandwidth', full_name='prototrace.Trace.video_bandwidth', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reference_level', full_name='prototrace.Trace.reference_level', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sweep_points', full_name='prototrace.Trace.sweep_points', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_sweep_time', full_name='prototrace.Trace.auto_sweep_time', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sweep_time', full_name='prototrace.Trace.sweep_time', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='single_sweep_mode', full_name='prototrace.Trace.single_sweep_mode', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_of_sweeps', full_name='prototrace.Trace.number_of_sweeps', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dwell_time', full_name='prototrace.Trace.dwell_time', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coupling', full_name='prototrace.Trace.coupling', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pre_amp_state', full_name='prototrace.Trace.pre_amp_state', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attenuation', full_name='prototrace.Trace.attenuation', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_attenuation', full_name='prototrace.Trace.auto_attenuation', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='antenna_offset', full_name='prototrace.Trace.antenna_offset', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detector_type', full_name='prototrace.Trace.detector_type', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_type', full_name='prototrace.Trace.trace_type', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='prototrace.Trace.latitude', index=20,
      number=21, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='prototrace.Trace.longitude', index=21,
      number=22, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='azimuth', full_name='prototrace.Trace.azimuth', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elevation', full_name='prototrace.Trace.elevation', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measurement_date_time', full_name='prototrace.Trace.measurement_date_time', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='significant_digits', full_name='prototrace.Trace.significant_digits', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=28,
  serialized_end=624,
)

DESCRIPTOR.message_types_by_name['Trace'] = _TRACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Trace = _reflection.GeneratedProtocolMessageType('Trace', (_message.Message,), {
  'DESCRIPTOR' : _TRACE,
  '__module__' : 'trace_pb2'
  # @@protoc_insertion_point(class_scope:prototrace.Trace)
  })
_sym_db.RegisterMessage(Trace)


# @@protoc_insertion_point(module_scope)