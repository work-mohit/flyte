# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/plugins/sagemaker/training_job.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-flyteidl/plugins/sagemaker/training_job.proto\x12\x1a\x66lyteidl.plugins.sagemaker\x1a\x1egoogle/protobuf/duration.proto\"(\n\tInputMode\"\x1b\n\x05Value\x12\x08\n\x04\x46ILE\x10\x00\x12\x08\n\x04PIPE\x10\x01\"1\n\rAlgorithmName\" \n\x05Value\x12\n\n\x06\x43USTOM\x10\x00\x12\x0b\n\x07XGBOOST\x10\x01\")\n\x10InputContentType\"\x15\n\x05Value\x12\x0c\n\x08TEXT_CSV\x10\x00\"<\n\x10MetricDefinition\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05regex\x18\x02 \x01(\tR\x05regex\"\xa8\x03\n\x16\x41lgorithmSpecification\x12J\n\ninput_mode\x18\x01 \x01(\x0e\x32+.flyteidl.plugins.sagemaker.InputMode.ValueR\tinputMode\x12V\n\x0e\x61lgorithm_name\x18\x02 \x01(\x0e\x32/.flyteidl.plugins.sagemaker.AlgorithmName.ValueR\ralgorithmName\x12+\n\x11\x61lgorithm_version\x18\x03 \x01(\tR\x10\x61lgorithmVersion\x12[\n\x12metric_definitions\x18\x04 \x03(\x0b\x32,.flyteidl.plugins.sagemaker.MetricDefinitionR\x11metricDefinitions\x12`\n\x12input_content_type\x18\x05 \x01(\x0e\x32\x32.flyteidl.plugins.sagemaker.InputContentType.ValueR\x10inputContentType\"8\n\x13\x44istributedProtocol\"!\n\x05Value\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x07\n\x03MPI\x10\x01\"\xfc\x01\n\x19TrainingJobResourceConfig\x12%\n\x0einstance_count\x18\x01 \x01(\x03R\rinstanceCount\x12#\n\rinstance_type\x18\x02 \x01(\tR\x0cinstanceType\x12)\n\x11volume_size_in_gb\x18\x03 \x01(\x03R\x0evolumeSizeInGb\x12h\n\x14\x64istributed_protocol\x18\x04 \x01(\x0e\x32\x35.flyteidl.plugins.sagemaker.DistributedProtocol.ValueR\x13\x64istributedProtocol\"\xf2\x01\n\x0bTrainingJob\x12k\n\x17\x61lgorithm_specification\x18\x01 \x01(\x0b\x32\x32.flyteidl.plugins.sagemaker.AlgorithmSpecificationR\x16\x61lgorithmSpecification\x12v\n\x1ctraining_job_resource_config\x18\x02 \x01(\x0b\x32\x35.flyteidl.plugins.sagemaker.TrainingJobResourceConfigR\x19trainingJobResourceConfigB\xfb\x01\n\x1e\x63om.flyteidl.plugins.sagemakerB\x10TrainingJobProtoP\x01Z=github.com/flyteorg/flyte/flyteidl/gen/pb-go/flyteidl/plugins\xa2\x02\x03\x46PS\xaa\x02\x1a\x46lyteidl.Plugins.Sagemaker\xca\x02\x1a\x46lyteidl\\Plugins\\Sagemaker\xe2\x02&Flyteidl\\Plugins\\Sagemaker\\GPBMetadata\xea\x02\x1c\x46lyteidl::Plugins::Sagemakerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flyteidl.plugins.sagemaker.training_job_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.flyteidl.plugins.sagemakerB\020TrainingJobProtoP\001Z=github.com/flyteorg/flyte/flyteidl/gen/pb-go/flyteidl/plugins\242\002\003FPS\252\002\032Flyteidl.Plugins.Sagemaker\312\002\032Flyteidl\\Plugins\\Sagemaker\342\002&Flyteidl\\Plugins\\Sagemaker\\GPBMetadata\352\002\034Flyteidl::Plugins::Sagemaker'
  _globals['_INPUTMODE']._serialized_start=109
  _globals['_INPUTMODE']._serialized_end=149
  _globals['_INPUTMODE_VALUE']._serialized_start=122
  _globals['_INPUTMODE_VALUE']._serialized_end=149
  _globals['_ALGORITHMNAME']._serialized_start=151
  _globals['_ALGORITHMNAME']._serialized_end=200
  _globals['_ALGORITHMNAME_VALUE']._serialized_start=168
  _globals['_ALGORITHMNAME_VALUE']._serialized_end=200
  _globals['_INPUTCONTENTTYPE']._serialized_start=202
  _globals['_INPUTCONTENTTYPE']._serialized_end=243
  _globals['_INPUTCONTENTTYPE_VALUE']._serialized_start=222
  _globals['_INPUTCONTENTTYPE_VALUE']._serialized_end=243
  _globals['_METRICDEFINITION']._serialized_start=245
  _globals['_METRICDEFINITION']._serialized_end=305
  _globals['_ALGORITHMSPECIFICATION']._serialized_start=308
  _globals['_ALGORITHMSPECIFICATION']._serialized_end=732
  _globals['_DISTRIBUTEDPROTOCOL']._serialized_start=734
  _globals['_DISTRIBUTEDPROTOCOL']._serialized_end=790
  _globals['_DISTRIBUTEDPROTOCOL_VALUE']._serialized_start=757
  _globals['_DISTRIBUTEDPROTOCOL_VALUE']._serialized_end=790
  _globals['_TRAININGJOBRESOURCECONFIG']._serialized_start=793
  _globals['_TRAININGJOBRESOURCECONFIG']._serialized_end=1045
  _globals['_TRAININGJOB']._serialized_start=1048
  _globals['_TRAININGJOB']._serialized_end=1290
# @@protoc_insertion_point(module_scope)
