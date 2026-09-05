# Deleting API Signing Keys from a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/API_Key/delete_api-key.htm
- Fetched: 2026-09-05 03:00 CDT

# Deleting API Signing Keys from a Roving Edge Infrastructure Device

Describes how to delete an API signing key credential from a user on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/API_Key/delete_api-key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/API_Key/delete_api-key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/API_Key/delete_api-key.htm#)
- 

- 

Open the navigation menu and select Identity Management &gt; Users . The Users page appears. All users are listed in tabular form.
- 

Select the user for which you want to create an auth token. The user's Details page appears.
- 

Select API Keys under Resources . The AOI Keys page appears. All API keys are listed in tabular form.
- 

Select the Actions menu ( ) for the API key you want to delete and select Delete .
- 

Confirm the deletion when prompted.
- 

Use the[oci iam user api-key delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/user/api-key/delete.html)command and required parameters to delete an API signing key credential from a user on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/API_Key/../../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/API_Key/../../../Access/cli_install.htm#CLI)
- 

Run the[
