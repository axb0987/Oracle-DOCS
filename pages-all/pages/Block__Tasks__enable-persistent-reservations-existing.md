# Enabling Persistent Reservations for an Existing Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enable-persistent-reservations-existing.htm
- Fetched: 2026-09-05 01:46 CDT

# Enabling Persistent Reservations for an Existing Volume

Enable persistent reservations for an existing volume in the Block Volume service. Persistent reservations is disabled by default.
Prerequisites: Before enabling persistent reservations, ensure that the volume is detached and in the`AVAILABLE`state. For instructions to detach a volume, see[Detaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enable-persistent-reservations-existing.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enable-persistent-reservations-existing.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enable-persistent-reservations-existing.htm#)
- 

- On the Block Volumes list page, find the volume that you want to work with. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- From the Actions menu (three dots) , select Edit .
The Edit block volume panel opens.
- Turn on Enable reservations .
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/update.html)oci bv volume update`command and required parameters to update the volume. Set the`--is-reservations-enabled`parameter to`true`to enable persistent reservations.
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume)UpdateVolume`operation to update a volume and specify the`isReservationsEnabled`attribute of`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails)UpdateVolumeDetails`to`true`
