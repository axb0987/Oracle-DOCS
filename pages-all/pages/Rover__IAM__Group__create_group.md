# Creating a User Group for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/create_group.htm
- Fetched: 2026-09-05 03:00 CDT

# Creating a User Group for a Roving Edge Infrastructure Device

Describes how to create a user group on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/create_group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/create_group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/create_group.htm#)
- 

- 

Open the navigation menu and select Identity Management &gt; Groups . The Groups page appears. All user groups are listed in tabular form.
- 

Select Create Group . The Create Group dialog box appears.
- 

Complete the following:
- 

Name : Enter a unique name for the user group. The name must be unique across all users in your tenancy. You cannot change this value later. The name must meet the following requirements: No spaces. Only Basic Latin letters (ASCII), numerals, hyphens, periods, underscores, +, and @.
- 

Description : Enter a description for the user group. You can change this value later.
- 

Select Create . The user group appears in the Groups page.
- 

Use the[oci iam group create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/group/create.html)command and required parameters to create a user group on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/../../Access/cli_install.htm#CLI)
- 

Run the[
