# Details for Network Firewall Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_networkfirewall.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Network Firewall Logs

Logging details for Network Firewall logs. Three types of customer logs are available: threat, traffic, and tunnel inspect logs.

## Resources
- NGFW

## Log Categories

API value (ID): Console (Display Name) Description
threat-log Threat Log Provides details on received firewall threats.
traffic-log Traffic Log Provides details on traffic passing through the firewall.
tunnellog Tunnel Inspection Log Provides details on received firewall tunnel inspect logs.

## Availability

Network Firewall logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Comments

Threat, traffic, and tunnel inspect logs are available. Logs are emitted to customers based on a five minute interval from the dataplane. The dataplane also registers logs as they're received.

## Contents of a Network Firewall Threat Log

Property Description
datetime Timestamp when the log was received.
action
Action taken for the session. Values are, allow, deny, drop.
- allow: Flood detection alert.
- deny: Flood detection mechanism activated and deny traffic based on configuration.
- drop: Threat detected and associated session was dropped.
device_name The hostname of the firewall on which the session was logged.
direction
Indicates the direction of the attack, whether client-to-server or server-to-client:
- 0: Direction of the threat is client-to-server.
- 1: Direction of the threat is server-to-client.
dst Original session destination IP address.
dstloc Destination country or internal region for private addresses. Maximum length is 32 bytes.
dstuser User name of the user to which the session was destined.
firewall-id OCID of the firewall.
proto IP protocol associated with the session.
receive_time Time the log was received at the management plane.
rule Name of the rule that the session matched.
sessionid An internal numerical identifier applied to each session.
severity Severity associated with the threat. Values are informational, low, medium, high, and critical.
src Original session source IP address.
srcloc Source country or internal region for private addresses. Maximum length is 32 bytes.
srcuser User name of the user who started the session.
subtype
Subtype of threat log. Values include the following:
- data: Data pattern matching a Data Filtering profile.
- file: File type matching a File Blocking profile.
- flood: Flood detected through a Zone Protection profile.
- packet: Packet-based attack protection triggered by a Zone Protection profile.
- scan: Scan detected through a Zone Protection profile.
- spyware: Spyware detected through an anti-spyware profile.
- url: URL filtering log.
- virus: Virus detected through an anti-virus profile.
- vulnerability: Vulnerability exploit detected through a Vulnerability Protection profile.
thr_category Describes threat categories used to classify different types of threat signatures.
threatid
Palo Alto Networks identifier for the threat. A description string followed by a 64-bit numerical identifier in parentheses for some subtypes:
- 8000-8099: Scan detection.
- 8500-8599: Flood detection.
- 9999: URL filtering log.
- 10000-19999: Spyware phone home detection.
- 20000-29999: Spyware download detection.
- 30000-44999: Vulnerability exploit detection.
- 52000-52999: File type detection.
- 60000-69999: Data filtering detection.
id UUID of the log message.
compartmentid OCID of the compartment.
ingestedtime Timestamp when log was received by the Logging service.
loggroupid OCID of the log group.
logid OCID of the log object.
tenantid OCID of the tenant.
source OCID of the firewall.
specversion The version of the CloudEvents specification which the event uses. Enables the interpretation of the context.
time Timestamp when log was written.
type Type of the logs.
regionId OCID of the firewall region.

## Example Network Firewall Threat Log
```

```

## Contents of a Network Firewall Traffic Log

