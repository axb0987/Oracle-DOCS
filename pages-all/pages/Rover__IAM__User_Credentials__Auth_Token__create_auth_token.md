# Creating Auth Tokens for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Auth_Token/create_auth_token.htm
- Fetched: 2026-09-05 03:00 CDT

# Creating Auth Tokens for a Roving Edge Infrastructure Device

Describes how to create an auth token credential for a user on your Roving Edge Infrastructure device.

If you are an administrator creating an auth token for another user, you need to securely deliver it to the user by providing it verbally, printing it out, or sending it through a secure email service.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Auth_Token/create_auth_token.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Auth_Token/create_auth_token.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Auth_Token/create_auth_token.htm#)
- 

- 

Open the navigation menu and select Identity Management &gt; Users . The Users page appears. All users are listed in tabular form.
- 

Select the user for which you want to create an auth token. The user's Details page appears.
- 

Select Auth Tokens under Resources . The Auth Tokens page appears. All auth tokens are listed in tabular form.
- 

Select Generate Token . The Generate Token dialog box appears.
- 

Enter a Description that indicates what this token is for, for example, "Swift password token."
- 

Select Generate Token . The new token string is displayed.
- 

Copy the token string immediately, because you can't retrieve it again after closing the Generate Token dialog box.
- 

Use the[oci iam auth-token create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/auth-token/create.html)command and required parameters to create an auth token credential for a user on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Auth_Token/../../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Auth_Token/../../../Access/cli_install.htm#CLI)
- 

Run the[
