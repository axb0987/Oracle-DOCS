# Editing an Object Storage Private Endpoint
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/update-private-endpoint.htm
- Fetched: 2026-09-05 02:51 CDT

# Editing an Object Storage Private Endpoint

Update an Object Storage private endpoint's configuration.

You can update the following settings for a private endpoint:
- Access targets
- Tagging
- Security attributes

You can't update the following:
- The compartment where the private endpoint resides.
- Private endpoint name
- DNS prefix
- Network security group

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/update-private-endpoint.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/update-private-endpoint.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/update-private-endpoint.htm#)
- 

- On the Private endpoints list page, select the Object Storage private endpoint that you want to work with. If you need help finding the list page or the Object Storage private endpoint, see[Listing Private Endpoints in Object Storage](https://docs.oracle.com/iaas/Content/Object/Tasks/list-private-endpoint.htm).
- From the Actions menu for the private endpoint, select Edit endpoint .
The Edit private endpoint panel opens.
- Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see[Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm).
- To add only security attributes, select the Security tab and then select Add security attributes .

You can add up to three security attributes to control access to this private endpoint. Select Add security attribute , and then enter the following information:
- Namespace : Select a security attribute namespace from the list. A security attribute namespace is a container for a set of security attributes in Zero Trust Packet Routing (ZPR).

This list contains those security attribute namespaces already configured. See[Creating a Security Attribute Namespace](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-security-attribute-namespace.htm)for more information.
- Key : Select a key from the list. The key is the name for a specific security attribute.
- Value : Enter a value or select a value for the corresponding key from the list. This is the value for a specific security attribute.

To understand the permissions required to apply, update, or remove a security attribute for a resource, see[Security Attributes](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm#zpr-secy-attributes).

See also[Adding Security Attributes to a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/objectstorage-usingzpr.htm#objectstorage-usingzpr).
- Select Update .
- 

Use the[oci os private-endpoint update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/update.html)command and required parameters to edit a private endpoint in Object Storage:
```

```

where`access_targets`lists one or more access targets being updated to the new settings using the following syntax:
```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the following API operation:
```

```

These are the available payload properties:
- name : The name of the private endpoint.
- accessTargets : A list of targets that can be accessed by the private endpoint.
- freeformTags (optional): Free-form tags for this resource.
- definedTags (optional): Defined tags for this resource.
- namespace The Object Storage namespace associated with the private endpoint.
- securityAttributes (optional): Security attributes for this resource. Each key is predefined and scoped to a namespace.

Example:`{"Oracle-ZPR": {"MaxEgressCount": {"value": "42", "mode": "enforce"}}}`

See also[UpdatePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/PrivateEndpoint/UpdatePrivateEndpoint)
