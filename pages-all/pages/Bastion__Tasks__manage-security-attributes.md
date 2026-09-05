# Managing a Bastion's Security Attributes
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/manage-security-attributes.htm
- Fetched: 2026-09-05 01:42 CDT

# Managing a Bastion's Security Attributes

Manage the security attributes for a bastion.

You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/manage-security-attributes.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/manage-security-attributes.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/manage-security-attributes.htm#)
- 

- On the Bastions list page, find the bastion that you want to work with. If you need help finding the list page or the bastion, see[Listing Bastions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/list-bastion.htm).
- From the Actions menu (three dots) for the bastion, select Manage security attributes .
- Update the configuration of any existing security attribute listed.

- To add a security attribute, select Add security attribute . You can add up to three security attributes.
- To remove a security attribute, select the Delete Row button.
- Select Update to save the changes.

The security attributes that you added or updated are viewable on the Security tab of the bastion's[details](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/get-bastion.htm#top)page.
- 

Use the`--security-attributes`option when running the[oci bastion bastion update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bastion/bastion/update.html)command to add Zero Trust Packet Routing (ZPR) security attributes when you're updating a bastion:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateBastion](https://docs.oracle.com/iaas/api/#/en/bastion/latest/Bastion/UpdateBastion)operation to edit a bastion. Include the`securityAttributes`
