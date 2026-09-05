# Mounting File Systems
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm
- Fetched: 2026-09-05 02:04 CDT

# Mounting File Systems

Users of Unix-style operating systems and Windows Server 2012 R2 and later versions can connect to a file system and write files.[Mount targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm)serve as file system network access points for file systems. After your mount target is assigned an IP address, you can use it together with the file system[export path](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filesystempaths.htm)to mount the file system. On the instance from which you want to mount the file system, you need to install an NFS client. For Unix-style operating systems, you create a mount point. When you mount the file system, the mount point effectively represents the root directory of the File Storage file system, allowing you to write files to the file system from the instance. Windows operating systems use a drive letter assignment instead of a mount point to represent root access.
Tip  
  

To mount a file system on an on-premises instance, establish and verify network connectivity between the on-premises instance and OCI using FastConnect or Site-to-Site VPN IPSec. For more information, see[Access to Your On-Premises Network](https://docs.oracle.com/iaas/Content/Network/Concepts/connectivityonprem.htm). The steps to mount a File Storage file system are otherwise the same.

## Prerequisites

- The file system must have at least one export in at least one mount target. When you create a new file system, an export for the file system is created at the same time. See[Creating File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/creatingfilesystems.htm)for more information.
- Correctly configured security rules for the mount target. See[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)for information about how security rules work in Oracle Cloud Infrastructure. Use the instructions in[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm)to set up security rules correctly for your file systems.

## Mounting File Systems From an Instance

[Mounting File Systems From UNIX-Style Instances](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm)(Including Oracle Linux DB instances)

[Mounting File Systems From Windows Instances](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingwindowsos.htm)

## Mount Command Samples

Mount command samples that include mount information for a specific mount target and file system are available in the Console. Samples are available for the following operating system images:
- Oracle Linux
- CentOS
- Debian
- Red Hat Linux
- Ubuntu

If you specified a hostname for the mount target, the sample uses the FQDN in the commands. If you didn't specify a hostname, the sample uses the mount target IP address. Using a FQDN to mount your file system is optional; even if you specified a hostname, you can edit the command to use the IP address instead. If you use an FQDN to mount the file system, ensure that the the FQDN correctly resolves to the mount target's IP address. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm).
Mount command samples are different depending on the allowed authentication options selected in the[NFS Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm#Export). Ensure that you copy the command that matches the required authentication method.
Note  
  
If an NFS client uses an export which has multiple authentication types, and file system is mounted without specifying`sec= <auth_type>`, the client should automatically pick the strongest authentication type supported by the export.

Mount command samples mount the file system at the file system root directory. Mount command samples don't include subdirectory information for the file system. To mount a subdirectory of the file system, you must edit the sample to append the subdirectory path to the export path. For more information on mounting subdirectories in Linux-type instances, see[To mount a file system subdirectory (Linux)](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm#Mounting_File_System_Subdirectories). For more information on mounting subdirectories in Windows instances, see[To mount a file system subdirectory (Windows)](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingwindowsos.htm#Mounting_File_System_Subdirectories).

Caution  
  

When mounting file systems, the following mount option combination is not supported by the File Storage service:
- `soft`when the file system is mounted with the read/write mount option (`-o rw`). This combination can cause corruption of your data .

The following mount options or mount option combinations are not recommended for use with the File Storage service:
- `soft`when the file system is mounted with the read-only mount option (`-o ro`) and the`timeo`has been specified as less than`300`seconds. This combination can cause a profusion of I/O error responses.
- `rsize`, or`wsize`. These options cause issues with performance.
Note  
  

When mounting file systems, Network Lock Manager (NLM) is enabled for file locking by default. The default requires no specified mount option. Typical NFS workloads function normally using the default.

Some applications might require you to specify the`nolock`mount option. Refer to your application documentation for best practices regarding this mount option.

### Getting Mount Command Samples

- On the File Systems list page, select the file system that contains the quota rules that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Exports .
- 

Select the export path that you want to use to mount the file system.
Tip  
  

To be sure that you select the correct export, check the following:
- The export path : This[path](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filesystempaths.htm)uniquely identifies the file system within the mount target. No two exports in a mount target can have the same export path, even if the exports are for the same file system.
- The mount target name : File systems can be exported through more than one mount target. Be sure that you selected the export for the correct mount target.
- On the export details page, select Mount commands .
- In Image , choose the image of the Compute instance that you want to mount the file system to.
- Select the Copy links to copy the commands.

Next, mount the file system from a[UNIX-style](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm)or[Windows](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingwindowsos.htm)instance.

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users create, manage, and delete file systems](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#general-file-system-management)allows users to obtain mount commands.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Details for the File Storage Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm)
