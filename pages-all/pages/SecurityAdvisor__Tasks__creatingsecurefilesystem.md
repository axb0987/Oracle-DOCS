# Creating a Secure File System
- Source: https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Tasks/creatingsecurefilesystem.htm
- Fetched: 2026-09-05 03:05 CDT

# Creating a Secure File System

Use Security Advisor to create a secure file system in File Storage. In this context, a secure file system is one that's encrypted with a customer-managed key and therefore meets minimum security requirements established by security zones.

In addition to creating the file system, you create the Vault key to use to encrypt the file system, and then you assign the key to the file system. (You can't use Security Advisor to assign existing encryption keys, but you can use an existing vault to create a new key.)

Using Security Advisor to create a file system has some limitations. You can't use Security Advisor to create a file system with a new mount target. You must reuse an existing mount target.

Other security considerations exist outside Security Advisor, such as the use of resources after you create them. We encourage you to learn more about File Storage security features and best practices, and then implement them with the newly created resources. For more information, see[Securing File Storage](https://docs.oracle.com/iaas/Content/Security/Reference/filestorage_security.htm)and[About Security](https://docs.oracle.com/iaas/Content/File/Concepts/securitylayers.htm).

## Using the Console

Before creating a secure file system, you must have the[required permissions](https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Tasks/../Concepts/get-started.htm#creatingsecurefilesystem_topic-Required_IAM_Policy)and a[mount target](https://docs.oracle.com/iaas/Content/File/Tasks/managingmounttargets.htm)must exist.

- Open the navigation menu , select Identity &amp; Security , and then select Security Advisor .
- Click Create Secure File System .
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
- On the Create File System page, specify the attributes of the file system.

- 

Compartment: Select the compartment where you want the file system to reside. You must choose a compartment that contains the existing mount target you want to use.
- 

Name: Enter a display name for the file system. File Storage generates a default name that reflects the current year, month, day, and time, using the format`FileSystem- YYMMDD - HHMM - SS`. Optionally, change the default name. The name doesn't have to be unique because an Oracle Cloud Identifier (OCID) uniquely identifies the file system. Avoid entering confidential information.
- 

Availability Domain: Select the availability domain within the current region where you want to place the file system.
- 

Export Path: The File Storage service creates a default export path using the file system name. Optionally, replace the default export path name with a new path name, preceded by a slash (/). For example,`/fss`. This value specifies the mount path to the file system (relative to the mount target IP address or hostname).

The export path must start with a slash (/) followed by a sequence of zero or more slash-separated elements. If there are many file systems associated with a single mount target, the export path sequence for the first file system can't contain the complete path element sequence of the second file system export path sequence. Export paths can't end in a slash. No export path element can be a period (.) or two periods in sequence (..). No export path can exceed 1024 bytes. Lastly, no export path element can exceed 255 bytes.

Valid examples:
- `/example`and`/path`
- `/example`and`/example2`

Invalid examples:
- `/example`and`/example/path`
- `/`and`/example`
- `/example/`
- `/example/path/../example1`

Export paths can't be edited after the export is created. To use a different export path, you must create a new export with the appropriate path. Optionally, you can then delete the export with the old path.
Caution  
  
If one file system associated with a mount target has '/' specified as an export path, you can't associate another file system with that mount target.

For more information, see[Paths in File Systems](https://docs.oracle.com/iaas/Content/File/Concepts/filesystempaths.htm).
- 

Use Secure Export Options: Select to set the export options to require NFS clients to use a privileged port (1-1023) as its source port. This option enhances security because only a client with root privileges can use a privileged source port. After the export is created, you can edit the export options to adjust security. For more information, see[Working with NFS Export Options](https://docs.oracle.com/iaas/Content/File/Tasks/exportoptions2.htm).
Caution  
  
Leaving the Use Secure Export Options setting unselected lets unprivileged users read and change any file or directory on the target file system.
- 

Select Mount target: File systems must be associated with a mount target to be mounted by an instance. If you don't have a mount target in the selected availability domain in the compartment, you must choose a different availability domain or create the file system in a compartment and availability domain where you do have a mount target.
- 

Show Tagging Options : Optionally, apply tags to the file system. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Click Next .
- (Optional) To save this configuration as a stack in Resource Manager, click Save as stack .

For more information, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
-
