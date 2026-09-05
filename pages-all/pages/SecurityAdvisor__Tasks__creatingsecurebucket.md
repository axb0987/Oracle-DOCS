# Creating a Secure Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Tasks/creatingsecurebucket.htm
- Fetched: 2026-09-05 03:05 CDT

# Creating a Secure Bucket

Use Security Advisor to create a secure bucket in Object Storage. In this context, a secure bucket is one that's encrypted with a customer-managed key and therefore meets minimum security requirements established by security zones.

In addition to creating the bucket, you create the Vault key to use to encrypt the bucket, and then you assign the key to the bucket. (You can't use Security Advisor to assign existing encryption keys, but you can use an existing vault to create a new key.)

Other security considerations exist outside Security Advisor, such as the use of resources after you create them. We encourage you to learn more about Object Storage security features and best practices, and then implement them with the newly created resource. For more information, see[Securing Object Storage](https://docs.oracle.com/iaas/Content/Security/Reference/objectstorage_security.htm)and[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/encryption.htm#Using_Your_Own_Keys_for_ServerSide_Encryption).

## Using the Console

Before creating a secure bucket, you must have the[required permissions](https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Tasks/../Concepts/get-started.htm#creatingsecurebucket_topic-Required_IAM_Policy).

- Open the navigation menu , select Identity &amp; Security , and then select Security Advisor .
- Click Create Secure Bucket .
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
- On the Create Bucket page, specify the attributes of the bucket.

- Bucket Name: Enter a display name for the bucket. The system generates a default name that reflects the current year, month, day, and time, for example`bucket-20230101-1359`. Optionally, change the default name. Avoid entering confidential information.
- Create in compartment: Select the compartment where you want the bucket to reside. This doesn't need to be the same compartment as the vault and key.
- 

Storage Tier: Select the tier in which you want to store the data.
- Standard is the primary, default Object Storage tier for storing frequently accessed data that requires fast and immediate access.
- Archive is a special tier for storing infrequently accessed data that requires long retention periods. Access to data in the archive tier isn't immediate. Archived data must be restored before the data is accessible. For more information, see[Overview of Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm).
- Object Events: Select Emit Object Events to enable the bucket to emit events for object state changes. For more information, see[Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).
- Object Versioning: Select Enable Object Versioning if you want Object Storage to create an object version each time the content changes or the object is deleted. For more information, see[Object Storage Versioning](https://docs.oracle.com/iaas/Content/Object/Tasks/usingversioning.htm).
- Show Tagging Options: Optionally, apply tags to the bucket. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Click Next .
- (Optional) To save this configuration as a stack in Resource Manager, click Save as stack .

For more information, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
-
