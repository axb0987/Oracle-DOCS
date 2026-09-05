# Updating the Destination Region or Availability Domain Replication Settings for a Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-destination-region-ad-bv-boot-volume.htm
- Fetched: 2026-09-05 01:47 CDT

# Updating the Destination Region or Availability Domain Replication Settings for a Boot Volume

To change the destination region or availability domain for cross-region replication you need to first turn cross-region replication off for a boot volume. Then specify the new region and availability domain selections when you turn cross-region replication on again.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-destination-region-ad-bv-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-destination-region-ad-bv-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-destination-region-ad-bv-boot-volume.htm#)
- 

- On the Boot Volumes list page, select the boot volume you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm).
- On the details page, select Edit .
- In the Cross region replication section, move the Enable cross ad/region replication slider to the left to disable cross-region replication.
- 

Select Check here to confirm to acknowledge the replica deletion.
- 

Select Save changes . After a few minutes, the volume's status will change from Updating... to Available .
- 

On the details page, select Edit .
- In the Cross region replication section, move the Enable cross ad/region replication slider to the right to enable cross-region replication.
- Select the target region for the replica.
- Select the availability domain for the replica.
- Enter a name for the replica.
- 

Select Confirm to acknowledge the replica deletion.
- Select Save changes .
- (Optional) Encrypt the data in this volume by using your own encryption key. For more information, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr).
- Select Encrypt using customer-managed keys .
- Enter the encryption key OCID for the destination region.
- 

Select Save changes .
- 

[re-enable cross-region replication](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-boot-volume.htm#cli)replication. When you re-enable cross-region replication, specify the new availability domain you want to replicate to

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

[Disable](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-boot-volume.htm)and[re-enable cross-region replication](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-boot-volume.htm)
