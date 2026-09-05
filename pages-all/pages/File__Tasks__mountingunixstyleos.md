# Mounting File Systems From UNIX-Style Instances
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm
- Fetched: 2026-09-05 02:04 CDT

# Mounting File Systems From UNIX-Style Instances

Users of Ubuntu and Linux operating systems can use the command line to connect to a file system and write files.[Mount targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm)serve as network access points for file systems. After your mount target is assigned an IP address, you can use it together with the[export path](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filesystempaths.htm)to mount the file system. On the instance from which you want to mount the file system, you need to install an NFS client and create a mount point. When you mount the file system, the mount point effectively represents the root directory of the File Storage file system, allowing you to write files to the file system from the instance. You can mount to any directory within the file system.

## Prerequisites

- The file system must have at least one export in at least one mount target. When you create a new file system, an export for the file system is created at the same time. See[Creating File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/creatingfilesystems.htm)for more information.
- Correctly configured security rules for the mount target. See[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)for information about how security rules work in Oracle Cloud Infrastructure. Use the instructions in[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm)to set up security rules correctly for your file systems.

## Mounting File Systems

You can use the following instructions to construct your mount commands, or use the Console to get mount command samples that include all the information for a specific mount target and file system. For more information, see[Mount Command Samples](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm#samples).

Mount command samples mount the file system at the file system root directory. Mount command samples don't include subdirectory information for the file system. If you want to mount your Linux-type instance at a subdirectory of the file system, you must edit the sample to append the subdirectory path to the export path. For more information, see[To mount a file system subdirectory](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm#CLIsubdirectory).

Caution  
  

When mounting file systems, the following mount option combination is not supported by the File Storage service:
- `soft`when the file system is mounted with the read/write mount option (`-o rw`). This combination can cause corruption of your data .

The following mount options or mount option combinations are not recommended for use with the File Storage service:
- `soft`when the file system is mounted with the read-only mount option (`-o ro`) and the`timeo`has been specified as less than`300`seconds. This combination can cause a profusion of I/O error responses.
- `rsize`, or`wsize`. These options cause issues with performance.
Note  
  

When mounting file systems, Network Lock Manager (NLM) is enabled for file locking by default. The default requires no specified mount option. Typical NFS workloads function normally using the default.

Some applications might require you to specify the`nolock`mount option. Refer to your application documentation for best practices regarding this mount option.

[To mount a file system from Ubuntu or Debian](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm#)

- Open a command window. Then, get the NFS client by copying and pasting the Install Command from the Console or type the following:

```

```

- Create a mount point by copying and pasting the Create Mount Point Command from the Console or type the following, replacing`yourmountpoint`with the local directory from which you want to access your file system.

```

```

- 

Mount the file system by copying and pasting the Mount Command from the Console or type the following:

```

```

- Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target.
Note  
  
If the export uses[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm), use the fully qualified domain name (FQDN) of the mount target instead of the IP address.
- 

Replace`fs-export-path`with the export path you specified when associating the file system with the mount target.
- Replace`yourmountpoint`with the path to the local mount point.
- If the export is using AUTH_SYS alone, the`sec`option is optional. If the export uses[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm), replace`sys`with`krb5`,`krb5i`, or`krb5p`.
Note  
  
If an NFS client uses an export which has multiple authentication types, and file system is mounted without specifying`sec= <auth_type>`, the client should automatically pick the strongest authentication type supported by the export.
Tip  
  
IP address, hostname, FQDN, and export path information is available in the Details page of the mount target associated with your file system. See[Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-mount-target-details.htm)for more information.
Caution  
  
Omitting the`-o nosuid`option may allow unprivileged users to escalate their permissions to 'root'. The`nosuid`option disables set-user-identifier or set-group-identifier bits within the mounted system, which are rarely used.
Note  
  
The`-o resvport`option is required when the "Require Privileged Source Port" export option is used and otherwise optional. It causes the mounting filesystem to connect from a privileged source port (1-1023). See[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm)for more information.
- View the file system.

```

```

- 

Write a file to the file system by typing the following. Replace`yourmountpoint`with the path to the local mount point and`helloworld`with your file name.

```

```

- 

Verify that you can view the file by typing the following. Replace`yourmountpoint`with the path to the local mount point.

```

```

```

```

See[Mount Command Fails](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/exportpaths.htm)in[Troubleshooting a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/troubleshootingfilesystems.htm)for more information about common issues you may encounter.

[To mount a file system from Solaris](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm#)

- Open a command window.
- Create a mount point by typing the following, replacing`yourmountpoint`with the local directory from which you want to access your file system.

```

```

- 

Mount the file system by typing the following:

```

```

- Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target.
Note  
  
If the export uses[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm), use the fully qualified domain name (FQDN) of the mount target instead of the IP address.
- 

Replace`fs-export-path`with the export path you specified when associating the file system with the mount target.
- Replace`yourmountpoint`with the path to the local mount point.
- If the export is using AUTH_SYS alone, the`sec`option is optional. If the export uses[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm), replace`sys`with`krb5`,`krb5i`, or`krb5p`.
Note  
  
If an NFS client uses an export which has multiple authentication types, and file system is mounted without specifying`sec= <auth_type>`, the client should automatically pick the strongest authentication type supported by the export.
Tip  
  
IP address, hostname, FQDN, and export path information is available in the Details page of the mount target associated with your file system. See[Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-mount-target-details.htm)for more information.
- 

View the file system.

```

```

- 

Write a file to the file system by typing the following. Replace`yourmountpoint`with the path to the local mount point and`helloworld`with your file name.

```

```

- 

Verify that you can view the file by typing the following. Replace`yourmountpoint`with the path to the local mount point.

```

```

```

```

See[Mount Command Fails](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/exportpaths.htm)in[Troubleshooting a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/troubleshootingfilesystems.htm)for more information about common issues you may encounter.

[To mount a file system from Linux, Red Hat, or CentOS](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm#)

- Open a command window. Then, get the NFS client by copying and pasting the Install Command from the Console or typing the following:

```

```

- Create a mount point by copying and pasting the Create Mount Point Command from the Console or type the following, replacing`yourmountpoint`with the local directory from which you want to access your file system.

```

```

- 

Mount the file system by copying and pasting the Mount Command from the Console or type the following:

```

```

- Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target.
Note  
  
If the export uses[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm), use the fully qualified domain name (FQDN) of the mount target instead of the IP address.
- 

Replace`fs-export-path`with the export path you specified when associating the file system with the mount target.
- Replace`yourmountpoint`with the path to the local mount point.
- If the export is using AUTH_SYS alone, the`sec`option is optional. If the export uses[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm), replace`sys`with`krb5`,`krb5i`, or`krb5p`.
Note  
  
If an NFS client uses an export which has multiple authentication types, and file system is mounted without specifying`sec= <auth_type>`, the client should automatically pick the strongest authentication type supported by the export.
Tip  
  
IP address, hostname, FQDN, and export path information is available in the Details page of the mount target associated with your file system. See[Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-mount-target-details.htm)for more information.
Caution  
  
Omitting the`-o nosuid`option may allow unprivileged users to escalate their permissions to 'root'. The`nosuid`option disables set-user-identifier or set-group-identifier bits within the mounted system, which are rarely used.
Note  
  
The`-o resvport`option is required when the "Require Privileged Source Port" export option is used and otherwise optional. It causes the mounting file system to connect from a privileged source port (1-1023). See[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm)for more information.
- View the file system.

```

```

- 

Write a file to the file system by typing the following. Replace`yourmountpoint`with the path to the local mount point and`helloworld`with your file name.

```

```

- 

Verify that you can view the file by typing the following. Replace`yourmountpoint`with the path to the local mount point.

```

```

```

```

See[Mount Command Fails](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/exportpaths.htm)in[Troubleshooting a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/troubleshootingfilesystems.htm)for more information about common issues. See[Mounting File System Subdirectories](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm#Mounting_File_System_Subdirectories)to mount a subdirectory of the file system.

[To mount a file system from a Database VM instance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm#)

Database VM instances are built on Oracle Linux 8 or later. The NFS Utilities package is pre-installed on DB instances, but the Open Network Computing Remote Procedure Call (ONC RPC)`rpcbind`utility is disabled by default. An Oracle DB instance comes with firewall rules that exclude any non-database ports and need to be updated to allow mount target traffic.
- 

SSH to the DB system.

```

```

- 

For backward-compatibility with NFSv3, start the`rpcbind`service and configure it to start automatically on boot:

```

```

- 

Change the default firewall configuration to include the mount target IP address and allow traffic. Replace`10.x.x.x`with the local subnet IP address assigned to the mount target for the file system.

```

```

```

```

- 

Create a mount point by typing the following, replacing`yourmountpoint`with the local directory from which you want to access your file system.

```

```

- 

Mount the file system by copying and pasting the Mount Command from the Console or type the following:

```

```

- Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target.
Note  
  
If the export uses[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm), use the fully qualified domain name (FQDN) of the mount target instead of the IP address.
- 

Replace`fs-export-path`with the export path you specified when associating the file system with the mount target.
- Replace`yourmountpoint`with the path to the local mount point.
- If the export is using AUTH_SYS alone, the`sec`option is optional. If the export uses[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm), replace`sys`with`krb5`,`krb5i`, or`krb5p`.
Note  
  
If an NFS client uses an export which has multiple authentication types, and file system is mounted without specifying`sec= <auth_type>`, the client should automatically pick the strongest authentication type supported by the export.
Tip  
  
IP address, hostname, FQDN, and export path information is available in the Details page of the mount target associated with your file system. See[Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-mount-target-details.htm)for more information.
Caution  
  
Omitting the`-o nosuid`option may allow unprivileged users to escalate their permissions to 'root'. The`nosuid`option disables set-user-identifier or set-group-identifier bits within the mounted system, which are rarely used.
Note  
  
The`-o resvport`option is required when the "Require Privileged Source Port" export option is used and otherwise optional. It causes the mounting file system to connect from a privileged source port (1-1023). See[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm)for more information.

See[Mount Command Fails](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/exportpaths.htm)in[Troubleshooting a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/troubleshootingfilesystems.htm)for more information about common issues you may encounter.

[To auto-mount a file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm#)

Auto-mount ensures that a file system is automatically re-mounted on an instance if it is rebooted.
- Open a command window. Then, mount the file system using the steps described in the previous section.
- Type the following command to get the file system entry point:

```

```

- Copy the file system entry point, and open the`/etc/fstab`file:

```

```

```

```

- 

Add the following line to the`fstab`file:

```

```

Caution  
  
Omitting the`-o nosuid`option may allow unprivileged users to escalate their permissions to 'root'. The`nosuid`option disables set-user-identifier or set-group-identifier bits within the mounted system, which are rarely used.
Important  
  
Be sure to add the`nofail`option to each entry. This option ensures that an unavailable file system does not cause the instance reboot process to fail.
Note  
  
The`-o resvport`option is required when the "Require Privileged Source Port" export option is used and otherwise optional. It causes the mounting filesystem to connect from a privileged source port (1-1023). See[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm)for more information.
- Save the`fstab`file.

See[Mount Command Fails](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/exportpaths.htm)in[Troubleshooting a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/troubleshootingfilesystems.htm)for more information about common issues you may encounter.

## Mounting File System Subdirectories

If your file system has an existing directory structure, you can mount any file system subdirectory. The subdirectory becomes the effective root directory at the mount point of the instance, and excludes sibling directories.

For example, suppose "FileSystem1" has an export path of`/FileSystem1`and a directory structure like this:

[

The file system is exported from "MountTarget1" which has an IP address of`10.0.0.16`.

The following command mounts`directoryA`to the instance mount point`/mnt/mymountpoint`:

```

```

Neither`directoryB`or`FileB`would be accessible from the instance mount point.
Caution  
  
Mounting a subdirectory to limit access to sibling directories is not sufficient to secure your file system. For information on security methods, see[About File Storage Security](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/securitylayers.htm).

[To mount a file system subdirectory](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm#)

- Open a command window. Then, get the NFS client by copying and pasting the Install Command from the Console or typing the following:

```

```

- Create a mount point by copying and pasting the Create Mount Point Command from the Console or type the following, replacing`yourmountpoint`with the local directory from which you want to access your file system.

```

```

- 

Mount the file system by copying and editing the Mount Command from the Console or type the following:

```

```

- Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target.
- 

Replace`fs-export-path`with the export path you specified when associating the file system with the mount target.
- Replace`directory-path`with the path from the root directory to subdirectory you want to mount.
- Replace`yourmountpoint`with the path to the local mount point.
Tip  
  
IP address and export path information is available in the Details page of the mount target associated with your file system. See[Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-mount-target-details.htm)for more information.
Caution  
  
Omitting the`-o nosuid`option may allow unprivileged users to escalate their permissions to 'root'. The`nosuid`option disables set-user-identifier or set-group-identifier bits within the mounted system, which are rarely used.
Note  
  
The`-o resvport`option is required when the "Require Privileged Source Port" export option is used and otherwise optional. It causes the mounting file system to connect from a privileged source port (1-1023). See[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm)for more information.
- View the file system.

```

```

- 

Write a file to the file system by typing the following. Replace`yourmountpoint`with the path to the local mount point and`helloworld`with your file name.

```

```

- 

Verify that you can view the file by typing the following. Replace`yourmountpoint`with the path to the local mount point.

```

```

```

```

[To unmount a file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm#)

- Open a terminal window on the instance.
- 

Use the following command to unmount the file system:

```

```

Replace`yourmountpoint`with the path to the local mount point.

## Writing to File Systems

When a file system is created, its root directory is owned by the root user. If you're connecting from an instance that uses a Linux or CentOS platform image, the default user is opc . If you're connecting from an instance that uses an Ubuntu platform image, the default user is ubuntu . These default users are not root users, so you can't initially write a file or directory to a new file system with these users. Depending on your security requirements, there are several ways to proceed:
- Connect as the root user. Then, create files or directories in the new file system.
- 

Connect as the root user. Then, change the ownership or permissions of the file system root directory to allow other users (such as opc or ubuntu ) to write to the file system.
- 

Connect as the root user. Then, create subdirectories with ownership or permissions that allow other users to write to the subdirectory.

[Learn more about updating file and directory ownership and permissions.](https://linux.die.net/man/3/chmod)
- 

Connect as the default user. Then, use the`sudo`command to write or to change permissions or ownership of files or directories. The`sudo`command temporarily provides a regular user with root user permissions. Here's an example of using the`sudo`command to write to the file system:

```

```

[Learn more about the`sudo`command.](https://linux.die.net/man/8/sudo)

For more information about accessing instances, see[Connecting to an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm).

## Unmounting File Systems

- Open a terminal window.
- 

Unmount the file system by typing the following command:

```

```

- Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target.
- 

Replace`fs-export-path`with the export path you specified when associating the file system with the mount target.
- Replace`yourmountpoint`with the path to the local mount point.
Note  
  
Unmounting might require using the`-f`flag in the`umount`command. For example:
```

```
