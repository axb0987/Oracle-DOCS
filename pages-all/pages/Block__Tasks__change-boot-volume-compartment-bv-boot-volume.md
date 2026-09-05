# Moving a Boot Volume to Another Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-boot-volume-compartment-bv-boot-volume.htm
- Fetched: 2026-09-05 01:45 CDT

# Moving a Boot Volume to Another Compartment

Move a boot volume in the Block Volume service to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-boot-volume-compartment-bv-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-boot-volume-compartment-bv-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-boot-volume-compartment-bv-boot-volume.htm#)
- 

- On the Boot Volumes list page, find the boot volume that you want to work with. If you need help finding the list page or the boot volumes, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-bv-boot-volume.htm).
- From the Actions menu (three dots) for the boot volume, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[`oci bv boot-volume change-boot-volume-compartment`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/change-compartment.html)command and specify the`--boot-volume-id`and`--compartment-id`parameters to move the boot volume to a different compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`ChangeBootVolumeCompartment`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/ChangeBootVolumeCompartment)operation and specify the`bootVolumeId`attribute in the request body and the`compartmentId`attribute in the[`ChangeBootVolumeCompartmentDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/ChangeBootVolumeCompartmentDetails)
