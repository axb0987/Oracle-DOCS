# Updating a Bastion
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/update-bastion.htm
- Fetched: 2026-09-05 01:42 CDT

# Updating a Bastion

Edit the details of a bastion.

Changes to a bastion's settings don't affect existing sessions on the bastion. Changes apply only to new sessions.

You can't move a bastion to a different VCN (virtual cloud network) or subnet .

- [Console](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/update-bastion.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/update-bastion.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/update-bastion.htm#)
- 

- On the Bastions list page, select the bastion that you want to work with. If you need help finding the list page or the bastion, see[Listing Bastions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/list-bastion.htm).
- On the details page, select Edit .
- Under CIDR block allowlist , update the address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion. A more limited range offers better security.
- (Optional) Expand Advanced options and change the maximum amount of time that any session on this bastion can remain active by entering a value for Maximum session time-to-live . Provide a value of at least 30 minutes that doesn't exceed 180 minutes (3 hours). You can delete a session before it expires.
- Select Save changes .
- 

Use the[oci bastion bastion update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bastion/bastion/update.html)command and required parameters to edit a bastion:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateBastion](https://docs.oracle.com/iaas/api/#/en/bastion/latest/Bastion/UpdateBastion)
