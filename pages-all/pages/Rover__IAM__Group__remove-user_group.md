# Removing a User from a User Group for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/remove-user_group.htm
- Fetched: 2026-09-05 03:00 CDT

# Removing a User from a User Group for a Roving Edge Infrastructure Device

Describes how to remove a user from a user group on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/remove-user_group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/remove-user_group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/remove-user_group.htm#)
- 

- 

Open the navigation menu and select Identity Management &gt; Groups . The Groups page appears. All user groups are listed in tabular form.
- 

Select the user group whose member that you want to remove. The user group's Details page appears.
- 

Select Group Members under the left-side navigation. All the members in the group are listed in tabular form.
- 

Select the Actions menu ( ) for the member that you want to remove and select Remove Member from Group .
- 

Confirm the removal when prompted.
- 

Use the[oci iam group remove-user](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/group/remove-user.html)command and required parameters to remove a user from a user group on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/../../Access/cli_install.htm#CLI)
- 

Run the[
