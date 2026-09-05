# Creating a Customer Secret Key for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Secret_Keys/create_customer-secret-key.htm
- Fetched: 2026-09-05 03:00 CDT

# Creating a Customer Secret Key for a Roving Edge Infrastructure Device

Describes how to create a customer secret key for a user on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Secret_Keys/create_customer-secret-key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Secret_Keys/create_customer-secret-key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Secret_Keys/create_customer-secret-key.htm#)
- 

- 

Open the navigation menu and select Identity Management &gt; Users . The Users page appears. All users are listed in tabular form.
- 

Select the user for whom you want to create a customer secret key. The user's Details page appears.
- 

Select Customer Secret Keys under Resources . The Customer Secret Keys page appears. All customer secret keys are listed in tabular form.
- 

Select Generate Secret Key . The Generate Secret Key dialog box appears.
- 

Enter a name for the secret key.
- 

Select Generate Secret Key .

The generated Secret Key is displayed in the Generate Secret Key dialog box. At the same time, Oracle generates the Access Key that is paired with the Secret Key . The newly generated Customer Secret key is added to the list of Customer Secret Keys .
- 

Copy the Secret Key immediately, because you cannot retrieve the Secret Key again after closing the dialog box for security reasons. If you are an administrator creating a customer secret key for another user, you need to securely deliver it to the user by providing it verbally, printing it out, or sending it through a secure email service.
- Select Close .
- To show or copy the Access Key , select the Show or Copy action to the left of the Name of a particular customer secret key.
- 

Use the[oci iam customer-secret-key create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/customer-secret-key/create.html)command and required parameters to create a customer secret key for a user on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Secret_Keys/../../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/Secret_Keys/../../../Access/cli_install.htm#CLI)
- 

Run the[
