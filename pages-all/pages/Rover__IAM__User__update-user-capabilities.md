# Updating a User's Capabilities for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/update-user-capabilities.htm
- Fetched: 2026-09-05 03:00 CDT

# Updating a User's Capabilities for a Roving Edge Infrastructure Device

Describes how to update the capabilities of a user on your Roving Edge Infrastructure device.

You can make updates to the following user capabilities:
- 

API signing keys
- 

Auth token
- 

Customer secret keys
- 

OAuth 2.0 client credentials
- 

Local password
- 

SMTP credentials

See[About User Capabilities](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingusers.htm#usercaps)in the Oracle Cloud Infrastructure documentation for more information on this feature.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/update-user-capabilities.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/update-user-capabilities.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/update-user-capabilities.htm#)
- 

- 

Open the navigation menu and select Identity Management &gt; Users . The Users page appears. All users are listed in tabular form.
- 

Select the user whose details you want to get. The user's Details page appears.
- 

Select Edit User Capabilities . The Edit User Capabilities dialog box appears.
- 

Update any of the following capabilities:
- 

API Keys
- 

Auth Token
- 

Customer Secret Keys
- 

OAuth 2.0 Client Credentials
- 

Local password
- 

SMTP credentials
- 

Select Save Changes .
- 

Use the[oci iam user update-user-capabilities](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/user/update-user-capabilities.html)command and required parameters to update the capabilities of a user on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/../../Access/cli_install.htm#CLI)
- 

Run the[
