# Adding a User to a User Group for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/add-user_group.htm
- Fetched: 2026-09-05 03:00 CDT

# Adding a User to a User Group for a Roving Edge Infrastructure Device

Describes how to add a user to a user group on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/add-user_group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/add-user_group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/add-user_group.htm#)
- 

- 

Open the navigation menu and select Identity Management &gt; Groups . The Groups page appears. All user groups are listed in tabular form.
- 

Select the user group whose details that you want to get. The user group's Details dialog box appears.
- 

Select Group Members under the left-side navigation. All the members in the group are listed in tabular form.
- 

Select Add User to Group under Group Members . The Add User to Group dialog box appears.
- 

Select a user from the Users list and select Add . The Group Members list reappears listing the user you just added.
- Add any other users to the group using the same method.
- 

Use the[oci iam group add-user](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/group/add-user.html)command and required parameters to add a user to a user group on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/../../Access/cli_install.htm#CLI)
- 

Run the[
