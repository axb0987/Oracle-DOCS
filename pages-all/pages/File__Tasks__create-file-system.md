# Creating a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-file-system.htm
- Fetched: 2026-09-05 02:02 CDT

# Creating a File System

Create a new file system.

When creating a file system using the Console, you can create the mount target and export necessary to access the file system. If you don't create a mount target while creating a file system, you can[create a mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm)and[export](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export.htm)later.
Note  
  
File systems are encrypted by default. You can't turn off encryption.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-file-system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-file-system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-file-system.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select File Systems .
- Select Create file system .
- Select the type of file system that you want to create:
- File system for NFS : Create a file system, an associated mount target, and an export that lets you mount and access the file system as soon as it's created.
- File system for replication : Create an unexported file system. Unexported file systems are used as target file systems for replications. For more information, see[File System Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm).
- File System information section, you can accept the system defaults or change them as needed.
- Name : File Storage service creates a default name using`FileSystem-YYMMDD-HHMM`. Optionally, change the default name for the file system. It doesn't have to be unique; an Oracle Cloud Identifier (OCID) uniquely identifies the file system. Avoid entering confidential information.
- Compartment : Specify the compartment where you want to create the file system.
- Availability Domain : The first availability domain is used as default.
- 
Encryption : File systems use Oracle-managed keys by default, which leaves all encryption-related matters to Oracle. Optionally, you can encrypt the data in this file system using your own Vault encryption key.
Note  
  
Only symmetric Advanced Encryption Standard (AES) keys are supported for file system encryption. To use[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)for your encryption needs, select Encrypt using customer-managed keys and see the[required IAM policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/creatingfilesystems.htm#Required_IAM_Service_Policy). Select the vault compartment and vault that contains the master encryption key that you want to use, and then select the master encryption key compartment and master encryption key.
Caution  
  
Be sure to back up your vaults and keys. Deleting a vault and key otherwise means losing the ability to decrypt any resource or data that the key was used to encrypt. For more information, see[Backing Up and Restoring Vaults and Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys.htm).
- To attach a snapshot policy to the file system, turn on Attach Snapshot Policy , select a compartment, then select the snapshot policy. For more information, see[Policy-Based Snapshots and Scheduling](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm).
- 

(Optional) To add tags to the file system, select Add tag . If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- In the Export information , you can accept the system defaults, or change them.

Mount targets use exports to manage access to file systems. The path name uniquely identifies the file system within the mount target, and is used by an instance to mount the file system.
- 

Export path : The File Storage service creates a default export path using the file system name. Optionally, replace the default export path name with a new path name, preceded by a forward slash (/). For example,`/fss`. This value specifies the mount path to the file system (relative to the mount target IP address or hostname). Avoid entering confidential information.

Important  
  

The export path must start with a slash (/) followed by a sequence of zero or more slash-separated elements. If there are many file systems associated with a single mount target, the export path sequence for the first file system can't contain the complete path element sequence of the second file system export path sequence. Export paths can't end in a slash. No export path element can be a period (.) or two periods in sequence (..). No export path can exceed 1024 bytes. Lastly, no export path element can exceed 255 bytes.

Valid examples:
- `/example`and`/path`
- `/example`and`/example2`

Invalid examples:
- `/example`and`/example/path`
- `/`and`/example`
- `/example/`
- `/example/path/../example1`
Caution  
  
If one file system associated with a mount target has '/' specified as an export path, you can't associate another file system with that mount target.
Note  
  
Export paths can't be edited after the export is created. To use a different export path, you must create a new export with the appropriate path. Optionally, you can then delete the export with the old path.

For more information, see[Paths in File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filesystempaths.htm).
- 

Use secure export options : Select to set the export options to require NFS clients to use a privileged port (1-1023) as its source port. This option enhances security because only a client with root privileges can use a privileged source port. After the export is created, you can edit the export options to adjust security. For more information, see[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm).
Caution  
  
Leaving the Use secure Export options setting disabled allows unprivileged users to read and modify any file or directory on the target file system.
- 

Use LDAP for group list : Select to use a configured LDAP server to map the user to UNIX groups instead of the groups listed within the NFS request's RPC header. For more information, see[Using LDAP for Authorization](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm).
- In the Mount Target information section, associate the file system with a mount target to be mounted by an instance.

You can accept the system defaults, or change them.

If you have existing mount targets in the availability domain, the File Storage service automatically chooses the most recently created mount target in the list.

Create new mount target : If you don't have a mount target in the selected availability domain, the File Storage service creates one using the following defaults.

- New mount target name : File Storage service creates a default mount target name using`Mount-YYYYMMDD-HHMM`.
- Compartment : The compartment you're currently working in.
- Virtual Cloud Network : The first VCN listed in the availability domain is used as default.
- Subnet : The most recently created subnet listed in the availability domain is used as default. Subnets can be either AD-specific or regional (regional ones have " regional" after the name).Subnets can support IPv4 or IPv6. For more information, see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)

