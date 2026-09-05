# Getting a Boot Volume's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-boot-volume.htm
- Fetched: 2026-09-05 01:46 CDT

# Getting a Boot Volume's Details

Get details about a boot volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-boot-volume.htm#)
- 

On the Boot Volumes list page, select the boot volume that you want. If you need help finding the list page or the boot volumes, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-bv-boot-volume.htm).

The details page opens.
Note  
  
If the volume lacks a recent backup or isn't configured for replication, then a message indicating this unprotected status appears on the details page.
Tip  
  
To list boot volume attachments, select Attached instances . If no instances are listed, either the boot volume was detached from the associated instance or the instance was terminated (while the boot volume was preserved).
- 

Use the[oci bv boot-volume get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/get.html)command and required parameters to get a boot volume:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/GetBootVolume)
