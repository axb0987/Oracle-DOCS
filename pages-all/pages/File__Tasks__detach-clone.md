# Detaching a Clone
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/detach-clone.htm
- Fetched: 2026-09-05 02:03 CDT

# Detaching a Clone

Detach a File Storage clone from its parent file system.

When you detach a clone from its parent file system, any shared data on the parent file system is copied to the clone.

Because detaching a clone requires copying data, the process isn't instant. The detachment operation runs in the background and you can continue to use the file system as it's detaching. Use the file system's Clone attached status to monitor the status of the detach operation. After the detachment completes, no data is shared between the two file systems. This can result in increased disk usage on the cloned file system. For more information, see[Metering and Billing](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/cloningFS.htm#Metering_and_Billing).

Only certain clones can be detached, for more information, see[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/cloningFS.htm#Limitations_and_Considerations__detach).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/detach-clone.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/detach-clone.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/detach-clone.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Clones , select the clone you want to detach, and then select Detach .
- In the Detach file system dialog box, select Detach .
- 

Use the[`fs file-system detach`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/detach.html)command and required parameters to detach a clone from its parent file system:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DetachClone](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/DetachClone)operation with required parameters to detach a cloned a file system from its parent.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
