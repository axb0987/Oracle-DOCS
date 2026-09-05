# Contents of an Audit Log Event
- Source: https://docs.oracle.com/en-us/iaas/Content/Audit/Reference/logeventreference.htm
- Fetched: 2026-09-05 01:39 CDT

# Contents of an Audit Log Event

Describes the contents of an Audit log event.

The following explains the contents of an Audit log event. Every Audit log event includes two main parts:
- Envelopes that act as a container for all event messages
- Payloads that contain data from the resource emitting the event message

## Resource Identifiers

Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

## Event Envelope

These attributes for an event envelope are the same for all events. The structure of the envelope follows the[CloudEvents](https://github.com/cloudevents/spec)industry standard format hosted by the[Cloud Native Computing Foundation ( CNCF)](https://www.cncf.io/).

Property Description
`cloudEventsVersion`

The version of the CloudEvents specification.

Note: Audit uses version 0.1 specification of the CloudEvents event envelope.
`contentType`Set to`application/json`. The content type of the data contained in the`data`attribute.
`data`The payload of the event. Information within`data`comes from the resource emitting the event.
`eventID`

The UUID of the event. This identifier is not an OCID, but just a unique ID for the event.
`eventTime`The time of the event, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.
`eventType`

The type of event that happened.

Note: The service that produces the event can also add, remove, or change the meaning of a field. A service implementing these type changes would publish a new version of an`eventType`and revise the`eventTypeVersion`field.
`eventTypeVersion`

The version of the event type. This version applies to the payload of the event, not the envelope. Use`cloudEventsVersion`to determine the version of the envelope.
`source`The resource that produced the event. For example, an Autonomous AI Database or an Object Storage bucket.

## Payload

The data in these fields depends on which service produced the event log and the event type it defines.

### Data

The data object contains the following attributes.

Property Description
`data.additionalDetails`A container object for attributes unique to the resource emitting the event.
`data.availabilityDomain`The availability domain where the resource resides.
`data.compartmentId`The OCID of the compartment of the resource emitting the event.
`data.compartmentName`The name of the compartment of the resource emitting the event.
`data.definedTags`Defined tags added to the resource emitting the event.
`data.eventGroupingId`

This value links multiple audit events that are part of the same API operation. For example, a long running API operation that emits an event at the start and the end of the operation.
`data.eventName`

Name of the API operation that generated this event.

Example:`LaunchInstance`
`data.freeformTags`Free-form tags added to the resource emitting the event.
`data.identity`A container object for identity attributes. See[Identity](https://docs.oracle.com/en-us/iaas/Content/Audit/Reference/logeventreference.htm#payload).
`data.request`A container object for request attributes. See[Request](https://docs.oracle.com/en-us/iaas/Content/Audit/Reference/logeventreference.htm#payload).
`data.resourceId`An OCID or an ID for the resource emitting the event.
`data.resourceName`The name of the resource emitting the event.
`data.response`A container object for response attributes. See[Response](https://docs.oracle.com/en-us/iaas/Content/Audit/Reference/logeventreference.htm#payload).
`data.stateChange`A container object for state change attributes. See[State Change](https://docs.oracle.com/en-us/iaas/Content/Audit/Reference/logeventreference.htm#payload).

### Identity

The identity object contains the following attributes.

Property Description
`data.identity.authType`The type of authentication used.
`data.identity.callerId`The OCID of the caller. The caller that made a request on behalf of the principal.
`data.identity.callerName`The name of the user or service issuing the request. This value is the friendly name associated with`callerId`.
`data.identity.consoleSessionId`This value identifies any Console session associated with this request.
`data.identity.credentials`The credential ID of the user.
`data.identity.ipAddress`The IP address of the source of the request.
`data.identity.principalId`The OCID of the principal.
`data.identity.principalName`The name of the user or service. This value is the friendly name associated with`principalId`.
`data.identity.tenantId`The OCID of the tenant.
`data.identity.userAgent`The user agent of the client that made the request.

### Request

The request object contains the following attributes.

Property Description
`data.request.action`

The HTTP method of the request.

Example:`GET`
`data.request.headers`The HTTP header fields and values in the request.
`data.request.id`The unique identifier of a request.
`data.request.parameters`All the parameters supplied by the caller during this operation.
`data.request.path`

The full path of the API request.

Example:`/20160918/instances/ocid1.instance.oc1.phx. <unique_ID>`

### Response

The response object contains the following attributes.

Property Description
`data.response.headers`The headers of the response.
`data.response.message`A friendly description of what happened during the operation.
`data.response.payload`This value is included for backward compatibility with the Audit version 1 schema, where it contained metadata of interest from the response payload.
`data.response.responseTime`The time of the response to the audited request, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.
`data.response.status`The status code of the response.

### State Change

The state change object contains the following attributes.

Property Description
`data.stateChange.current`Provides the current state of fields that may have changed during an operation. To determine how the current operation changed a resource, compare the information in this attribute to`data.stateChange.previous`.
`data.stateChange.previous`Provides the previous state of fields that may have changed during an operation. To determine how the current operation changed a resource, compare the information in this attribute to`data.stateChange.current`.

## An Example Audit Log

The following is an example of an event recorded by the Audit service.

```

```
