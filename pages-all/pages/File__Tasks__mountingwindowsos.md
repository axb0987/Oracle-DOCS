# Mounting File Systems From Windows Instances
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingwindowsos.htm
- Fetched: 2026-09-05 02:04 CDT

# Mounting File Systems From Windows Instances

Users of Windows Server 2012 R2 and later versions can mount a file system on any available drive letter using the mount target IP address and the file system[export path](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filesystempaths.htm).

The Windows NFS client must be installed on the instance from which you want to mount the file system.
Caution  
  
Installing the Windows NFS client might require a restart of your system.
Access to NFS file systems requires UNIX-style user and group identities, which aren't the same as Windows user and group identities. To enable users to access NFS shared resources, Windows client for NFS accesses file systems anonymously, using`AnonymousGid`and`AnonymousUid`. On brand new file systems, write permissions are only granted to the root user. The`AnonymousGid`and`AnonymousUid`identity values must be configured to allow write access.
Caution  
  
Updating the 'AnonymousGid' and 'AnonymousUid' values require registry changes to your system. After you have installed the NFS client and correctly mapped user identities, you can mount the file system to any available drive letter using the command line or Map network drive . You can access your file system through the chosen drive letter to write files.

## Prerequisites

- The file system must have at least one export in at least one mount target. When you create a new file system, an export for the file system is created at the same time. See[Creating File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/creatingfilesystems.htm)for more information.
- Correctly configured security rules for the mount target. See[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)for information about how security rules work in Oracle Cloud Infrastructure. Use the instructions in[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm)to set up security rules correctly for your file systems.

Caution  
  

Because Windows network providers prioritize SMB traffic over NFS traffic, there can be delays when connecting to a File Storage mount target for the first time. Subsequent connections are faster because the mount information is cached, but after the cache expires, the delay reoccurs. This causes intermittent slow performance. To improve performance, you can change the network provider order so that the NFS client is prioritized. For more information, see[Accessing a Mounted File System is Slow or Fails After a Few Seconds](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/winNFSerror53.htm).
Note  
  

When mounting file systems, Network Lock Manager (NLM) is enabled for file locking by default. The default requires no specified mount option. Typical NFS workloads function normally using the default.

Some applications might require you to specify the`nolock`mount option. Refer to your application documentation for best practices regarding this mount option.

## Using Windows Command Prompt

