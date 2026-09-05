# Enabling Cross-Region Replication When Updating an Existing Volume Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume-group.htm
- Fetched: 2026-09-05 01:47 CDT

# Enabling Cross-Region Replication When Updating an Existing Volume Group

Use the steps described in this procedure to enable replication on an existing volume group. You can also enable replication when you create a volume.

For more information, see[Creating a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/create-volume-group.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume-group.htm#)
- 

- On the Volume Groups list page, select the volume group you want to work with. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/list-volume-group.htm).
- On the details page, select Edit .
- Select Next twice to display the Cross region replication section.
- In the Cross region replication section, move the Enable cross region replication slider to the right to enable cross-region replication.
- Select Confirm to acknowledge the cost warning.
- (Optional) Encrypt the data in this volume group by using your own encryption key. For more information, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr).
- Select Encrypt using customer-managed keys .
- Enter the encryption key OCID for the destination region.
Note  
  
The service doesn't support encrypting volumes with keys that are encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When you use your own keys, you must use keys that are encrypted using the Advanced Encryption Standard (AES) algorithm. This restriction applies to block volumes and boot volumes.
- Select Next twice to display the Summary section.
- 

Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/update.html)oci bv volume-group update`command and specify the`--volume-group-id`,`--volume-group-replicas '[{"displayName"`,`"availabilityDomain"`and`"xrrKmsKeyId"`parameters to enable cross-region replication for an existing volume group:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/UpdateVolumeGroup)UpdateVolumeGroup`operation and specify the`volumeGroupReplicas`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeGroupDetails)UpdateVolumeGroupDetails`
