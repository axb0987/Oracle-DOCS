# Filtering Resource Search Results
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Filtering_Results.htm
- Fetched: 2026-09-05 03:03 CDT

# Filtering Resource Search Results

Apply filters to narrow down a list of resource results according to various resource attributes.

How you filter the results from a search for resources depends on the mode you use to find the results.
Basic search mode supports the filtering of resource search results through the Console. You can use the following methods to filter, depending on the options available:
- Use the in-page search box
- Use the column headings in the results list

This topic describes how to use the in-page search box to access filters, but the filters in column headings in the results list behave the same way, if you have them.

Advanced query mode supports filtering and sorting resources through query language syntax. You effectively filter results by adding or removing clauses or changing the content of clauses. The only query you can perform that doesn't filter results is a query for everything. The only filter that exists in the Console itself for results returned by a query is the region filter. Query language doesn't support specifying a region in which to find results.
Understanding the following information can help you filter resource search results to better find what you need:
- By default, if you have more than one string with spaces between them in a free text search or in basic search mode, the Console finds resources containing any of the search strings. Search doesn't try to find resources containing all the search strings. For more information about free text searches, see[Free Text Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/freetextsearch.htm).
- In basic mode, you can use the in-page search box when working with a list of search results to apply filters to the results. If available, you can also use the filters in column headings.
- Some filters include all possible attribute values by default. Namely, the compartment filter includes all compartments in the search until you specify compartments to remove from the filter. Meanwhile, other filters match no attribute values by default.
- You can clear filters. For more information, see[Clearing Resource Search Filters](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Clearing_Filters.htm).
- You can change filters. For more information, see[Changing Resource Search Filters](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Changing_Filters.htm).
- You can sort results. For more information, see[Sorting Resource Search Results](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Sorting_Results.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Filtering_Results.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Filtering_Results.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Filtering_Results.htm#)
- 

These steps assume that you already performed a free text search and selected the Resources category of results according to the instructions in[Performing a Free Text Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_perform_a_free_text_search.htm).

- On the Resources page, select the search box, and then type or select a resource type or resource attribute to include in the filtered search results. (Available attributes depend on the resource types in the results list.)
- Then, do one of the following:
- If you selected a filter that provides predefined options, select the option from a menu or by selecting one or more checkboxes.
- If you selected a filter that requires you to specify the value of the resource attribute to compare potential search results to, select the filter box and enter an appropriate value. ( Note: Filters where you can enter a custom value require that you enter at least three characters before you apply the filter.)
- If you selected the Display name or OCID filter, you can only enter one value at a time for either filter.
- If you selected the Tag filter, first select the type of tag from the menu options. Then, specify the value or values that you want the filter to match. Lastly, specify whether you want to Match any value or Specify matching values . (The information in the Console might be shown in a different order than is presented in this topic.)
- If you selected a time-based filter, specify the Start date , Start time , End date , and End time .
- When you're ready, select Apply filter .
- (Optional) To add another filter, repeat the previous steps.
- 

Use the[oci search resource structured-search](https://docs.oracle.com/iaas/tools/oci-cli/3.23.0/oci_cli_docs/cmdref/search/resource/structured-search.html)command and required parameters to apply filters when finding resources:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). For information about the syntax for queries, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm).
- 

Run the[SearchResources operation to use structured query language to filter resources.
Example: Finding All Resource Attributes of a Resource-Type That Contain a Specific String

This section describes how to use the API to query all indexed fields of a particular resource-type for matches to a specific string.

The following query finds users with any attributes that contain "doe".

```

```

When you use the[SearchResources](https://docs.oracle.com/iaas/api/#/en/search/latest/ResourceSummary/SearchResources)operation to issue the query, the request looks similar to the following. (This example purposefully omits the authorization header and other headers.)

```

```

If the query produces results, the response lists the resources that match the resource-type and tag that you specified. The response looks similar to the following:
```

```

With these results, you can take more action, if needed. For more information about a resource type, such as its attributes, see its reference page in the API Reference Guide. For the reference pages of resource types that have been indexed for Search, see[Supported Resources](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/queryoverview.htm#resourcetypes)
