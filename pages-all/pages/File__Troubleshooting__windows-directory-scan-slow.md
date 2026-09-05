# Slow Data Copy in Windows Compared to Copy of Same Data in Linux
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/windows-directory-scan-slow.htm
- Fetched: 2026-09-05 02:07 CDT

# Slow Data Copy in Windows Compared to Copy of Same Data in Linux

Copying many files or directories to or within File Storage and a Windows instance takes more time than a copy of the same files using the same resources and a Linux instance.

Cause: The Windows NFS client calls for a directory scan for each file creation. The directory scan, a`READDIR`NFS call, increases overall copy time. This is expected Windows NFS behavior and doesn't occur when using a Linux NFS client.

Solution: Edit the`NFSReaddir`registry setting to avoid the READDIR call and increase the efficiency of the copy command.
- Click Windows Search .
- Enter`regedit`in the Search field and press Enter .
- Click Yes to allow changes to the device.
- Click`HKEY_LOCAL_MACHINE`.
- Browse to`SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Users\Default\Defaults\NFSReaddir`.
- Set the value for`NFSReaddir`to`0`.
- Restart the instance.
Caution
