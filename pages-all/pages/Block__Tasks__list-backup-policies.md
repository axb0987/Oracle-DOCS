# Listing Backup Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-backup-policies.htm
- Fetched: 2026-09-05 01:46 CDT

# Listing Backup Policies

List Oracle-based and user-defined backup policies in Block Volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-backup-policies.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-backup-policies.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-backup-policies.htm#)
- 

- Open the navigation menu and select Storage . Under Block Storage , select Backup Policies .

The Backup Policies list page opens. Oracle-based backup policies and any user-defined backup policies in the selected compartment are displayed in a table.
- To view the backup policies in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the backup policies in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a backup policy to open its details page, where you can view its status and perform other tasks.

To perform an action on a backup policy directly from the list table, select an available option from the Actions menu in the row for that backup policy:
- View details : Open the details page for the backup policy.
- Edit : Change the backup policy's name or cross-region copy target. See[Enabling Cross-region Copy for a User-defined Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-destinationregion-bv-volume-backup-policy.htm)and[Disabling Cross-region Copy for a User-defined Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-destinationregion-bv-volume-backup-policy.htm).
- Duplicate This Backup Policy :[Duplicate the backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-volume-backup-policy.htm).
- Copy OCID : Copy the OCID of the backup policy to the clipboard.
- Manage Tags : Add one or more tags to the backup policy. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete :[Delete the backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-schedule-bv-volume-backup-policy.htm).

To create a backup policy, select Create backup policy .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/list.html)oci bv volume-backup-policy list`command and specify the`--compartment-id`parameter to list the backup policies for a compartment in your tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/ListVolumeBackupPolicies)ListVolumeBackupPolicies`
