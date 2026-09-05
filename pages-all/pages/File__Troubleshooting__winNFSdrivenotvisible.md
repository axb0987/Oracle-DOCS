# Mounted Drive isn't Visible in File Explorer
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFSdrivenotvisible.htm
- Fetched: 2026-09-05 02:07 CDT

# Mounted Drive isn't Visible in File Explorer

Learn how to troubleshoot an issue where a mounted drive isn't visible on a file system mounted using Windows NFS.
Important  
  

Before proceeding with troubleshooting, be sure to implement the following prerequisites for connecting to file systems from Windows instances:
- Install the NFS Client. Follow the installation procedure found in[Mounting File Systems From Windows Instances](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingwindowsos.htm).
- Set up security rules to work with File Storage. Follow the procedure found in[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm)

Symptom : After installing Windows NFS client, you can successfully mount the file system from Windows, but the file system drive isn't visible in File Explorer.

Cause : A standard user is trying to access a file system that was mounted using the Administrator: Command Prompt (CMD). When mounting file systems, it isn't necessary to run the Command Prompt as Administrator.

Solution : Unmount the file system and then remount the file system using a standard Command Prompt (CMD). See[To remount a file system with a standard Command Prompt (CMD)](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFScreatefail.htm#Create_and_Write_to_File_System_Fails_using_Windows_NFS__remountstandardCMD)
