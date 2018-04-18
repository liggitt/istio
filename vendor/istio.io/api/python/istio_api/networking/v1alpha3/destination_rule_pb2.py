# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: networking/v1alpha3/destination_rule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='networking/v1alpha3/destination_rule.proto',
  package='istio.networking.v1alpha3',
  syntax='proto3',
  serialized_pb=_b('\n*networking/v1alpha3/destination_rule.proto\x12\x19istio.networking.v1alpha3\x1a\x1egoogle/protobuf/duration.proto\"\xa3\x01\n\x0f\x44\x65stinationRule\x12\x0c\n\x04host\x18\x01 \x01(\t\x12@\n\x0etraffic_policy\x18\x02 \x01(\x0b\x32(.istio.networking.v1alpha3.TrafficPolicy\x12\x32\n\x07subsets\x18\x03 \x03(\x0b\x32!.istio.networking.v1alpha3.Subset\x12\x0c\n\x04name\x18\x04 \x01(\t\"\xa0\x02\n\rTrafficPolicy\x12\x46\n\rload_balancer\x18\x01 \x01(\x0b\x32/.istio.networking.v1alpha3.LoadBalancerSettings\x12J\n\x0f\x63onnection_pool\x18\x02 \x01(\x0b\x32\x31.istio.networking.v1alpha3.ConnectionPoolSettings\x12\x46\n\x11outlier_detection\x18\x03 \x01(\x0b\x32+.istio.networking.v1alpha3.OutlierDetection\x12\x33\n\x03tls\x18\x04 \x01(\x0b\x32&.istio.networking.v1alpha3.TLSSettings\"\xc6\x01\n\x06Subset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12=\n\x06labels\x18\x02 \x03(\x0b\x32-.istio.networking.v1alpha3.Subset.LabelsEntry\x12@\n\x0etraffic_policy\x18\x03 \x01(\x0b\x32(.istio.networking.v1alpha3.TrafficPolicy\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xda\x02\n\x14LoadBalancerSettings\x12J\n\x06simple\x18\x01 \x01(\x0e\x32\x38.istio.networking.v1alpha3.LoadBalancerSettings.SimpleLBH\x00\x12[\n\x0f\x63onsistent_hash\x18\x02 \x01(\x0b\x32@.istio.networking.v1alpha3.LoadBalancerSettings.ConsistentHashLBH\x00\x1a\x42\n\x10\x43onsistentHashLB\x12\x13\n\x0bhttp_header\x18\x01 \x01(\t\x12\x19\n\x11minimum_ring_size\x18\x02 \x01(\r\"H\n\x08SimpleLB\x12\x0f\n\x0bROUND_ROBIN\x10\x00\x12\x0e\n\nLEAST_CONN\x10\x01\x12\n\n\x06RANDOM\x10\x02\x12\x0f\n\x0bPASSTHROUGH\x10\x03\x42\x0b\n\tlb_policy\"\x99\x03\n\x16\x43onnectionPoolSettings\x12J\n\x03tcp\x18\x01 \x01(\x0b\x32=.istio.networking.v1alpha3.ConnectionPoolSettings.TCPSettings\x12L\n\x04http\x18\x02 \x01(\x0b\x32>.istio.networking.v1alpha3.ConnectionPoolSettings.HTTPSettings\x1aZ\n\x0bTCPSettings\x12\x17\n\x0fmax_connections\x18\x01 \x01(\x05\x12\x32\n\x0f\x63onnect_timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x1a\x88\x01\n\x0cHTTPSettings\x12\"\n\x1ahttp1_max_pending_requests\x18\x01 \x01(\x05\x12\x1a\n\x12http2_max_requests\x18\x02 \x01(\x05\x12#\n\x1bmax_requests_per_connection\x18\x03 \x01(\x05\x12\x13\n\x0bmax_retries\x18\x04 \x01(\x05\"\x89\x02\n\x10OutlierDetection\x12\x46\n\x04http\x18\x01 \x01(\x0b\x32\x38.istio.networking.v1alpha3.OutlierDetection.HTTPSettings\x1a\xac\x01\n\x0cHTTPSettings\x12\x1a\n\x12\x63onsecutive_errors\x18\x01 \x01(\x05\x12+\n\x08interval\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x35\n\x12\x62\x61se_ejection_time\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1c\n\x14max_ejection_percent\x18\x04 \x01(\x05\"\xed\x01\n\x0bTLSSettings\x12<\n\x04mode\x18\x01 \x01(\x0e\x32..istio.networking.v1alpha3.TLSSettings.TLSmode\x12\x1a\n\x12\x63lient_certificate\x18\x02 \x01(\t\x12\x13\n\x0bprivate_key\x18\x03 \x01(\t\x12\x17\n\x0f\x63\x61_certificates\x18\x04 \x01(\t\x12\x19\n\x11subject_alt_names\x18\x05 \x03(\t\x12\x0b\n\x03sni\x18\x06 \x01(\t\".\n\x07TLSmode\x12\x0b\n\x07\x44ISABLE\x10\x00\x12\n\n\x06SIMPLE\x10\x01\x12\n\n\x06MUTUAL\x10\x02\x42\"Z istio.io/api/networking/v1alpha3b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])



_LOADBALANCERSETTINGS_SIMPLELB = _descriptor.EnumDescriptor(
  name='SimpleLB',
  full_name='istio.networking.v1alpha3.LoadBalancerSettings.SimpleLB',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROUND_ROBIN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEAST_CONN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANDOM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASSTHROUGH', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1025,
  serialized_end=1097,
)
_sym_db.RegisterEnumDescriptor(_LOADBALANCERSETTINGS_SIMPLELB)

_TLSSETTINGS_TLSMODE = _descriptor.EnumDescriptor(
  name='TLSmode',
  full_name='istio.networking.v1alpha3.TLSSettings.TLSmode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISABLE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIMPLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUTUAL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1984,
  serialized_end=2030,
)
_sym_db.RegisterEnumDescriptor(_TLSSETTINGS_TLSMODE)


_DESTINATIONRULE = _descriptor.Descriptor(
  name='DestinationRule',
  full_name='istio.networking.v1alpha3.DestinationRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='istio.networking.v1alpha3.DestinationRule.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='traffic_policy', full_name='istio.networking.v1alpha3.DestinationRule.traffic_policy', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subsets', full_name='istio.networking.v1alpha3.DestinationRule.subsets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='istio.networking.v1alpha3.DestinationRule.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=269,
)


_TRAFFICPOLICY = _descriptor.Descriptor(
  name='TrafficPolicy',
  full_name='istio.networking.v1alpha3.TrafficPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='load_balancer', full_name='istio.networking.v1alpha3.TrafficPolicy.load_balancer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_pool', full_name='istio.networking.v1alpha3.TrafficPolicy.connection_pool', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outlier_detection', full_name='istio.networking.v1alpha3.TrafficPolicy.outlier_detection', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tls', full_name='istio.networking.v1alpha3.TrafficPolicy.tls', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=560,
)


_SUBSET_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='istio.networking.v1alpha3.Subset.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.networking.v1alpha3.Subset.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.networking.v1alpha3.Subset.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=716,
  serialized_end=761,
)

