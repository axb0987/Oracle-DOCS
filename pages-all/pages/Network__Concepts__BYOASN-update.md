# Updating the Origin ASN
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-update.htm
- Fetched: 2026-09-05 02:40 CDT

# Updating the Origin ASN

Associate your BYOIP CIDRs (IPv4/IPv6) with your own Autonomous System Number (ASN).

## Prerequisites

Create a Route Origin Authorization (ROA) object for your BYOIP CIDR block and your own ASN. Set an expiry date at least 6 months in the future. Follow the instructions appropriate for your RIR:
- ARIN:[ROA Requests](https://www.arin.net/resources/manage/rpki/roa_request/)
- RIPE NCC:[Managing ROAs](https://www.ripe.net/manage-ips-and-asns/resource-management/rpki/resource-certification-roa-management/)
- APNIC:[Route/ROA management](https://www.apnic.net/wp-content/uploads/2017/01/route-roa-management-guide.pdf)
Note  
  
If you don't create an ROA, Oracle can't advertise the BYOIP IPv4 CIDR block or IPv6 prefix with your ASN set as the origin.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-update.htm#)
- 

- Open the navigation menu and select Networking . Under IP management , select BYOIP .
- On the BYOIP page, select the Actions menu (three dots) for the BYOIP IPv4 CIDR block or IPv6 prefix that you want to associate your ASN with and select Update Origin ASN .
- On the Update origin ASN page, select the Select your ASN option.
- Select the compartment where your ASN is imported to.
- Select your ASN from the list.
- (Optional) Select the Append ASN option.
- (Optional) In the Prepend count field, enter a value.
You can prepend your ASN up to 20 times using the Prepend count option to influence route preference. This depends on whether the service providers along the network path honor AS-PATH prepending.
- Select Update origin ASN .
View the work request to see the status.
- 

Use the`network byoip-range set-origin-asn`command and required parameters to associate your BYOIP CIDRs (IPv4/IPv6) with your own ASN instead of the OCI ASN:

```

```

Use the`network byoip-range set-origin-asn-to-oracle`command and required parameters to associate your BYOIP CIDRs (IPv4/IPv6) with the OCI ASN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

- 

Run the[UpdateByoasn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Byoasn/UpdateByoasn)operation to associate your BYOIP CIDRs (IPv4/IPv6) with your own ASN instead of the OCI ASN.

Run the[ChangeByoasnCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Byoasn/ChangeByoasnCompartment)
