# Deleting Auth Tokens from a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Auth_Token/delete_auth_token.htm
- Fetched: 2026-09-05 03:00 CDT

# Deleting Auth Tokens from a Roving Edge Infrastructure Device

Describes how to delete an auth token credential from a user on your Roving Edge Infrastructure device.
Note  
  

Deleting an auth token makes it no longer valid for accessing third-party APIs.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Auth_Token/delete_auth_token.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Auth_Token/delete_auth_token.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Auth_Token/delete_auth_token.htm#)
- 

- 

Open the navigation menu and select Identity Management &gt; Users . The Users page appears. All users are listed in tabular form.
- 

Select the user for which you want to create an auth token. The user's Details page appears.
- 

Select Auth Tokens under Resources . The Auth Tokens page appears. All auth tokens are listed in tabular form.
- 

Select the Actions menu ( ) for the auth token you want to delete and select Delete .
- 

Confirm the deletion when prompted.
- 

Use the[oci iam auth-token delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/auth-token/delete.html)command and required parameters to delete an auth token credential from a user on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Auth_Token/../../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Auth_Token/../../../Access/cli_install.htm#CLI)
- 

Run the[
