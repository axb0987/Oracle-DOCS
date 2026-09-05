# Viewing and Working with Search Results
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/work_with_search_results.htm
- Fetched: 2026-09-05 02:36 CDT

# Viewing and Working with Search Results

Learn about viewing and working with search results on the Search page.

After you get an initial set of results, you can view more details, whether in terms of the log fields, JSON, or before and after states, and[visually as a chart](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/visualize_search_results.htm). On the Explore tab, a Number of log events per minute bar graph displays the number of log events, according to your filter settings. The Explore tab displays a maximum of 100 search results.
Note  
  
To see the latest logs, ensure you select Search after time has passed while on the Search page.
Note  
  
For any actions taken on the Explore and Visualize tabs, you can define how often to refresh the data on the Search page by selecting a value from the Autorefresh list (select from OFF , 5 Minutes , or 15 Minutes ). The default is OFF .

Your search results can also be visualized. See[Visualizing Search Results](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/visualize_search_results.htm)for more information.

[To search with Quick Start Queries](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/work_with_search_results.htm#)

You can quickly search according to several predetermined queries. From Quick Start Queries , select a query from the list. The Search page displays the results for the chosen query.

[To examine a single log entry](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/work_with_search_results.htm#)

On the Explore tab, select the down arrow ( ) to expand the log entry in JSON view.

The JSON view is displayed. In JSON view you can view the log data fields and values, collapse and expand nodes, or select the copy icon to copy the log entry to the clipboard.

[To view all log data](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/work_with_search_results.htm#)

From the Explore tab's Actions menu, select Expand log data . All the log entries from your search are fully expanded, without having to select the down arrow ( ) for each one. To reverse this state, select Collapse log data to close every entry simultaneously.

[To wrap or unwrap lines](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/work_with_search_results.htm#)

From the Explore tab's Actions menu, select Wrap lines . The Wrap lines option allows you to view each entry's data with line wrapping. Select Unwrap lines to undo. The Wrap lines feature also works when you're viewing an expanded log entry in JSON view.

[To switch between JSON and Before &amp; After view](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/work_with_search_results.htm#)

On the Explore tab, select the down arrow ( ) to expand the log entry and select JSON .

The JSON view is displayed. Select the Before &amp; After tab to switch to its view.

[To examine Before &amp; After view](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/work_with_search_results.htm#)

On the Explore tab, select the down arrow ( ) to expand the log entry and select Before &amp; After .

The Before &amp; After view is displayed. In contrast to the entry labeled as Current , this view displays the preceding and successive logging lines in the log object. Select Show newer entries or Show older entries to view extra corresponding newer or older entries in the Before &amp; After view.

[View more options for log entry rows and fields in JSON view](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/work_with_search_results.htm#)

On the Explore tab, each entry has three interactive header columns, which correspond to: the log timestamp ( datetime ), the plugin where the log occurred ( type ), and the log message ( data.message ).

You can interact with and customize the log entry view whether a log entry is collapsed or expanded.

When selecting a collapsed entry, select one of the log entry columns to open a context-sensitive menu for that entry and the column header. The following options are shown:
- Copy value
- Filter matching
Note  
  
Not available for the data.message column of an open or closed log entry.
- Filter not matching
Note  
  
Not available for the data.message column of an open or closed log entry.
- Remove from summary view
Note  
  
This option does not apply to the first default column ( datetime ). It is only available for new fields you add to the Explore tab's summary view, or the type and data.message columns which you can also remove.

For an expanded log entry with the JSON view visible, you can select a log field to access the following options:
- Copy value
- Filter matching
- Filter not matching
- Add to summary view
Note  
  
These options are also available on the JSON tab of an opened Before &amp; After view.

When selecting Add to summary view for a particular field, the field is added to the Explore tab view, to the right of the first three default columns ( datetime , type , data.message ). For example, if you select`"logContent"`and select Add to summary view , a new logContent column is added, just after data.message .

[To manage and add log fields](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/work_with_search_results.htm#)

From the Explore tab's Actions menu, select Manage log fields . The Manage log fields panel opens. Select the fields you want to add to the Explore tab and select Apply . The Explore tab reloads and appends the new fields to the right of the first three default fields ( datetime , type , data.message ). You can remove any added fields by selecting the X icon in the column header, which reloads the tab to display the results without the additional fields. The type and data.message columns can also be removed, so you can potentially add nine other log fields of interest, for a total of 10 columns that can be displayed in the Explore tab results. The datetime column can't be removed.
Note  
  
If you are managing and adding log fields in[Basic Mode search](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm#basic_search_queries)and then switch to[Advanced Mode](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm#advanced_search_queries), column header selections are still maintained, even as you type an advanced query.

[To export log data](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/work_with_search_results.htm#)
