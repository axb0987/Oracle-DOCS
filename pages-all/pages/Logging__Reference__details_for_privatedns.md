# Details for Private DNS Resolver Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_privatedns.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Private DNS Resolver Logs

Logging details for DNS Resolver logs.

## Resources
- privateResolver

## Log Categories

API value (ID): Console (Display Name) Description
`dns.dnsresolver.private_resolver_query_response`Query Response Logs Log for Private DNS query responses.

## Availability

Private DNS logging is available in all regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Contents of a Private DNS Log

Note  
  
Some fields depend on the DNS query response and contain query-specific information. The most common fields are defined in the following table. For more information on OCI supported DNS records see[Supported Resource Records](https://docs.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm). For more information on RFC DNS definitions, see the[DNS RFC specification](https://datatracker.ietf.org/doc/html/rfc8499).

Property Description

`specversion`

Oracle Cloud Infrastructure Logging schema version. For example:`1.0`.

`type`

OCI log type. Always set to`com.oraclecloud.dns.private.resolver`.

`source`

Name of the DNS resolver OCID that sent a DNS query for resolution.

`id`

Random UUID, unique to each log entry. For example,`10936-1708978182-7f44ccc0848b5dff`

`time`

Time the function output was generated, in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`oracle.ingestedtime`Time the log line was ingested by Oracle Cloud Infrastructure logging, in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`oracle.logid`OCID of the Oracle Cloud Infrastructure Logging log object.

`oracle.loggroupid`OCID of the Oracle Cloud Infrastructure Logging log group.
`oracle.resourceType`The resource type that returned the response. For example,`dns.privateResolver`.

`oracle.tenantid`OCID of the tenancy the log object is in.

`oracle.compartmentid`OCID of the compartment the function/application is in.

`data.additionalcount`

The number of resource records in the "additional information" section, defined in the[DNS RFC specification](https://datatracker.ietf.org/doc/html/rfc8499).

`data.answer`Answer record type and data. For example,`[A 10.0.3.6]`("A" record is an address record followed by the address data.) See[Supported Resource Records](https://docs.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm)for more information.
`data.answercount`

The number of resource records (RRs) present in the answer section, defined in the[DNS RFC specification](https://datatracker.ietf.org/doc/html/rfc8499).
`data.authoritycount`

The number of entries in the authority section of the DNS message, defined in the[DNS RFC specification](https://datatracker.ietf.org/doc/html/rfc8499).
`data.forwardSourceAddress`

Reverse Connection Endpoint (RCE) IP address (if any).
`data.forwardDestinationPort`

IP address of the final forwarded query destination (if any).
`data.forwardDestinationAddress`

Port number for the final forwarded query destination (if any).
`data.latency`

Query latency expressed in milliseconds.
`data.messageId`

Message identifier with value in range of 0 to 65535. Used to link public log entries to internal log entries for troubleshooting.
`data.path`

Indicates how the query was answered. Possible values include:`"internet"`,`"private"`,`"private-internet"`,`"private-rule:forwarded"`,`"private-rule:internet"`,`"private-rule:nxdomain"`,`"private-rule:drop"`,`"rule:forwarded"`,`"rule:internet"`,`"rule:nxdomain"`,`"rule:drop"`, or`"throttled"`.

`data.protocol`

The protocol used by the response. For example`udp`. See[RFC-1180](https://datatracker.ietf.org/doc/html/rfc1180)and[RFC-768](https://datatracker.ietf.org/doc/html/rfc768)for more about these protocols.
`data.qclass`

Query class code. For example,`IN`. Possible values:`IN`(Internet),`CH`(Chaos),`HS`(Hesiod)

`data.qname`

Query Name: Domain or subdomain requested. For example,`name.org`.

`data.qtype`Type of record requested. For example,`A`("A" record is an address record). See[Supported Resource Records](https://docs.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm)for more information.

`data.rcode`

DNS response code. For example,`0`. See[DNS RCODEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6)for more detail.

`data.rcodeName`

DNS response code data. For example,`NOERROR`. See[DNS RCODEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6)for more detail.
`data.sourceAddress`IP address that the request was received from. For example,`10.0.0.2`.
`data.sourcePort`The port that the request was received from. For example,`1234`.
`data.schema`

Version of the data format in OCI Logging.
`data.ednsClientSubnet`

Extension mechanism for DNS (EDNS) subnet information.
`data.ttl`The Time to Live of the response record. See[Supported Resource Records](https://docs.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm)for more information.
`data.destinationPort`Initial query destination port.
`data.destinationAddress`Initial query destination IP address.

`oracle.vcnId`The VCN from which the log was generated.

`oracle.viewId`

If present, indicates the DNS response that was provided by a private DNS view.

## Examples of a Private DNS Resolver Log

The following are JSON format examples of a private DNS resolver log.

Log Example 1
```

```

Log Example 2
```

```

Log Example 3
```

```
