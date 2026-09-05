# Creating an Export
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export-mt.htm
- Fetched: 2026-09-05 02:02 CDT

# Creating an Export

Create an export for an existing File Storage file system and mount target.

Typically, an export is created in a mount target when[a file system is created](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/creatingfilesystems.htm). Thereafter, you can create additional exports for a file system in any mount target that resides in the same availability domain as the file system.

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

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export-mt.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export-mt.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export-mt.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select File Systems .
- Select a compartment that you have permission to work in.
- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Exports .
- Select Create export .
- To accept the default settings, select Create . To customize the export, continue with the following steps.
- In the Export information section, specify details for the export associated with the file system:
- 

Export path : The File Storage creates a default export path using the file system name. Optionally, replace the default export path with a new path, starting with a slash (/). For example,`/fss`. This value specifies the mount path to the file system (relative to the mount target IP address or hostname). Avoid entering confidential information. For more information, see[Paths in File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filesystempaths.htm).
- 

Use secure export options : Turn on this option to require NFS clients to use a privileged port (1–1023) as the source port. This option enhances security because only clients with root privileges can use a privileged source port. After the export is created, you can edit the export options to adjust security. For more information, see[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm).
Caution  
  
If you leave the Use secure export options option turned off, unprivileged users can read and change any file or directory on the target file system.
- 

Use LDAP for group list : Turn on this option to use a configured LDAP server to map the user to UNIX groups instead of the groups listed in the NFS request's RPC header when using AUTH_SYS authentication. For more information, see[Using LDAP for Authorization](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm). This option doesn't affect[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm), because mapping is always enabled with Kerberos.
- In the Resource locks section, select the type of resource lock to apply:
- No lock : No restrictions.
- Delete : Prevents deleting the resource.
- Full : Prevents all modifications except reading the resource.
- In the Mount target information section, specify information for the mount target associated with the file system:
- Select an existing mount target : Select this option to associate the file system with a mount target that you already created.

If there aren't any mount targets in the current combination of availability domain and compartment, this option is disabled. You can select a different compartment or create a new mount target.
- Create new mount target : Select this option to create a new mount target associated with this file system.
Important  
  
The mount target is always in the same availability domain as the file system. While you can access mount targets from any Availability domain in a region, for best performance, ensure the mount target and file system are in the same availability domain as the Compute instances that access them. For more information, see[Regions and Availability Domains](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filestorageoverview.htm#Regions).
- If you're creating a new mount target, provide the following information:
- Compartment : Select the compartment you want to create the mount target in.
- 

New mount target name : Optionally, enter a friendly name for the mount target. It doesn't have to be unique; an Oracle Cloud Identifier (OCID) uniquely identifies the mount target. Avoid entering confidential information.
Note  
  
The mount target name is different from the DNS hostname, which is specified under IP details.
- Virtual cloud network compartment : Select the compartment that contains the virtual cloud network (VCN) where you want to create the mount target.
- Virtual cloud network : Select the VCN where you want to create the new mount target.
- Subnet compartment : Select the compartment containing the subnet within the VCN to attach the mount target to.
- Subnet : Select a subnet to attach the mount target to. Subnets can be either AD-specific or regional (regional subnets have " regional " after the name). Subnets can support IPv4 or IPv6. For more information, see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm). For more information, see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).
Caution  
  
Each mount target requires three internal IP addresses in the subnet to function. Don't use /30 or smaller subnets for mount target creation because there are not enough available IP addresses. Two of the IP addresses are used during mount target creation and the third IP address must remain available for high availability failover.
- Use network security groups to control traffic : Turn on this option to add this mount target to an existing network security group (NSG). Select a Network security groups compartment and then a Network security group under that compartment.
Note  
  
The rules for the NSG you select must allow traffic to the mount target's VNIC using specific protocols and ports. For more information, see[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm).
- IP details :
- IP address : You can specify an unused IP address in the subnet you selected for the mount target. If the subnet uses dual-stack IPv4/IPv6 addressing, or single-stack IPv6 addressing, you can specify an IPv6 address. For more information, see[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/managingmounttargets.htm#limitations)for Mount Targets and[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).
- 

Hostname : Optionally, specify a hostname to assign to the mount target.
Note  
  
The File Storage constructs a fully qualified domain name (FQDN) by combining the hostname with the FQDN of the subnet the mount target is find in.

For example,`myhostname.subnet123 . dnslabel.oraclevcn.com`.

After it's created, you can change the hostname in the mount target's details page. For more information, see[Managing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm).
Important  
  
If you enable[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm)for a mount target in a VCN that uses the default Internet and VCN Resolver for DNS, you must specify a hostname.
- Tags : (Optional) Expand the Tags section and select Add tag .

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create to create the export. You can also select Cancel to exit without creating, or (optional) select Save as stack to save the configuration as a Resource Manager stack. For more information, see[Managing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm).

Next, mount the file system from an instance so that you can read and write directories and files in the file system. For instructions on obtaining mount commands for the OS and mounting the file system, see[Mounting File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm).
- 

Use the[`fs export create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export/create.html)command and required parameters to create an export for a specified file system within a specified export set:

```

```

Include the`--export-options`parameter with required values to set export options when you create the export. If you don't want a file system to be visible to any clients through this export, you can set`source`to an empty value. For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateExport](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Export/CreateExport)operation to create an export.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
