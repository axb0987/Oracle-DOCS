# Deleting a Customer Secret Key from a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Secret_Keys/delete_customer-secret-key.htm
- Fetched: 2026-09-05 03:00 CDT

# Deleting a Customer Secret Key from a Roving Edge Infrastructure Device

Describes how to delete a customer secret key from a user on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Secret_Keys/delete_customer-secret-key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Secret_Keys/delete_customer-secret-key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Secret_Keys/delete_customer-secret-key.htm#)
- 

- 

Open the navigation menu and select Identity Management &gt; Users . The Users page appears. All users are listed in tabular form.
- 

Select the user whose customer secret key you want to delete. The user's Details page appears.
- 

Select Customer Secret Keys under Resources . The Customer Secret Keys page appears. All customer secret keys are listed in tabular form.
- 

Select the secret key you want to delete. The Customer Secret Key dialog box appears.
- 

Select Delete .
- 

Confirm the deletion when prompted.
- 

Use the[oci iam customer-secret-key delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/customer-secret-key/delete.html)command and required parameters to delete a customer secret key from a user on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Secret_Keys/../../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Secret_Keys/../../../Access/cli_install.htm#CLI)
- 

Run the[
