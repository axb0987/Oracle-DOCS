# Changing Resource Search Filters
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Changing_Filters.htm
- Fetched: 2026-09-05 03:03 CDT

# Changing Resource Search Filters

Change the filters applied to a list of resource search results to update the parameters of the search.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Changing_Filters.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Changing_Filters.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Changing_Filters.htm#)
- 

These steps assume that you already filtered a list of resources results according to the instructions in[Filtering Resource Search Results](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Filtering_Results.htm).

- On the Resources page, next to Applied filters or Currently applied , do one or more of the following:
- To add a value to a filter that you already included in the search, select the filter name, enter or find the value that you want to add, and then select the checkbox next to the value.
- To remove a filter value that you no longer want to include in the search, select the filter name, enter or find the value that you want to remove, and then clear the checkbox next to the value.
- When you're ready, select Apply filter .
- (Optional) Repeat the previous step for any other filters that you want to use to constrain search results.
- (Optional) If you have any resource types or resource attributes that you no longer want to use to filter search results altogether, next to Applied filters , select the X next to the filter name.
- (Optional) If you have new filters that you want to add, select the in-page search box (directly preceding the compartment scope and other filters), and then enter or find that filter that you want to add. If you need to specify a value for the filter, in the filter box, enter the value. Then, select Apply filter .
- 

Use the[oci search resource structured-search](https://docs.oracle.com/iaas/tools/oci-cli/3.23.0/oci_cli_docs/cmdref/search/resource/structured-search.html)command and required parameters to change filters during a search for resources:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). For information about the syntax for queries, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm).
- 

Run the[SearchResources operation to use structured query language to change filters during a search for resources.

For information about query language syntax, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm). For information about a resource type, such as its attributes, see its reference page in the API Reference Guide. For the reference pages of resource types that have been indexed for Search, see[Supported Resources](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/queryoverview.htm#resourcetypes)
