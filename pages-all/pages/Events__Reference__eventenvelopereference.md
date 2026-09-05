# Contents of an Event Message
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Reference/eventenvelopereference.htm
- Fetched: 2026-09-05 02:02 CDT

# Contents of an Event Message

Learn about the contents of an event message.

Every event message includes two main parts:
- 

Envelope: a container for all event messages
- 

Payload: the data from the resource emitting the event message

## Event Envelope

These attributes for an event envelope are the same for all events. The structure of the envelope follows the[CloudEvents](https://github.com/cloudevents/spec)industry standard format hosted by the[Cloud Native Computing Foundation ( CNCF)](https://www.cncf.io/).

Property Description
`cloudEventsVersion`

The version of the CloudEvents specification.

Note: Events uses version 0.1 specification of the CloudEvents event envelope.
`contentType`Set to`application/json`. The content type of the data contained in the`data`attribute.
`data`The payload of the event. All of the information within`data`comes from the resource emitting the event. See the following table for more detail on the structure of the payload.
`eventID`

The UUID of the event. This identifier is not an OCID, but just a unique ID for the event.
`eventTime`The time of the event, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.
`eventType`

The type of event that happened. For a list of all services that produce events and the even types that those services track, see[Services that Produce Events](https://docs.oracle.com/en-us/iaas/Content/Events/Reference/eventsproducers.htm).

Note: The service that produces the event can also add, remove, or change the meaning of a field by publishing a new version of an`eventType`and revising the`eventTypeVersion`field.
`eventTypeVersion`

The version of the event type.
`extensions`The OCID of the compartment from which the event originates. If the event originates from the root compartment of the tenancy, then this attribute specifies a tenancy OCID. This attribute is mandatory in the Oracle Cloud Infrastructure implementation of the[CloudEvents](https://github.com/cloudevents/spec)specification.
`source`The resource that produced the event. For example, an Autonomous AI Database or an Object Storage bucket.

## Payload

The data in these fields depends on which service produced the event and the event type it defines.

Property Description
`compartmentId`

The OCID of the compartment of the resource emitting the event.
`compartmentName`The name of the compartment of the resource emitting the event.
`resourceName`The name of the resource emitting the event.
`resourceId`

An OCID or an ID for the resource emitting the event.
`availabilityDomain`The availability domain of the resource emitting the event.
`freeFormTags`

Free-form tags added to the resource emitting the event.
`definedTags`Defined tags added to the resource emitting the event.
`additionalDetails`

A container for attributes unique to the resource emitting the event. In the example bucket event that follows, the payload includes three Object Storage attributes:
- `namespace`
- `publicAccessType`
- `eTag`

To determine what attributes are included for other resources, retrieve an event or consult the reference samples listed on[Services that Produce Events](https://docs.oracle.com/en-us/iaas/Content/Events/Reference/eventsproducers.htm).

## Resource Identifiers

Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

## An Example Event

The following is an example bucket event emitted by Object Storage.

```

```
