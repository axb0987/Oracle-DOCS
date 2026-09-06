# Audit Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html#dcoc-content-body)

## Audit Common Types

### DBMS_CLOUD_OCI_AUDIT_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_AUDIT_IDENTITY_T Type

A container object for identity attributes.

Syntax
```

```

Fields

Field Description

`principal_name`

(optional) The name of the user or service. This value is the friendly name associated with `principalId`. Example: `ExampleName`

`principal_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the principal.

`auth_type`

(optional) The type of authentication used. Example: `natv`

`caller_name`

(optional) The name of the user or service. This value is the friendly name associated with `callerId`.

`caller_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the caller. The caller that made a request on behalf of the prinicpal.

`tenant_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenant.

`ip_address`

(optional) The IP address of the source of the request. Example: `172.24.80.88`

`credentials`

(optional) The credential ID of the user. This value is extracted from the HTTP 'Authorization' request header. It consists of the tenantId, userId, and user fingerprint, all delimited by a slash (/).

`user_agent`

(optional) The user agent of the client that made the request. Example: `Jersey/2.23 (HttpUrlConnection 1.8.0_212)`

`console_session_id`

(optional) This value identifies any Console session associated with this request.

### DBMS_CLOUD_OCI_AUDIT_REQUEST_T Type

A container object for request attributes.

Syntax
```

```

Fields

Field Description

`id`

(optional) The opc-request-id of the request.

`path`

(optional) The full path of the API request. Example: `/20160918/instances/ocid1.instance.oc1.phx.&lt;unique_ID&gt;`

`action`

(optional) The HTTP method of the request. Example: `GET`

`parameters`

(optional) The parameters supplied by the caller during this operation.

`headers`

(optional) The HTTP header fields and values in the request. Example: ----- { \"opc-principal\": [ \"{\\\"tenantId\\\":\\\"ocid1.tenancy.oc1..&lt;unique_ID&gt;\\\",\\\"subjectId\\\":\\\"ocid1.user.oc1..&lt;unique_ID&gt;\\\",\\\"claims\\\":[{\\\"key\\\":\\\"pstype\\\",\\\"value\\\":\\\"natv\\\",\\\"issuer\\\":\\\"authService.oracle.com\\\"},{\\\"key\\\":\\\"h_host\\\",\\\"value\\\":\\\"iaas.r2.oracleiaas.com\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_opc-request-id\\\",\\\"value\\\":\\\"&lt;unique_ID&gt;\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"ptype\\\",\\\"value\\\":\\\"user\\\",\\\"issuer\\\":\\\"authService.oracle.com\\\"},{\\\"key\\\":\\\"h_date\\\",\\\"value\\\":\\\"Wed, 18 Sep 2019 00:10:58 UTC\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_accept\\\",\\\"value\\\":\\\"application/json\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"authorization\\\",\\\"value\\\":\\\"Signature headers=\\\\\\\"date (request-target) host accept opc-request-id\\\\\\\",keyId=\\\\\\\"ocid1.tenancy.oc1..&lt;unique_ID&gt;/ocid1.user.oc1..&lt;unique_ID&gt;/8c:b4:5f:18:e7:ec:db:08:b8:fa:d2:2a:7d:11:76:ac\\\\\\\",algorithm=\\\\\\\"rsa-pss-sha256\\\\\\\",signature=\\\\\\\"&lt;unique_ID&gt;\\\\\\\",version=\\\\\\\"1\\\\\\\"\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_(request-target)\\\",\\\"value\\\":\\\"get /20160918/instances/ocid1.instance.oc1.phx.&lt;unique_ID&gt;\\\",\\\"issuer\\\":\\\"h\\\"}]}\" ], \"Accept\": [ \"application/json\" ], \"X-Oracle-Auth-Client-CN\": [ \"splat-proxy-se-02302.node.ad2.r2\" ], \"X-Forwarded-Host\": [ \"compute-api.svc.ad1.r2\" ], \"Connection\": [ \"close\" ], \"User-Agent\": [ \"Jersey/2.23 (HttpUrlConnection 1.8.0_212)\" ], \"X-Forwarded-For\": [ \"172.24.80.88\" ], \"X-Real-IP\": [ \"172.24.80.88\" ], \"oci-original-url\": [ \"https://iaas.r2.oracleiaas.com/20160918/instances/ocid1.instance.oc1.phx.&lt;unique_ID&gt;\" ], \"opc-request-id\": [ \"&lt;unique_ID&gt;\" ], \"Date\": [ \"Wed, 18 Sep 2019 00:10:58 UTC\" ] } -----

### DBMS_CLOUD_OCI_AUDIT_RESPONSE_T Type

A container object for response attributes.

Syntax
```

```

Fields

Field Description

`status`

(optional) The status code of the response. Example: `200`

`response_time`

(optional) The time of the response to the audited request, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-09-18T00:10:59.278Z`

`headers`

