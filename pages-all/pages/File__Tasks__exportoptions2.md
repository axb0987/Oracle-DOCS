# Working with NFS Exports and Export Options
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm
- Fetched: 2026-09-05 02:03 CDT

# Working with NFS Exports and Export Options

Learn the basic features of NFS exports and export options, and how to improve security and control client access to File Storage file systems.

## Overview

NFS export options enable you to create more granular access control than is possible using just security list rules to limit VCN access. You can use NFS export options to specify access levels for IP addresses or CIDR blocks connecting to file systems through exports in a mount target. Access can be restricted so that each client's file system is inaccessible and invisible to the other, providing better security controls in multi-tenant environments.

Using NFS export option access controls, you can limit clients' ability to connect to the file system and view or write data. For example, if you want to allow clients to consume but not update resources in your file system, you can set access to Read Only. You can also reduce client root access to your file systems and map specified User IDs (UIDs) and Group IDs (GIDs) to an anonymous UID/GID of your choice. For more information about how NFS export options work with other security layers, see[About File Storage Security](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/securitylayers.htm).
Tip  
  
Watch a[video](https://www.youtube.com/watch?v=WH1aE3QnqXs&t=0s&list=PLvlciYga5j3x-i-cJGudmpGuUupUliIck&index=3)about working with NFS export options in File Storage.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users create, manage, and delete file systems](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#general-file-system-management)allows users to manage NFS export options.

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Exports

Exports control how NFS clients access file systems when they connect to a mount target. File systems are exported (made available) through mount targets. Each mount target maintains an export set which contains one or many exports. A file system may be exported through one or more mount targets. A file system must have at least one export in one mount target in order for instances to mount the file system. The information used by an export includes the file system OCID, mount target OCID, export set OCID,[export path](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filesystempaths.htm), and client[export options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/exportoptions.htm#Export). Typically, an export is created in a mount target when the file system is created. Thereafter, you can create additional exports for a file system in any mount target that resides in the same availability domain as the file system.

You can perform the following export management tasks:
- [Creating an Export](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export.htm)
- [Listing Exports](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-exports.htm)
- [Getting an Export's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-export-details.htm)
- [Editing an Export and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-export.htm)
- [Enabling Secondary Group Lists with LDAP](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/enable-ldap-export.htm)
- [Deleting an Export](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-export.htm)

## NFS Export Options

NFS export options are a set of parameters within the export that specify the level of access granted to NFS clients when they connect to a mount target. An NFS export options entry within an export defines access for a single IP address or CIDR block range. You can have up to 100 options per export.

Each separate client IP address or CIDR block you want to define access for needs a separate export options entry in the export. For example, to set options for NFS client IP addresses 10.0.0.6, 10.0.08, and 10.0.0.10, you need to create three separate entries, one for each IP address.

File Storage service considers the listed order of each export options entry for the export. During an NFS request by a client, File Storage service applies the first set of options that matches the client Source IP address. Only the first set is applied; the rest are ignored.

For example, consider the following two export options entries specifying access for an export:

Entry 1: Source: 10.0.0.0/16, Access: Read Only

Entry 2: Source: 10.0.0.8, Access: Read/Write

In this case, clients who connect to the export from IP address 10.0.0.8 have Read Only access. The request Source IP address is contained in the CIDR block specified in the first entry, and File Storage applies the options in the first match.
Important  
  
File systems can be associated with one or more exports, contained within one or more mount targets. If the client source IP address doesn't match any entry on the list for a single export, then that export isn't visible to the client. However, the file system could be accessed through other exports on the same or other mount targets. To completely deny client access to a file system, be sure that the client source IP address or CIDR block isn't included in any export for any mount target associated with the file system.

The following options can be set to control export access:
- Source : The IP address or CIDR block of a connecting NFS client.
- 

Ports : This setting determines whether the NFS clients specified in Source are required to connect from a privileged source port. Privileged ports are any port including 1-1023. On UNIX-like systems, only the root user can open privileged ports. Setting this value to Privileged disallows requests from unprivileged ports. The default for this setting is different depending on how the export is created.

Creating an export in the Console using the default selections sets Ports to Any unless you select Use Secure Export Options .

Creating an export using the API or CLI without an explicit`ClientOption`array sets the`requirePrivilegedSourcePort`attribute of the client option to`false`. When you create a`ClientOption`array explicitly,`requirePrivilegedSourcePort`defaults to`true`.
Important  
  

When Ports is set to Privileged , you also must follow these additional configuration steps:
- 

When mounting the file system from a UNIX-like system, include the`resvport`option in a mount command when mounting. For example:

```

```

For more information, see[Mounting File Systems From UNIX-Style Instances](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm).
- 

When mounting the file system from a Windows system, be sure the UseReserverdPort s registry key value is set to 1 .

For more information, see[Mounting File Systems From Windows Instances](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingwindowsos.htm).
- Access : This setting specifies the Source NFS client access.
- Read/Write is the default.
- Read Only .
- Anonymous Access : This setting specifies whether to enable anonymous access for Kerberos authentication in cases where the mount target can't find a user in the LDAP server. If Anonymous Access is Not Allowed and the user isn't found in the LDAP directory, or the lookup attempt returns an LDAP error, the operation fails. If Anonymous Access is Allowed and the user isn't found in the LDAP directory, the operation uses the export's Squash UID and Squash GID values. For more information, see[Using Kerberos Authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm).
Note  
  
If the export doesn't use Kerberos authentication, choose Not Allowed .
- Allowed Authentication Options : This setting specifies the authentication methods allowed by the NFS client.
- SYS : NFS v3 UNIX authentication. If you do not specify an allowed authentication value when you create the export option, a default value of SYS is used.
- KRB5 : NFS v3 Kerberos authentication.
- KRB5I : NFS v3 Kerberos authentication and data integrity.
- KRB5P : NFS v3 Kerberos authentication, data integrity, and data privacy (in-transit encryption).

You can select multiple authentication methods. For example, setting Allowed Authentication Options to KRB5 and KRB5I would allow basic Kerberos and Kerberos with data integrity, but disallow the SYS authentication and KRB5P.
Caution  
  
An empty Allowed Authentication Options selection removes all authentication types and can result in a loss of access. Clients requiring SYS authentication lose access if the SYS option isn't present.
Important  
  

The mount commands that you use to mount the file system differ depending on what authentication methods are allowed in the export options. If NFS clients connect through a Kerberos-enabled mount target, the mount command must include the`sec`option. For example:
```

```

```

```

```

```

For NFS clients connecting with AUTH_SYS on the same export, the mount command would include`sec=sys`. For example:

```

```

If the export is using AUTH_SYS alone, the`sec`option is optional.[Mount command samples](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm#samples)provided by the Console are based on the selected export options.

Note  
  
If an NFS client uses an export which has multiple authentication types, and file system is mounted without specifying`sec= <auth_type>`, the client should automatically pick the strongest authentication type supported by the export.
- Squash : This setting determines whether the source clients accessing the file system have their User ID (UID) and Group ID (GID) remapped to Squash UID and Squash GID .
- None : No users are remapped. This is the default value.
- Root : Only the root user UID/GID combination 0/0 is remapped.
- All : All users and groups are remapped.
- Squash UID : This setting is used along with the Squash and Anonymous Access options. When remapping users, you can use this setting to change the default value from 65534 to any other user ID.
- Squash GID : This setting is used along with the Squash and Anonymous Access options. When remapping groups, you can use this setting to change the default value from 65534 to any other group ID.

## Typical Access Control Scenarios

When you create file system and export, the NFS export options for that file system are set to the following defaults, which allow full access for all NFS client source connections. These defaults must be changed if you want to restrict access:
- Source : 0.0.0.0/0 (All)
- Require Privileged Source Port : Any
- Allowed Authentication Options : SYS
- Access : Read/Write
- Squash : None
Note  
  
If the exported mount target has an IPv6 address, and NFS export options aren't specified at creation, an empty array is used as the default, and the export isn't visible to any clients. Oracle

### Control Host Based Access

Provide a managed hosted environment for two clients. The clients share a mount target, but each has their own file system, and cannot access each other's data. For example:
- Client A, who is assigned to CIDR block 10.0.0.0/24, requires Read/Write access to file system A, but not file system B.
- Client B, who is assigned to CIDR block 10.1.1.0/24, requires Read/Write access to file system B, but not file system A.
- Client C, who is assigned to CIDR block 10.2.2.0/24, has no access of any kind to file system A or file system B.
- Both file systems A and B are associated to a single mount target, MT1. Each file system has an export contained in the export set of MT1.

Since Client A and Client B access the mount target from different CIDR blocks, you can set the client options for both file system exports to allow access to only a single CIDR block. Client C is denied access by not including its IP address or CIDR block in the NFS export options for any export of either file system.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm#)
- 

Set the export options for File System A to allow Read/Write access only to Client A, who is assigned to CIDR block 10.0.0.0/24. Client B and Client C are not included in this CIDR block, and cannot access the file system.

File System A export options:
- Source : 10.0.0.0/24
- Ports : Privileged
- Access : Read/Write
- Squash : None

Set the export options for File System B to allow Read/Write access only to Client B, who is assigned to CIDR block 10.1.1.0/24. Client A and Client C are not included in this CIDR block, and cannot access the file system.

File System B export options:
- Source : 10.1.1.0/24
- Ports : Privileged
- Access : Read/Write
- Squash : None
- 

Set the export options for File System A to allow Read_Write access only to Client A, who is assigned to CIDR block 10.0.0.0/24. Client B and Client C are not included in this CIDR block, and cannot access the file system.

```

```

Set the export options for File System B to allow Read_Write access only to Client B, who is assigned to CIDR block 10.1.1.0/24. Client A and Client C are not included in this CIDR block, and cannot access the file system.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Set the export options for File System A to allow READ_WRITE access only to Client A, who is assigned to CIDR block 10.0.0.0/24. Client B and Client C are not included in this CIDR block, and cannot access the file system.

```

```

Set the export options for File System B to allow READ_WRITE access only to Client B, who is assigned to CIDR block 10.1.1.0/24. Client A and Client C are not included in this CIDR block, and cannot access the file system.

```

```

### Limit the Ability to Write Data

Provide data to customers for consumption, but don't allow them to update the data.

For example, you'd like to publish a set of resources in file system A for an application to consume, but not change. The application connects from IP address 10.0.0.8.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm#)
- 

Set the source IP address 10.0.0.8 to Read Only in the export for File System A. File System A export options:
- Source : 10.0.0.8
- Ports : Privileged
- Access : Read Only
- Squash : None
- 

Set the source IP address 10.0.0.8 to READ_ONLY in the export for File System A:

```

```

- 

Set the source IP address 10.0.0.8 to READ_ONLY in the export for File System A:

```

```

### Improve File System Security

To increase security, you'd like to limit the root user's privileges when connecting to File System A. Use Identity Squash to remap root users to UID/GID 65534. In Unix-like systems, this UID/GID combination is reserved for ' nobody ', a user with no system privileges.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm#)
- 

File System A export options:
- Source : 0.0.0.0
- Ports : Privileged
- Access : Read/Write
- Squash : Root
- UID : 65534
- GID : 65534
- 

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

```

```

Tip  
  

If you don't want a file system to be visible to any clients, you can set all of the properties in the`exportOptions`array to empty values. For example,
```

```

### Use Kerberos for Authentication

To increase security, you'd like to require Kerberos authentication with data integrity and data privacy (in-transit encryption) when connecting to File System A from CIDR block 10.0.0.0/24. Use[Anonymous Access](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/kerberos.htm#overview__ldap-anon)to squash users who aren't found with the LDAP lookup to proceed with the specified UID and GID and no secondary groups.

[Enable Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/kerberos-oci-setup.htm)for File System A then set the export options.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions2.htm#)
- 

File System A export options:
- Source : 10.0.0.0/24
- Ports : Any
- Access : Read/Write
- Squash : None
- Anonymous Access : True
- Allowed Authentication Options : KRB5P
- Squash UID : 65534
- Squash GID : 65534
Note  
  
The export must also have Use LDAP for Group List enabled.
- 

```

```

Note  
  
The export must also have`--is-idmap-groups-for-sys-auth`set to`true`.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

```

```

Note  
  
The export must also have`isIdmapGroupsForSysAuth`set to`true`
