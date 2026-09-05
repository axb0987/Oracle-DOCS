# Private Endpoints in Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/private-endpoints.htm
- Fetched: 2026-09-05 02:51 CDT

# Private Endpoints in Object Storage

Learn about using private endpoints to reach your Object Storage buckets and objects using a private IP address within your VCN instead of the public internet.

Private endpoints provide secure access to Object Storage from your OCI VCNs or on-premise networks. The private endpoint is a VNIC with a private IP address in a subnet you choose within your VNC. This method is an alternative to using a service gateway using public IP addresses associated with OCI services.

Private endpoints differ from dedicated endpoints in that dedicated endpoints are tenancy-specific endpoints that each have a dedicated namespace string in the URL. This attribute ensure full isolation to help meet your organization's security and compliance requirements. Similar to the traditional public endpoint URLs, the dedicated endpoints resolve to the public IP address of Object Storage.

In contrast, private endpoints are customizable endpoints which resolve to a private IP address of a VNIC. Requests go to a private IP address in the your VCN. The traffic is then routed to Object Storage service from the VNIC.

Creating a private endpoint in a VCN and associating it with a bucket doesn't limit access to the bucket from the internet or other network sources. You need to define rules using IAM polices on the bucket, so requests are only authorized if they originate from a specific VCN or a CIDR block within that VCN. All other access, including over the internet, is blocked to these buckets. See[Managing Network Sources](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingnetworksources.htm)for more information.

The following is a sample policy to restrict a specific bucket to a specific network source:
```

```

When you create a private endpoint, you can restrict access to certain Object Storage resources by specifying access targets. Each access target consists of the following required parameters:
- Namespace : Specifies the target namespace that's to be allowed to egress from the private endpoint.
- Compartment : Specifies what namespace/compartments the private endpoint can access. You can configure either a single compartment or all compartments.
- Bucket : Specifies what namespace/buckets within the allowed compartments the private endpoint can access. You can configure either a single bucket or all buckets within the allowed compartments.

Specify either the parameter's name or a wildcard ("*") to allow any parameter access. See[Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm)for more information on configuring access targets.

Each private endpoint must have at least one access target to a maximum of 10.

In the following example, an access target has the following configuration:
- Namespace = Namespace1
- Compartment = Compartment1
- Bucket = Bucket1

In this configuration, the private endpoint has access to objects in Bucket1, which resides in Compartment1 and which belongs to the Namespace1. If you move a Bucket1 to a different compartment (Compartment2), the private endpoint can no longer access bucket Bucket1.

Adding an access target doesn't automatically grant you access to the bucket or object. Your request to Object Storage through the private endpoint is always authorized by OCI IAM to ensure they have the correct IAM policies to access the bucket or object.

Object Storage buckets using a private endpoint aren't limited to that private endpoint only. Buckets using a private endpoint can use other access methods as well.

You can perform the following Object Storage private endpoint tasks:

[List the Object Storage private endpoints in a compartment.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-private-endpoint.htm)

[Create an Object Storage private endpoint.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm)

