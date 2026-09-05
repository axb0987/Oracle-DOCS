# Dual-Stack Endpoints and Support for IPv6
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/use-ipv6-urls.htm
- Fetched: 2026-09-05 02:50 CDT

# Dual-Stack Endpoints and Support for IPv6

You can use dual-stack endpoints to access Object Storage from networks that use IPv6, while still supporting IPv4.

A dual-stack endpoint supports both IPv6 and IPv4 , so the same host name can resolve to either address family.

Dual-stack endpoints use the Dedicated Endpoints format.

## Constructing endpoints

Dual-stack endpoints use the Dedicated Endpoints format for improved tenant isolation and security. See:[Object Storage Dedicated Endpoints](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/dedicatedendpoints.htm#dedicated-endpoints).

The following table illustrates how to construct a dual-stack dedicated endpoint. You include your tenancy's namespace as a prefix in the host name, along with the applicable region.

API IPv4-only endpoint Dual-stack endpoint
V2`objectstorage. {region} .oraclecloud.com``{MyNamespace} .objectstorage. {region} .ds.oci.customer-oci.com`
Swift`swiftobjectstorage. {region} .oraclecloud.com``{MyNamespace} .swiftobjectstorage. {region} .ds.oci.customer-oci.com`
S3`{MyNamespace} .compat.objectstorage. {region} .oraclecloud.com``{MyNamespace} .compat.objectstorage. {region} .ds.oci.customer-oci.com`
Important  
  
In the OC1 commercial realm, only dedicated endpoints using the`ds.oci.customer-oci.com`format can support both IPv6 and IPv4 addresses. The traditional`oraclecloud.com`endpoints continue to support only IPv4 addresses.
Note  
  
Virtual-hosted style URLs and private endpoints aren't supported with dual-stack endpoints and IPv6. They're supported only on IPv4. For more information, see:
- [Amazon S3 Compatibility API Hosted Style Support in Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/../s3-virtual-style.htm#top)
- [Private Endpoints in Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/../Tasks/private-endpoints.htm#private-endpoints)

## Using Dual-Stack Endpoints with APIs (REST)

The REST API can directly access an Object Storage endpoint by using the endpoint name (URI).

## Using Dual-Stack Endpoints with SDKs

You can enable dual-stack endpoints in SDK-based clients either by setting an environment variable or by enabling dual-stack behavior on the client (where supported).

### OCI Python SDK (Object Storage)

Python version 2.165.0 or later:

- Environment variable: set`OCI_DUAL_STACK_ENDPOINT_ENABLED=true`in the session.
- Client setting: set`client_level_dualstack_endpoints_enabled = True`and`client_level_realm_specific_endpoint_template_enabled = True`to direct Object Storage requests to the dual-stack endpoint for the region.

Example:

Python

```

```

### OCI Java SDK (Object Storage)

Java version 3.80.1 or later:

- Client setting: set`enableDualStackEndpoints(true)`and`useRealmSpecificEndpointTemplate(true)`to direct Object Storage requests to the dual-stack endpoint for the region. Example:

Java

```

```

### OCI Go SDK (Object Storage)

Go version: v65.123.0 or later:

- Environment variable: set`OCI_DUAL_STACK_ENDPOINT_ENABLED=true`and`OCI_REALM_SPECIFIC_SERVICE_ENDPOINT_TEMPLATE_ENABLED=true`in the session.
- Client setting: call`EnableDualStackEndpoints(true)`and`RealmSpecificServiceEndpointTemplateEnabled: common.Bool(true)`to direct Object Storage requests to the dual-stack endpoint for the region. Example:

go

```

```

```

```

```

```

```

```

## Using Dual-Stack Endpoints with the CLI

You can direct Object Storage CLI requests to dual-stack endpoints in one of these ways.

- Session-wide: Set the following settings to`true`. These settings direct Object Storage requests made by CLI commands in the session to the dual-stack endpoint for the specified region.
- `OCI_DUAL_STACK_ENDPOINT_ENABLED=true`
- `OCI_REALM_SPECIFIC_SERVICE_ENDPOINT_TEMPLATE_ENABLED=true`
- Per command:

Include`--enable-dual-stack`and`--realm-specific-endpoint`in Object Storage commands. Example:

```

```

- Endpoint override: specify the dual-stack endpoint directly using`--endpoint <dual-stack-url>`.

## Testing IP address compatibility

### Linux/UNIX/macOS

You can test whether you can access a dual-stack endpoint over IPv6 by using`curl -v -6`with the dual-stack health check path. Example:

```

```

What you might see:
- If you're configured to access IPv6, the connected IP address shows as an IPv6 address.
- If you aren't configured to access IPv6, output can stop after`Trying IPv6 Address...`with no further information.

### Windows 7 / Windows 10

You can test whether you can access a dual-stack endpoint over IPv6 or IPv4 by using`ping`. Example:
```

```

What you might see:
- If you're configured to access IPv6, the connected IP address shows as an IPv6 address.
- If you aren't configured to access IPv6, output can stop after`Trying IPv6 Address...`
