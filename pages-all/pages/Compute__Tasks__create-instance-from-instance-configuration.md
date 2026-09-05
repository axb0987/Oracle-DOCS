# Creating an Instance from an Instance Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-instance-from-instance-configuration.htm
- Fetched: 2026-09-05 01:50 CDT

# Creating an Instance from an Instance Configuration

You can create an instance by using an instance configuration as a template.

Many of the settings that are defined in the instance configuration can't be changed when you create an instance from the instance configuration. For example, the availability domain, compartment, image, shape, and subnet can't be changed.

## Before You Begin

Before you create an instance from an instance configuration, you need an[instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm)to use as a template for the instance. In addition, there are specific requirements for Linux and Windows.

### Linux Instance Requirements

To connect to your Linux instance, consider the following.
- If the instance configuration doesn't include a public key, and you want to use your own Secure Shell (SSH) key to connect to the instance using SSH, you need the public key from the SSH key pair that you plan to use. The key must be in OpenSSH format. For more information, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm).
- If the instance configuration does include an SSH key, that SSH key must be used to connect to all instances created from the instance configuration.

### Windows Instance Requirements

For Windows, you need a VCN security rule that enables Remote Desktop Protocol (RDP) access so that you can connect to your instance. To do so, you need a stateful ingress rule for TCP traffic on destination port 3389 from source 0.0.0.0/0 and any source port. For more information, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). You can implement this security rule in a network security group that you add this Windows instance to. Or, you can implement this security rule in a security list that is used by the instance's subnet.

[To enable RDP access:](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-instance-from-instance-configuration.htm#)

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- 

Under List Scope , select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
- Select the VCN you want to create the security rule in.
- 

Do one of the following:
- 

Add the rule to a network security group that the instance belongs to:
- Under Resources , select Network Security Groups .
- Select the network security group to add the rule to.
- Select Add Rules .
- 

Enter the following values for the rule:
- Stateless: Leave the checkbox cleared.
- Direction: Ingress
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: RDP (TCP/3389)
- Source Port Range: All
- Destination Port Range: 3389
- Description: An optional description of the rule.
- Select Add .
- 

To add the rule to a security list that is used by the instance's subnet:
- Under Resources , select Security Lists .
- Select the security list that you're interested in.
- Select Add Ingress Rules .
- 

Enter the following values for the rule:
- Stateless: Leave the checkbox cleared.
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: RDP (TCP/3389)
- Source Port Range: All
- Destination Port Range: 3389
- Description: An optional description of the rule.
- Select Add Ingress Rules .

## Steps to Create an Instance from an Instance Configuration

Follow these steps to create an instance from an instance configuration using the Console, CLI, or API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-instance-from-instance-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-instance-from-instance-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-instance-from-instance-configuration.htm#)
- 

- On the Instance Configurations list page, select the instance configuration that you want to use as a template to create the instance. If you need help finding the list page, see[Listing Instance Configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/list-instance-configurations.htm).
- Select Launch instance .
- Enter a name for the instance. You can add or change the name later. The name doesn't need to be unique, because an Oracle Cloud Identifier (OCID) uniquely identifies the instance. Avoid entering confidential information.
- For Placement , Image and shape , and Networking , you can change some advanced options, including the[capacity type](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/computeoverview.htm#capacity_types),[fault domain](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/bestpracticescompute.htm#Fault),[shielding options](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/shielded-instances.htm), and[launch options](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#instance-network-launch-types). For more information about the settings in these sections, see[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm).
- 

Linux instances: If the instance configuration doesn't include an SSH public key for the instance, you can provide one now. If the instance configuration does include an SSH public key for the instance, that SSH key must be used to connect to all instances created from the instance configuration.
In the Add SSH keys section, generate an SSH key pair or upload your own public key. Select one of the following options:
- 

Generate a key pair for me: Oracle Cloud Infrastructure generates an RSA key pair for the instance. Select Save Private Key , and then save the private key on your computer. Optionally, select Save Public Key and then save the public key.

Caution  
  
Anyone who has access to the private key can connect to the instance. Store the private key in a secure location.
Important  
  
To use a key pair that is generated by OCI, access the instance from a system with OpenSSH installed. OpenSSH is included by default on all current versions of Linux, MacOS, Windows, and Windows Server. For more information, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).
- Upload public key files (.pub): Upload the public key portion of your key pair. Either browse to the key file that you want to upload, or drag and drop the file into the box. To provide multiple keys, press and hold down the Command key (on Mac) or the Ctrl key (on Windows) while selecting files.
- Paste public keys: Paste the public key portion of your key pair in the box.
- No SSH keys: Select this option only if you do not want to connect to the instance using SSH. You can't provide a public key or save the key pair that is generated by Oracle Cloud Infrastructure after the instance is created.
- Specify the Boot volume details for the instance. For more information about the settings in this section, see[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm).
- To configure live migration, select Show advanced options , and on the Availability configuration tab, make your selections. For more information about the settings in this section, see[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm).
- 

Select Create .

Tip  
  
To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-work-requests)that occur during instance creation, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).

#### What's Next

Here are some things you can do with the new instance.
- After the instance is provisioned, details about it appear in the instance list. To view more details, including IP addresses and the initial password (for Windows instances), select the instance name.
- When the instance is fully provisioned and running, you can connect to the instance. You[connect to a Linux instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm)by using a Secure Shell (SSH) connection, and you[connect to a Windows instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm)by using a Remote Desktop connection.
- You can attach a[block volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm)to the instance, provided the volume is in the same availability domain.
- You can[let additional users connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/addingusers.htm).
- 

Use the[instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)command and required parameters to create an instance from an instance configuration:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use these API operations to create instances:
- [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance)
- [LaunchInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstanceConfiguration): Create an instance from an instance configuration
- [GetInstanceDefaultCredentials](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceCredentials/GetInstanceDefaultCredentials)