[Get an Object Storage private endpoint's details.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-private-endpoint.htm)

[Edit an Object Storage private endpoint's settings.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/update-private-endpoint.htm)

[View the fully-qualified domain names for an Object Storage private endpoint](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-fqdn.htm).

[View the access targets for an Object Storage private endpoint](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-access-targets.htm).

[View the Object Storage private endpoint work requests in a compartment](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-pe-work-request.htm).

[Delete an Object Storage private endpoint from a compartment.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/delete-private-endpoint.htm)

## Finding Details for Private Endpoint Resources

The new Oracle Cloud Console experience uses tabs to organize the information on the details page for each private endpoint resource in the Object Storage service.

The following sections describe what information is displayed on the tabs for the private endpoint resources in Object Storage. Depending on the resource type, you might see some or all of the tabs listed here.

### Object Storage

Tab Information on Tab
Details
- General
- Usage
FQDNs
- FQDNs
Access Targets
- Pre-Authenticated Requests
- Uncommitted Multipart Uploads
Work Requests
- Work Requests
Tags
- Tags

## IAM Policies

Use policies to limit access to Object Storage private endpoints. A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

The following permissions are required to perform the corresponding operations:
```

```

We recommend the following IAM policies be added to allow Object Storage private endpoint management:

IAM Policies
Operation Object Storage IAM Permissions Other IAM Permissions

Create a private endpoint

`OBJECTSTORAGE_ PRIVATE_ENDPOINT_CREATE`

`VNIC_CREATE`(private endpoint compartment)

`VNIC_DELETE`(private endpoint compartment)

`SUBNET_ATTACH`(subnet compartment)

`NETWORK_SECURITY_GROUP_UPDATE_MEMBERS`(private endpoint compartment)

`VNIC_ASSOCIATE_NETWORK_SECURITY_GROUP`(private endpoint compartment)

List the private endpoints in a compartment

`OBJECTSTORAGE_ PRIVATE_ENDPOINT_INSPECT`

Get a private endpoint's details

`OBJECTSTORAGE_ PRIVATE_ENDPOINT_READ`

Edit a private endpoint

`OBJECTSTORAGE_ PRIVATE_ENDPOINT_UPDATE`

`VNIC_UPDATE`(private endpoint compartment)

`NETWORK_SECURITY_GROUP_UPDATE_MEMBERS`(private endpoint compartment)

`VNIC_ASSOCIATE_NETWORK_SECURITY_GROUP`(private endpoint compartment)

`VNIC_DISASSOCIATE_NETWORK_SECURITY_GROUP`(private endpoint compartment)

Delete a private endpoint from a compartment

`OBJECTSTORAGE_ PRIVATE_ENDPOINT_DELETE`

`VNIC_DELETE`(private endpoint compartment)

`SUBNET_DETACH`(subnet compartment)

### Access Targets

Use the following access policy to restrict a specific bucket to a specific network source:
```

```

## Limits

The following limits apply to private endpoints in Object Storage:
- You can use a maximum of 10 private endpoints within a tenancy.
- You can use up to 10 access targets for each private endpoint.
- Each private endpoint has a maximum bandwidth of 25 Gbps.

## Pre-Authenticated Request Behavior

When creating pre-authenticated requests (PARs) through private endpoints, note the following points:
- The PAR has the private endpoint fully-qualified domain name (FQDN) as part of the PAR URL.
- You can create a PAR through the private endpoint on buckets that are allowed by Access Targets only.
- You can access PAR buckets and objects from the public endpoint as well by replacing the private endpoint FQDN in the URL with the public endpoint.

For more information, see[Pre-Authenticated Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm).

## Using Private Endpoints

After you create an Object Storage private endpoint, it becomes usable. The fully-qualified domain names (FQDNs) that are created from the DNS prefix input become resolvable by the private DNS zone within the VCN. These FQDNs become the endpoint that are used in requests to Object Storage to ensure the requests go through the private endpoint.

Here is an example of how the FQDNs appear in the CLI-based details of a private endpoint:
```

```

Here is an example getting details of an object using one of the FQDNs you created using the CLI:
```

```

## Best Practices

To help ensure secure, private connectivity to Object Storage, we recommend the following best practices when using private endpoints:
- You must allow ingress for port 443 using one of the following methods:
- Adding a security list rule in the default security list. This security rule is applied to all VNICs in the subnet. See[Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)for more information.
- Creating a network security group (NSG) with the ingress' security list rule, and then including the NSG in the private endpoint creation. This NSG is only applied to the private endpoint. See[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)for more information. We recommend using this method as it provides a greater level of secuirty.
- To avoid data exfiltration across tenancies, begin with an access target configured such as namespace = your_namespace , compartment = *, bucket = *. This configuration allows the private endpoint to access all buckets in all compartments in your namespace.
- To further restrict access to only one or more buckets that can be accessed by the private endpoint, begin with an access target configured such as namespace = &lt; your_namespace &gt;, compartment = Compartment1, bucket = Bucket1. You can specify up to 10 buckets using access targets.
- Use IAM polices on the bucket, so requests are only authorized if they originate from a specific VCN or a CIDR block within that VCN. All other access, including over the internet, is blocked to these buckets. See[Managing Network Sources](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingnetworksources.htm)for more information.

The following is a sample policy to restrict a specific bucket to a specific network source:
```

```

- One or more private DNS zones are created in the VCN during the creation of a private endpoint. This private DNS zone helps resolve the private endpoint fully-qualified domain name to the private IP address of the private endpoint. When using private endpoints, we recommend not to change DNS entries in the private DNS zone of the VCN. Changing these can affect the behavior of traffic and requests flowing through the private endpoint.
-
