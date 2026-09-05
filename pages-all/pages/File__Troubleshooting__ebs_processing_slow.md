# Oracle E-Business Suite Concurrent Processing is Slow
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/ebs_processing_slow.htm
- Fetched: 2026-09-05 02:05 CDT

# Oracle E-Business Suite Concurrent Processing is Slow

On an Oracle E-business Suite (EBS) system that uses File Storage for shared applications, the application performs slowly.

Symptoms might include, but aren't limited to:
- EBS concurrent requests take a longer time to complete, or never complete
- The EBS application is slow
- Commands take increased time or hang in instances
- High server load in instances

Cause: Running`ls`,`find`,`du`, or`rsync`directly or indirectly on large directories using the command line or scripts at an operating system or application level. These directory scanning operations are expensive for File Storage. As directory sizes increase, the operations take more time to complete, which impacts the performance of applications.

Solution: Verify the size of the concurrent processing`log`and`out`directories by running the following commands:
```

```

```

```

If these directories contain over 100,000 files, cancel any`ls`,`find`,`du`, or`rsync`jobs. Always keep the directory size smaller than 100,000 files. If there are other large folders in the file system, and concurrent processing is dependent on such folders, consider reducing their size.

Use the`APPLLDM`storage scheme, which implements a subdirectory structure to store concurrent processing files and limits directory sizes. See[Sharing the Application Tier File System in Oracle E-Business Suite Release 12.2 or 12.1.3 Using the Oracle Cloud Infrastructure File Storage Service](https://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/compute-iaas/sharing_app_tier_file_system_ebs_fss/24fss.html)
