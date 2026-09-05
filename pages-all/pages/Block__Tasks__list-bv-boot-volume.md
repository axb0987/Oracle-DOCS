# Listing Boot Volumes
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm
- Fetched: 2026-09-05 01:46 CDT

# Listing Boot Volumes

Learn how list all boot volumes in a specific compartment, or detailed information for a single boot volume.

A boot volume is created when you[create an instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm). For more information about boot volumes, see[Working with Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/bootvolumes.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm#)
- 

- Open the navigation menu and select Storage . Under Block Storage , select Block Volumes . In the Block Storage menu on the sidebar, select Boot Volumes .

The Boot Volumes list page opens. All boot volumes in the selected compartment are displayed in a table.
- To view the boot volumes in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the boot volumes in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a boot volume to open its details page, where you can view its status and perform other tasks.

To perform an action on a boot volume directly from the list table, select an available option from the Actions menu in the row for that boot volume:
- View details : Open the details page for the boot volume.
- Edit : Edit the boot volume.
- Create Instance :[Start the Create instance workflow](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
- Create Clone :[Clone the boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-clone-bv-boot-volume.htm).
- Create Manual Backup :[Manually back up the boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-boot-volume-backup.htm).
- Assign master encryption key : Assign a master encryption key to the boot volume. See[Changing the Assigned Master Encryption Key](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm).
- Move resource : Move the boot volume to another compartment.
- Copy OCID : Copy the OCID of the boot volume to the clipboard.
- Manage Tags : Add one or more tags to the boot volume. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Terminate :[Delete the boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-boot-volume.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/list.html)oci bv boot-volume list`command and specify the`--availabilty-domain`and`--compartment-id`parameters to view the boot volumes in that availability domain and compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListBootVolumes](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/ListBootVolumes)operation and specify the`availabilityDomain`and`compartmentId`
