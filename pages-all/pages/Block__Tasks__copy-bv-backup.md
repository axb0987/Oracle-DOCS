# Copying a Volume Backup Between Regions
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-backup.htm
- Fetched: 2026-09-05 01:45 CDT

# Copying a Volume Backup Between Regions

Learn how to create a volume backup copy in a specific region.

These procedures apply to volume backups. For volume group backups, see[Copying a Volume Group Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-volume-group-backup.htm).

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The first two statements listed in the[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)policy lets the specified group do everything with block volumes and backups with the exception of copying volume backups across regions. The aggregate resource type`volume-family`does not include the`VOLUME_BACKUP_COPY`permission, so to enable copying volume backups across regions you need to ensure that you include the third statement in that policy, which is:

```

```

To restrict access to just creating and managing volume backups, including copying volume backups between regions, use the policy in[Let boot volume backup admins manage only backups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#boot-volume-backup-admins-manage-only-backups). The individual resource type`volume-backups`includes the`VOLUME_BACKUP_COPY`permission, so you do not need to specify it explicitly in this policy.

If you are copying volume backups encrypted using Vault between regions or you want the copied volume backup to use Vault for encryption in the destination region, you need to use a policy that allows the Block Volume service to perform cryptographic operations with keys in the destination region. For a sample policy showing this, see[Let Block Volume, Object Storage, File Storage, Kubernetes Engine, and Streaming services encrypt and decrypt volumes, volume backups, buckets, file systems, Kubernetes secrets, and stream pools](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#services-use-key).

### Restricting Access

The specific permissions needed to copy volume backups across regions are:
- Source region :`VOLUME_BACKUP_READ`,`VOLUME_BACKUP_COPY`
- Destination region :`VOLUME_BACKUP_CREATE`

### Sample Policies

[To restrict a group to specific source and destination regions for copying volume backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-backup.htm#)

In this example, the group is restricted to copying volume backups from the UK South (London) region to the Germany Central (Frankfurt) region.

```

```

[To restrict some source regions to specific destination regions while enabling all destination regions for other source regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-backup.htm#)

In this example, the following is enabled for the group:
- 

Manage volume backups in all regions.
- 

Copy volume backups from the US West (Phoenix) and US East (Ashburn) regions to any destination regions.
- 

Copy volume backups from the Germany Central (Frankfurt) and UK South (London) regions only to the Germany Central (Frankfurt) or UK South (London) regions.

```

```

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

## Steps

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-backup.htm#)
- 

- On the Block Volume Backups list page, find the block volume backup that you want to work with. If you need help finding the list page or the block volume backups, see[Listing Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-bv-backup.htm).
- From the Actions menu (three dots) , select Copy to Another Region .
- In the Copy block volume backup panel, enter the following values:

- Name : Backup name.
- Compartment : The compartment to copy the backup to.
- Region : The region to copy the backup to.
- Encryption : To use your own Vault encryption key, copy and paste in the OCID for the encryption key from the destination region.
- Select Copy block volume backup .
- Confirm that the source and destination region details are correct in the confirmation dialog and then select OK .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/backup/copy.html)oci bv backup copy`command and specify the`--destination-region`and`--volume-backup-id`parameters to copy a volume backup to the specified region:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/CopyVolumeBackup)CopyVolumeBackup`operation and specify the`volumeBackupId`attribtue in the request body and and`destinationRegion`attribute in the[`CopyVolumeBackupDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CopyVolumeBackupDetails)
