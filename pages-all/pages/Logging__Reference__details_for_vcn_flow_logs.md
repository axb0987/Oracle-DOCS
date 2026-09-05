# Details for VCN Flow Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_vcn_flow_logs.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for VCN Flow Logs

Logging details for VCN Flow logs.

## Resources
- Virtual Cloud Network (VCN)
- 

Subnet
- VNIC

## Log Categories

API value (ID): Console (Display Name) Description
all Flow Logs (All records) Traffic is logged for existing and future VNICs in the subnet.
vcn Flow Logs - vcn records Traffic is logged for existing and future VNICs in all subnets in the VCN.
subnet Flow Logs - subnet records Traffic is logged for existing and future VNICs in the subnet. Similar to the all category, which is logged for existing and future VNICs in the subnet.
vnic Flow Logs - vnic records Traffic is logged for specific VNICs in a VCN.

## Availability

VCN Flow Logs are available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). See the[Oracle Cloud Infrastructure Government Cloud](https://docs.oracle.com/iaas/Content/General/Concepts/govlanding.htm)section for information about availability in the Government Cloud realm.

## Comments

Each instance in a VCN has one or more[virtual network interface cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm). The Networking service uses[security rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)to determine what traffic is allowed through a given VNIC. Security rules can be defined using Security lists or Network security groups.

To help troubleshoot the traffic in and out of your VNICs, you can set up VCN flow logs . Flow logs record details about traffic that has been accepted or rejected based on the security rules set up for your VCN.

You can enable flow logs for a given subnet , which means traffic is logged for all existing and future VNICs in that subnet. Each flow log contains information about traffic for a single VNIC.
Note  
  
Certain traffic to core Oracle infrastructure services hosted on link-local (169.254.0.0/16) IP addresses don't appear in flow logs. This includes items such as VCN DNS, DHCP, and block storage. Also excluded is network management traffic, such as ARP.

For more information on VCN Flow Logs usage, see[VCN Flow Logs](https://docs.oracle.com/iaas/Content/Network/Concepts/vcn-flow-logs.htm).

## Contents of a VCN Flow Log

A flow log record contains the following fields:

Property Description Sample Value
data.action

Type of record. Possible values:
- ACCEPT: This record's traffic was accepted by the security lists.
- REJECT: This record's traffic was rejected by the security lists. ACCEPT
data.bytesOut Number of bytes recorded in the capture window. 17114
data.destinationAddress

IP address of the destination, either in IPv4 dot, or IPv6 colon notation.

Note: When IPv6 traffic is encountered in a customer's virtual cloud network, a flow log entry with IPV6 address values is generated, in place of the current location of IPV4 values. The source and destination addresses could be either IPv4 or IPv6, based on the configuration and traffic present in the customer’s VCN. This data is only available in regions where IPv6 support is available, and configured by the customer.

10.0.99.4

8222:91f5:88bb:2bf0:94a:e71b:65d3:4bd7
data.destinationPort[IANA port number](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)of the destination. 36266
data.endTime End time of the capture window in UNIX epoch seconds. 1598917970
data.flowid Hash of key fields (source and destination addresses, ports, and protocol). a6a73770
data.packets Number of packets recorded in the capture window. 250
data.protocol[IANA protocol number.](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)6
data.protocolName IANA name for protocol. TCP
data.sourceAddress

IP address of the source, either in IPv4 dot, or IPv6 colon notation.

See the note in the data.destinationAddress description.

123.0.0.1

1fde:9f1c:2433:4038:68fc:e0b:73f3:3b3b
data.sourcePort[IANA port number](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)of the source. 443
data.startTime

Start time of the capture window in[Unix epoch seconds](https://en.wikipedia.org/wiki/Unix_time).

UNIX epoch time uses a fixed point in the past to reference the current time. Every second of the current time can be expressed as a number, such as 1576090259 (which is Wednesday, December 11, 2019 6:50:59 PM GMT).

Each flow log record records a one-minute interval (0 to 59 seconds) of data flow, using epoch start and end times to indicate the time that data appears during the 60-second interval for that record. Let's consider the epoch time entries that would appear for data flow during a fixed interval of 140 seconds. At five seconds past a particular minute, you open a connection to the host and begin to continuously send data over that connection for the next 140 seconds (&lt; three minutes, three records).

Epoch start and end times would appear in the log according to the following:
- The first record would show an epoch start time at the five seconds past the minute mark and an epoch end time at the end of that minute (54 seconds later).
- The next record would show an epoch start time at the zero-seconds mark, and epoch end time at the end of that minute (59 seconds later). This assumes you sent the data continuously . If the transmission had been intermittent, the epoch times would reflect the first and last second data flow that occurred during that 60-second interval (the absolute time).
- The final record would show an epoch start time at the zero-seconds mark, and an epoch end time for 20 seconds later (since the total flow life was only 140 seconds, or 20 seconds into the third one-minute logging interval recorded by each record). 1598917969
data.status

Status of data capture window. Possible values:
- OK: Normal packet log.
- NODATA: No traffic was recorded during the capture window, in which case, only the following data fields are set: endTime, startTime, status, and version. The remaining data fields are set to null: action, bytesOut, destinationAddress, destinationPort, flowid, packets, protocol, protocolName, sourceAddress, an sourcePort.
- SKIPDATA: Some traffic was not logged during the capture window because of system errors or capacity issues, in which case, only data fields endTime, startTime, status, and version are set, and the remaining data fields are set to null. The flow log can contain other records for accepted or rejected traffic in the capture window. OK
data.version Version of the flow log record schema. 2
datetime Timestamp in milliseconds. Same as the oracle.ingestedtime field but in milliseconds. 1598917955000
id Random UUID, unique to each log entry. abcdabcd-abcd-abcd-abcd-abcdabcdabcd
oracle.compartmentid OCID of the compartment the log group is in. ocid1.compartment.oc1. &lt;region-id&gt; . &lt;unique-id&gt;
oracle.ingestedtime Time the log was ingested by OCI Logging. 2020-08-31T23:53:54Z
oracle.loggroupid OCID of the log group. ocid1.loggroup.oc1. &lt;region-id&gt; . &lt;unique-id&gt;
oracle.logid OCID of the log. ocid1.log.oc1. &lt;region-id&gt; . &lt;unique-id&gt;
oracle.tenantid OCID of the tenant. ocid1.tenancy.oc1.. &lt;region-id&gt; . &lt;unique-id&gt;
oracle.vniccompartmentocid OCID of the compartment to which the VNIC belongs. ocid1.compartment.oc1.. &lt;region-id&gt; . &lt;unique-id&gt;
oracle.vnicocid OCID of the VNIC. ocid1.vnic.oc1. &lt;region-id&gt; . &lt;unique-id&gt;
oracle.vnicsubnetocid OCID of the subnet to which the VNIC belongs. ocid1.subnet.oc1. &lt;region-id&gt; . &lt;unique-id&gt;
specversion OCI logging schema version. 1.0
time Same as startTime. 2020-08-31T23:52:35Z
type Category of log: DataEvent, QualityEvent.NoData, or QualityEvent.SkipData. com.oraclecloud.vcn.flowlogs.DataEvent

## Limitations and Considerations
- Some traffic might not be logged during a capture window because of capacity issues or system errors. In such cases, NODATA, or SKIPDATA log status is recorded.
- Some services manage VNICs. For example, the Load Balancing service manages VNICs attached to load balancers. Flow logs for managed VNICs are captured, and identified by VNIC ID. Flow logs, however, don't include a field to indicate what service such VNICs belong to.
- For traffic over the public IP of a compute instance, flow logs records the corresponding private IP.
- Flow logs can be enabled on the subnet resource, either with category all or a subnet. No differences exist in the flows captured under these categories.

## Using the CLI

See[VCN Flow Logs Example](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/../Task/vcn_flowlogs_eg.htm)