Tip  
  
We recommend using a subnet dedicated to mount targets so that instances or other resources don't use the IP addresses that mount targets need. For more information, see[Choosing the Subnet for a Mount Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm#subnet-selection).

Select an existing Mount Target : Use this option to select a different, existing mount target.
Tip  
  

If there aren't any mount targets in the current combination of availability domain and compartment, this option is disabled. You can:
- Select a different compartment.
- Select a different availability domain in the File System information section.
- Create a new mount target.

Create new Mount Target

Select this option to create a new mount target associated with this file system. By default, the mount target is created in the current compartment and you can use network resources in that compartment. Select the click here link in the dialog box to enable compartment selection for the mount target, its VCN, or subnet resources.
Important  
  
The mount target is always in the same availability domain as the file system. While it's possible to access mount targets from any AD in a region, for best performance, the mount target and file system should be in the same availability domain as the Compute instances that access them. For more information, see[Regions and Availability Domains](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filestorageoverview.htm#Regions).
- Create in Compartment : Specify the compartment you want to create the mount target in.
- 

New Mount Target name : Optionally, replace the default with a friendly name for the mount target. It doesn't have to be unique; an Oracle Cloud Identifier (OCID) uniquely identifies the mount target. Avoid entering confidential information.
Note  
  
The mount target name is different than the DNS hostname, which is specified in the advanced options.
- Virtual Cloud Network Compartment : The compartment containing the cloud network (VCN) in which to create the mount target.
- Virtual Cloud Network : Select the cloud network (VCN) where you want to create the new mount target.
- Subnet Compartment : Specify the compartment containing a subnet within the VCN to attach the mount target to.
- 

Subnet : Select a subnet to attach the mount target to. Subnets can be either AD-specific or regional (regional ones have " regional" after the name). Subnets can support IPv4 or IPv6. For more information, see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).
Caution  
  
Each mount target requires three IP addresses. Don't use /30 or smaller subnets for mount target creation because they don't have enough available IP addresses. As an example, a /28 subnet with 13 available IP addresses could support four mount targets. For more information, see[Mount Target Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#limitations).

Tip  
  
We recommend using a subnet dedicated to mount targets so that instances or other resources don't use the IP addresses that mount targets need. For more information, see[Choosing the Subnet for a Mount Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm#subnet-selection).
- 

Use Network Security Groups to control traffic : Turn on this option to add this mount target to an existing NSG. Select an NSG from the list.
Important  
  
Rules for the NSG you select must be configured to allow traffic to the mount target's VNIC using specific protocols and ports. For more information, see[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm).
- 

(Optional) You can configure the mount target's advanced options, including IP details and tagging.

IP Details :
- IP address : You can specify an unused IP address in the subnet you selected for the mount target. If the subnet uses dual-stack IPv4/IPv6 addressing, or single-stack IPv6 addressing, you can specify an IPv6 address. For more information, see[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/managingmounttargets.htm#limitations)for Mount Targets and[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).
- 

Hostname : You can specify a hostname you want to assign to the mount target.
Note  
  

The File Storage service constructs a fully qualified domain name (FQDN) by combining the hostname with the FQDN of the subnet the mount target is located in.

For example,`myhostname.subnet123 . dnslabel.oraclevcn.com`.

After it's created, the hostname can be changed in the mount target's details page. For more information, see[Managing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm).
Important  
  
If enabling[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm)for a mount target in a VCN that uses the default Internet and VCN Resolver for DNS, you must specify a hostname.
- (Optional) To add tags to the mount target, select Tagging .

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- In the Resource locks section, select a lock level for the file system:
- No Lock : No restrictions.
- Delete : Prevents the file system from being deleted.
- Full : Prevents all modifications except reading the file system
- To create the file system, select Create .
- (Optional) To save the configuration as a Resource Manager stack, select Save as stack . For more information, see[Managing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm).
- 

Use the[`fs file-system create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/create.html)command and required parameters to create a file system:

```

```

File systems use Oracle-managed keys by default, which leaves all encryption-related matters to Oracle. Optionally, you can encrypt the data in this file system using your own Vault encryption key. For more information, see[Encryption](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/securitylayers.htm#Encryption)and[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm). Include the`--kms-key-id`parameter to create a file system that uses your own encryption key:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/CreateFileSystem)operation to create a file system.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
