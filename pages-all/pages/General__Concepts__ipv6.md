# IPv6 Support
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/ipv6.htm
- Fetched: 2026-09-05 02:10 CDT

# IPv6 Support

Learn how you can use IPv6 addresses with Oracle Cloud Infrastructure (OCI) services.

## API Endpoint Overview

All OCI services offer API endpoints that support IPv4 addressing and clients. All OCI services use IPv4-only endpoints, as documented in[API Reference and Endpoints](https://docs.oracle.com/iaas/api/). These endpoints use the following naming convention:
```

```

Select OCI services offer additional API endpoints that provide both IPv4 and IPv6 (dual-stack) support. The endpoints for these services include the`.ds`identifier indicating dual-stack, that offers both A and AAAA DNS record responses for both IPv4 and IPv6 connectivity. These dual-stack endpoints typically use the following naming convention:
```

```

The following table shows a comparison of endpoint types.

OCI Service API Endpoint Types
Details Default API Endpoint Dual-Stack API Endpoint
`<endpoint_schema>``<service> . <region> . <oracle_domain> . <top_level_domain>``<service> . <region> .ds. <oracle_domain> . <top_level_domain>`
Logging Management service – US East region[https://logging.us-ashburn-1.oci.oraclecloud.com](https://logging.us-ashburn-1.oci.oraclecloud.com)[https://logging.us-ashburn-1.ds.oci.oraclecloud.com](https://logging.us-ashburn-1.ds.oci.oraclecloud.com)
DNS Records A record A, AAAA
Client IP connections supported IPv4-only IPv4, IPv6

To confirm a service's dual-stack endpoint name, review the listed services in OCI Services with Dual-stack Endpoints .

## Using Dual-stack API Endpoints

To use the dual-stack API endpoint, you can opt-in to use the new endpoint through client configuration set with enable-dual-stack or use a manual endpoint override. If you use the enable-dual-stack behavior built into the following OCI clients and the service doesn't offer a dual-stack endpoint, the OCI client falls back to the original IPv4-only endpoint.

See the following list of OCI-provided clients to learn how to use dual-stack endpoints automatically using the enable-dual-stack behavior:
- [OCI CLI](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/oci.html)command reference library.
- [Configuring the OCI Terraform Provider](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm)
- OCI SDK for[Java](https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdkconcepts.htm#yv5_d1h_33c).
- OCI SDK for[Python](https://github.com/oracle/oci-python-sdk/blob/master/examples/enable_dual_stack_endpoint_example.py).
- OCI SDK for[Go](https://docs.oracle.com/iaas/tools/go/latest/).
- OCI SDK for[.NET](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/EnableDualStackEndpointsExample.cs).
- OCI SDK for[JavaScript](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/javascript/use-dual-stack-endpoints.js)and[TypeScript](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/typescript/use-dual-stack-endpoints.ts).
Note  
  
OCI SDK for[Ruby](https://docs.oracle.com/iaas/Content/API/SDKDocs/rubysdk.htm)is no longer being actively developed by Oracle and doesn't provide dual-stack support.

## OCI Services with Dual-Stack Endpoints

The following services support dual-stack endpoints.

### Core Services

OCI Core Services includes the[Networking](https://docs.oracle.com/iaas/Content/Network/Concepts/landing.htm)and[Compute](https://docs.oracle.com/iaas/Content/Compute/home.htm)services. For IPv6 support for Core Services, see the following resources:
- 

[Core Services API](https://docs.oracle.com/iaas/api/#/en/iaas/latest/)
- Networking:[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm)
- Compute:[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)

### File Storage

For IPv6 support for[File Storage](https://docs.oracle.com/iaas/Content/File/home.htm), see the following resources:
- [File Storage API](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/)

### Identity and Access Management Data Plane API

For IPv6 support for Identity and Access Management Data Plane API, see the following resources:
- [Identity and Access Management Data Plane API](https://docs.oracle.com/iaas/api/#/en/identity-dp/v1/)

### Load Balancer

For IPv6 support for[Load Balancer](https://docs.oracle.com/iaas/Content/Balance/home.htm), see the following resources:
- [Load Balancing API](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/)

### Logging

For IPv6 support for[Logging](https://docs.oracle.com/iaas/Content/Logging/home.htm), see the following resources:
- [Logging Ingestion API](https://docs.oracle.com/iaas/api/#/en/logging-dataplane/latest/)
- [Logging Management API](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/)
- [Logging Search API](https://docs.oracle.com/iaas/api/#/en/logging-search/latest/)
- [Logging APIs](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm#how_logging_works__logging_apis)

### Monitoring

For IPv6 support for[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm), see the following resources:
- [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/)

### Object Storage

For IPv6 support for[Object Storage](https://docs.oracle.com/iaas/Content/Object/home.htm), see the following resources:
- [Object Storage Service API](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/)
- [Dual-Stack Endpoints and Support for IPv6](https://docs.oracle.com/iaas/Content/Object/Concepts/use-ipv6-urls.htm)

### OS Management Hub

For IPv6 support for[OS Management Hub](https://docs.oracle.com/iaas/osmh/doc/home.htm), see the following resources:
- [OS Management Hub API](https://docs.oracle.com/iaas/api/#/en/osmh/latest/)
- [Ways to Access](https://docs.oracle.com/iaas/osmh/doc/overview.htm#access)

### Search

For IPv6 support for[Search](https://docs.oracle.com/iaas/Content/Search/home.htm), see the following resources:
- [Search Service API](https://docs.oracle.com/iaas/api/#/en/search/latest/)
