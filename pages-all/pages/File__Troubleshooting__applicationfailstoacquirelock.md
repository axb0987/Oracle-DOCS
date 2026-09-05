# Application Fails with Error 50: Request Not Supported
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/applicationfailstoacquirelock.htm
- Fetched: 2026-09-05 02:05 CDT

# Application Fails with Error 50: Request Not Supported

A Windows application using the File Storage service returns`Error 50: The request is not supported`.

Cause 1: The application is configured to access files using the UNC path instead of a drive letter, but file locking is not enabled for UNC paths.

Solution 1: Enable file locking for UNC paths.
- Click Windows Search .
- Enter`regedit`in the Search field and press Enter .

If prompted, click Yes to allow changes to your device.
- Click`HKEY_LOCAL_MACHINE`, then browse to:`SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Users\Default\Defaults`.
- 

Add a new DWORD32 registry entry for`Locking`:
- Click Edit , and select New DWORD (32 bit) Value .
- In the Name field, enter`Locking`.
- Right-click`Locking`, and select Modify .
- In the Value Data field, enter`1`.
- Click OK .
- Restart the instance.

Cause 2: The`nolock`option was used to mount the file system.

Solution 2: Unmount the file system and remount it without the`nolock`option. See[Mounting File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingfilesystems.htm)
