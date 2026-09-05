# Creating a Roving Edge Ultra Node
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/create_ultra.htm
- Fetched: 2026-09-05 03:02 CDT

# Creating a Roving Edge Ultra Node

Create a Roving Edge Ultra node in Oracle Cloud Infrastructure (OCI) to request a Roving Edge Ultra.

These instructions create the Roving Edge Ultra node.
Note  
  

Roving Edge Ultra node orders can only be shipped to specific countries depending on where the order is placed. Contact your Oracle account representative for more information. See[Country Support](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/../country_support.htm#country_support)for more information.

For information about Roving Edge models and shapes, see[Roving Edge Infrastructure Device Specifications](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/../device_specifications.htm#DeviceSpecifications).

To view the status of your request, see[Viewing Your Ultra Request Status](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/../Getting_Started/viewing_request_status.htm#ViewRequestStatus).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/create_ultra.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/create_ultra.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/create_ultra.htm#)
- 

Note  
  
Depending on your OCI Region, you might be prompted to enter all the following menu items, or a subset of items. For example, the Console might not prompt you for a password, passphrase, or shipping information. In such cases, nothing is wrong. Continue to enter what you're prompted to enter, and create the node.
- In the Oracle Cloud Console, open the navigation menu, select Hybrid , then select Nodes .
- Select an compartment.
- 

Select Create Node .

The Create Node dialog box is displayed.
- 

Enter the following information under Basic information :
- Name : Enter a name for the Roving Edge Ultra node.
- Create in compartment : Select the compartment in which the Roving Edge Ultra node you create resides from the list.
- 

Shape : Select ULTRA.USB.1.RX2.12 from the list. Select this shape option if you're requesting a Roving Edge Ultra node.
- 

Enclosure Type : Select Ruggedized case .

All Roving Edge Ultras include a ruggedized case.
- 

Enter a Super user password and Confirm the super user password .

The password is for the super user account on the node.

Password requirements:
- Length: 8 - 12 characters
- Must include at least one: lowercase, numeric, and special character: ! # $ % &amp; ( ) * + - . / : ; @ = &lt; &gt; [ ] ^ _ | ~ \ { {
- 

Enter an Unlock passphrase and Confirm unlock passphrase .

The passphrase is used to decrypt data at rest on the node.

passphrase requirements:
- Length: 8 - 12 characters
- Must include at least one: lowercase, numeric, and special character: ! # $ % &amp; ( ) * + - . / : ; @ = &lt; &gt; [ ] ^ _ | ~ \ { {
- 

Shipping Information : Choose one of the options:
- 

Shipped by Oracle : Complete the following shipping information:
- Point of contact
- Care of
- Recipient phone
- Recipient email
- Country
- Address line 1
- Address line 2 (optional)
- City/Locality
- State/Province/Region
- Zip/Postal code
- Country : Roving Edge Infrastructure device node orders can only be shipped to specific countries depending on where the order is placed. Contact your Oracle account representative for more information.
- Pickup from Oracle
- 

(optional) Expand Certificate options : Select to display and complete the following certificate options:

You have different options for certificate management:
- (Optional) You can use the default self-signed certificates for the device. For this option, leave this section blank. You configure self-signed certificates after you receive the device (see[Certificate Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/../certificate-management.htm#certificate-management)). You can also configure the OCI Certificate service later.

Or:
- (Optional) You can use the OCI Certificate service to manage certificates. For this option, enter the certificate information you got when you created a certificate authority. See[Managing Certificate Authorities](https://docs.oracle.com/iaas/Content/certificates/managing-certificate-authorities.htm). If you don't have the certificate information, you can enter it later using[Editing a Node for Compute, GPU, and Storage Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/../Node2/update_node2.htm#top), but before you provision the device.

Or:
- (Optional) You can use your own certificate service to manage certificates. For this option, enter the certificate information you got when you created a certificate authority. If you don't have the certificate information, you can enter it later using[Editing a Node for Compute, GPU, and Storage Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/../Node2/update_node2.htm#top), but before you provision the device.
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

(optional) Show Tagging options : Select to display the Tagging option. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace.
Note  
  

If you're not sure about whether to apply tags, then skip this option (you can apply tags later) or ask your administrator.

Complete the following:
- 

Tag Namespace
- 

Tag Key
- 

Value

Select +Another Tag to add another tag. Select X to remove the associated tag.

See[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm)for descriptions of these fields.
- 

Select Create Node .

The Roving Edge Ultra node you created is added to the list of nodes.

After creating the node, submit a device node request. See[Submitting a Roving Edge Ultra Node Request](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/request_ultra.htm#top).
- 

Use the[oci rover node create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/node/create.html)command and required parameters to create a Roving Edge Ultra node (model ULTRA.USB.1.RX2.12) in Oracle Cloud Infrastructure:
```

```

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/../compartments.htm#comparments).

The shape value`ULTRA.USB.1.RX2.12`indicates you're creating a Roving Edge Ultra device node.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).

After creating the node, submit a device node request. See[Submitting a Roving Edge Ultra Node Request](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/request_ultra.htm#top).
- 

Run the[CreateRoverNode](https://docs.oracle.com/iaas/api/#/en/rover/latest/RoverNode/CreateRoverNode)
