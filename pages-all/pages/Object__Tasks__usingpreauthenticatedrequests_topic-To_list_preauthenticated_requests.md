# Listing Object Storage Pre-Authenticated Requests
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_list_preauthenticated_requests.htm
- Fetched: 2026-09-05 02:52 CDT

# Listing Object Storage Pre-Authenticated Requests

View a list of the pre-authenticated requests in a bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_list_preauthenticated_requests.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_list_preauthenticated_requests.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_list_preauthenticated_requests.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Management and find the Pre-authenticated requests section.
All pre-authenticated requests are displayed in a table.
- To view the pre-authenticated requests in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the pre-authenticated requests in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a pre-authenticated request to open its details page, where you can view its status and perform other tasks.

To perform an action on a pre-authenticated request directly from the list table, select an available option from the Actions menu in the row for that pre-authenticated request:
- View pre-authenticated request details : Open the details page for the pre-authenticated request.
- Copy pre-authenticated request ID :[Copy the pre-authenticated request ID to the clipboard](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_copy_a_preauthenticated_request_ID.htm).
- Delete pre-authenticated request :[Delete the pre-authenticated request](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_delete_a_preauthenticated_request.htm).

To create a pre-authenticated request, select Create pre-authenticated request .
- 

Use the[oci os preauth-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/preauth-request/list.html)command and required parameters to list the pre-authenticated requests in a bucket:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListVcns](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/ListVcns)
