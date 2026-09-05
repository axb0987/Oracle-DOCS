# Running a Custom, Free-Form Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_custom_freeform_query_to_find_a_resource.htm
- Fetched: 2026-09-05 03:03 CDT

# Running a Custom, Free-Form Query

Free-form queries let you customize a search for resources by using structured query language that can specify conditions, resource attributes, and resource values that you want from results.

Queries support filtering and sorting resources through query language syntax. You effectively filter results by adding or removing clauses or changing the content of clauses. The only query you can perform that doesn't filter results is a query for everything.

For more information about syntax for advanced resource queries, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_custom_freeform_query_to_find_a_resource.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_custom_freeform_query_to_find_a_resource.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_custom_freeform_query_to_find_a_resource.htm#)
- 

- 

In the top navigation bar, select Search for resources, services, documentation, and Marketplace , and then select Advanced resource query .
- 

In the query text box, enter a query that conforms to query language syntax, and then select Search . For more information about syntax, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm).
- 

If needed, change what regions to search: next to Currently applied , select Regions , select the checkbox next to up to three regions that you want to include, and then select Apply filter .
- 

To filter results further, change the language of the query.
Note  
  
In advanced query mode, while you can filter and sort results by changing the query language, you can't filter or sort results through the results list displayed in the Console. Also, if you switch to advanced query mode from basic search mode, by default, results are sorted by the time the resource was created. You can change to sorting results by best match by removing the`sorted by`clause in the query language.

The results are eventually consistent, but might not immediately include resources that you created recently. If you don't see the results that you expect, you can change to a different region or edit the query.
- 

Use the[oci search resource structured-search](https://docs.oracle.com/iaas/tools/oci-cli/3.23.0/oci_cli_docs/cmdref/search/resource/structured-search.html)command and required parameters to use structured query language to find resources:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). For information about the syntax for queries, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm).
- 

Run the[SearchResources operation to use structured query language to find resources.

#### Example: Finding Instance Resources With a Specific Defined Tag

This section describes how to use the API to query for a specific type of resource based on the resource's defined tags.

The following query finds instances with a defined tag within the namespace "rqs", where the tag's key is "costcenter" and the key's value is "1234".

```

```

When you use the[SearchResources](https://docs.oracle.com/iaas/api/#/en/search/latest/ResourceSummary/SearchResources)operation to issue the query, the request will look similar to the following. (This example purposefully omits the authorization header and other headers.)

```

```

If the query produces results, the response lists the resources that match the resource type and tag that you specified. The response looks similar to the following:
```

```

With these results, you can take more action, if needed. For more information about a resource type, such as its attributes, see its reference page in the API Reference Guide. For the reference pages of resource types that have been indexed for Search, see[Supported Resources](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/queryoverview.htm#resourcetypes)
