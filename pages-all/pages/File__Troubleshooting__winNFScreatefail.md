# Create and Write to File System Fails using Windows NFS
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFScreatefail.htm
- Fetched: 2026-09-05 02:07 CDT

# Create and Write to File System Fails using Windows NFS

Learn how to troubleshoot failures to create or write files on a file system mounted using Windows NFS.
Important  
  

Before proceeding with troubleshooting, be sure to implement the following prerequisites for connecting to file systems from Windows instances:
- Install the NFS Client. Follow the installation procedure found in[Mounting File Systems From Windows Instances](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingwindowsos.htm).
- Set up security rules to work with File Storage. Follow the procedure found in[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm)

Symptom : After installing Windows NFS client, you can successfully mount the file system from Windows, but any attempt to create or update a file in the file system fails.

Cause 1: Registry entries that map the`AnonymousGid`and`AnonymousUid`to the root user are missing or in the wrong place.

Access to NFS file systems requires UNIX-style user and group identities, which are not the same as Windows user and group identities. To enable users to access NFS shared resources, Windows client for NFS accesses file systems anonymously, using`AnonymousGid`and`AnonymousUid`. On brand new file systems, write permissions are only granted to the root user.

Solution : Verify that the correct registry entries are located in`HKEY_LOCAL_MACHINE\Software\Microsoft\ClientForNFS\CurrentVersion\Default`. If not, add the`AnonymousGid`and`AnonymousUid`registry entries to map them to the root user, and then remount the file system with the new user privileges.
Tip  
  

You can verify the`AnonymousGid`and`AnonymousUid`are correctly set for a mounted file system by opening a Windows Command Line (CMD) window and typing the`mount`command without any arguments. A list of all mounted file systems and their properties is shown. The`AnonymousGid (GID)`and`AnonymousUid (UID)`values should appear as`0`.

For example:

```

```

If they appear as`-2`, they have not been correctly set. Proceed to the instructions below.

[To map the AnonymousGid and AnonymousUid to the root user](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFScreatefail.htm#)

- 

In the Windows Command Line (CMD) window, unmount the file system by typing the following. Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target,`fs-export-path`with the export path you specified when associating the file system with the mount target, and`X`with the drive letter of any available drive you want to map the file system to.
Tip  
  
IP address and export path information is available in the Details page of the mount target associated with your file system. See[Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/get-mount-target-details.htm)for more information.

```

```

- 

Open the registry editor (regedit):
- Click Windows Search.
- Enter`regedit`in the Search field and press Enter .
- Click Yes to allow changes to your device.
- Click`HKEY_LOCAL_MACHINE`. Then, browse to:`Software\Microsoft\ClientForNFS\CurrentVersion\Default.`
- 

Add a new DWORD32 registry entry for`AnonymousGid`:
- Click Edit , and select New DWORD (32 bit) Value .
- In the Name field, enter`AnonymousGid`. Leave the value at`0`.
- 

Repeat step 3 to add a second DWORD32 registry entry named`AnonymousUid`with a value of`0`.
- 

Open Windows Command Line (CMD) and run as Administrator:
- Go to Start and scroll down to Apps .
- In the Windows System section, press Ctrl+Shift and click Command Prompt .
- 

In the Windows Command Line (CMD) window, restart the NFS Client by typing the following:

```

```

```

```

- 

Close the Administrator: Windows Command Prompt (CMD) window. Open a standard Command Prompt Window:
- Click Start , then click Command Prompt .
Important  
  
NFS file systems mounted as Administrator are not available to standard users.
- 

In the standard Windows Command Line (CMD) window, mount the file system by typing the following. Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target,`fs-export-path`with the export path you specified when associating the file system with the mount target, and`X`with the drive letter of any available drive you want to map the file system to.

```

```

Cause 2: A standard user is trying to access a file system that was mounted using the Administrator: Command Prompt (CMD). When mounting file systems, it isn't necessary to run the Command Prompt as Administrator.

Solution: Unmount the file system and then remount the file system using a standard Command Prompt. (CMD)

[To remount a file system with a standard Command Prompt (CMD)](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFScreatefail.htm#)

- 

Open Windows Command Line (CMD) and run as Administrator:
- Go to Start and scroll down to Apps .
- In the Windows System section, press Ctrl+Shift and click Command Prompt .
- 

In the Administrator: Windows Command Line (CMD) window, unmount the file system by typing the following. Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target,`fs-export-path`with the export path you specified when associating the file system with the mount target, and`X`with the drive letter of any available drive you want to map the file system to.
Tip  
  
IP address and export path information is available in the Details page of the mount target associated with your file system. See[Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/get-mount-target-details.htm)for more information.

```

```

- Close the Administrator: Windows Command Line (CMD) window.
- 

Open a standard Command Prompt Window:
- Click Start , then click Command Prompt .
- 

In the standard Command Line (CMD) window, mount the file system by typing the following. Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target,`fs-export-path`with the export path you specified when associating the file system with the mount target, and`X`with the drive letter of any available drive you want to map the file system to.

```

```
