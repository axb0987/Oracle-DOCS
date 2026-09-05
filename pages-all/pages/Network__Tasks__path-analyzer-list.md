# Listing Path Analysis Tests
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-list.htm
- Fetched: 2026-09-05 02:45 CDT

# Listing Path Analysis Tests

View a list of all path analysis tests in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-list.htm#)
- 

- Open the navigation menu and select Networking . Under Network Command Center , select Network Path Analyzer .
All saved path analysis tests are shown in tabular form.
- To view the path analysis tests in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the path analysis tests in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a path analysis test to open its details page, where you can view its status and perform other tasks.

To run the path analysis test, select Analyze .

Use the Actions button above the table to perform the following actions:
- Edit : See[Editing a Path Analysis Test](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path-analyzer-edit.htm#top)
- Move : See[Moving a Path Analysis Test to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-change-compartment.htm#top)
- Delete : See[Deleting a Path Analysis Test](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-deleting_test.htm#top)

To perform other actions on a path analysis test directly from the list table, you can also select any of the following options from the Actions menu (three dots) in the row for that VCN:
- View details : Open the details page for the path analysis test.
- Delete :[Deleting a Path Analysis Test](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-deleting_test.htm#top)
- Move resource :[Moving a Path Analysis Test to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-change-compartment.htm#top).
- Manage tags : Add one or more tags to the path analysis test. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Copy OCID : Copy the OCID of the path analysis test to the clipboard.
- 

Use the[path-analyzer-test list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vn-monitoring/path-analyzer-test/list.html)command and required parameters to list all path analysis tests in a compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListPathAnalyzerTests](https://docs.oracle.com/iaas/api/#/en/NetMonitor/latest/PathAnalyzerTestCollection/ListPathAnalyzerTests)
