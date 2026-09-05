# Creating a Secure Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Tasks/creatingsecureblockvolume.htm
- Fetched: 2026-09-05 03:05 CDT

# Creating a Secure Block Volume

Use Security Advisor to create a secure block volume in Block Volume. In this context, a secure block volume is one that's encrypted with a customer-managed key and therefore meets minimum security requirements established by security zones.

In addition to creating the block volume, you create the Vault key that you want to use to encrypt the volume, and then you assign the key to the volume. (You can't use Security Advisor to assign existing encryption keys, but you can use an existing vault to create a new key.)

Using Security Advisor to create a block volume has some limitations. You can't use Security Advisor to create a block volume with a backup policy. For more information, see[Policy-Based Backups](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).

Other security considerations exist outside Security Advisor, such as the use of resources after you create them. We encourage you to learn more about Compute and Block Volume security features and best practices, and then implement them with your newly created resources. For more information, see[Securing Compute](https://docs.oracle.com/iaas/Content/Security/Reference/compute_security.htm),[Securing Block Volume](https://docs.oracle.com/iaas/Content/Security/Reference/blockstorage_security.htm), and[Best Practices for Your Compute Instances](https://docs.oracle.com/iaas/Content/Compute/References/bestpracticescompute.htm).

## Using the Console

Before creating a secure block volume you must have the[required permissions](https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Tasks/../Concepts/get-started.htm#creatingsecureblockvolume_topic-Required_IAM_Policy).

- Open the navigation menu , select Identity &amp; Security , and then select Security Advisor .
- Click Create Secure Block Volume .
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
- On the Create Block Volume page, specify the attributes of the volume:

- Block Volume Name : Enter a display name for the volume. The name doesn't need to be unique, because an Oracle Cloud Identifier (OCID) uniquely identifies the instance. Avoid entering confidential information.
- Create In Compartment : Select the compartment where you want to create the volume.
- Availability Domain : Select the same availability domain as the instance you plan to use this block volume with.
- Volume Size and Performance : Select Default or Custom .

The volume size must be between 50 GB and 32,768 GB (32 TB). You can choose in 1 GB increments within this range. The default is 1024 GB. If you choose a size outside of the service limit, you might be prompted to request an increase. For more information, see[Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm).

The default volume performance setting is Balanced . For more information, see[Block Volume Performance](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm).
- Show Tagging Options : Optionally, apply tags to the volume. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Click Next .
- (Optional) To save this configuration as a stack in Resource Manager, click Save as stack .

For more information, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
-
