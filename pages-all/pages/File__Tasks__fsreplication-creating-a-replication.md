# Creating a Replication
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm
- Fetched: 2026-09-05 02:03 CDT

# Creating a Replication

Creating a File Storage replication resource automatically creates an associated replication target resource. Data is replicated from the source file system to the target file system at the interval you specify.

Tags applied to a replication resource are copied to the automatically created replication target resource.

Replicated data in the target file system has the same file and folder structure, snapshots, metadata, and permissions settings as the source file system. File system resource-specific data such as file locks, encryption keys, and tags aren't replicated.

Replications require an unexported target file system that you can replicate data to. For the requirements for target file systems, see[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm#limitations-and-considerations). You can choose to[create the target file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-file-system.htm)before you begin creating the replication, or you can create it along with the replication.
Tip  
  
Before creating a replication for a file system, you can[estimate how long the initial process will take](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-estimating-replication-time.htm).

The replication is created immediately. The first delta cycle starts as soon as the replication is active. The initial replication can take hours depending on the amount of data that's in the source file system.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Replications .
- Select Create replication .
- 

In the Create replication panel, provide the required information:
- Name : Enter a user-friendly name for the replication. You can change this name later. Avoid entering confidential information.
- Replication interval : Enter the replication interval in minutes. The replication interval determines the frequency of data replication. If you don't provide a value, the replication interval recommended by the[replication estimator](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-estimating-replication-time.htm)is used. If the replication estimator can't provide a recommendation, the replication uses the default value of 60 minutes. The minimum allowed value is 15 minutes.
- (Optional) To add tags to the replication, select Show tagging options .

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- In the Resource locks section, select a lock level:
- No Lock : No restrictions.
- Delete : Prevents the file system from being deleted.
- Full : Prevents all modifications except reading.
- 

In the Target file system section, select one of the following options:
- Use existing target file system : Enter the Target file system OCID of an unexported file system.
Tip  
  
If you have an existing file system that was used as the replication target for this source, and you never exported that target file system or created or deleted snapshots on the file system after deleting the replication resource, you can use that file system as a replication target again. This can avoid a full base copy.
- Create new target file system : Enter information for the new target file system. For details about individual fields, see[Creating a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-file-system.htm).
Note  
  
When creating a new target file system, you need to specify the Target region . For more information, see[Recommended Target Regions](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm#limitations-and-considerations__target-regions).
- To create the replication, select Create .
- (Optional) To save the configuration as a Resource Manager stack, select Save as stack . For more information, see[Managing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm).
- 

Use the[`fs replication create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/replication/create.html)command and required parameters to create a replication:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateReplication](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Replication/CreateReplication)operation to create a replication.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
