# Listing HTTP Redirects
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-list.htm
- Fetched: 2026-09-05 01:59 CDT

# Listing HTTP Redirects

View a list of all HTTP redirects in a compartment.

See[HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/httpredirect.htm)for a feature overview and more information.

For general service information, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-list.htm#)
- 

- Open the navigation menu and select Networking . Under DNS management , select HTTP redirects .

The HTTP redirects list page opens. All HTTP redirects in the selected compartment are displayed in a table.
- To view the HTTP redirects in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the HTTP redirects in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a HTTP redirect to open its details page, where you can view its status and perform other tasks.

To create another HTTP redirect, select Create HTTP Redirect .

To perform other actions on an HTTP redirect directly from the list table, you can also select any of the following options from the Actions menu (three dots) in the row for that HTTP redirect:
- View details : Open the details page for the HTTP redirect.
- Copy OCID : Copy the OCID of the HTTP redirect to the clipboard.
- Move resource : See[Moving an HTTP Redirect Between Compartments](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-move-compartment.htm).
- Manage tags : Add one or more tags to the HTTP redirect. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Open support request : See[Creating a Support Request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm).
- Delete : See[Deleting an HTTP Redirect](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-delete.htm).
- 

Use the[http-redirect list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/http-redirect/list.html)command and required parameters to list all HTTP redirects in a compartment:
```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListHttpRedirects](https://docs.oracle.com/iaas/api/#/en/waas/latest/HttpRedirect/ListHttpRedirects)
