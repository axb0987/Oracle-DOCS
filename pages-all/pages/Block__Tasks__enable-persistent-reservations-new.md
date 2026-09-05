# Enabling Persistent Reservations for a New Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enable-persistent-reservations-new.htm
- Fetched: 2026-09-05 01:46 CDT

# Enabling Persistent Reservations for a New Volume

Enable persistent reservations for a new volume in the Block Volume service. You can enable persistent reservations when you create a new volume, clone an existing volume, restore a volume from a backup, or activate a volume replica. Persistent reservations is disabled by default.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enable-persistent-reservations-new.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enable-persistent-reservations-new.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enable-persistent-reservations-new.htm#)
- 

See[Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html)oci bv volume create`command and required parameters to create the volume. Set the`--is-reservations-enabled`parameter to`true`to enable persistent reservations.
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume)CreateVolume`operation to update a volume and specify the`isReservationsEnabled`attribute of`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/CreateVolumeDetails)CreateVolumeDetails`to`true`
