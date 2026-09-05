# Creating and Submitting a Node for Compute, GPU, and Storage Devices
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/create_node2.htm
- Fetched: 2026-09-05 03:01 CDT

# Creating and Submitting a Node for Compute, GPU, and Storage Devices

Roving Edge nodes are the resources in Oracle Cloud Infrastructure (OCI) that are associated with the Roving Edge Device at the customer site. Each node is associated with one Roving Edge device.
Important  
  

For new deployments of Roving Edge, see[Creating a Roving Edge Infrastructure in OCI](https://docs.oracle.com/iaas/roving-edge-infrastructure/rvr/infrastructure/create-infrastructure.htm). Content below is for Roving Edge Classic infrastructure which is being deprecated.

You must create a node in your OCI tenancy before you can install and self-provision the Roving Edge Device at your site.

By default, the device generates a self-signed certificate. If you plan to use another certificate management service such as the[OCI Certificate Management service](https://docs.oracle.com/iaas/Content/certificates/managing-certificate-authorities.htm), have the following information handy:
- 

Certificate name
- 

The certificate authority to be used for generating and renewing certificates for the device node
- 

Date and time on which the certificate is no longer valid
- 

Signature algorithm to use with the certificate
- 

Key algorithm
- 

Compartment for the certificate

For information about Roving Edge models and shapes, see[Roving Edge Infrastructure Device Specifications](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/../device_specifications.htm#DeviceSpecifications).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/create_node2.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/create_node2.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/create_node2.htm#)
- 

Note  
  
Depending on the realm that your region is in, you might be prompted to provide a password, passphrase, and shipping details. If you see these prompts, include the information. If you're not prompted for these items, continue to enter what you're prompted to enter, and create the node.
- 

In the Oracle Cloud Console, open the navigation menu, select Hybrid , then select Nodes .
- 

Select Create Node .

The Create Node dialog box is displayed.
- 

Enter the required information:
- 

Name : Enter a name for the device node. Avoid entering confidential information.
- 

Create in Compartment : Select the compartment for the node.
- 

Shape : Select a shape based on the Roving Edge Device model that you're requesting. For a description of shapes, see[Roving Edge Infrastructure Device Specifications](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/../device_specifications.htm#DeviceSpecifications).
- 

Enclosure type : Select one of the following options:
- 

Ruggedized case : If selected, you receive a ruggedized case. For more information about cases, see[Ruggedizing Roving Edge Infrastructure Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/../Getting_Started/ruggedizing_devices.htm#ruggedizing-devices).
- 

No case : Select this option if you don't want a case.
- 

(optional) Expand Certificate options : Select to display and complete the following certificate options:

You have different options for certificate management:
- (Optional) You can use the default self-signed certificates for the device. For this option, leave this section blank. You configure self-signed certificates after you receive the device (see[Certificate Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/../certificate-management.htm#certificate-management)). You can also configure the OCI Certificate service later.

Or:
- (Optional) You can use the OCI Certificate service to manage certificates. For this option, enter the certificate information you got when you created a certificate authority. See[Managing Certificate Authorities](https://docs.oracle.com/iaas/Content/certificates/managing-certificate-authorities.htm). If you don't have the certificate information, you can enter it later using[Editing a Node for Compute, GPU, and Storage Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/update_node2.htm#top), but before you provision the device.

Or:
- (Optional) You can use your own certificate service to manage certificates. For this option, enter the certificate information you got when you created a certificate authority. If you don't have the certificate information, you can enter it later using[Editing a Node for Compute, GPU, and Storage Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/update_node2.htm#top), but before you provision the device.
- 

Common Name : Enter a name for the certificate.
- 

Issuer Certificate Authority in &lt;compartment&gt; : Select a certificate authority to be used for generating and renewing certificates for the device node. Select Change Compartment to select a certificate authority in another compartment.
- 

Certificate Validity End Date : Enter the date and time on which the certificate is no longer valid.
- 

Signature Algorithm : Select a signature algorithm from the list.
- 

Key Algorithm : Select a key algorithm from the list.
- 

Certificate Compartment : Select the compartment where the certificate resides.
- 

(Optional) Show Tagging options : Select to display the Tagging option. If you're not sure about whether to apply tags, skip this option (you can apply tags later) or ask your administrator.
- 

Select Create Node .

The device node details page is displayed.
- Select Submit for approval.

What's Next?

After you receive the device, set up the device. See[Setting Up an Oracle Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/../Setup-RED/install-overview.htm#SettingUpDevices).
- 

Use the[oci rover node create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/node/create.html)command and required parameters to create a Roving Edge Infrastructure device node in Oracle Cloud Infrastructure:
```

```

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/../compartments.htm#comparments).

For shape_name , specify one of the following shape values based on the Roving Edge Ultra device model.

Use the[oci rover node request-approval](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/node/request-approval.html)command and required parameters to submit a request for a Roving Edge Ultra node in Oracle Cloud Infrastructure:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).

What's Next?

After you receive the device, set up the device. See[Setting Up an Oracle Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/../Setup-RED/install-overview.htm#SettingUpDevices).
- 

Run the[CreateRoverNode](https://docs.oracle.com/iaas/api/#/en/rover/latest/RoverNode/CreateRoverNode)operation to create a Roving Edge Infrastructure device node in Oracle Cloud Infrastructure.

After the device node is created, use the Oracle Cloud Console to submit the node for approval. See Step[7](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/create_node2.htm#console__step-submit)in[Using the OCI Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/create_node2.htm#console).

For information about using the API and signing requests, see[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).

What's Next?

After you receive the device, set up the device. See[Setting Up an Oracle Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/../Setup-RED/install-overview.htm#SettingUpDevices)
