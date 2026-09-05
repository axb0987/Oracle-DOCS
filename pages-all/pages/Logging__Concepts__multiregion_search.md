# Searching Multiple Regions
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/multiregion_search.htm
- Fetched: 2026-09-05 02:36 CDT

# Searching Multiple Regions

When performing either a basic search or advanced search on the Search page, you can search for logs from not only your home region, but also across multiple Oracle regions.

Multi-region search allows you to centrally run queries from the same location, rather than having to run a duplicate query in other regions. As result, you can search for overall logging events. When searching multiple regions, the results are fetched from the regions and the results are displayed on the Search page.
Note  
  
The maximum number of search results for all regions is 10000.

To search multiple regions:
- Select More search options . The Select regions to search field is displayed. By default, the field is populated with your active home region.
- To add more regions, select the field. The Select regions to search panel is displayed.
- Select the extra regions you want to search, and select Update regions .

On the Search page, the Select regions to search field is updated with the extra regions you have selected, and the log data in the Explore tab is reloaded according to your multi-region search settings. The Visualize tab is not available for this type of search. Under the Explore tab, when you have toggled regions off in the Show/hide regions in results panel, the tab indicates that you are viewing filtered region results.
Note  
  
With multi-region search, you cannot create connectors. You can use the[saved searches](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/log-saved-search-management.htm)
