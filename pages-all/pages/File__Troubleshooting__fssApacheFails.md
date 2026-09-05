# Apache Webserver Fails
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/fssApacheFails.htm
- Fetched: 2026-09-05 02:06 CDT

# Apache Webserver Fails

Learn how to troubleshoot File Storage and Apache webserver issues.

Symptom 1: When Apache webserver is installed on a File Storage file system, login to the web page fails and the Apache`error_log`contains messages like the following:

```

```

```

```

Additional Information:

Permission checks show sufficient read and execute access on the directory and the files. Providing full access (777 permission) to the file storage mount point for testing purposes also fails.
Caution  
  
The '777' permission is used strictly for testing purposes, and might compromise your security policy. Be sure to revert your file system mount point permissions to their previous state after testing is complete.

Cause: By default, the Apache webserver installation expects a local drive. You need to explicitly direct the installation to NFS.

Solution : Enable NFS compatibility for Apache.

Open a terminal on the instance and run:

```

```

Or:

```

```