[To mount a file system from Windows Server Command Prompt](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingwindowsos.htm#)

If you're using Windows platform images, the NFS client is already installed, and the correct user identities are mapped. Skip to step 4.
- 

Open Windows PowerShell and run as Administrator :
- Go to Start and select the Windows PowerShell icon.
- 

In Windows PowerShell, type the following to run as Administrator:

```

```

- In the User Account Control window, select Yes . A new Administrator: PowerShell window opens. You can close the standard PowerShell window to avoid confusing them.
- In Administrator: PowerShell, get the NFS client by typing the following:

```

```

Important  
  

If you've set export options for the file system to require clients to connect from a privileged source port (1-1023), then you must set the UseReservedPorts registry key to 1 .

For example:

```

```

For more information, see[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm).
- 

Close the Administrator: PowerShell window. Open a standard Command Prompt Window. Select Start , then select Command Prompt .
Important  
  
NFS file systems mounted as Administrator aren't available to standard users.
- 

In the standard Windows Command Line (CMD) window, mount the file system by typing the following:

```

```

- Replace`10.x.x.x:`with the local subnet IP address assigned to the mount target.
Note  
  
If the export uses[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm), use the fully qualified domain name (FQDN) of the mount target instead of the IP address.
- 

Replace`fs-export-path`with the export path you specified when associating the file system with the mount target.
Tip  
  
Export path information is available in the details page of the mount target associated with the file system. See[Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-mount-target-details.htm)for more information.
Important  
  
The export path is the path to the file system (relative to the mount target IP address or hostname). If you didn't specify a path when you associated the file system and mount target, then "/" represents the full extent of the mount target. In that case, you must use a "!" when mounting the file system. For example:`mount 10.0.0.0:/! X:`
- Replace`X`with the drive letter of any available drive you want to map the file system to.
- If the export is using AUTH_SYS alone, the`sec`option is optional. If the export uses[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm), replace`sys`with`krb5`,`krb5i`, or`krb5p`.
Note  
  
If an NFS client uses an export which has multiple authentication types, and file system is mounted without specifying`sec= <auth_type>`, the client should automatically pick the strongest authentication type supported by the export.
- 

Write a file to the file system by typing the following. Replace`X`with the drive letter you used in step 10 and`helloworld`with your file name.

```

```

```

```

- 

Verify that you can view the file by entering the following:

```

```

See[Troubleshooting Windows NFS Connections](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/winNFSTS.htm)for more information about common issues.

## Using Windows File Explorer

[To mount a file system from Windows Server File Explorer](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingwindowsos.htm#)

If you're using Windows platform images, the NFS client is already installed, and the correct user identities are mapped. Skip to step 9.
- 

Open Windows PowerShell and run as Administrator :
- Go to Start and select the Windows PowerShell icon.
- 

In Windows PowerShell, type the following to run as Administrator:

```

```

- In the User Account Control window, select Yes . A new Administrator: PowerShell window opens. You can close the standard PowerShell window to avoid confusing them.
- 

In Administrator: PowerShell, get the NFS client by typing the following:

```

```

- If prompted, restart your system.
- 

Open the registry editor (regedit) to map the AnonymousGid and AnonymousUid to the root user.
Caution  
  
User identity mapping requires changes to your system registry.
- Select Windows Search.
- Enter`regedit`in the Search field and press Enter .
- Select Yes to allow changes to your device.
- Select`HKEY_LOCAL_MACHINE`. Then, browse to:`Software\Microsoft\ClientForNFS\CurrentVersion\Default`.
- 

Add a new DWORD32 registry entry for`AnonymousGid`:
- Select Edit , and select New DWORD (32 bit) Value .
- In the Name field, enter`AnonymousGid`. Leave the value at`0`.
- 

Repeat step 5 to add a second DWORD32 registry entry named`AnonymousUid`with a value of`0`.
Important  
  

If you set export options for the file system to require clients to connect from a privileged source port (1-1023), then you must set the UseReserverdPorts registry key to 1 .

For more information, see[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm).
- 

Open Windows Command Line (CMD) and run as Administrator:
- Go to Start and scroll down to Apps .
- In the Windows System section, press Ctrl+Shift and select Command Prompt .
- 

In the Windows Command Line (CMD) window, restart the NFS Client by typing the following:

```

```

```

```

- 

Open File Explorer and select This PC . In the Computer tab, select Map network drive .
- Select the Drive letter that you want to assign to the file system.
- 

In the Folder field, enter the following. Replace`10.x.x.x`with the local subnet IP address assigned to your mount target, and`fs-export-path`with the export path you specified when associating the file system with the mount target.

```

```

Tip  
  
IP address and export path information is available in the Details page of the mount target associated with your file system. See[Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-mount-target-details.htm)for more information.
Important  
  
The export path is the path to the file system (relative to the mount target IP address or hostname). If you did not specify a path when you associated the file system and mount target, then "\" represents the full extent of the mount target. In that case, you must use a "!" when entering the file system folder path. For example:`\\10.0.0.0\!`
- Select the Finish button when complete.

See[Troubleshooting Windows NFS Connections](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/winNFSTS.htm)for more information about common issues.

## Mounting File System Subdirectories

If your file system has an existing directory structure, you can mount any file system subdirectory. The subdirectory becomes the effective root directory at the mount point of the instance, and excludes sibling directories.

For example, suppose "FileSystem1" has an export path of`/FileSystem1`and a directory structure like this:

[

The file system is exported from "MountTarget1" which has an IP address of`10.0.0.16`.

The following command mounts`directoryA`to drive letter X:

```

```

Neither`directoryB`or`FileB`would be accessible from drive X.
Caution  
  
Mounting a subdirectory to limit access to sibling directories is not sufficient to secure your file system. For information on security methods, see[About File Storage Security](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/securitylayers.htm).

[To mount a file system subdirectory](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingwindowsos.htm#)

- Choose the method you want to use to mount the file system[Using Windows Command Prompt](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingwindowsos.htm#Using2)or[Using Windows File Explorer](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingwindowsos.htm#Using).
- Follow the instructions to install the NFS client and add the registry entries for`AnonymousGid`and`AnonymousUid`.
- After the NFS client is installed and registry entries are added, both mounting methods describe how to enter the mount information for the file system. Depending on which method you use, edit the mounting information to append the subdirectory path to the export path:
- 

If you're[Using Windows Command Prompt](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingwindowsos.htm#Using2), type the following command (step 4):
- Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target.
- 

Replace`fs-export-path`with the export path you specified when associating the file system with the mount target.
- Replace`directory-path`with the path from the root directory to subdirectory you want to mount.

```

```

- 

If you're[Using Windows File Explorer](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingwindowsos.htm#Using), enter the following in the Folder field of the drive letter you want to map the file system to (step 11):
- Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target.
- 

Replace`fs-export-path`with the export path you specified when associating the file system with the mount target.
- Replace`directory-path`with the path from the root directory to subdirectory you want to mount.

```

```

## Unmounting File Systems

Using the command line:
- 

In the standard Windows Command Line (CMD) window, mount the file system by typing the following. Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target,`fs-export-path`with the export path you specified when associating the file system with the mount target, and`X`with the drive letter of any available drive you want to map the file system to.

```

```

Note  
  
Unmounting might require using the`-f`flag in the`umount`command. For example:

```

```
