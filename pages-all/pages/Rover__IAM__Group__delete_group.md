# Deleting a User Group from a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/delete_group.htm
- Fetched: 2026-09-05 03:00 CDT

# Deleting a User Group from a Roving Edge Infrastructure Device

Describes how to delete a user group from your Roving Edge Infrastructure device.
Note  
  

You cannot delete a user group that contains users. Delete all users in the group first before deleting the user group. See[Removing a User from a User Group](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/remove-user_group.htm#RemovingUserGroup)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/delete_group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/delete_group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/delete_group.htm#)
- 

- 

Open the navigation menu and select Identity Management &gt; Groups . The Groups page appears. All user groups are listed in tabular form.
- 

Select the user group that you want to delete. The user group's Details dialog box appears.
- 

Select Delete .
- 

Confirm the deletion when prompted.
- 

Use the[oci iam group delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/group/delete.html)command and required parameters to delete a user group from your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/../../Access/cli_install.htm#CLI)
- 

Run the[
