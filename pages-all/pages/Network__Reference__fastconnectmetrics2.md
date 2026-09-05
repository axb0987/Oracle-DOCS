# FastConnect Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Reference/fastconnectmetrics2.htm
- Fetched: 2026-09-05 02:42 CDT

# FastConnect Metrics

You can monitor the health, capacity, and performance of a[FastConnect connection](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Concepts/fastconnect.htm)by using metrics, alarms, and notifications. For more information, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)and[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

This topic describes the metrics emitted by the metric namespace`oci_fastconnect`.

Resources: cross-connect groups, virtual circuits

## Overview of Metrics: oci_fastconnect

Metrics are available for several resources in the FastConnect connection. The metrics help you decide quickly whether the FastConnect connection is up, how much data is flowing over the connection, and whether packets are being dropped for unexpected errors. FastConnect offers different[connectivity models:](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../shared/../Concepts/fastconnectoverview.htm#How)
- [Connect with an Oracle partner](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../shared/../Concepts/fastconnectprovider.htm): Metrics are available for virtual circuits in the connection.
- [Connect with a third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../shared/../Concepts/fastconnectthirdpartyprovider.htm): Metrics are available for the cross-connect group (LAG) and virtual circuits in the connection. Metrics for cross-connects aren't yet available.
- [Colocate with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../shared/../Concepts/fastconnectcolocate.htm): Metrics are available for the cross-connect group (LAG) and virtual circuits in the connection. Metrics for cross-connects aren't available.

A cross-connect group (LAG) contains one or more cross-connects. If there are several and one goes down, the cross-connect group stays up, but the group might experience a lower overall bandwidth.

### Required IAM Policy

To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).

## Available Metrics: oci_fastconnect

The metrics listed in the following table are automatically available for each virtual circuit or cross-connect group that you create. You don't need to enable monitoring to get these metrics.

You also can use the Monitoring service to create custom queries. See[Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).

Each metric includes the following dimensions: COMPONENT Possible values are`crossconnectgroup`,`crossconnect`, and`virtualcircuit`. If you[connect through an Oracle partner](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../shared/../Concepts/fastconnectprovider.htm), only the`virtualcircuit`component is available. RESOURCEID The OCID of the resource (either a cross-connect group, cross-connect, or virtual circuit). RESOURCENAME The name assigned to the resource.

Metric Metric Display Name Unit Description Dimensions
`BitsReceived`Bits Received

Bits

Number of bits received on the FastConnect interface at the Oracle end of the connection.

For a cross-connect group (LAG), the value is the sum across all cross-connects in the group.

`component`

`resourceId`

`resourceName`
`BitsSent`Bits Sent

Bits

Number of bits sent from the FastConnect interface at the Oracle end of the connection.

For a cross-connect group (LAG), the value is the sum across all cross-connects in the group.
`BitRateReceived`Bit Rate Received

Bits per second Rate at which bits are received on the FastConnect interface at the Oracle end of the connection.
`BitRateSent`Bit Rate Sent

Bits per second Rate at which bits are sent from the FastConnect interface at the Oracle end of the connection.
`BytesReceived`Bytes Received

Bytes

Number of bytes received on the FastConnect interface at the Oracle end of the connection.

For a cross-connect group (LAG), the value is the sum across all cross-connects in the group.
`BytesSent`Bytes Sent

Bytes

Number of bytes sent from the FastConnect interface at the Oracle end of the connection.

For a cross-connect group (LAG), the value is the sum across all cross-connects in the group.
`ConnectionState`Connection State

Binary (1 or 0)

The values are up (1) or down (0).

For a virtual circuit, the operational state of the virtual circuit's interface.

For a cross-connect group, this reflects the overall operational state of the cross-connects that make up the cross-connect group (LAG). If at least one of the cross-connects is up, this value is up (1). If all the cross-connects in the group are down, this value is down (0).
`PacketsError`Packets with Errors

Packets

Number of packets dropped at the Oracle end of the connection. Dropped packets indicate a misconfiguration in some part of the overall system. Check if there was a change to the configuration of the VCN, the virtual circuit, or the CPE.

For a cross-connect group (LAG), the value is the sum across all cross-connects in the group.
`PacketsDiscarded`Packets Discarded Packets Number of packets discarded at the Oracle end of the connection.
`PacketsReceived`Packets Received

Packets

Number of packets received on the FastConnect interface at the Oracle end of the connection.

For a cross-connect group (LAG), the value is the sum across all cross-connects in the group.
`PacketsSent`Packets Sent

Packets

Number of packets sent from the FastConnect interface at the Oracle end of the connection.

For a cross-connect group (LAG), the value is the sum across all cross-connects in the group.
`Ipv4BgpSessionState`IPv4 BGP Session State Binary (1 or 0) The values are up (1) or down (0). The status of the IPv4 BGP session for a virtual circuit.
`Ipv6BgpSessionState`IPv6 BGP Session State Binary (1 or 0) The values are up (1) or down (0). The status of the IPv6 BGP session for a virtual circuit.

## Using the Console

The instructions depend on which FastConnect[connectivity model](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Concepts/fastconnectoverview.htm#How)you use.

### If You Use an Oracle Partner

[To view default metric charts for FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/fastconnectmetrics2.htm#)

- On the FastConnect connections list page, select the cross-connect group, cross-connect, or virtual circuit that you want to work with. If you need help finding the list page, see[To list virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../shared/../Concepts/fastconnectprovider.htm#fastconnectprovider_topic_To_list_virtual_circuits)
- 

Change to the Monitoring tab. The default metrics charts are displayed on the resulting page.

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

[To view default metric charts for all FastConnect connections in a compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/fastconnectmetrics2.htm#)

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Service Metrics .
- For Compartment , select the compartment that you're interested in.
- 

For Metric namespace , select oci_fastconnect .

The Service Metrics page dynamically updates the page to show charts for each metric emitted by the selected metric namespace.

If many FastConnect connections are in the compartment, by default the charts show a separate line for each one (each virtual circuit).

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

#### If You Use a Third-Party Provider or Colocate with Oracle

In this situation, you manage both the physical connection (cross-connects) and logical connection (virtual circuit).

For the physical connection, metrics are available for the cross-connect group (LAG), but not the individual cross-connects. If you're using only a single cross-connect with no cross-connect group, then no metrics are available for the physical connection.

For the logical connection, metrics are available for each virtual circuit.

[To view default metric charts for all FastConnect connections in a compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/fastconnectmetrics2.htm#)

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Service Metrics .
- For Compartment , select the compartment that you're interested in.
- 

For Metric namespace , select oci_fastconnect .

The Service Metrics page dynamically updates the page to show charts for each metric emitted by the selected metric namespace.

By default the charts show a separate line for each resource in the compartment (each cross-connect group and virtual circuit).

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
- [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/)for metrics and alarms
- [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/)