Property Description
datetime Timestamp when log was received.
action
Action taken for the session. Possible values are:
- allow: Session allowed by policy.
- deny: Session denied by policy.
- drop: Session dropped silently.
- drop ICMP: Session silently dropped with an ICMP unreachable message to the host or application.
- reset both: Session ended and a TCP reset is sent to both sides of the connection.
bytes Number of total bytes (transmit and receive) for the session.
bytes_received Number of bytes in the server-to-client direction of the session.
bytes_sent Number of bytes in the client-to-server direction of the session.
chunks Sum of SCTP chunks sent and received for an association.
chunks_received Number of SCTP chunks sent for an association.
chunks_sent Number of SCTP chunks received for an association.
config_ver Configuration version.
device_name The hostname of the firewall on which the session was logged.
dport Destination port used by the session.
dst Original session destination IP address.
dstloc Destination country or internal region for private addresses. Maximum length is 32 bytes.
firewall-id OCID of the firewall.
packets Number of total packets (transmit and receive) for the session.
pkts_received Number of server-to-client packets for the session.
pkts_sent Number of client-to-server packets for the session.
proto IP protocol associated with the session.
receive_time Time the log was received at the management plane.
rule Name of the rule that the session matched.
rule_uuid The UUID that permanently identifies the rule.
serial Serial number of the firewall that generated the log.
sessionid An internal numerical identifier applied to each session.
sport Source port used by the session.
src Original session source IP address.
srcloc Source country or internal region for private addresses. Maximum length is 32 bytes.
time_received Time when the log has been processed and committed to its database.
id UUID of the log message.
compartmentid OCID of the compartment.
ingestedtime Timestamp when log was received by the Logging service.
loggroupid OCID of the log group.
logid OCID of the log object.
tenantid OCID of the tenant.
source OCID of the firewall.
specversion The version of the CloudEvents specification which the event uses. Enables the interpretation of the context.
time Timestamp when the log was written.
type Type of the logs.
regionId OCID of the firewall region.

## Example Network Firewall Traffic Log
```

```

## Contents of a Network Firewall Tunnel Inspect Log

Property Description
src Source IP address of packets in the session.
dst Destination IP address of packets in the session.
receive_time Month, day, and time the log was received at the management plane.
rule Name of the security policy rule in effect on the session.
srcloc Source country or internal region for private addresses. The maximum length is 32 bytes.
dstloc Destination country or internal region for private addresses. The maximum length is 32 bytes.
sessionid Session ID of the session being logged.
proto IP protocol associated with the session.
action Action taken for the session. The possible values are:
- ALLOW
- DENY
- DROP
- DROP ICMP
- RESET BOTH
- RESET CLIENT
- RESET SERVER
serial Serial number of the firewall that generated the log.
sport Source port used by the session.
dport Destination port used by the session.
device_name The firewall hostname on which the session was logged.
bytes Number of bytes in the session.
bytes_sent Number of bytes in the client-to-server direction of the session.
bytes_received Number of bytes in the server-to-client direction of the session.
packets Number of total packets (send and receive) for the session.
pkts_sent Number of client-to-server packets for the session.
pkts_received Number of server-to-client packets for the session.
app Application identified for the session.
tunnelid Tunnel ID being inspected or the International Mobile Subscriber Identity (IMSI) ID of the mobile user.
monitortag Monitor name configured for the Tunnel Inspection policy rule or the International Mobile Equipment Identity (IMEI) ID of the mobile device.
parent_session_id Session ID in which the particular session is tunneled. Applies only to the inner tunnel (if two levels of tunneling) or inside content (if one level of tunneling).
parent_start_time Year/month/day hours:minutes:seconds that the parent tunnel session began.
tunnel The tunnel type, such as VXLAN.
max_encap Number of packets the firewall dropped because the packet exceeded the maximum number of encapsulation levels configured in the Tunnel Inspection policy rule (drops the packet if the maximum tunnel inspection level is exceeded).
unknown_proto Number of packets the firewall dropped because the packet contains an unknown protocol, as enabled in the Tunnel Inspection policy rule (drops the packet if the unknown protocol is inside the tunnel).
strict_check Number of packets the firewall dropped because the tunnel protocol header in the packet failed to comply with the RFC for the tunnel protocol, as enabled in the Tunnel Inspection policy rule (drops the packet if the tunnel protocol fails the strict header check).
tunnel_fragment Number of packets the firewall dropped because of fragmentation errors.
tunnel_insp_rule Name of the tunnel inspection rule matching the clear text tunnel traffic.

## Example Network Firewall Tunnel Inspect Log
```

```
