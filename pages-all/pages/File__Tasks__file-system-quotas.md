# File System Quotas
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/file-system-quotas.htm
- Fetched: 2026-09-05 02:03 CDT

# File System Quotas

Quotas help control costs by limiting the capacity that individual users or groups can consume in a file system or by limiting the total consumption of a file system.

## Quota Types

Administrators can set three types of quotas on a file system:
- File system quota: the overall file system quota limits storage consumption for the file system. A file system can't grow beyond its specified limit, even if users or groups using that file system haven't exceeded their quota.
- User quotas: user quotas are tied to a specific UNIX principal designated by UID.
- Group quotas: group quotas are tied to a specific UNIX principal and designated by GID.

Administrators can set default quota rules to limit storage for all users and all groups for any file system. When you create default quotas, you don't have to define the quota limits for every user or group.

Explicit limits for individual users or groups can be larger or smaller than the default. Explicit individual limits override any default quotas for that user or group.

Any user can be subject to three quotas at the same time: user, group, and file system. The minimum quota is always used first. For example, the user might be 32 GB under their user quota, but only 10 GB under the group quota. In this case, they couldn't write a 24 GB file.

A soft quota acts as a warning threshold. A soft quota doesn't stop new writes, but it can be used to understand the users or groups who are reaching the limits. When a user or group reaches the hard quota , any new writes are prevented until they free up space or the applicable quota is increased.

File system quotas differ from compartment quotas. For example, file system quotas ensure that the live usage for a file system stays within configured limits, while a compartment quota ensures that metered usage is within configured limits. Also, file system quotas don't include space taken up by snapshots but compartment quotas do include space taken up by snapshots. For more information about compartment quotas, see[Overview of Compartment Quotas](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../../Quotas/Concepts/resourcequotas.htm#top).

Note  
  
Administrators can[enable or disable quotas for the file system on demand](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-enable.htm)without the need to reconfigure all existing quotas. Quotas aren't enforced until the file system's quota state changes to Enabled .

Quota Type Details
File system quota Limits the size of the file system. The total consumption of the file system can't exceed this limit.
Default user quota This limit is automatically applied to all users accessing the file system. You don't need to create separate quotas for each user. You can specify both soft and hard limits.
Default group quota This limit is automatically applied to all groups accessing the file system. You don't need to create separate quotas for each group. You can specify both soft and hard limits.
Individual user quota This limit applies to an individual user accessing the file system and overrides the default user quota. Users are specified by their UNIX user ID (UID). You can specify both soft and hard limits.
Individual group quota This limit applies to a single group accessing the file system and overrides the default group quota. The total consumption for a group is measured by the total size of the file system objects (files and directories) owned by that group. Groups are specified by their UNIX group ID (GID). You can specify both soft and hard limits.

## Monitoring Quotas

Administrators can[list users and groups and their usage and quotas](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-list.htm)or use[metrics](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Reference/filemetrics.htm)and events to monitor requests that exceed quotas.

File system[logs](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/logging.htm)track quota management history.

When quota enforcement is enabled on the file system,`du`reflects the file system quota limit as`total`and usage as`Used`and also in`du --exclude=.snapshot <FSS_mountpoint>`

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users create, manage, and delete file systems](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#general-file-system-management)allows users to manage file systems, including quotas.

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Limitations and Considerations

Consider the following when working with quotas:
- File systems with enabled quotas might experience impacts to performance. Impact depends on many factors, but primary factors include:
- The number of active, simultaneous file system users
- If the user or group is near the quota limit
- If the file system is exported through multiple mount targets
- It might take up to one hour after quotas are initially enabled for a file system for enforcement to take place.
- Usage on file systems isn't tracked unless quotas are enabled for that file system. If quotas are disabled, the usage reported[when listing quotas](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-list.htm)is zero (0). Reported quota usage is only correct when enforcement is enabled.
- The minimum quota size is 10 GB, specified with a minimum granularity of 1 GB. A quota of 0 GB means that the principal can't write to the file system.
- The margin of error for a quota is 64 K.
- Any write that would push the user over the limit is rejected with an`NFS_QUOTA`error. If a user is 10 GB under their limit, and they try to write 32 GB to a file, the write is rejected. Partial writes aren't supported. If the user tries an 8 GB write, it succeeds.
- Quotas enforce data usage, not metadata usage. Even if a user has reached their hard quota, they can still create empty files and directories.
- Snapshots don't count against quotas.
- Cloned and replicated file systems inherit parent and source quotas, but those quotas are disabled by default and must be explicitly[enabled](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-enable.htm).
- Individual user and group quotas are specified by UNIX ID or GID. Integration with LDAP, Active Directory, or Oracle Cloud Infrastructure Identity and Access Management isn't supported. Without integration with an external common identity store, File Storage can't enforce that the client-presented User ID maps to the same actual user across all clients. If business processes or security postures requires this consistency, you must enforce it.
- File Storage quotas operate differently than the Linux native file quota. For example, Linux quotas include grace periods, which aren't supported by File Storage. Commands such as`edquota`and`repquota`aren't supported.
- Only one quota rule can be updated at a time. Bulk edits of individual user or group quotas aren't supported.
-
