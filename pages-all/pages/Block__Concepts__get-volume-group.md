# Getting a Volume Group's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-group.htm
- Fetched: 2026-09-05 01:44 CDT

# Getting a Volume Group's Details

Get details for a volume group in the Block Volume service, including a list of the block volumes and boot volumes in the volume group.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-group.htm#)
- 

On the Volume Groups list page, select the volume group that you want. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Concepts/list-volume-group.htm).
To view the volume group's volumes, select Block volumes and Boot volumes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/get.html)oci bv volume-group get`command and required parameters to get details for a volume group:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/GetVolumeGroup)operation and specify the`volumeGroupId`
