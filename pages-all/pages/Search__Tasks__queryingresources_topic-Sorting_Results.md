# Sorting Resource Search Results
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Sorting_Results.htm
- Fetched: 2026-09-05 03:03 CDT

# Sorting Resource Search Results

Sort results from a search or resource query to better help you find what you need.
When you have more than 100 results, you can only sort resources by the following attributes:
- Display name
- Time created
- Status (depending on whether you have the option)

- [Console](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Sorting_Results.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Sorting_Results.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Sorting_Results.htm#)
- 

These steps assume that you already performed a free text search and selected the Resources category of results according to the instructions in[Performing a Free Text Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_perform_a_free_text_search.htm).

- On the Resources page, in the list of search results, select the column header of the column that you want to use to sort results.
Selecting the same column header again sorts the results in reverse order.
- (Optional) If needed, repeat the previous step with a different column header to sort results by using values from a different resource attribute.
- 

Use the[oci search resource structured-search](https://docs.oracle.com/iaas/tools/oci-cli/3.23.0/oci_cli_docs/cmdref/search/resource/structured-search.html)command and required parameters to sort results from a search for resources:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). For information about the syntax for queries, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm).
- 

Run the[SearchResources operation to use structured query language to sort results from a search for resources.

For information about query language syntax, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm). For information about a resource type, such as its attributes, see its reference page in the API Reference Guide. For the reference pages of resource types that have been indexed for Search, see[Supported Resources](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/queryoverview.htm#resourcetypes)
