# Viewing Recommendation History
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/history.htm
- Fetched: 2026-09-05 01:48 CDT

# Viewing Recommendation History

This section of Implementing Recommendations describes the history table and how to view the recommendation status changes that it contains.

- [Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/history.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/history.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/history.htm#)
- 

- Open the navigation menu and select Governance &amp; Administration . Under Cloud Advisor , select History .
This page tracks recommendation status changes. For example, it lists information about recommendations that have been implemented, postponed, and dismissed.
- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table.
- Optionally change the order of the items in the list table by using the sort icons next to the column names.

Tip  
  
For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).
- 

Use the[oci optimizer history-summary list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/history-summary/list.html)command to list user changes to recommendations.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/).
- 

Use the[ListHistories](https://docs.oracle.com/iaas/api/#/en/advisor/latest/HistorySummary/ListHistories)
