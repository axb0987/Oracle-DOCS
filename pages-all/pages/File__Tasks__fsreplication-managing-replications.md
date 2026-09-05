# Managing Replications
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-managing-replications.htm
- Fetched: 2026-09-05 02:03 CDT

# Managing Replications

Learn about File Storage replication components and how to manage them.

Replications consist of two parts:
- Replication resource: This is the control component. It contains all of the necessary configuration information for the replication operation. The replication resource is attached to the source file system, and captures data updates by creating a replication snapshot. Then, the replication snapshot is transmitted to the replication target.
- Replication target resource: This component is attached to the target file system. It receives the replication snapshot from the replication resource, and writes the data to the target file system.

## Replication Resource Details

For more information, see[Getting a Replication's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-details.htm).

- OCID: Every Oracle Cloud Infrastructure resource has an Oracle-assigned unique ID called an Oracle Cloud Identifier (OCID). See[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
- Created: The date and time the replication resource was created.
- Compartment: The compartment the replication resides in. For more information, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).
- Availability Domain: The availability domain that the replication resides in. The replication is always in the same availability domain as the source file system. For more information, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
- Source File System: A name link to the replication's source file system.
- Replication Target OCID: The OCID for the replication target associated with the replication resource.
- Target File System OCID: The OCID for the target file system associated with the replication resource.
- Delta Status: The current status of the latest replication snapshot:
- Idle: The replication is not capturing or applying data.
- Capturing: The replication is capturing differentiated data in the source snapshot.
- Transferring: The replication is both capturing and committing snapshot data.
- Applying: The replication is committing the snapshot data to the target file system.
- Service Error: The replication encountered a recoverable error in the File Storage service.
- User Error: The replication encountered an error that requires user intervention to correct.
- Failed: The replication encountered a nonrecoverable error.
- Replication Interval in Minutes: The frequency of the replication operation.
- Replication Progress: The current progress of the replication while applying data to the target file system. Shown as a percentage of complete.
- Last Snapshot: A link to the last successfully captured and applied replication snapshot. The link text is composed of that snapshot's suffix, which corresponds to the date and time it was created.
- Recovery Point Time: The date and time of the last successful data replication.

## Replication Target Details

For more information, see[Getting a Replication Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-target-details.htm).

- OCID: Every Oracle Cloud Infrastructure resource has an Oracle-assigned unique ID called an Oracle Cloud Identifier (OCID). See[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
- Created: The date and time the replication target was created.
- Compartment: The compartment the replication target resides in. For more information, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).
- Availability Domain: The availability domain that the replication target resides in. The replication target is always in the same availability domain as the target file system. For more information, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
- Target File System: A name link to the replication target's target file system.
- Replication OCID: The OCID for the replication resource associated with the replication target.
- Source File System OCID: The OCID for the source file system associated with the replication resource.
- Delta Status: The current status of the latest replication snapshot:
- Idle: The replication is not capturing or applying data.
- Capturing: The replication is capturing differentiated data in the source snapshot.
- Transferring: The replication is both capturing and committing snapshot data.
- Applying: The replication is committing the snapshot data to the target file system.
- Service Error: The replication encountered a recoverable error in the file storage service.
- User Error: The replication encountered an error that requires user intervention to correct.
- Failed: The replication encountered a nonrecoverable error.
- Replication Progress: The current progress of the replication while applying data to the target file system. Shown as a percentage of complete.
- Last Snapshot: A link to the last successfully captured and applied replication snapshot. The link text is composed of that snapshot's suffix, which corresponds to the date and time it was created.
- Recovery Point Time: The date and time of the last successful data replication.

## Next Steps

- [Listing Replications](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-replications.htm)
- [Listing Replication Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-replication-targets.htm)
- [Getting a Replication's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-details.htm)
- [Getting a Replication Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-target-details.htm)
- [Editing a Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-replication.htm)
- [Locking a Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-replication.htm)
- [Deleting a Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm)
- [Deleting a Replication Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication-target.htm)
- [Using Replication for Disaster Recovery](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-disaster-recovery.htm)
- [Using Replication for Data Transfer](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-copy-data.htm)

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users create, manage, and delete file systems](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#general-file-system-management)allows users to manage file systems and replications.

A more restrictive policy that only allows management of replications:
```

```

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)
