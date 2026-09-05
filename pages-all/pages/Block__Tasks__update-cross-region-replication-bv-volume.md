# Enabling Cross-Region Replication When Updating an Existing Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume.htm
- Fetched: 2026-09-05 01:47 CDT

# Enabling Cross-Region Replication When Updating an Existing Block Volume

Learn how to enable cross-region replication for an existing block volume

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume.htm#)
- 

Use the steps described in this procedure to enable replication on an existing volume. You can also enable replication when you create a volume, see[Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm).
- On the Block Volumes list page, select the volume you want enable cross-region replication for. If you need help finding the list page, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumes.htm).
- On the details page, select Edit .
- In the Cross/ad region replication section, move the Enable cross ad/region replication slider to the right to enable cross-region replication.
- Select the target region for the replica.
- Select the availability domain for the replica.
- Enter a name for the replica.
- Select Confirm to acknowledge the cost warning.
- 

Optionally, encrypt the volume replica in the destination region by using your own Vault encryption key. In the Cross ad/region replica encryption section, select Encrypt using customer-managed keys , and then specify the OCID for a valid encryption key in the region you selected to replicate the volume to. For more information, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr).
- 

Select Save changes .
- 

Use the[`oci bv volume update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/update.html)command and specify the`--volume-id`,`"displayName"`,`"availabilityDomain"`and`"xrrKmsKeyId"`parameters to enable cross-region replication when updating an existing block volume:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume)UpdateVolume`operation and specify the`blockVolumeReplicas`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails)UpdateVolumeDetails`
