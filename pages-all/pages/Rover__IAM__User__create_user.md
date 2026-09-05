# Creating a User for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/create_user.htm
- Fetched: 2026-09-05 03:00 CDT

# Creating a User for a Roving Edge Infrastructure Device

Describes how to create a user on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/create_user.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/create_user.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/create_user.htm#)
- 

- 

Open the navigation menu and select Identity Management &gt; Users . The Users page appears. All users are listed in tabular form.
- 

Select Create User . The Create User dialog box appears.
- 

Enter the following:
- 

Name : A unique name or email address for the user. The name must be unique across all users in your tenancy. You cannot change this value later. The name must meet the following requirements: No spaces. Only Basic Latin letters (ASCII), numerals, hyphens, periods, underscores, +, and @.
- 

Description : This value could be the user's full name, a nickname, or other descriptive information. You can change this value later.
- 

Select Create . The new user appears in the User page. Next, you must access a secret key from the new user's UI console OAuth 2.0 client credential and forward it to the intended user. This key is the user's login password for accessing the Device Console.
- 

Select the user entry in the User page. The user's Details page appears.
- 

Select OAuth 2.0 Client Credentials on the left side of the page. The OAuth 2.0 Client Credentials page appears. By default, only the UI-console-oauth-credential is present in the list of OAuth 2.0 client credentials for a newly created user.
- 

Select UI-console-oauth-credential. The UI-console-oauth-credential's Details page appears.
- 

Select Regenerate Secret . The Regenerate OAuth 2.0 Client Credential dialog box appears, displaying the new password for the user.
- 

Copy the generated secret and store it for your records. You cannot display this secret key after the dialog box is closed.
- 

Select Close to close the dialog box.
- 

Forward the secret key to the intended user. This key acts as the initial password for the user. The user can reset their Device Console login password by repeating the steps to regenerate a secret key within their user account.

New users created through the Device Console are automatically assigned to the default Administrators group. Now you need to give the user the credentials they need. See[User Credentials for Roving Edge Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/../User_Credentials/user_credential_management.htm#UserManagement).
- 

Use the[oci iam user create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/user/create.html)command and required parameters to create a user on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/../../Access/cli_install.htm#CLI)
- 

Run the[
