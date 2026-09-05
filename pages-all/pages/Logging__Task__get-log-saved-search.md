# Getting a Log Saved Search's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-log-saved-search.htm
- Fetched: 2026-09-05 02:37 CDT

# Getting a Log Saved Search's Details

Get the details of a saved search in Logging.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-log-saved-search.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-log-saved-search.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-log-saved-search.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Saved Searches .
- Select the compartment that contains the saved search whose details you want to get.
- On the Saved Searches page, select the name of the saved search.

The saved search details page opens and displays general information about the log.

The Tags tab shows associated tags for the log, and you can add or edit tags.

The Latest Results tab shows log data. To filter this data, you can use the Search and Filter field.
- To view this saved search on the Search page directly, select Explore with Log Search .

The Search page opens with the saved search loaded, whether it's a basic or advanced search. You can perform more analysis and investigation related to this search directly on the Search page. For more information, see[Logging Search](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/searchinglogs.htm).

While on the Search page, you can also switch between any of the saved searches by selecting them from the Saved Searches list.
- 

Use the[oci logging log-saved-search get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log-saved-search/get.html)command and required parameters to get the details of a log saved search:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[GetLogSavedSearch](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogSavedSearch/GetLogSavedSearch)
