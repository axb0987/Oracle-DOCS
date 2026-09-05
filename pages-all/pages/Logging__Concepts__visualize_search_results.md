# Visualizing Search Results
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/visualize_search_results.htm
- Fetched: 2026-09-05 02:36 CDT

# Visualizing Search Results

You can visualize your Logging Search page results, for both Basic and Advanced Mode searches.

[To visualize log data as a chart in Basic Search](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/visualize_search_results.htm#)

You can view log data graphically as a chart in[Basic Mode](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm#basic_search_queries)search, along with accompanying tabular data.

Select from the following chart settings:
- Visualization Type : Select from Stacked Bar , Pie , Donut , or Line . The Stacked Bar and Line charts are organized by default in terms of time (UTC) on the X-axis ( datetime ), and the chosen Group By logging field. You can hover the mouse over the chart data, which both highlights the area of interest, and displays the data in a tool tip. The Legend in all four chart types also provides an orientation to the displayed chart data.
- X Axis (stacked bar and line charts only): Select a logging field of interest to replace the default Time in UTC X-axis.
- Interval (only for stacked bar and line charts, and when datetime is the X Axis ): Select from 1 minute , 5 minutes , 15 minutes , 30 minutes , or 1 hour .
- Group By : Select a logging field to group the results by.

For any chart type being viewed, you can select to expand the &lt;number of&gt; records found list below the chart, which lists the total record sum, and the number of records at each time interval.

[To visualize log data as a chart in Advanced Search](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/visualize_search_results.htm#)

Searches can also be visualized during[Advanced Mode](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm#advanced_search_queries)search. When an advanced query is formulated according to a specific syntax format, the Visualize tab is also available in Advanced Mode , allowing you to view stacked bar, pie, donut, and line charts.

To view charts in Advanced Mode , create your queries using the following syntax:
- Stacked Bar :
```

```

This query returns a table with three columns:`<user_selected_field1>`,`<user_selected_field2>`, and`count`. The chart uses`<user_selected_field1>`as the x-axis,`count`for the y-axis, and`<user_selected_field2>`for the stacked bar group by dimension.
- Pie :
```

```

This query returns a table with two columns: &lt;user_selected_field&gt; and`count`. The chart uses &lt;user_selected_field&gt; as the legend, and`count`for the distribution of the pie chart.
- Donut :
```

```

This query returns a table with two columns:`<user_selected_field>`and`count`. The chart uses`<user_selected_field>`as the legend, and`count`for the distribution of the donut chart.
- Line :
```

```

The query returns a table with three columns:`<user_selected_field1>``, <user_selected_field2>`, and`count`. The chart uses`<user_selected_field1>`as the x-axis,`count`for the y-axis, and`<user_selected_field2>`
