# Mounting from File Explorer Fails With "An Unexpected Error Occurred."
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFSunexpectederror.htm
- Fetched: 2026-09-05 02:07 CDT

# Mounting from File Explorer Fails With "An Unexpected Error Occurred."

Learn how to troubleshoot mount failures with unexpected errors when mounting with Windows File Explorer.
Important  
  

Before proceeding with troubleshooting, be sure to implement the following prerequisites for connecting to file systems from Windows instances:
- Install the NFS Client. Follow the installation procedure found in[Mounting File Systems From Windows Instances](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingwindowsos.htm).
- Set up security rules to work with File Storage. Follow the procedure found in[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm)

Symptom: The IP address and export path are correctly represented in the Folder field. When you click Finish , the system attempts to connect to the file system, but fails with an error: "The mapped network drive could not be created because the following error has occurred: An unexpected error occurred."

Solution 1: Reboot the instance, and[mount the file system again using File Explorer.](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingwindowsos.htm)

Solution 2:[Mount the file system using the Command Prompt](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingwindowsos.htm#Using2)
