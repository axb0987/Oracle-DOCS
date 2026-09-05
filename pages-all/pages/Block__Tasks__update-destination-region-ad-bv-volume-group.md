# Updating the Destination Region or Availability Domain Replication Settings for a Volume Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-destination-region-ad-bv-volume-group.htm
- Fetched: 2026-09-05 01:47 CDT

# Updating the Destination Region or Availability Domain Replication Settings for a Volume Group

To change the destination region or availability domain for cross-region replication you need to first turn cross-region replication off for a volume group. Then specify the new region and availability domain selections when you turn cross-region replication on again.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-destination-region-ad-bv-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-destination-region-ad-bv-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-destination-region-ad-bv-volume-group.htm#)
- 

- On the Volume Groups list page, select the volume group you want to work with. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/list-volume-group.htm).
- On the details page, select Edit .
- Select Next twice to display the Cross region replication section.
- In the Cross region replication section, move the Enable cross ad/region replication slider to the left to disable cross-region replication.
- Select Check here to confirm to acknowledge the that volume group replica will be deleted.
- (Optional) To turn off individual volume replication for each volume in the group, select Volume replication off .
- Select Next twice to display the Summary section.
- 

Select Save changes . After a few minutes, the volume group's status will change from Updating... to Available .
- On the details page, select Edit .
- Select Next twice to display the Cross region replication section.
- In the Cross region replication section, move the Enable cross ad/region replication slider to the right to enable cross-region replication.
- Select the target region for the replica.
- Select the availability domain for the replica.
- Enter a name for the replica.
- 

Optionally, encrypt the volume group replica in the destination region by using your own Vault encryption key. Select Encrypt using customer-managed keys for Cross region replication encryption , and then specify the OCID for a valid encryption key in the region you selected to replicate the volume group to. For more information, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr).
- 

Select Save changes .
- 

[re-enable](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume-group.htm#cli)cross-region replication for a volume group to change the destination or availability domain replication settings.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

[re-enable](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume-group.htm#api)
