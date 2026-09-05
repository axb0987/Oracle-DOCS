# Listing Polices
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_get_a_list_of_your_policies.htm
- Fetched: 2026-09-05 02:26 CDT

# Listing Polices

List the policies in an IAM compartment.

Note  
  

If you use the name of a group, dynamic group, or compartment in a policy, the policy is mapped to the OCID of the group, dynamic group, or compartment when the policy is created. If the OCID of the group, dynamic group, or compartment changes, you must recompile one of the policies that applies to the group or compartment to update the OCID in all the policies.

To recompile the policy, open a policy, and make a small edit. Save the policy.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies .

The Policies page opens. All policies in the selected compartment are displayed in a table.
- To view policies in a different compartment, under List scope , select that compartment from the list.
- To decide which policies apply to a particular group, you must view the individual statements inside all your policies. There isn't a way to automatically obtain that information in the Console.

## Filtering List Results

Use filters to limit the policies in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a policies to open its details page, where you can view its status and perform other tasks.

To perform an action on a policy directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that policy:
- View details : Open the details page for the policy.
- Copy OCID : Copy the OCID of the policy to the clipboard.
- Manage tags : Add one or more tags to the policy. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete :[Deleting a Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_delete_a_policy.htm)
