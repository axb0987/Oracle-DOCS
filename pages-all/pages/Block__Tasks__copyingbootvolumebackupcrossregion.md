# Copying a Boot Volume Backup Between Regions
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingbootvolumebackupcrossregion.htm
- Fetched: 2026-09-05 01:45 CDT

# Copying a Boot Volume Backup Between Regions

You can copy boot volume backups from one region to another region using the Oracle Cloud Infrastructure Block Volume service.

For more information, see[Copying Boot Volume Backups Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/bootvolumebackups.htm#Copying).
Note  
  

Limitations for Copying Boot Volume Backups Across Regions

When copying boot volume backups across regions in your tenancy, you can only copy one backup per boot volume at a time from a specific source region.

You can only copy boot volume backups for instances created from[platform image](https://docs.oracle.com/iaas/Content/Compute/References/images.htm), or custom images built from platform images. If you try to copy a boot volume for an instance based on other image types, such as Marketplace images, the request will fail with an error.

You cannot add compatible shapes in the destination region for boot volume backups, the shape compatibility list is from the source region and cannot be changed.

When you create an instance from the Console and specify a boot volume backup that was copied from another region as the image source, you may encounter a message indicating that there was an error loading the source image. You can ignore this error message and select Create Instance to finish the instance creation process and launch the instance.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The first two statements listed in the[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)policy lets the specified group do everything with boot volumes and boot volume backups with the exception of copying boot volume backups across regions. The aggregate resource type`volume-family`does not include the`BOOT_VOLUME_BACKUP_COPY`permission, so to enable copying boot volume backups across regions you need to ensure that you include the third statement in that policy, which is:

```

```

To restrict access to just creating and managing boot volume backups, including copying boot volume backups between regions, use the policy in[Let boot volume backup admins manage only backups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#boot-volume-backup-admins-manage-only-backups). The individual resource type`boot-volume-backups`includes the`BOOT_VOLUME_BACKUP_COPY`permission, so you do not need to specify it explicitly in this policy.

If you are copying volume backups encrypted using Vault between regions or you want the copied volume backup to use Vault for encryption in the destination region, you need to use a policy that allows the Block Volume service to perform cryptographic operations with keys in the destination region. For a sample policy showing this, see[Let Block Volume, Object Storage, File Storage, Kubernetes Engine, and Streaming services encrypt and decrypt volumes, volume backups, buckets, file systems, Kubernetes secrets, and stream pools](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#services-use-key).

### Restricting Access

The specific permissions needed to copy volume backups across regions are:
- Source region :`BOOT_VOLUME_BACKUP_READ`,`BOOT_VOLUME_BACKUP_COPY`
- Destination region :`BOOT_VOLUME_BACKUP_CREATE`

[To restrict a group to specific source and destination regions for copying volume backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingbootvolumebackupcrossregion.htm#)

In this example, the group is restricted to copying volume backups from the UK South (London) region to the Germany Central (Frankfurt) region.

```

```

[To restrict some source regions to specific destination regions while enabling all destination regions for other source regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingbootvolumebackupcrossregion.htm#)

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

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingbootvolumebackupcrossregion.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingbootvolumebackupcrossregion.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingbootvolumebackupcrossregion.htm#)
- 

- In the Boot Volume Backups list page, find the boot volume you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-backup.htm).
- From the Actions menu (three dots) , select Copy to Another Region .
- In the Copy boot volume backup panel, enter the following information.
- Name : Enter a name for the backup. Avoid entering confidential information.
- Compartment : Select the compartment to copy the backup to.
- Destination Region : Select the region to copy the backup to.
- Encryption : Select the type of encryption that you want. If you select the option to use your own key, paste the OCID for encryption key from the destination region.
- 

Select Copy Boot Volume Backup .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume-backup/copy.html)oci bv boot-volume-backup copy`command and specify the`boot-volume-backup-id`and`--destination-region`parameters to copy a boot volume backup to a different region:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CopyBootVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup/CopyBootVolumeBackup)operation to copy a boot volume backup to a different region.

## Next Steps

After copying the boot volume backup, switch to the destination region in the Console and verify that the copied backup appears in the list of boot volume backups for that region. You can then restore the backup using the steps in[Restoring a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-boot-volume-backup.htm).

For more information about backups, see[Boot Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/bootvolumebackups.htm)
