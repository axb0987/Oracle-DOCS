# About File Storage Security
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Concepts/securitylayers.htm
- Fetched: 2026-09-05 02:02 CDT

# About File Storage Security

The File Storage service uses five different layers of access control. Each layer has its own authorization entities and methods which are separate from the other layers.
Tip  
  
Watch a[video](https://www.youtube.com/watch?v=Gc9jb8hKRwc&t=0s&list=PLvlciYga5j3x-i-cJGudmpGuUupUliIck&index=2)about security in File Storage and review[the File Storage security guide](https://docs.oracle.com/iaas/Content/Security/Reference/filestorage_security.htm).

The Oracle Cloud Infrastructure (OCI) policy layer[uses policies](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)to control what users can do within Oracle Cloud Infrastructure, such as creating instances, a VCN and its security rules, mount targets, and file systems.

The Network security layer controls which instance IP addresses or CIDR blocks can connect to a host file system. It uses VCN[security list rules](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/securitylistsfilestorage.htm)to allow or deny traffic to the mount target, and therefore access to any associated file system.

The NFS export option layer is a method of applying access control per-file system export based on source IP address that bridges the Network Security layer and the NFS v.3 UNIX Security layer.

The NFS v.3 UNIX security and NFS v.3 Kerberos security layers control what users can do on the instance, such as reading and writing files and directories.

This security layer... Uses these... To control actions like...
[Oracle Cloud Infrastructure Identity and Access Management](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/securitylayers.htm#About_Security__Identity)Users and policies Creating instances and VCNs. Creating, listing, and associating file systems and mount targets.
[Network security](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/securitylayers.htm#About_Security__Network)IP addresses, CIDR blocks, security lists Connecting the client instance to the mount target.
[NFS v.3 Unix security](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/securitylayers.htm#About_Security__NFS)UNIX users, file mode bits Reading and writing files and directories.
[NFS v.3 Kerberos security](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/securitylayers.htm#About_Security__kerberos)Kerberos principals mapped to UNIX users, file mode bits Reading and writing files and directories.
[NFS export options](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/securitylayers.htm#About_Security__Exports)File system exports, IP addresses, UNIX users Privileged source port connection, reading and writing files, and limiting root user access on a per-export basis.

## Oracle Cloud Infrastructure Identity and Access Management

You can create users and groups in Oracle Cloud Infrastructure. Then, you can use policies to specify which users and groups can create, access, or change resources such as file systems, mount targets, snapshots, outbound connectors, and export options. See[Overview of Identity and Access Management](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm)to learn more about how to set up access.

## Network Security

The network security layer allows you to use VCN network security groups (NSGs) and security rules to block the appropriate ports from specific IP addresses and CIDR blocks and restrict host access. However, it's on an 'all or nothing' basis - the client either can or cannot access the mount target, and therefore all file systems associated with it. See[Ways to Secure Your Network](https://docs.oracle.com/iaas/Content/Network/Concepts/waystosecure.htm)for general information about VCN security groups, security lists, and rules. See[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/securitylistsfilestorage.htm)for specific information about the security rules necessary for File Storage.

## NFS v.3 UNIX Security

File Storage service supports the AUTH_SYS style of authentication and permission checking for remote NFS client requests. When mounting file systems, we recommend that you use the`-nosuid`option. This option disables set-user-identifier or set-group-identifier bits. Remote users are prevented from gaining higher privileges using a`setuid`program. For more information, see[Mounting File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/mountingfilesystems.htm).

Remember that users in UNIX aren't the same as users in Oracle Cloud Infrastructure - they're not linked or associated in any way. The Oracle Cloud Infrastructure policy layer doesn't govern anything that happens inside the file system, the UNIX security layer does. Conversely, the UNIX security layer doesn't govern creating file systems or mount targets in Oracle Cloud Infrastructure.

File Storage doesn't support file level Access Control Lists (ACLs). Only`user`,`group`, and`world`permissions are supported, including SUID and SGID. File Storage uses the NFSv3 protocol, which doesn't include support for ACLs.`setfacl`fails on mounted file systems.`getfacl`returns only standard permissions.

## NFS v.3 Kerberos Security

The File Storage service supports Kerberos authentication via RPCSEC_GSS (RFC2203) with the following security options:
- KRB5 for authentication over NFS
- KRB5I for authentication over NFS and data integrity (unauthorized modification of data in-transit)
- KRB5P for authentication over NFS, data integrity, and data privacy (in-transit encryption)

When Kerberos is configured for a mount target, it's used to prove the identity of the user making the request. After authentication, File Storage contacts your LDAP server for permissions information that it uses for authorization checks. For more information, see[Using LDAP for Authorization](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/ldap.htm)and[Using Kerberos Authentication](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/kerberos.htm).

## NFS Export Options

NFS export options are a method of applying access control at both the network security layer and the NFS v.3 security layer. You can use NFS export options to limit access to the export by IP addresses or CIDR blocks through an associated mount target. Access to each file system can be restricted to a limited set of clients, allowing for managed hosted environment security. Moreover, you can set NFS v.3 security layer permissions for read-only, read/write, or root-squash for your file systems. See[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/exportoptions.htm)for more information.

## Encryption

### Within Oracle Cloud Infrastructure
All data is encrypted at rest. You can leave all encryption-related matters to Oracle, or you can choose to manage your own encryption using the Oracle Cloud Infrastructure Vault service. You can use Vault to create master encryption keys and data encryption keys, rotate keys to generate new cryptographic material, enable or disable keys for use in cryptographic operations, assign keys to file systems, and use keys for encryption and decryption.
Note  
  
Currently, only symmetric Advanced Encryption Standard (AES) keys are supported for file system encryption. For more information, see[Encrypting a File System](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/encrypt-file-system.htm)and[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).

### In-transit Between Instances and Mounted File Systems

File Storage supports the following two methods of in-transit encryption:
- [In-transit encryption over TLS](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/intransitencryption.htm)(Transport Layer Security) using the`oci-fss-utils`client package or stunnel
- In-transit encryption[using Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/kerberos.htm)with the KRB5P option

In-transit encryption using`oci-fss-utils`or stunnel provides a way to secure your data between instances and mounted file systems using TLS v. 1.2 encryption. In-transit encryption of TLS requires installation of a client package on your Linux instance or stunnel on Windows.

The Linux package creates an NFS endpoint, network namespace, and network interface. Installing and configuring stunnel similarly encrypts requests and uses a TLS tunnel.

Kerberos authentication and the`KRB5P`security option, which offers data privacy (in-transit encryption), allows you to use confidentiality at a scale that isn't possible with NFS over TLS. For more information, see[limitations and considerations of TLS encryption for Linux users](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/intransitencryption.htm#Limitations_and_Considerations)and[limitations and considerations of TLS encryption for Windows users.](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/intransitencryption.htm#intransitencryption-windows-limitations)
