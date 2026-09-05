# Restoring a Volume Group from a Volume Group Backup
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-volume-group.htm
- Fetched: 2026-09-05 01:46 CDT

# Restoring a Volume Group from a Volume Group Backup

Learn how to restore a volume group from a volume group backup.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-volume-group.htm#)
- 

- On the Volume Group Backups list page, select the volume group backup that you want. If you need help finding the list page or the volume group backups, see[Listing Volume Group Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-bv-volume-group-backup.htm).
- From the Actions menu (three dots) for the volume group backup, select Restore volume group .
- Fill in the required volume information:

- Name : A user-friendly name or description. Avoid entering confidential information.
- Compartment : The compartment for the volume group.
- Availability Domain : The availability domain for the volume group.
- Cluster Placement Group : (Optional) Select the cluster placement group in which to restore the volume group to.
Note  
  
This option is visible when cluster placement groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources. See[Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/clusterplacementgroups.htm).
- Optionally:
- Add tags.
- Enable cross-region replication.
- Select a backup policy.
- Select Restore .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/create.html)oci bv volume-group create`command and specify the`--compartment-id`,`--availability-domain`,`--source-details`parameters to restore a volume group a volume group backup:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`CreateVolumeGroup`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup)operation and specify the`compartmentId`,`availabilityDomain`and`sourceDetails`attributes of the[`CreateVolumeGroupDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeGroupDetails)
