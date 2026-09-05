# Creating a Log Saved Search
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-log-saved-search.htm
- Fetched: 2026-09-05 02:37 CDT

# Creating a Log Saved Search

Create a saved search in Logging.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-log-saved-search.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-log-saved-search.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-log-saved-search.htm#)
- 

You can save the search parameters that you use for any searches performed in[Basic Mode](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/searchinglogs.htm#basic_search_queries)and[Advanced Mode](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/searchinglogs.htm#advanced_search_queries).

To save a search:
- Open the navigation menu and select Observability &amp; Management . Under Logging , select Saved Searches .
- Select a compartment that you have permission to work in.
- On the Saved Searches page, select New Search , which opens the Logging Search page, where you can begin a search.
- Apply filter and search settings as described in[Basic Search Queries](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/searchinglogs.htm#basic_search_queries)and[Advanced Search Queries](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/searchinglogs.htm#advanced_search_queries).
- Select Save search .
- In the New Saved Search panel, in Search Name , enter a name to associate with your saved search. Avoid entering confidential information.
- In Compartment , select the compartment that you want to create the saved search in.
- In Description , enter a description for the saved search.
- 

Select Save Search .

The search is saved and a message appears with the linked name of the saved search.

Select the saved search name to open the saved search details page with the Saved Search Information tab selected.

The Tags tab shows tags associated with the saved search, and you can add or edit tags. Under Latest Results , log data is displayed. You can apply some simple filters, such as sorting by newest or oldest from the Sort field, or filtering by time from the corresponding Filter by time field.

To view this saved search on the Search page directly, select Explore with Log Search from the Actions menu. The Search page opens with the saved search loaded, whether it's a basic or advanced search. You can perform more analysis and investigation related to this search directly on the Search page. For more information, see[Logging Search](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/searchinglogs.htm).

While on the Search page, you can also switch between any of the saved searches by selecting them from the Saved Searches list.
Note  
  
When[editing a saved search](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-log-saved-search.htm)from the Saved Searches page, you can change the values in only the Search Name , Compartment , and Description fields in the Edit Saved Search panel. If you need to change the search parameters, create a new saved search.
- 

Use the[oci logging log-saved-search create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log-saved-search/create.html)command and required parameters to create a log saved search:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateLogSavedSearch](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogSavedSearch/CreateLogSavedSearch)
