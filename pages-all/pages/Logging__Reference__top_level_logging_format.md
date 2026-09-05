# Logging Format Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/top_level_logging_format.htm
- Fetched: 2026-09-05 02:37 CDT

# Logging Format Overview

Details for the top-level Oracle Cloud Infrastructure Logging format.
Every log line is normalized into a common event format for ease of correlation. This format is based on the[JSON implementation of CloudEvents v1.0](https://github.com/cloudevents/spec/blob/v1.0/json-format.md)specification. A log line has three key sections:
- Unified envelope
- Oracle-specific metadata (oracle.*)
- Contents of the log line (data)

## Outer Envelope Format

All messages sent to the ingestion front end use the outer envelope format, and only change the message body based on the log type. The outer envelope format conforms to the[CloudEvents v1.0 spec](https://github.com/cloudevents/spec/blob/v1.0/spec.md), with extension fields defined for logging purposes. The following table describes this format.

Name Required Position Type Description
Specification Version Yes Body: specversion String The version of the CloudEvents specification this message conforms to.
Id Yes Body: id String A source-unique identifier for this message. Duplicate messages can have the same ID. Consumers can assume events with the same IDs are unique.
Type Yes Body: type String The type of the message. Consumers use the`type`and`specversion`to determine how to interpret the body. Pattern:`com.oraclecloud.{service}.{resource-type}.{category}`. For example:`com.oraclecloud.compute.instance.terminated`
Source Yes Body: source URI-reference

The message source.

When emitted by a service, refers to the name of the resource that generated the message, for example, the Object Storage bucket name, Instance Name.

When emitted by an agent, based on the source/input used to read events. For example, the instance name (not the OCID) or the hostname of the asset in an on-premise environment.
Subject No Body: subject String

A specific subresource that generated the event, if applicable to the source. This is useful for sources with subresources. Examples:
- 

Object Storage example:
```

```

```

```

- 

Custom Logging example:
```

```

```

```

Time No Body: time Timestamp The time the message was generated. If present, must adhere to the format specified in[RFC 3339](https://tools.ietf.org/html/rfc3339). If not provided, the wall clock of the ingestion host that receives the request is used.
Data Schema No Body: dataschema String The schema version for the`data`field. This is not required, and if not provided, is assumed to be the initial version.
Data Content Type No Body: datacontenttype String The format in which the message body is encoded. If not provided, the default is JSON (equivalent to`datacontenttype: application/json`).
Message Body Yes Body: data Object The message body encoded in the format defined by`datacontenttype`. If`datacontenttype`is not specified, this is expected to be JSON (equivalent to`datacontenttype: application/json`).
Oracle Cloud Metadata Yes Body: oracle Object More Oracle-specific metadata is provided in a map of attributes at the top level of the envelope. This conforms to[CloudEvents v1 Attribute Extensions](https://github.com/cloudevents/spec/blob/main/cloudevents/primer.md#cloudevents-extension-attributes)specification. See the following table for supported Oracle Cloud Infrastructure metadata attributes.

## Oracle Metadata Attributes

The following attributes are supported in the`oci`extension field of the message format. Naming for these attributes conforms to the[CloudEvents v1 Attribute Naming Convention](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md#context-attributes), that is, they are lowercase alpha-numeric identifiers fewer than 20 characters long.

Name Required for Ingestion Enriched for Retrieval Type Description
logid Yes - String The OCID of the log object the message was sent to.
loggroupid No Yes String The OCID of the log group the object resides in.
tenantid No Yes String The OCID of the tenant that owns the log object.
