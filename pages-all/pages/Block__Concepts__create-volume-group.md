# Creating a Volume Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-volume-group.htm
- Fetched: 2026-09-05 01:44 CDT

# Creating a Volume Group

Create a volume group in the Block Volume service.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-volume-group.htm#)
- 

On the Volume Groups list page, select Create volume group . If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Concepts/list-volume-group.htm).

## 1. Basic information

Enter the following values:
- Name : Enter a user-friendly name for the volume group. Avoid entering confidential information.
- Compartment : Select the compartment that you want to store the volume group in.
- Availability domain : Select the availability domain for the volume group.
- Show tagging options : Add one or more tags to the volume group. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.

Select Next .

## 2. Add volumes

Add each volume that you want to include in the group, changing compartments as needed. Optionally select the cluster placement group.

For both block volumes and boot volumes:
- You can't add a volume with an existing backup policy assignment to a volume group with a backup policy assignment. Remove the backup policy assignment from the volume before you add it to the volume group.
- If any of the volumes you add to the group are configured for replication, the destination region configured for them must match the destination region you configure for the volume group. See[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations).

Select Next .

## 3. Cross region replication

- (Optional) To enable asynchronous[cross region replication](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)for the volume group, enter the following information.
- Turn on Enable cross ad/region replication .
- Select Confirm to confirm replication.
- Select the target region and availability domain.
- (Optional) Update the name for the volume group replica.

If any of the volumes you add to the group are configured for replication, the destination region configured for them must match the destination region you configure for the volume group. See[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations).
- (Optional) To encrypt the data in this replica using[your own encryption key](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/assign-encryption-key.htm#cust-key-xrr), enter the following information.
- Select Encrypt using customer-managed keys .
- Enter the OCID for the encryption key in the destination region.
Note  
  
The service doesn't support encrypting volumes with keys that are encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When you use your own keys, you must use keys that are encrypted using the Advanced Encryption Standard (AES) algorithm. This restriction applies to block volumes and boot volumes.

Select Next .

## 4. Backup policies

Select a backup policy to configure schedule backups for the volume group.

For more information, see[Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/schedulingvolumebackups.htm).
Note  
  
If you select a backup policy enabled for cross region backup copies, then you can encrypt the volume group backup copy in the destination region with your own Vault encryption key. For more information, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/assign-encryption-key.htm#cust-key-xrr)and[Managing Assigned Backup Policies for Volume Groups (Policy-Based Volume Group Backups)](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups_topic-Scheduled_Backups.htm).

Select Next .

## 5. Summary

Review the information to confirm that it's correct. If you need to revise a value, select Edit and change the values as needed.

Select Create . The creation process begins and its progress is displayed. You can cancel the creation at any time.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/create.html)oci bv volume-group create`command and required parameters to create a volume group from existing volumes:

```

```

Volume lifecycle status must be`AVAILABLE`to add it to a volume group.

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup)CreateVolumeGroup`operation and specify the`availabilityDomain`and`compartmentId`attributes in the[`CreateVolumeDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeGroupDetails)
