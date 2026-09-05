# Editing a Session in Bastion
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/update-session.htm
- Fetched: 2026-09-05 01:42 CDT

# Editing a Session in Bastion

Describes how to edit the details of a bastion session.

You can update only the display name of a session.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/update-session.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/update-session.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/update-session.htm#)
- 

- On the Bastions list page, select the bastion that hosts the session that you want to work with. If you need help finding the list page or the bastion, see[Listing Bastions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/list-bastion.htm).
- On the details page, select the Sessions tab or link.
- Select the Actions menu (three dots) for the session that you want to update, and then select Edit session name .
- Change the name of the session.

Avoid entering any confidential information in this field.
- Select Update .
- 

Use the[oci bastion session update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bastion/session/update.html)command and required parameters to edit the details of a bastion session:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateSession](https://docs.oracle.com/iaas/api/#/en/bastion/latest/Session/UpdateSession)
