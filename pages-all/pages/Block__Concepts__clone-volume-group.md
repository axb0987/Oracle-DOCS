# Cloning a Volume Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/clone-volume-group.htm
- Fetched: 2026-09-05 01:44 CDT

# Cloning a Volume Group

Clone a volume group in the Block Volume service.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/clone-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/clone-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/clone-volume-group.htm#)
- 

- On the Volume Groups list page, select the volume group you want to clone. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm).
- 

On the details page, select Clones .
- 

Select Create volume group clone .
- 

Select the compartment to create the volume group clone in.
- (Optional) Select the cluster placement group in which to clone the volume to.
Note  
  
This option is visible when cluster placement groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources. See[Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/clusterplacementgroups.htm).
- 

Enter a name for the new volume group clone.
- 

Select Create .
- 

Use the[oci bv volume-group create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/create.html)command and required parameters to clone a volume group from an existing volume group:

```

```

For example:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup)CreateVolumeGroup`operation and specify the`availabilityDomain`and`compartmentId`parameters in the[`CreateVolumeGroupDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeGroupDetails)
