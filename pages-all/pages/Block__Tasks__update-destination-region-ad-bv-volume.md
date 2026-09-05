# Updating the Destination Region or Availability Domain Replication Settings for a Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-destination-region-ad-bv-volume.htm
- Fetched: 2026-09-05 01:47 CDT

# Updating the Destination Region or Availability Domain Replication Settings for a Block Volume

Learn how to update replication settings for an existing block volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-destination-region-ad-bv-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-destination-region-ad-bv-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-destination-region-ad-bv-volume.htm#)
- 

- 

On the Block Volumes list page, find the block volume that you want to edit. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- From the Actions menu (three dots) , select Edit .
- In the Edit block volume panel, turn off Enable cross ad/region replication (might be labeled Cross ad/region replication ).
- 

Select Confirm to acknowledge the replica deletion.
- 

Select Save changes .

After a few minutes, the volume's status changes from Updating... to Available .
- 

On the details page, select Edit .
- In the Edit block volume panel, turn on Enable cross ad/region replication (might be labeled Cross ad/region replication ).
- Select the target region for the replica.
- Select the availability domain for the replica.
- Enter a name for the replica.
- Select Confirm .
- (Optional) Encrypt the data in this volume by using your own encryption key. For more information, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr).
- Select Encrypt using customer-managed keys .
- Select the vault compartment and vault that contain the master encryption key you want to use.
- Select the master encryption key compartment and master encryption key.
Note  
  
The service doesn't support encrypting volumes with keys that are encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When you use your own keys, you must use keys that are encrypted using the Advanced Encryption Standard (AES) algorithm. This restriction applies to block volumes and boot volumes.
- 

Select Save changes .
- 

[re-enable cross-volume replication](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume.htm#cli). When you re-enable cross-region replication, specify the new availability domain you want to replicate to.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

[re-enable cross-region replication](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume.htm#api)
