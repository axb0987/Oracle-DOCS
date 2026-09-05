# Object Storage Dedicated Endpoints
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/dedicatedendpoints.htm
- Fetched: 2026-09-05 02:50 CDT

# Object Storage Dedicated Endpoints

Object Storage dedicated endpoints provide tenancy-specific API endpoints that you can use to securely access your Object Storage buckets.

Each tenancy is assigned a unique, immutable, system-generated endpoint that includes your Object Storage namespace in the URL. Because these endpoints are dedicated to a single tenancy, they provide tenant isolation and can help your organization meet security and compliance requirements.

Your existing Object Storage service API endpoints continue to work, and using dedicated endpoints is optional. If you develop your own applications or clients that access Object Storage, you can direct requests to any of the dedicated endpoint domains. For the strongest security posture, we recommend using the namespace-prefixed endpoints on the`oci.customer-oci.com`domain.

## Advantages of Dedicated Endpoints

- Dedicated endpoints isolate Object Storage customers from each other, preventing a malicious or inadvertent API usage by customer, causing the common URL to be blocked, thus impacting all other customers.
- They also help to minimize the broad impact of DNS-based blocking of Object Storage endpoints by security software.
- And, they provide protection against malicious cyber-attacks and blocking on a per-tenancy level.

## Prerequisites

Firewalls, proxy servers, or other devices that your network administrators use to control access to the internet can affect your ability to connect to a dedicated endpoint. To allow access, you should whitelist the second level domain.

To allow network access to the Console, your network administrator should add *. customer-oci.com to the allowlist of your firewall or proxy server.
Note  
  
The dedicated endpoint URLs are shown in detail in the following table. Note that these changes in the URL apply only to the OC1 commercial realm; other areas continue with existing URLs.

## Dedicated Endpoint URLs

To construct the dedicated endpoint URLs, Object Storage registers DNS records with a wild-card prefix on the OCI customer zone SLD (customer-oci.com).

The following table lists the dedicated endpoint structure.
Important  
  
You can access Object Storage from networks that use IPv6, while still supporting IPv4, by using dual-stack dedicated endpoints with the`ds.oci.customer-oci.com`format. This means that if you leverage Object Storage's IPv6 functionality using the available dual-stack endpoints, you automatically get the security benefits of dedicated endpoints. For more information, see[Dual-Stack Endpoints and Support for IPv6](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/use-ipv6-urls.htm#object-storage-ipv6-dual-stack-endpoints).

API Type Traditional Endpoint Format Dedicated Endpoint Format
Native

objectstorage.$region.oraclecloud.com

objectstorage.$region. oci . customer-oci.com (only used in cases where namespace is not known. For e.g. GetNamespace / WorkRequests etc. )

$namespace .objectstorage.$region. oci . customer-oci.com
S3 compatible

$namespace.compat.objectstorage.$region.oraclecloud.com $namespace.compat.objectstorage.$region. oci . customer-oci.com
Swift

swiftobjectstorage.$region.oraclecloud.com

swiftobjectstorage.$region. oci . customer-oci.com

$namespace .swiftobjectstorage.$region. oci . customer-oci.com
PARs objectstorage.$region.oraclecloud.com/p/&lt;&gt;/n/&lt;&gt;/b/&lt;&gt;/o/ $namespace .objectstorage.$region. oci.customer-oci.com /p/&lt;&gt;/n/&lt;&gt;/b/&lt;&gt;/o/
Note  
  
$namespace refers to the Object Storage namespace. See[Understanding Object Storage Namespaces](https://docs.oracle.com/iaas/Content/Object/Tasks/understandingnamespaces.htm)to know more about Object Storage namespaces.

## OCI UI (Object Storage Console)

The OCI Console uses dedicated endpoints for Object Storage. This keeps the overall flow of using Object Storage unchanged.

## OCI SDK / CLI

Uptake of dedicated endpoints with SDK/CLI can be done via setting environment variables or command line flags. Examples are available at[SDK Guides](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm). Accessing dedicated endpoints is currently optional for tenants.

## Known Issues
