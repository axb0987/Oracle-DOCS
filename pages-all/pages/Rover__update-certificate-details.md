# Updating Certificate Details for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/update-certificate-details.htm
- Fetched: 2026-09-05 03:03 CDT

# Updating Certificate Details for a Roving Edge Infrastructure Device

Describes how to make changes to edit certificate for a Roving Edge Infrastructure device node.

Use the updating certificate details feature to update any combination of the certificate authority, key algorithm and signature algorithm the Roving Edge Infrastructure device node uses to create certificates. First, make the updates on the Oracle Cloud Infrastructure Cloud Console. Next, create a certificate by following the instructions depending on your device node's connected state or disconnected state.

## Using the OCI Cloud Console

- Access the Oracle Cloud Console.
- Open the navigation menu, select Hybrid , then select Nodes . The Nodes page is displayed.
- Select the nodes whose certificate details you want to update. The Details page of the node appears.
- Select the Certificate information tab.
- From the Actions menu at the top of the page, select Update Node Certificate Details . The Update Node Certificate Details dialog box appears.
- Update any of the following items:

- 

Issuer Certificate Authority in &lt;compartment&gt; : Select a certificate authority to be used for generating and renewing certificates for the device node. Select Change Compartment to select a certificate authority in another compartment.
- 

Signature Algorithm for Certificate : Select a signature algorithm from the list.
- 

Key Algorithm : Select a key algorithm from the list.
- Select Save Changes . The Details page displays a message confirming the certificate details for the device node were successfully updated.
- Continue on with the subsequent steps in the following topics depending on whether your device node is in a connected or disconnected state:

- 

[Creating a certificate while connected](https://docs.oracle.com/en-us/iaas/Content/Rover/create-certificate-node.htm#top)
- 

[Creating a certificate while disconnected](https://docs.oracle.com/en-us/iaas/Content/Rover/create-certificate-offline.htm#top)

## Using the CLI

Use the[oci rover node certificate-authority update-root-ca](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/node/certificate-authority/update-root-ca.html)command and required parameters to update certificate details of a for a Roving Edge Infrastructure device node:
```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI)