_SUBSET = _descriptor.Descriptor(
  name='Subset',
  full_name='istio.networking.v1alpha3.Subset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='istio.networking.v1alpha3.Subset.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='istio.networking.v1alpha3.Subset.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='traffic_policy', full_name='istio.networking.v1alpha3.Subset.traffic_policy', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SUBSET_LABELSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=563,
  serialized_end=761,
)


_LOADBALANCERSETTINGS_CONSISTENTHASHLB = _descriptor.Descriptor(
  name='ConsistentHashLB',
  full_name='istio.networking.v1alpha3.LoadBalancerSettings.ConsistentHashLB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_header', full_name='istio.networking.v1alpha3.LoadBalancerSettings.ConsistentHashLB.http_header', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimum_ring_size', full_name='istio.networking.v1alpha3.LoadBalancerSettings.ConsistentHashLB.minimum_ring_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=957,
  serialized_end=1023,
)

_LOADBALANCERSETTINGS = _descriptor.Descriptor(
  name='LoadBalancerSettings',
  full_name='istio.networking.v1alpha3.LoadBalancerSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simple', full_name='istio.networking.v1alpha3.LoadBalancerSettings.simple', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consistent_hash', full_name='istio.networking.v1alpha3.LoadBalancerSettings.consistent_hash', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOADBALANCERSETTINGS_CONSISTENTHASHLB, ],
  enum_types=[
    _LOADBALANCERSETTINGS_SIMPLELB,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='lb_policy', full_name='istio.networking.v1alpha3.LoadBalancerSettings.lb_policy',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=764,
  serialized_end=1110,
)


_CONNECTIONPOOLSETTINGS_TCPSETTINGS = _descriptor.Descriptor(
  name='TCPSettings',
  full_name='istio.networking.v1alpha3.ConnectionPoolSettings.TCPSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_connections', full_name='istio.networking.v1alpha3.ConnectionPoolSettings.TCPSettings.max_connections', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connect_timeout', full_name='istio.networking.v1alpha3.ConnectionPoolSettings.TCPSettings.connect_timeout', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1293,
  serialized_end=1383,
)

_CONNECTIONPOOLSETTINGS_HTTPSETTINGS = _descriptor.Descriptor(
  name='HTTPSettings',
  full_name='istio.networking.v1alpha3.ConnectionPoolSettings.HTTPSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='http1_max_pending_requests', full_name='istio.networking.v1alpha3.ConnectionPoolSettings.HTTPSettings.http1_max_pending_requests', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http2_max_requests', full_name='istio.networking.v1alpha3.ConnectionPoolSettings.HTTPSettings.http2_max_requests', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_requests_per_connection', full_name='istio.networking.v1alpha3.ConnectionPoolSettings.HTTPSettings.max_requests_per_connection', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_retries', full_name='istio.networking.v1alpha3.ConnectionPoolSettings.HTTPSettings.max_retries', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1386,
  serialized_end=1522,
)

_CONNECTIONPOOLSETTINGS = _descriptor.Descriptor(
  name='ConnectionPoolSettings',
  full_name='istio.networking.v1alpha3.ConnectionPoolSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tcp', full_name='istio.networking.v1alpha3.ConnectionPoolSettings.tcp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http', full_name='istio.networking.v1alpha3.ConnectionPoolSettings.http', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONNECTIONPOOLSETTINGS_TCPSETTINGS, _CONNECTIONPOOLSETTINGS_HTTPSETTINGS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1113,
  serialized_end=1522,
)


_OUTLIERDETECTION_HTTPSETTINGS = _descriptor.Descriptor(
  name='HTTPSettings',
  full_name='istio.networking.v1alpha3.OutlierDetection.HTTPSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='consecutive_errors', full_name='istio.networking.v1alpha3.OutlierDetection.HTTPSettings.consecutive_errors', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='istio.networking.v1alpha3.OutlierDetection.HTTPSettings.interval', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_ejection_time', full_name='istio.networking.v1alpha3.OutlierDetection.HTTPSettings.base_ejection_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_ejection_percent', full_name='istio.networking.v1alpha3.OutlierDetection.HTTPSettings.max_ejection_percent', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1618,
  serialized_end=1790,
)

_OUTLIERDETECTION = _descriptor.Descriptor(
  name='OutlierDetection',
  full_name='istio.networking.v1alpha3.OutlierDetection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='http', full_name='istio.networking.v1alpha3.OutlierDetection.http', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OUTLIERDETECTION_HTTPSETTINGS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1525,
  serialized_end=1790,
)


_TLSSETTINGS = _descriptor.Descriptor(
  name='TLSSettings',
  full_name='istio.networking.v1alpha3.TLSSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='istio.networking.v1alpha3.TLSSettings.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_certificate', full_name='istio.networking.v1alpha3.TLSSettings.client_certificate', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private_key', full_name='istio.networking.v1alpha3.TLSSettings.private_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ca_certificates', full_name='istio.networking.v1alpha3.TLSSettings.ca_certificates', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subject_alt_names', full_name='istio.networking.v1alpha3.TLSSettings.subject_alt_names', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sni', full_name='istio.networking.v1alpha3.TLSSettings.sni', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TLSSETTINGS_TLSMODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1793,
  serialized_end=2030,
)

_DESTINATIONRULE.fields_by_name['traffic_policy'].message_type = _TRAFFICPOLICY
_DESTINATIONRULE.fields_by_name['subsets'].message_type = _SUBSET
_TRAFFICPOLICY.fields_by_name['load_balancer'].message_type = _LOADBALANCERSETTINGS
_TRAFFICPOLICY.fields_by_name['connection_pool'].message_type = _CONNECTIONPOOLSETTINGS
_TRAFFICPOLICY.fields_by_name['outlier_detection'].message_type = _OUTLIERDETECTION
_TRAFFICPOLICY.fields_by_name['tls'].message_type = _TLSSETTINGS
_SUBSET_LABELSENTRY.containing_type = _SUBSET
_SUBSET.fields_by_name['labels'].message_type = _SUBSET_LABELSENTRY
_SUBSET.fields_by_name['traffic_policy'].message_type = _TRAFFICPOLICY
_LOADBALANCERSETTINGS_CONSISTENTHASHLB.containing_type = _LOADBALANCERSETTINGS
_LOADBALANCERSETTINGS.fields_by_name['simple'].enum_type = _LOADBALANCERSETTINGS_SIMPLELB
_LOADBALANCERSETTINGS.fields_by_name['consistent_hash'].message_type = _LOADBALANCERSETTINGS_CONSISTENTHASHLB
_LOADBALANCERSETTINGS_SIMPLELB.containing_type = _LOADBALANCERSETTINGS
_LOADBALANCERSETTINGS.oneofs_by_name['lb_policy'].fields.append(
  _LOADBALANCERSETTINGS.fields_by_name['simple'])
_LOADBALANCERSETTINGS.fields_by_name['simple'].containing_oneof = _LOADBALANCERSETTINGS.oneofs_by_name['lb_policy']
_LOADBALANCERSETTINGS.oneofs_by_name['lb_policy'].fields.append(
  _LOADBALANCERSETTINGS.fields_by_name['consistent_hash'])
_LOADBALANCERSETTINGS.fields_by_name['consistent_hash'].containing_oneof = _LOADBALANCERSETTINGS.oneofs_by_name['lb_policy']
_CONNECTIONPOOLSETTINGS_TCPSETTINGS.fields_by_name['connect_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CONNECTIONPOOLSETTINGS_TCPSETTINGS.containing_type = _CONNECTIONPOOLSETTINGS
_CONNECTIONPOOLSETTINGS_HTTPSETTINGS.containing_type = _CONNECTIONPOOLSETTINGS
_CONNECTIONPOOLSETTINGS.fields_by_name['tcp'].message_type = _CONNECTIONPOOLSETTINGS_TCPSETTINGS
_CONNECTIONPOOLSETTINGS.fields_by_name['http'].message_type = _CONNECTIONPOOLSETTINGS_HTTPSETTINGS
_OUTLIERDETECTION_HTTPSETTINGS.fields_by_name['interval'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_OUTLIERDETECTION_HTTPSETTINGS.fields_by_name['base_ejection_time'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_OUTLIERDETECTION_HTTPSETTINGS.containing_type = _OUTLIERDETECTION
_OUTLIERDETECTION.fields_by_name['http'].message_type = _OUTLIERDETECTION_HTTPSETTINGS
_TLSSETTINGS.fields_by_name['mode'].enum_type = _TLSSETTINGS_TLSMODE
_TLSSETTINGS_TLSMODE.containing_type = _TLSSETTINGS
DESCRIPTOR.message_types_by_name['DestinationRule'] = _DESTINATIONRULE
DESCRIPTOR.message_types_by_name['TrafficPolicy'] = _TRAFFICPOLICY
DESCRIPTOR.message_types_by_name['Subset'] = _SUBSET
DESCRIPTOR.message_types_by_name['LoadBalancerSettings'] = _LOADBALANCERSETTINGS
DESCRIPTOR.message_types_by_name['ConnectionPoolSettings'] = _CONNECTIONPOOLSETTINGS
DESCRIPTOR.message_types_by_name['OutlierDetection'] = _OUTLIERDETECTION
DESCRIPTOR.message_types_by_name['TLSSettings'] = _TLSSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DestinationRule = _reflection.GeneratedProtocolMessageType('DestinationRule', (_message.Message,), dict(
  DESCRIPTOR = _DESTINATIONRULE,
  __module__ = 'networking.v1alpha3.destination_rule_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.DestinationRule)
  ))
_sym_db.RegisterMessage(DestinationRule)

TrafficPolicy = _reflection.GeneratedProtocolMessageType('TrafficPolicy', (_message.Message,), dict(
  DESCRIPTOR = _TRAFFICPOLICY,
  __module__ = 'networking.v1alpha3.destination_rule_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.TrafficPolicy)
  ))
_sym_db.RegisterMessage(TrafficPolicy)

Subset = _reflection.GeneratedProtocolMessageType('Subset', (_message.Message,), dict(

  LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SUBSET_LABELSENTRY,
    __module__ = 'networking.v1alpha3.destination_rule_pb2'
    # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.Subset.LabelsEntry)
    ))
  ,
  DESCRIPTOR = _SUBSET,
  __module__ = 'networking.v1alpha3.destination_rule_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.Subset)
  ))
_sym_db.RegisterMessage(Subset)
_sym_db.RegisterMessage(Subset.LabelsEntry)

LoadBalancerSettings = _reflection.GeneratedProtocolMessageType('LoadBalancerSettings', (_message.Message,), dict(

  ConsistentHashLB = _reflection.GeneratedProtocolMessageType('ConsistentHashLB', (_message.Message,), dict(
    DESCRIPTOR = _LOADBALANCERSETTINGS_CONSISTENTHASHLB,
    __module__ = 'networking.v1alpha3.destination_rule_pb2'
    # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.LoadBalancerSettings.ConsistentHashLB)
    ))
  ,
  DESCRIPTOR = _LOADBALANCERSETTINGS,
  __module__ = 'networking.v1alpha3.destination_rule_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.LoadBalancerSettings)
  ))
_sym_db.RegisterMessage(LoadBalancerSettings)
_sym_db.RegisterMessage(LoadBalancerSettings.ConsistentHashLB)

ConnectionPoolSettings = _reflection.GeneratedProtocolMessageType('ConnectionPoolSettings', (_message.Message,), dict(

  TCPSettings = _reflection.GeneratedProtocolMessageType('TCPSettings', (_message.Message,), dict(
    DESCRIPTOR = _CONNECTIONPOOLSETTINGS_TCPSETTINGS,
    __module__ = 'networking.v1alpha3.destination_rule_pb2'
    # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.ConnectionPoolSettings.TCPSettings)
    ))
  ,

  HTTPSettings = _reflection.GeneratedProtocolMessageType('HTTPSettings', (_message.Message,), dict(
    DESCRIPTOR = _CONNECTIONPOOLSETTINGS_HTTPSETTINGS,
    __module__ = 'networking.v1alpha3.destination_rule_pb2'
    # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.ConnectionPoolSettings.HTTPSettings)
    ))
  ,
  DESCRIPTOR = _CONNECTIONPOOLSETTINGS,
  __module__ = 'networking.v1alpha3.destination_rule_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.ConnectionPoolSettings)
  ))
_sym_db.RegisterMessage(ConnectionPoolSettings)
_sym_db.RegisterMessage(ConnectionPoolSettings.TCPSettings)
_sym_db.RegisterMessage(ConnectionPoolSettings.HTTPSettings)

OutlierDetection = _reflection.GeneratedProtocolMessageType('OutlierDetection', (_message.Message,), dict(

  HTTPSettings = _reflection.GeneratedProtocolMessageType('HTTPSettings', (_message.Message,), dict(
    DESCRIPTOR = _OUTLIERDETECTION_HTTPSETTINGS,
    __module__ = 'networking.v1alpha3.destination_rule_pb2'
    # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.OutlierDetection.HTTPSettings)
    ))
  ,
  DESCRIPTOR = _OUTLIERDETECTION,
  __module__ = 'networking.v1alpha3.destination_rule_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.OutlierDetection)
  ))
_sym_db.RegisterMessage(OutlierDetection)
_sym_db.RegisterMessage(OutlierDetection.HTTPSettings)

TLSSettings = _reflection.GeneratedProtocolMessageType('TLSSettings', (_message.Message,), dict(
  DESCRIPTOR = _TLSSETTINGS,
  __module__ = 'networking.v1alpha3.destination_rule_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.TLSSettings)
  ))
_sym_db.RegisterMessage(TLSSettings)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z istio.io/api/networking/v1alpha3'))
_SUBSET_LABELSENTRY.has_options = True
_SUBSET_LABELSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)