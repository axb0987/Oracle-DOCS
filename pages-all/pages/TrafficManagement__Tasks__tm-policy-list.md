# Listing Steering Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm
- Fetched: 2026-09-05 03:07 CDT

# Listing Steering Policies

View a list of all Traffic Management steering policy attachments in a compartment.
See[Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/../Concepts/overview.htm)for a feature overview and more information about traffic management steering policies.

- [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#)
- 

- Open the navigation menu and select Networking . Under DNS management , select Traffic management steering policies .
- To view the policies in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the steering policies in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a steering policy to open its details page, where you can view its status and perform other tasks.

To create another steering policy, select Create traffic management steering policy .

To perform other actions on a steering policy directly from the list table, you can also select any of the following options from the Actions menu (three dots) in the row for that steering policy:
- Copy OCID : Copy the OCID of the steering policy to the clipboard.
- Move resource : See[Moving a Steering Policy Between Compartments](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-move.htm#top).
- Manage tags : Add one or more tags to the HTTP redirect. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete : See[Deleting a Steering Policy](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-delete.htm#top).
- 

Use the[steering-policy list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/list.html)command and required parameters to view a list of steering policies in a compartment.

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/ListSteeringPolicies)
