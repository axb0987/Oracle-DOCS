# Enabling Cross-Region Replication When Updating An Existing Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-boot-volume.htm
- Fetched: 2026-09-05 01:47 CDT

# Enabling Cross-Region Replication When Updating An Existing Boot Volume

Learn how to enable cross-region replication for an existing boot volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-boot-volume.htm#)
- 

Use the steps described in this procedure to enable replication on an existing boot volume.
- On the Boot Volumes list page, select the boot volume you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm).
- On the details page, select Edit .
- In the Cross/ad region replication section, move the Enable cross ad/region replication slider to the right to enable cross-region replication.
- Select the target region for the replica.
- Select the availability domain for the replica.
- Enter a name for the replica.
- Select Confirm to acknowledge the cost warning.
- (Optional) Encrypt the data in this volume by using your own encryption key. For more information, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr).
- Select Encrypt using customer-managed keys .
- Enter the encryption key OCID for the destination region.
- 

Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/update.html)oci bv boot-volume update`command and specify the`--boot-volume-id`,`--boot-volume-replicas`,`"displayName"`,`"availabilityDomain"`and`"xrrKmsKeyId"`parameters to enable cross-region replication when updating an existing boot volume:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume)UpdateVolume`operation and specify the`bootVolumeReplicas`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails)UpdateVolumeDetails`
