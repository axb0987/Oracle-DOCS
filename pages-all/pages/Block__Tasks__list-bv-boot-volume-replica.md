# Listing Boot Volume Replicas
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-replica.htm
- Fetched: 2026-09-05 01:46 CDT

# Listing Boot Volume Replicas

Learn how to list the boot volume replicas in a specified compartment and availability domain.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-replica.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-replica.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-replica.htm#)
- 

- Open the navigation menu and select Storage . Under Block Storage , select Block Volumes . In the Block Storage menu on the sidebar, select Boot Volume Replicas .

The Boot Volume Replicas list page opens. All boot volume replicas in the selected compartment are displayed in a table.
- To view the boot volume replicas in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the boot volume replicas in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a boot volume replica to open its details page, where you can view its status and perform other tasks.

To perform an action on a boot volume replica directly from the list table, select an available option from the Actions menu in the row for that boot volume replica:
- View details : Open the details page for the boot volume replica.
- Activate :[Activate the boot volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-activate-replica-bv-boot-volume.htm).
- Copy OCID : Copy the OCID of the boot volume replica to the clipboard.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume-replica/list.html)oci bv boot-volume-replica list`command and specify the`--availability-domain`and`compartment-id`parameters to list the boot volume replicas in a specified compartment and availability domain.

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeReplica/ListBootVolumeReplicas)ListBootVolumeReplicas`operation to and specify the`availabilityDomain`and`compartmentId`
