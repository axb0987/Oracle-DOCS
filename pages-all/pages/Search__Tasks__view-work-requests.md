# Viewing Work Requests
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/view-work-requests.htm
- Fetched: 2026-09-05 03:03 CDT

# Viewing Work Requests

View work requests to see the current status of in-progress long-running, asynchronous operations associated with selected resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/view-work-requests.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/view-work-requests.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/view-work-requests.htm#)
- 

These steps assume that you already have resource results. You got resource results by doing one of the following:
- You accessed a resource collection from the home page or according to the instructions in[Getting a Resource Collection's Details](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/get-resource-collection.htm).
- You performed a free text search and selected the Resources category of results according to the instructions in[Performing a Free Text Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_perform_a_free_text_search.htm)
- You ran an advanced resource query according to the instructions in[Running a Custom, Free-Form Query](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_custom_freeform_query_to_find_a_resource.htm).

- (Optional) To further refine the list of resources for which you want to perform bulk actions, select the checkbox next to the resource name in the list of resource results.
- Select Actions .
- Select View work requests .
The Console displays any work requests associated with the selected resources.
- 

Use the[list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/work-request/list.html)command and required parameters to view work requests:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListWorkRequests](https://docs.oracle.com/iaas/api/#/en/identity/latest/WorkRequestSummary/ListWorkRequests)
