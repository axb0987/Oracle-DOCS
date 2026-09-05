# Activating a Volume Group Replica
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-activate-replica-bv-volume-group.htm
- Fetched: 2026-09-05 01:45 CDT

# Activating a Volume Group Replica

To create a new volume from a volume replica, you need to activate the replica. The activation process creates a new volume by cloning the replica.

Note  
  
For volumes in a volume group configured for replication, activate the volume group replica instead of individual volume replicas if you want to ensure that all volume replicas are activated from the same coordinated synchronization point. See[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-activate-replica-bv-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-activate-replica-bv-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-activate-replica-bv-volume-group.htm#)
- 

- On the Volume Group Replicas list page, find the volume group replica you want to work with. If you need help finding the list page or the volume group replica, see[Listing Volume Group Replicas](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-volume-group-replica.htm).
- From the Actions menu (three dots) , select Activate and then Confirm .
- In the Activate Volume Group Replica panel, enter the following information:
- Compartment : Compartment to create the clone of the source volume group in.
- Volume Group Name : Replica name.
- Select Activate .

The new volume group appears in the list, in the provisioning state.
- 

Use the[`oci bv volume-group create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/create.html)command and specify the`--source-details '{"type": "volumeGroupReplicaId", "volumeGroupReplicaId"`,`--compartment-id`and`--availability-domain`parameters to activate a volume group replica:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup)CreateVolumeGroup`operation and specify the`volumeGroupReplicas`attribute in the[`CreateVolumeGroupDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeGroupDetails)
