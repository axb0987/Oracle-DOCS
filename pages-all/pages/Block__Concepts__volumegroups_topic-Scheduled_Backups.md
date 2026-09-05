# Managing Assigned Backup Policies for Volume Groups (Policy-Based Volume Group Backups)
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups_topic-Scheduled_Backups.htm
- Fetched: 2026-09-05 01:44 CDT

# Managing Assigned Backup Policies for Volume Groups (Policy-Based Volume Group Backups)

Schedule automated backups according to the volume group's assigned backup policy. The backup policy assigned to a volume group defines the frequency and schedule for backing up all volumes in the volume group.
Note  
  

- Oracle-defined backup policies aren't supported for scheduled volume group backups.
- For keys in cross-region operations, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/assign-encryption-key.htm#cust-key-xrr).

For more information about backups, see[Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/schedulingvolumebackups.htm).

## Tasks

- [Assigning a Backup Policy to a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-assign-to-group-bv-volume-backup-policy-assignment.htm)
- [Changing the Backup Policy Assigned to a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-change-assignment-to-group-bv-volume-backup-policy-assignment.htm)
- [Deleting a Backup Policy Assigned to a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-for-volume-group-bv-volume-backup-policy-assignment.htm)
- [Getting a Volume Group's Backup Assignment Policy Details](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-backup-policy-asset-assignment-bv-volume-backup-policy-assignment.htm)
- [Getting Details for a Specific Backup Policy Assignment](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-bv-volume-backup-policy-assignment.htm)

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

When a volume backup is created, the source volume's tags are automatically included. This also includes volumes with custom backup policies applied to create scheduled backups. Source volume tags are automatically assigned to all backups when they are created. You can also apply additional tags to volume backups as needed.
