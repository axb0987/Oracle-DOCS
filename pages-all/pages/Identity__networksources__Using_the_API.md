# Using the API
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/networksources/Using_the_API.htm
- Fetched: 2026-09-05 02:25 CDT

# Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use these API operations to manage network sources:
- [CreateNetworkSource](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSources/CreateNetworkSource)
- [ListNetworkSources](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSourcesSummary/ListNetworkSources)
- [GetNetworkSource](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSources/GetNetworkSource)
- [UpdateNetworkSource](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSources/UpdateNetworkSource)
- [DeleteNetworkSource](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSources/DeleteNetworkSource)

## Creating the Network Source Object

A sample network source object looks like the following example:

```

```

The elements are:
- `virtualSourceList`- specifies the VCN (OCID) and subnet IP ranges within that VCN that are allowed access. The`virtualSourceList`must contain both the VCN OCID and the subnet IP ranges:
- `vcnID`- the OCID of the VCN
- `IpRanges`- comma-separated list of the IP addresses or CIDR blocks of the subnets belonging to the specified VCN that are allowed to access the resource. To allow all ranges in the specified VCN, enter 0.0.0.0/0.
- `publicSourceList`- comma-separated list of the public IP ranges that are allowed access.

Example:

```

```
