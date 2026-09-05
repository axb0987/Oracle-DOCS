# Performing a Free Text Search
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_perform_a_free_text_search.htm
- Fetched: 2026-09-05 03:03 CDT

# Performing a Free Text Search

A free text search lets you specify search terms that might be found anywhere in resource metadata, in the names of pages in the Console, in documentation, or in Oracle Cloud Infrastructure Marketplace listings.

Although queries can only be used to find resources, you can use free text searches to help you find pages in the Console, help in the documentation, or listings in Marketplace. A free text search finds results for the search terms that you specify anywhere in resource metadata. A free text search looks for search terms in the display names of Console pages and lists pages according to where they appear within services in the tenancy. A free text search can also find search terms in the Oracle Cloud Infrastructure Getting Started Guide and Oracle Cloud Infrastructure User Guide documentation. The results for both these types of searches depend on the language, but not the region. Lastly, a free text search looks for search terms in the title of Marketplace listings.

For more information about how free text search applies search terms, see[Free Text Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/../Concepts/freetextsearch.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_perform_a_free_text_search.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_perform_a_free_text_search.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_perform_a_free_text_search.htm#)
- 

- 

In the top navigation bar, select Search resources, services, documentation, and Marketplace .
- 

Enter the free-form text you want to search for.
- 

Under one of the categories of search results, select a result. (To see all results on a full page instead, select View all next to the category name.)
- 

(Optional) In full page view, you can do the following:
- If you chose the Resources category, you can sort results, expand individual results to see the matching text, or you can filter results. To sort results, see[Sorting Resource Search Results](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Sorting_Results.htm). To filter results, see[Filtering Resource Search Results](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-Filtering_Results.htm).
- For the Services category, you can only sort or filter results. To sort results, see[Sorting Service Search Results](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/searchingservices_topic-Sorting_Results.htm). To filter results, see[Filtering Service Search Results](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/searchingservices_topic-Filtering_Results.htm).
- Similarly, for the Documentation category, you can only sort or filter results. To sort results, see[Sorting Documentation Search Results](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/searchingdocumentation_topic-Sorting_Results.htm). To filter results, see[Filtering Documentation Search Results](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/searchingdocumentation_topic-Filtering_Results.htm).

For any category, filter options only include resource types, service groups, or documentation presented in the full list of results.

Results are eventually consistent, but might not immediately include resources that you created very recently.

If you don't see the results that you expect, you can change to a different region (if searching for a resource), change to a different language (if searching for a service or documentation), view a different category of search results, or edit the search terms. For a documentation search, you might try a plural or singular form of one or more search terms or a different, supported language. If searching for a resource, you can also refine the search with a query by selecting Advanced resource query . Then, follow the instructions in[Running a Custom, Free-Form Query](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_custom_freeform_query_to_find_a_resource.htm)or[Running a Sample Query](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_sample_query_to_find_a_resource.htm).
- 

Use the[oci search resource free-text-search](https://docs.oracle.com/iaas/tools/oci-cli/3.23.1/oci_cli_docs/cmdref/search/resource/free-text-search.html)command and required parameters to perform a free text search of all indexed attributes of all searchable resource-types:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[
