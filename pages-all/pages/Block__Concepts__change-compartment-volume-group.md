# Moving a Volume Group to Another Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/change-compartment-volume-group.htm
- Fetched: 2026-09-05 01:44 CDT

# Moving a Volume Group to Another Compartment

Move a volume group in the Block Volume service to another compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/change-compartment-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/change-compartment-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/change-compartment-volume-group.htm#)
- 

- On the Volume Groups list page, find the volume group that you want to work with. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm).
- From the Actions menu (three dots) for the volume group, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci bv volume-group change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/change-compartment.html)command and specify the`--volume-group-id`and`--compartment-id`parameters to move a volume group to a different compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/ChangeVolumeGroupCompartment)ChangeVolumeGroupCompartment`operation and specify the`volumeGroupId`attribute in the request body and the`compartmentId`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/ChangeVolumeGroupCompartmentDetails)ChangeVolumeGroupCompartmentDetails`
