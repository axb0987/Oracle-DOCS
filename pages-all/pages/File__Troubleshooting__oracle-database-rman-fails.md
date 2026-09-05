# Oracle Database RMAN Operation Fails with ORA-17500 Error
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/oracle-database-rman-fails.htm
- Fetched: 2026-09-05 02:06 CDT

# Oracle Database RMAN Operation Fails with ORA-17500 Error

When using Oracle database Recovery Manager (RMAN) to backup to or restore from File Storage, the operation fails with an "ORA-17500: ODM err:KGNFS_NFSERR_BADHANDLE" error.

Cause: File Storage[NFS export options](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/exportoptions.htm#Export)include a setting for requiring use of a privileged port. Oracle database has its own NFS client driver called Direct NFS (dNFS). If dNFS is enabled, it bypasses the kernel NFS client. Because dNFS functions outside of the privileged port range, it can't communicate with a file system that has been exported with the Port option set to Privileged .

Solution: Update the NFS export option for Port to Any instead of Privileged . See[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/exportoptions.htm)
