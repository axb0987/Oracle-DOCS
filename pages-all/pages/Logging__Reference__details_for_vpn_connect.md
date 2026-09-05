# Details for Site-to-Site VPN
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_vpn_connect.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Site-to-Site VPN

Logging details for Site-to-Site VPN logs.

## Resources
- IPSecConnection

## Log Categories

API value (ID): Console (Display Name) Description
read IPSec Logs Includes Site-to-Site VPN logs for read access.

## Availability

Site-to-Site VPN is available in all commercial regions. See[Updated Site-to-Site VPN service](https://docs.oracle.com/iaas/Content/Network/Tasks/workingwithIPsec.htm#Working_with_VPN_Connect__v2)for more about Site-to-Site VPN v2.

## Comments

Site-to-Site VPN logs contain all status-related information of the IPSec tunnels associated with the site-to-site type of IPSec connections. This includes bringing of tunnels up or down, and accompanying negotiation information. Each IPSec connection has two IPSec tunnels created, thus the Site-to-Site VPN logs will contain status on both tunnels. Amongst other types of filtering, IPSec tunnels can be distinguished and thus filtered on their data.TunnelId (see[Contents of a Site-to-Site VPN Log](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_vpn_connect.htm#details_for_vpn_connect_0__section_lnn_z1x_r4b)below for details).

Most Site-to-Site VPN log messages begin with a connection name. The connection name is unique for each IPSec tunnel. Its base form is comprised of ten numeric digits (see the sample value for the data.message property in the table below). In total, a connection name has three additional variants, and which variant(s) are used is based on the following:
- Each IPSec tunnel has a unique ten-digit key assigned to (for example,`9123456789`) which is contained in the beginning of many of the IPSec log messages. This is the form for IPv4 tunnels.
- If the given IPSec tunnel is also configured for IPv6, IPSec log messages can also contain the same ten-digit key with a`_v6`appended to it (for example,`9123456789_v6`).
- If the tunnel is policy-based (that is, MED is enabled) there can be multiple SAs depending on the configuration. The form of the ten-digit key for IPv4 tunnels with multiple SAs is a sequence of`_1`,`_2`,`_3`, and accordingly depending on the number of SAs (for example,`9123456789_1`,`9123456789_2`,`9123456789_3`).
- If the given policy-based tunnel is also configured for IPv6, IPSec log messages can also contain the same ten-digit key and SA index, along with v6 (for example,`9123456789_v6_1`).

## Contents of a Site-to-Site VPN Log

A Site-to-Site VPN log contains the following fields:

Property Description Sample Value
data.message The Site-to-Site VPN log message. \"2062988354\": terminating SAs using this connection
data.tunneld The IPSec tunnel OCID of one of the IPSec connection's IPSec tunnels. ocid1.ipsectunnel.region1.sea. &lt;unique_ID&gt;
id Random UUID, unique to each log entry. e3002eaa-d717-472e-8474-d024943a0f27
oracle.compartmentid OCID of the compartment that the log group belongs to. ocid1.tenancy.region1.. &lt;unique_ID&gt;
oracle.ingestedtime Time the log was ingested by Oracle Cloud Infrastructure Logging. 2021-02-18T18:22:01.453Z
oracle.loggroupid OCID of the log group. ocid1.loggroup.region1.sea. &lt;unique_ID&gt;
oracle.logid OCID of the log. ocid1.log.region1.sea. &lt;unique_ID&gt;
oracle.tenantid OCID of the tenant. ocid1.tenancy.region1.. &lt;unique_ID&gt;
source OCID of the IPSec connection, which is comprised of two IPSec tunnels. ocid1.ipsecconnection.region1.sea. &lt;unique_ID&gt;
specversion OCI logging schema version. 1.0
time Time the log was generated in the IPSec tunnel. 2021-02-18T18:21:52.024Z
type Category of the log. Set of possible values: read com.oraclecloud.vpn.ipseclog. read

## An Example Site-to-Site VPN Log
```

```
