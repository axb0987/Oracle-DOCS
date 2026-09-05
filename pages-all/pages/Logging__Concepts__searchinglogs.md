# Logging Search
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm
- Fetched: 2026-09-05 02:36 CDT

# Logging Search

Use the Logging Search page to search logs.

Logging provides a powerful tool to search indexed logs. Use the Console to perform any of the following tasks:
- Search logs, whether in a basic user interface mode, or by typing custom queries in an advanced mode.
- Filter on values in logs, whether by log fields, text search, or time intervals, all in terms of chosen compartments or log groups.
- Visualize log data in a bar chart view, along with accompanying tabular data.
- Explore each log line in more detail. View the raw JSON payload, and view before/after information.
- Export search results to a JSON file.

Logs are indexed by default, which allows them to be searched using the Console.
Note  
  
For logs to be available and to be searchable from a certain time frame, they must first be[enabled](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/enabling_logging.htm), and you can only search for logs after they start ingesting.

You can run log searches by using either the Basic mode filter controls in the interface, or the Advanced mode custom query language interface. See[Basic Search Queries](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm#basic_search_queries)and[Advanced Search Queries](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm#advanced_search_queries)for more information. Searches can also be[saved](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/log-saved-search-management.htm), and you can also search[multiple regions](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/multiregion_search.htm).
Note  
  
Only a 14-day range is available when performing log search queries.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

Administrators : For specific examples of policy, see[Required Permissions for Searching Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm#required_permissions_for_searching_logs).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). If you want to know more about writing policies for Logging, see[Details for Logging](https://docs.oracle.com/iaas/Content/Identity/policyreference/loggingpolicyreference.htm).

## Required Permissions for Searching Logs

To search indexed logs, a user must have the`read`permission on the log content and`read`access to the log group.
```

```

To search indexed logs, you must have access to the log group that contains the indexed logs. For more information, see[Required Permissions for Working with Logs and Log Groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/managinglogs.htm#required_permissions_logs_groups).

To view and search[Audit Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/audit_logs.htm), you must also have the corresponding Audit-related permissions. See[Details for the Audit Service](https://docs.oracle.com/iaas/Content/Identity/Reference/auditpolicyreference.htm)for more information. For example:
- `search "compartment"`requires`AUDIT_EVENT_READ`, and if there are any log objects, it would also require`LOG_CONTENT_READ`
- `search "compartment/_Audit"`requires just`AUDIT_EVENT_READ`.
- `search "compartmentOcid/logGroupNameOrOcid/logNameOrOcid"`requires`LOG_CONTENT_READ`only.
- `search "compartmentOcid1/_Audit" "compartmentOcid2/logGroupNameOrOcid/logNameOrOcid"`requires`LOG_CONTENT_READ`on`logGroupNameOrOcid`and`AUDIT_EVENT_READ`on`compartmentOcid1`.

## Basic Search Queries

To search and filter logs:
- Open the navigation menu and select Observability &amp; Management . Under Logging , select Search .
- In Custom filters , you can start typing to automatically display filter settings, along with operators. For example, entering`d`displays filters starting with that letter. Use the up or down arrow keys to select from the list, or continue typing to enter what you want to filter on. For example, data.compartmentName='&lt;tenancy_name&gt;' .
- In Select logs to search , the root compartment is already selected by default for filtering. Select this field to open the Select logs to search panel, where you can filter by compartments you have permission to work in, in addition to filtering by Log Groups and Logs . You can filter by multiple compartments and log groups. For any filters you create in this panel that you want to remove, select the filter X icon in the Select Logs to Search field.
- You can limit results to a specific time range. In Filter by time , select a predetermined time range from the list, or select Custom to specify a date range in the calendar Start Date and End Date . You can also specify a time value in the box next to the calendar. Use an end time to refine the time window.
- The log data in the Explore and Visualize tabs is reloaded according to your filter settings, or you can select Search to apply the filter.
Note  
  
Because the Search page automatically refreshes after applying filters and selecting logs, you don't need to select the Search button as you select different filters. You will, however, need to select Search again after some time has passed and new logs have appeared. When performing Advanced Mode queries however, you do need to always select this button to submit a query.
Note  
  
Filter settings are maintained when switching to Advanced Mode .

To remove a filters from the Search page, under Filters , select the X icon next to the filter.

See[Viewing and Working with Search Results](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/work_with_search_results.htm)for more information on search results, and[Visualizing Search Results](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/visualize_search_results.htm)for more information on visualizing Basic Mode searches.

## Advanced Search Queries

When performing a search on the Logging Search page, you can select Show Advanced Mode to enter your own custom log search queries. In addition, Advanced Mode searching provides more comprehensive search options that aren't available in Basic Mode .

Be default, the following is displayed in the Query field after selecting Show Advanced Mode :
```

```

For example, you can modify this default search by entering:
```

```

This returns`{"interval": 1600364700000,"cnt": 31}`and`{"interval": 1600365600000,"cnt": 220}`under Log Data in the Explore tab.

When entering search queries, auto-complete hints are providing as you type (which you can select from a pop-up menu as you type), and syntax validation is performed in real time in the background as you type a query.
Note  
  
When you switch from Advanced Mode to Basic Mode , the query is lost and is not available in Basic Mode . A warning is displayed for this scenario to confirm your preference.

The Advanced Mode search uses a specific syntax, using the Logging query language, which is described in[Logging Query Language Specification](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Reference/query_language_specification.htm).

See[Viewing and Working with Search Results](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/work_with_search_results.htm)for more information on search results, and[Visualizing Search Results](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/visualize_search_results.htm)
