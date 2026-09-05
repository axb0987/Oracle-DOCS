# Getting a Block Volume's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume.htm
- Fetched: 2026-09-05 01:46 CDT

# Getting a Block Volume's Details

View a block volume's details.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume.htm#)
- 

On the Block Volumes list page, select the volume that you want. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
The details page opens, listing general information about the volume and links to its resources. Some items in the page are read-only, while other items allow you to edit and update the block volume's configuration.
Note  
  
If the volume lacks a recent backup or isn't configured for replication, then a message indicating this unprotected status appears on the details page.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/get.html)oci bv volume get`command and required parameters to get the details of a block volume:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/GetVolume)GetVolume`operation and specify the`volumeId`
