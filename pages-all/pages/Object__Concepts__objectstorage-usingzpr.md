# Adding Security Attributes to a Private Endpoint
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorage-usingzpr.htm
- Fetched: 2026-09-05 02:50 CDT

# Adding Security Attributes to a Private Endpoint

Use Zero Trust Packet Routing to manage access to private endpoints in Object Storage.

You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).

Prerequisites
- Create security attribute namespaces and security attributes, and grant the permissions required to apply, update, or remove a security attribute for a resource.

See[Security Attributes](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/security-attributes.htm)and[Zero Trust Packet Routing IAM Policies](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/policy-reference.htm).
- You must also[write ZPR policies](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-zpr-policy.htm)to connect resources using security attributes.
Caution  
  
If an endpoint has a Zero Trust Packet Routing (ZPR) security attribute, traffic to the endpoint must satisfy ZPR policies and also all NSG and security list rules. For example, if you're already using NSGs and you add a security attribute to an endpoint, all traffic to the endpoint is blocked. From then onward, a ZPR policy must explicitly allow traffic to the endpoint.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorage-usingzpr.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorage-usingzpr.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorage-usingzpr.htm#)
- 

- On the Private Endpoints list page, select Create private endpoint . If you need help finding the list page, see[Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/../Tasks/list-private-endpoint.htm).
- After entering required details for the private endpoint, scroll to the Security attributes section and select Add security attribute .
You can add up to three security attributes to control access to this private endpoint.
- Enter the following information:

- Namespace : Select a security attribute namespace from the list. A security attribute namespace is a container for a set of security attributes in Zero Trust Packet Routing (ZPR).

This list contains those security attribute namespaces already configured. See[Creating a Security Attribute Namespace](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-security-attribute-namespace.htm)for more information.
- Key : Select a key from the list. The key is the name for a specific security attribute.
- Value : Enter a value or select a value for the corresponding key from the list. This is the value for a specific security attribute.

These values must match an existing ZPR policy. For more information about security attributes and security attribute namespaces, see[Security Attributes](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/security-attributes.htm).
- When finished, select Add security attributes .
- 

Use the[oci os private-endpoint create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/create.html)command and parameters shown to add security attributes when you create a private endpoint:

```

```

Use the[oci os private-endpoint update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/update.html)command and parameters shown to add security attributes to an existing private endpoint:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreatePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/PrivateEndpoint/CreatePrivateEndpoint)operation to add security attributes when you create a private endpoint, and use the securityAttributes attribute.

Run the[UpdatePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/PrivateEndpoint/UpdatePrivateEndpoint)
