# Mounted Drive isn't Visible in PowerShell
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFSdriveNotVisiblePS.htm
- Fetched: 2026-09-05 02:07 CDT

# Mounted Drive isn't Visible in PowerShell

Learn how to troubleshoot an issue where a mounted drive isn't visible in PowerShell on a file system mounted using Windows NFS.
Important  
  

Before proceeding with troubleshooting, be sure to implement the following prerequisites for connecting to file systems from Windows instances:
- Install the NFS Client. Follow the installation procedure found in[Mounting File Systems From Windows Instances](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingwindowsos.htm).
- Set up security rules to work with File Storage. Follow the procedure found in[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm)

Symptom : After installing Windows NFS client, you can successfully mount the file system from either Windows File Explorer or the Command Prompt (CMD) using`mount`or`net use`commands. However, the file system drive isn't visible in PowerShell.

Cause : A known issue exists where drives mapped from outside PowerShell aren't visible from within PowerShell.

Solution : Unmount the file system and remount the file system within PowerShell, using options to make it visible in File Explorer and in the CMD application.

[To unmount a file system using the CMD prompt](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFSdriveNotVisiblePS.htm#)

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

[To map a drive in PowerShell and make it visible](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFSdriveNotVisiblePS.htm#)

You can map a drive in PowerShell and then use options to make it visible from File Explorer and the Windows Command Line (CMD).
- 

Open Windows PowerShell and run as Administrator :
- Go to Start and click the Windows PowerShell icon.
- 

In Windows PowerShell, type the following to run as Administrator:

```

```

- In the User Account Control window, click Yes . A new Administrator: PowerShell window opens. You can close the standard PowerShell window to avoid confusing them.
- 

Type the following cmdlet. Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target,`fs-export-path`with the export path you specified when associating the file system with the mount target, and`X`with the drive letter of any available drive you want to map the file system to:

```

```
