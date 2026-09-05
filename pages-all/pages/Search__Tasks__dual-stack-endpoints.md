# Using Dual-Stack Endpoints for the Search API
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/dual-stack-endpoints.htm
- Fetched: 2026-09-05 03:03 CDT

# Using Dual-Stack Endpoints for the Search API

Use a dual-stack endpoint to access the Search API over IPv6 or IPv4.

The Search API supports IPv4-only and dual-stack endpoints. A dual-stack endpoint can resolve to either an IPv6 or IPv4 address, so you can connect over IPv6 while retaining IPv4 compatibility.

To use a dual-stack endpoint, configure the client with an endpoint in the following format:
```

```

For example, the dual-stack endpoint for the US East (Ashburn) region is`query.us-ashburn-1.ds.oci.oraclecloud.com`.

- Create an authentication provider by using the user credentials.

```

```

- Create a`ResourceSearchClient`and specify the dual-stack endpoint.

For example, set the endpoint when you create the client:

```

```

Or, set the endpoint after you create the client:

```

```

For a complete list of endpoints for supported regions, see the[Search API](https://docs.oracle.com/iaas/api/#/en/search/latest/). For general information about IPv6 in OCI, see[Overview of IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm)
