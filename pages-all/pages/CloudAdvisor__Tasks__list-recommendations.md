# Listing Recommendations
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/list-recommendations.htm
- Fetched: 2026-09-05 01:48 CDT

# Listing Recommendations

You can list and view Cloud Advisor recommendations with the Console , CLI , or API .

- [Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/list-recommendations.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/list-recommendations.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/list-recommendations.htm#)
- 

To use the Console to list recommendations, complete the following steps.
- Open the navigation menu and select Governance &amp; Administration . Under Cloud Advisor , select Recommendations .
- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. By default, recommendations for all categories and services are shown.
Note  
  
You might not see every recommendation listed on the[Categories and Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Concepts/recommendations.htm)page, depending on how the tenancy or compartment is set up and what you have selected in the Category , Service , and Status filters.
- Optionally change the order of the items in the list table by using the sort icons next to the column names.
Tip  
  
For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).
- If you're using Organization Management to centrally manage many tenancies and you're currently viewing recommendations from a parent tenancy, you'll also see the Tenancy filter in the Search and Filter box. Use this filter to display recommendations for a specific tenancy. Otherwise, recommendations for all tenancies are displayed by default.
- Next to Applied filters , select one or more recommendation statuses to further narrow the list. The default is Active.

#### Downloading the data

You can filter and download the list of recommendations to a CSV file. The file is stored in the default downloads folder.
- Filter the data. Use the Category , Service , and Status filters to display the recommendations that you want to see.
- Download the data.

If you're in a standalone or child tenancy, select Download CSV to download the recommendations data.

If you're in a parent tenancy, you can download the data either by recommendation or by resource.
- Select Download by recommendation . Cloud Advisor converts the table on the page to a CSV file and downloads it to the default downloads folder.
- Select Download by resource . Cloud Advisor copies the data, sorts it by resource, and stores it in a CSV file that's downloaded to the default downloads folder.
- 

This topic explains how to list recommendations using the CLI.

Use the[oci optimizer recommendation-summary list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer/recommendation-summary/list.html)command to list recommendations.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/).
- 

This topic explains how to list recommendations using the Cloud Advisor API.

Use the[ListRecommendations](https://docs.oracle.com/iaas/api/#/en/advisor/latest/RecommendationSummary/ListRecommendations)
