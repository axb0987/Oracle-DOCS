# Managing a Resolver Endpoint's Security Attributes
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-security-attributes.htm
- Fetched: 2026-09-05 02:47 CDT

# Managing a Resolver Endpoint's Security Attributes

Add, update, and remove security attributes associated with a resolver endpoint.

Use Zero Trust Packet Routing (ZPR) along with, or in place of, network security groups to control network access to resolver endpoints by applying security attributes to them and creating ZPR policies to control communication among them. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-security-attributes.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-security-attributes.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-security-attributes.htm#)
- 

## Adding Security Attributes

- On the Resolver endpoints list page, select the endpoint that you want to work with. If you need help finding the list page or the endpoint, see[Listing Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-list.htm).
The endpoints detail's page opens.
- Select Security .
The Security page opens.
- Find the Security attributes section and select Add security attributes .
The Add security attributes panel opens.
- Enter the following information:

- Namespace : Select a security attribute namespace from the list. This list contains those security attribute namespaces already configured. See[Creating a Security Attribute Namespace](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-security-attribute-namespace.htm)for more information.
- Key : Select a key from the list.
- Value : Select a value for the corresponding key from the list.
- Select the Add security attribute button to add another attribute up to a total of three.
You can also update the configuration of any existing security attribute listed here.
- Select Add security attributes at the bottom of the panel to complete the task.
The security attributes you added are viewable Security tab in the endpoint's details page.

## Editing Security Attributes

To update an endpoint's existing security attributes, follow these steps

- On the Resolver endpoints list page, select the endpoint that you want to work with. If you need help finding the list page or the endpoint, see[Listing Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-list.htm).
The endpoints detail's page opens.
- Select Security .
The Security page opens.
- From the Actions menu (three dots) for the endpoint you want, select Edit .
The Edit security attribute panel opens.
- Update the security attributes as described earlier in this topic.
- Select Update .
The security attributes you added or updated are viewable in the Security tab in the endpoint's details page.

## Deleting Security Attributes

To delete an endpoint's existing security attributes, follow these steps

- On the Resolver endpoints list page, select the endpoint that you want to work with. If you need help finding the list page or the endpoint, see[Listing Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-endpoint-list.htm).
The endpoint's details page opens.
- Select Security .
The Security page opens.
- From the Actions menu (three dots) for the endpoint you want, select Delete .
- When prompted, confirm the deletion.
- 

## Adding Security Attributes

You can include ZPR security attributes when using[oci dns resolver-endpoint create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver-endpoint/create.html)command by including the`security-attributes`option and corresponding value:
```

```

where`security_attributes`are ZPR security attributes for this endpoint.

For example:
```

```

For information on creating an endpoint using the CLI, see[oci dns resolver-endpoint create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver-endpoint/create.html).

Similarly, you can use the`security-attributes`option when running the[oci dns resolver-endpoint update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver-endpoint/update.html)command to add ZPR security attributes when you're updating it:

```

```

For information on updating an endpoint using the CLI, see[oci dns resolver-endpoint update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver-endpoint/update.html).

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).

## Editing Security Attributes

Use the`security-attributes`option when running the[oci dns resolver-endpoint update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver-endpoint/update.html)command to change the settings of existing ZPR security attributes.

## Deleting Security Attributes

Use the`security-attributes`option with the value "`{}`" when running the[oci dns resolver-endpoint update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver-endpoint/update.html)command to delete the settings of ZPR security attributes. For example:
```

```

- 

## Adding Security Attributes

Run the[CreateResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/CreateResolverEndpoint)operation to add security attributes to an endpoint you're creating. Include the`securityAttributes`attributes and it values.

Run the[UpdateResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/UpdateResolverEndpoint)operation to add security attributes to an existing endpoint. Include the`securityAttributes`attributes and it values.

## Editing Security Attributes

Run the[UpdateResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/UpdateResolverEndpoint)operation to update an endpoint. Include the`securityAttributes`attributes and update their existing values.

## Deleting Security Attributes

Run the[UpdateResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/UpdateResolverEndpoint)operation to update an endpoint. Include the`securityAttributes`
