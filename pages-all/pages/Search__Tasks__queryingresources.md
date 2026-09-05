# Querying Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources.htm
- Fetched: 2026-09-05 03:03 CDT

# Querying Resources

This documentation describes the different ways that you can use Search to find Oracle Cloud Infrastructure resources. Search supports the following tasks for finding resources:
- [Performing a Free Text Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_perform_a_free_text_search.htm)
- [Reusing Recent Search Terms](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_reuse_recent_search_terms.htm)
- [Running a Custom, Free-Form Query](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_custom_freeform_query_to_find_a_resource.htm)
- [Running a Sample Query](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_sample_query_to_find_a_resource.htm)
- [Filtering Resource Search Results](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Filtering_Results.htm)
- [Clearing Resource Search Filters](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Clearing_Filters.htm)
- [Changing Resource Search Filters](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Changing_Filters.htm)
- [Sorting Resource Search Results](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Sorting_Results.htm)
- [Switching Search Modes](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Switching_Search_Modes.htm)
- [Listing Resource-Types Supported by Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Listing_Supported_Resource_Types.htm)
- [Getting Resource-Type Details](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Getting_Resource_Type_Details.htm)

You can find Oracle Cloud Infrastructure resources in a tenancy by performing a free text search or running a query. A free text search finds resources with the specified text anywhere in the resource metadata. An advanced query lets you find resources according to specific fields and conditions by using query language. When finding resources, both free text searches and queries rely on resource indexing and the indexed attributes for a particular resource type. Search also scopes resource results to the selected region.
Note  
  

Supported Resources and Using Advanced Resource Queries

The search results that you see reflect what Search considers supported resources. To see what Oracle Cloud Infrastructure services and resources Search supports, see the[Supported Resources](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/queryoverview.htm#resourcetypes)section of[Overview of Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/queryoverview.htm)or see[Listing Resource-Types Supported by Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Listing_Supported_Resource_Types.htm).

## Finding Instances

You can find instances (or a VNIC that comes with an instance) by entering an IPv4 or IPv6 address as a free text search. Also, in search results, Search offers an enhanced view of resource attributes for instance resources.

By default, search results display a limited, common set of resource attributes for any matching resource. In the Console, these resource attributes include the display name, resource type, OCID, compartment, lifecycle state, and time created. In the SDK or CLI, basic resource search results also include the availability domain and any tags associated with the resource.

You can see select additional details indexed for instance resources by applying the optional resource type filter to search results. To apply the resource type filter, you must first obtain search results by following any of the Console-based procedures in[Performing a Free Text Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_perform_a_free_text_search.htm),[Reusing Recent Search Terms](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_reuse_recent_search_terms.htm),[Running a Custom, Free-Form Query](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_custom_freeform_query_to_find_a_resource.htm), or[Running a Sample Query](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_sample_query_to_find_a_resource.htm).
When you try to find instances by providing an IP address in the search box, the service treats it as a free text search. Everything about how the service treats free text searches applies, as described in[Free Text Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/freetextsearch.htm), from matching and ranking of results to the use of wildcards. For example, you can enter the following IPv6 address:
```

```

Search interprets the wildcard character in the last 16-bit field as described in[Wildcards](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/freetextsearch.htm#wildcards). The service then tries to match the translated search term against the values of all indexed resource attributes for all indexed resources. If the string appears in an indexed field, such as the IP address of an instance, then Search considers the found item a matching result and returns it in the list of results. If you have an instance with the IPv6 address`68be:66d1:e4a1:ae53:6905:ecab:30a1:a814`, for example, you can filter by the instance resource type to get a detailed view of the search result and any other matching instance results.

For more information about performing a free text search and filtering results, see[Performing a Free Text Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_perform_a_free_text_search.htm).

## Finding Resources by OCID

You have several ways of finding a resource by its OCID . You can directly enter an OCID as a free text search. However, we recommend that you construct an advanced resource query instead. When constructing a query to find a resource by its OCID, you can either provide the OCID as part of a condition statement or as matching text. For example, to find a compartment with a specific OCID with a condition statement:
```

```

For more information about this query syntax, see[Conditions](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm#conditions).

Or, for example, to find a compartment with a specific OCID with a matching clause:
```

```

For more information about this query syntax, see[Matching](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/querysyntax.htm#matching).