(optional) The headers of the response. Example: ----- { \"ETag\": [ \"&lt;unique_ID&gt;\" ], \"Connection\": [ \"close\" ], \"Content-Length\": [ \"1828\" ], \"opc-request-id\": [ \"&lt;unique_ID&gt;\" ], \"Date\": [ \"Wed, 18 Sep 2019 00:10:59 GMT\" ], \"Content-Type\": [ \"application/json\" ] } -----

`payload`

(optional) This value is included for backward compatibility with the Audit version 1 schema, where it contained metadata of interest from the response payload. Example: ----- { \"resourceName\": \"my_instance\", \"id\": \"ocid1.instance.oc1.phx.&lt;unique_ID&gt;\" } -----

`message`

(optional) A friendly description of what happened during the operation. Use this for troubleshooting.

### DBMS_CLOUD_OCI_AUDIT_STATE_CHANGE_T Type

A container object for state change attributes.

Syntax
```

```

Fields

Field Description

`previous`

(optional) Provides the previous state of fields that may have changed during an operation. To determine how the current operation changed a resource, compare the information in this attribute to `current`.

`l_current`

(optional) Provides the current state of fields that may have changed during an operation. To determine how the current operation changed a resource, compare the information in this attribute to `previous`.

### DBMS_CLOUD_OCI_AUDIT_DATA_T Type

The payload of the event. Information within `data` comes from the resource emitting the event.

Syntax
```

```

Fields

Field Description

`event_grouping_id`

(optional) This value links multiple audit events that are part of the same API operation. For example, a long running API operations that emit an event at the start and the end of an operation would use the same value in this field for both events.

`event_name`

(optional) Name of the API operation that generated this event. Example: `GetInstance`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment of the resource emitting the event.

`compartment_name`

(optional) The name of the compartment. This value is the friendly name associated with compartmentId. This value can change, but the service logs the value that appeared at the time of the audit event. Example: `CompartmentA`

`resource_name`

(optional) The name of the resource emitting the event.

`resource_id`

(optional) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)or some other ID for the resource emitting the event.

`availability_domain`

(optional) The availability domain where the resource resides.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`identity`

(optional)

`request`

(optional)

`response`

(optional)

`state_change`

(optional)

`additional_details`

(optional) A container object for attribues unique to the resource emitting the event. Example: ----- { \"imageId\": \"ocid1.image.oc1.phx.&lt;unique_ID&gt;\", \"shape\": \"VM.Standard1.1\", \"type\": \"CustomerVmi\" } -----

### DBMS_CLOUD_OCI_AUDIT_AUDIT_EVENT_T Type

All the attributes of an audit event. For more information, see[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm).

Syntax
```

```

Fields

Field Description

`event_type`

(required) The type of event that happened. The service that produces the event can also add, remove, or change the meaning of a field. A service implementing these type changes would publish a new version of an `eventType` and revise the `eventTypeVersion` field. Example: `com.oraclecloud.ComputeApi.GetInstance`

`cloud_events_version`

(required) The version of the CloudEvents specification. The structure of the envelope follows the[CloudEvents](https://github.com/cloudevents/spec)industry standard format hosted by the[Cloud Native Computing Foundation ( CNCF)](https://www.cncf.io/). Audit uses version 0.1 specification of the CloudEvents event envelope. Example: `0.1`

`event_type_version`

(required) The version of the event type. This version applies to the payload of the event, not the envelope. Use `cloudEventsVersion` to determine the version of the envelope. Example: `2.0`

`source`

(required) The source of the event. Example: `ComputeApi`

`event_id`

(required) The GUID of the event.

`event_time`

(required) The time the event occurred, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-09-18T00:10:59.252Z`

`content_type`

(required) The content type of the data contained in `data`. Example: `application/json`

`data`

(required)

### DBMS_CLOUD_OCI_AUDIT_CONFIGURATION_T Type

The retention period setting, specified in days. For more information, see[Setting Audit Log Retention Period](https://docs.oracle.com/iaas/Content/Audit/Tasks/settingretentionperiod.htm).

Syntax
```

```

Fields

Field Description

`retention_period_days`

(optional) The retention period setting, specified in days. The minimum is 90, the maximum 365. Example: `90`

### DBMS_CLOUD_OCI_AUDIT_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm). Example: `400`

`message`

(required) A human-readable error string. Example: `InvalidParameter`

### DBMS_CLOUD_OCI_AUDIT_UPDATE_CONFIGURATION_DETAILS_T Type

The configuration details for the retention period setting, specified in days. For more information, see[Setting Audit Log Retention Period](https://docs.oracle.com/iaas/Content/Audit/Tasks/settingretentionperiod.htm).

Syntax
```

```

Fields

Field Description

`retention_period_days`

(required) The retention period setting, specified in days. The minimum is 90, the maximum 365. Example: `90`

- [Audit Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html#ADSDK-GUID-5AD367C2-63CA-4A53-85E5-6A212D6A2778)
- [DBMS_CLOUD_OCI_AUDIT_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html#ADSDK-GUID-3D0F33AA-A31F-42F8-A53E-F9C77BCC9295)
- [DBMS_CLOUD_OCI_AUDIT_IDENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html#ADSDK-GUID-363788B1-9581-4AD8-AEAE-AA455D9F9713)
- [DBMS_CLOUD_OCI_AUDIT_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html#ADSDK-GUID-5261B90D-630B-458D-8C0F-B2FC7A103CEE)
- [DBMS_CLOUD_OCI_AUDIT_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html#ADSDK-GUID-A9B2CA63-6FE2-4E9B-A06D-514E09E1E1F7)
- [DBMS_CLOUD_OCI_AUDIT_STATE_CHANGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html#ADSDK-GUID-766C767D-3901-4FDF-9E56-73DB8E555CC8)
- [DBMS_CLOUD_OCI_AUDIT_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html#ADSDK-GUID-EF3A65B3-9001-4CEF-9A28-2D7B5121629B)
- [DBMS_CLOUD_OCI_AUDIT_AUDIT_EVENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html#ADSDK-GUID-BF30EF70-BA23-4420-AD7C-1C16491A2D4C)
- [DBMS_CLOUD_OCI_AUDIT_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html#ADSDK-GUID-22267A91-E9F0-4F37-9171-4CFFD286D39D)
- [DBMS_CLOUD_OCI_AUDIT_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html#ADSDK-GUID-855C530E-3F54-490F-B4F0-245BCEB0EF8E)
- [DBMS_CLOUD_OCI_AUDIT_UPDATE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/audit_t.html#ADSDK-GUID-C230C2CB-BFD9-40BC-BB6B-54AAF9FDB0AD)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
