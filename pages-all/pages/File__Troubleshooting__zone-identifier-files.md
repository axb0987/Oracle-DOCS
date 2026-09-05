# Zone.Identifier Files Created on File Storage Mounted Drive
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/zone-identifier-files.htm
- Fetched: 2026-09-05 02:07 CDT

# Zone.Identifier Files Created on File Storage Mounted Drive

In Windows, when you copy and unzip a file downloaded from Internet browsers to an OCI File Storage mounted drive, an`originalfilename.Zone.Identifier`file is created for each`originalfilename`.

This behavior doesn't occur for files created locally in the Windows OS.

Cause: This is a Windows protection mechanism for modern browsers and NTFS formatted volumes. When a browser is used to download a file to a location on an NTFS formatted volume, the browser automatically adds an alternate data stream (ADS)`Zone.Identifier`file for the downloaded file. It indicates that the file came from the Internet and informs Windows so. This behavior is common in generic NFSv3 implementations where Windows machines are NFS clients. This behavior doesn't occur in Linux by default, but if a File Storage file system is mounted in both Windows and Linux, the extra files can be seen in Linux.

Solution: To change this behavior:
- Log in to the Windows VM where File Storage is mounted.
- Open the Run window (Win + R) and enter`gpedit.msc`.
- Under User Configuration , select Administrative Templates , then select Windows Components .
- Select Attachment Manager .
- Select Do not preserve zone information in file attachments and choose Enabled .

To delete the`*.Zone.Identifier`files:
- Open the`cmd`command prompt window.
- 

Navigate to the directory where the files are found and run the following command:
```

```
