# Moving a Block Volume to Another Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changecompartmentblockvolume.htm
- Fetched: 2026-09-05 01:45 CDT

# Moving a Block Volume to Another Compartment

Move a block volume in the Block Volume service to a different compartment.

When you move a block volume to a new compartment, associated Block Volume resources, such as volume backups, volume clones, and volume replicas aren't moved. After you move the block volume to the new compartment, inherent policies apply immediately and affect access to the block volume through the Console. For more information, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).
Important  
  
When you move a block volume between compartments, ensure that users have sufficient access permissions on the compartment the block volume is being moved to.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changecompartmentblockvolume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changecompartmentblockvolume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changecompartmentblockvolume.htm#)
- 

- On the Block Volumes list page, find the volume that you want to work with. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- From the Actions menu (three dots) , select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[`oci bv volume change-compartment`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/change-compartment.html)command and specify the`--compartment-id`and`--volume-id`parameters to move a block volume to a different compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeVolumeCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/ChangeVolumeCompartment)operation and specify the`volumeId`attribute in the request body and the`comparmentId`attribute in the[ChangeVolumeCompartmentDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/ChangeVolumeCompartmentDetails)
