# Creating a Secure Virtual Machine Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Tasks/creatingsecurevirtualmachine.htm
- Fetched: 2026-09-05 03:05 CDT

# Creating a Secure Virtual Machine Instance

Use Security Advisor to create a secure virtual machine (VM) instance in Compute. In this context, a secure instance is one with a boot volume that's encrypted with a customer-managed key and therefore meets minimum security requirements established by security zones.

In addition to creating the instance and associated boot volume, you create the Vault key that you want to use to encrypt the volume, and then you assign the key to the volume. (You can't use Security Advisor to assign existing encryption keys, but you can use an existing vault to create a new key.)

Using Security Advisor to create a VM instance has the following limitations.
- You can't configure private or public IP addresses for an instance.
- You can't change the image build. It always uses the latest version.
- You can't create the instance on a dedicated VM host, which lets you run the instance in isolation so that it's not running on shared infrastructure.
- You can't specify the volume performance settings for the boot volume.
- You can't use Security Advisor to generate SSH keys for you to remotely connect to the instance by using Secure Shell (SSH). You must generate SSH keys and have the public key available when you create the instance.

Other security considerations exist outside Security Advisor, such as the use of resources after you create them. We encourage you to learn more about Compute and Block Volume security features and best practices, and then implement them with the newly created resources. For more information, see[Securing Compute](https://docs.oracle.com/iaas/Content/Security/Reference/compute_security.htm),[Securing Block Volume](https://docs.oracle.com/iaas/Content/Security/Reference/blockstorage_security.htm), and[Best Practices for Your Compute Instances](https://docs.oracle.com/iaas/Content/Compute/References/bestpracticescompute.htm).

## Using the Console

Before creating a secure instance you must have the[required permissions](https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Tasks/../Concepts/get-started.htm#creatingsecurevirtualmachine_topic-Required_IAM_Policy)and a[virtual cloud network (VCN)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)must exist.

- Open the navigation menu , select Identity &amp; Security , and then select Security Advisor .
- Click Create Secure Instance .
- Review the prerequisites for getting started, and then click Next .
- On the Select Vault page, select one of the following options.
- To create a master encryption key in an existing vault, select Choose Existing Vault .
- To create a master encryption key in a new vault, select Create New Vault .
- Depending on your choice in the previous step, perform one of the following actions.
- If you chose to use an existing vault, select the compartment where the vault resides, and then select the vault.
- If you chose to create a vault, select the compartment where you want to create the vault, and then enter a display name to identify the vault. Avoid entering confidential information. Optionally, make the vault a virtual private vault by selecting the Make it a virtual private vault check box. For more information about vault types, see[Key and Secret Management Concepts](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
- Click Next .
- On the Create Key page, enter a name to identify the key.

Avoid entering confidential information.

The value for Key Shape: Length is fixed at 256 bits to maximize security based on key length.

The value for Key Shape: Algorithm is set to Advanced Encryption Standard (AES).
- (Optional) If you're using an existing vault and you want to import key material to create a key, select the Import external key check box.

Importing key material requires you to first generate the key material and wrap it using a vault's public wrapping key. This option isn't available when creating a new vault. For more information about importing keys, see[Importing Keys and Key Versions](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/importingkeys.htm).
- To apply tags to the key, click Show Tagging Options .
- Click Next .
- On the Create Compute Instance page, specify the attributes of the instance.

- Name: Enter a display name for the instance. The system generates a default name that reflects the current year, month, day, and time, using the format`instance- YYYYMMDD - HHMM`. Optionally, change the default name. The name doesn't need to be unique, because an Oracle Cloud Identifier (OCID) uniquely identifies the instance. Avoid entering confidential information.
- Create In Compartment: Select the compartment where you want to create the instance. This doesn't need to be the same compartment as the vault and key.
- Image or Operating System: By default, an Oracle Linux 7.x image is used to boot the instance. You can't use Security Advisor to create a VM instance with a different image.
- Availability Domain: Select the availability domain where you want to create the instance.
- Shape: The default shape for the selected image and availability domain combination. You can't use Security Advisor to create a virtual machine instance with a different shape. For more information about shapes, see[Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm).
- In the Configure Networking section, configure the network details for the instance.

- Select a virtual cloud network: Select the network in which to create the instance. You can select only an existing VCN. You can't use Security Advisor to create a new VCN. To use a VCN in a different compartment, click Change Compartment , and then select a different compartment.
- Select a subnet: A subnet within the VCN to attach the instance to. Subnets are either public or private. Private means that the instances in that subnet can't have public IP addresses. For a more secure instance, we recommend that you choose a private subnet. For more information, see[Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Private). Subnets are either specific to an availability domain or regional (regional ones have "regional" after the name). We recommend using[regional subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs_topic-Overview_of_VCNs_and_Subnets.htm#Overview__regional_subnet).

By default, when you create an instance in a public subnet, you can optionally assign the instance a public IP address. A public IP address makes the instance accessible from the internet. You can't use Security Advisor to create a VM instance with a public IP address.
- In the Boot Volume section, configure the size and encryption options for the instance's boot volume.

- To specify a custom size for the boot volume, select the Specify a Custom Boot Volume check box. Then, enter a custom size from 50 GB to 32,768 GB (32 TB). The specified size must be larger than the default boot volume size for the selected image. For more information, see[Custom Boot Volume Sizes](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm#Custom).
- To encrypt data while the data is in transit between the instance and the attached boot volume, select the Use in-transit encryption check box. The Vault service encryption key that you use to encrypt the boot volume data at rest is also used for in-transit encryption. For more information, see[Block Volume Encryption](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption). Security zones require data to be encrypted in-transit, so you must select this check box to comply with security zone requirements.
- In the Add SSH Keys section, choose one the following options:

- Choose SSH key files: Upload the public key part of the key pair. Either browse to the key file that you want to upload, or drag the file into the box. To provide many keys, press and hold down the Command key (on Mac) or the Ctrl key (on Windows) while selecting files.
- Paste SSH keys: Paste the public key part of the key pair in the box.
- No SSH keys: If you don't provide SSH keys, you can't connect to the instance using SSH.
Important  
  
To use a key pair that is generated by OCI, access the instance from a system with OpenSSH installed. OpenSSH is included by default on all current versions of Linux, MacOS, Windows, and Windows Server. For more information, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).
- (Optional) To apply tags to the instance, click Show Tagging Options .

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Click Next .
- (Optional) To save this configuration as a stack in Resource Manager, click Save as stack .

For more information, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
-
