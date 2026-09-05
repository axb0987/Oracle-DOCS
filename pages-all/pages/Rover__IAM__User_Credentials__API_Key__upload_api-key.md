# Uploading an API Signing Key for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/API_Key/upload_api-key.htm
- Fetched: 2026-09-05 03:00 CDT

# Uploading an API Signing Key for a Roving Edge Infrastructure Device

Describes how to create an API signing key credential for a user on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/API_Key/upload_api-key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/API_Key/upload_api-key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/API_Key/upload_api-key.htm#)
- 

- 

Open the navigation menu and select Identity Management &gt; Users . The Users page appears. All users are listed in tabular form.
- 

Select the user for which you want to create an auth token. The user's Details page appears.
- 

Select API Keys under Resources . The API Keys page appears. All API keys are listed in tabular form.
- 

Select Add Public Key . The Add Public Key dialog box appears.
- 

Select one of the following options:
- 

Choose Public Key File : Drag and drop a key file into the Public Key box or select select one to navigate to a location in your network where you can select a key file.
Note  
  

All public key files must have the`.pem`extension.
- 

Paste Public Keys : Copy and paste the public key into the Public Key box.
- 

Select Add .
- 

View the user's Details page to confirm the uploading.
- 

For the API key you want to delete, select Edit .
- 

Make your changes and select Save .
- 

Use the[oci iam user api-key upload](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/user/api-key/upload.html)command and required parameters to create an API signing key credential for a user on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/API_Key/../../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/API_Key/../../../Access/cli_install.htm#CLI)
- 

Run the[
