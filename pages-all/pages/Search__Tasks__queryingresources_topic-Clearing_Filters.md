# Clearing Resource Search Filters
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Clearing_Filters.htm
- Fetched: 2026-09-05 03:03 CDT

# Clearing Resource Search Filters

Clear one or more filters on a list of a resource search results to expand the list.
Note  
  
For the compartment filter, you can clear selections of individual compartments, but you can't remove the compartment filter from a search altogether. A search for resources always considers the compartment. Similarly, you can clear selections of individual regions, but you can't remove a region filter from a search altogether because a search always considers the region.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Clearing_Filters.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Clearing_Filters.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Clearing_Filters.htm#)
- 

These steps assume that you already filtered a list of resources results according to the instructions in[Filtering Resource Search Results](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Filtering_Results.htm).

- On the Resources page, next to Applied filters or Currently applied , select the X next to the resource types or resource attributes that you no longer want to use to filter search results.
- (Optional) To clear a value from a filter where you specified more than one value, next to Applied filters or Currently applied , select the filter name and either enter or find the value that you want to clear. Then, clear the checkbox next to the filter value that you no longer want to use to limit search results.
- When you're ready, select Apply filter .
- (Optional) Repeat the previous two steps for any other filters that specify more than one value.
- 

Use the[oci search resource structured-search](https://docs.oracle.com/iaas/tools/oci-cli/3.23.0/oci_cli_docs/cmdref/search/resource/structured-search.html)command and required parameters to clear filters from a search for resources:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). For information about the syntax for queries, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm).
- 

Run the[SearchResources operation to use structured query language to clear filters from a search for resources.

For information about query language syntax, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm). For information about a resource type, such as its attributes, see its reference page in the API Reference Guide. For the reference pages of resource types that have been indexed for Search, see[Supported Resources](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/queryoverview.htm#resourcetypes)
