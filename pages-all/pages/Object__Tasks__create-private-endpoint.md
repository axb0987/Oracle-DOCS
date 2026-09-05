# Creating an Object Storage Private Endpoint
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm
- Fetched: 2026-09-05 02:50 CDT

# Creating an Object Storage Private Endpoint

Create a private endpoint to reach Object Storage using a private IP address within your VCN without accessing the public internet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm#)
- 

- On the Private Endpoints list page, select Create private endpoint . If you need help finding the list page, see[Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-private-endpoint.htm).
The Create private endpoint panel opens.
- Enter the following information:

- Name : Enter a name for the private endpoint. The name value is a case-insensitive string using alpha-numeric characters (no special characters).
- DNS prefix : Enter a DNS prefix for the private endpoint. This value is part of the URL used to access Object Storage. The DNS prefix is a case-insensitive string using alpha-numeric characters (no special characters). It must be unique within the VCN.
- Select VCN compartment : Select the compartment containing the VCN you want.
- Select VCN : Select the VCN you want from the list of all VCNs available in the compartment you previously chose.
- Select subnet: Select a subnet from the list of subnets available from the VCN you previously chose.

## Access targets

Add an access target to the private endpoint. Enter the following information:
- Namespace : Enter the namespace for the access target. You can enter either the namespace's name or "*" to specify a wildcard. You can only use the wildcard if the compartment and buckets values also specified as "*" as described below. See[Namespaces](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm)for more information.
- Compartment OCID : Enter the OCID of the compartment for the access target. You can enter either the compartment's OCID, or "*" to indicate all the compartments are available.
- Bucket name : Enter the name of the bucket for the target. You can enter either the bucket's name, or "*" to indicate all the buckets within the compartments are available.

Select Add access target to create another access target. You can create a total of 10 access targets.

## Tags

Select the Tags tab.

Select Add tag . The tagging options appear where you can apply tags to the resource. For information about tagging, see[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).

## Security Attributes

Add security attributes.

Prerequisites

To add a security attribute, you must have permissions to use the security attribute namespace. For more details on the permissions required to apply, update, or remove a security attribute for a resource, see[Security Attributes](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/security-attributes.htm)and[Zero Trust Packet Routing IAM Policies](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/policy-reference.htm).

You must also[write ZPR policies](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-zpr-policy.htm)to connect resources using security attributes.

If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.

Add security attributes

Once permissions are in place, you can add up to three security attributes to control access to this private endpoint. In the Security attributes section, select Add security attribute and then enter the following information:
- Namespace : Select a security attribute namespace from the list. A security attribute namespace is a container for a set of security attributes in Zero Trust Packet Routing (ZPR).

This list contains those security attribute namespaces already configured. See[Creating a Security Attribute Namespace](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-security-attribute-namespace.htm)for more information.
- Key : Select a key from the list. The key is the name for a specific security attribute.
- Value : Enter a value or select a value for the corresponding key from the list. This is the value for a specific security attribute.

See also[Adding Security Attributes to a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/objectstorage-usingzpr.htm#objectstorage-usingzpr).

## Advanced options

Select Advanced options . Here you can configure the following optional features.

IP address : Enter or select the IP address you prefer used with the private endpoint.

### Network security group (NSG)

Select Add NSG to add a Network security group (NSG) to the private endpoint. Enter the name of the NSG from the list. The available NSGs are determined by the VCN you selected earlier.

### Additional DNS prefixes

Select Add DNS prefix to add another DNS prefix to the private endpoint.
Select Create private endpoint .
- 

Use the[oci os private-endpoint create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/create.html)command and required parameters to create a private endpoint in Object Storage:

```

```

where the following variables apply:
- 

`prefix`is the DNS prefix of the private endpoint.
- 

`access_targets`are listed in JSON format. Separate each access target with a comma (",").

For example:
```

```

If you have several access targets, the output would appear as this:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the following API operation:
```

```

These are the available payload properties:
- accessTargets : A list of targets that can be accessed by the private endpoint.
- additionalPrefixes (optional): A list of more DNS prefixes that you can provide.
- compartmentId : The ID of the compartment the private endpoint is created.
- definedTags (optional): Defined tags for this resource.
- freeformTags (optional): Free-form tags for this resource.
- name : The name of the private endpoint.
- nsgIds (optional): A list of the OCIDs of the network security groups (NSGs) to add the private endpoint's VNIC.
- prefix : The DNS prefix to use for the private endpoint FQDN in the VCN's private DNS zone.
- privateEndpointIp (optional): The private IP address to assign to this private endpoint if its available. Will return an error if IP address unavailable.
- securityAttributes (optional): Security attributes for this resource. Each key is predefined and scoped to a namespace.

Example:`{"Oracle-ZPR": {"MaxEgressCount": {"value": "42", "mode": "enforce"}}}`
- subnetId : The OCID of the customer's subnet where the private endpoint VNIC resides.

See also[CreatePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/PrivateEndpoint/CreatePrivateEndpoint)
