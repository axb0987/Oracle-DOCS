# Audit Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/audit_logs.htm
- Fetched: 2026-09-05 02:36 CDT

# Audit Logs

On the Audit page, you can explore audit logs. Audit logs are also searchable on the Search page, and you can view Audit logs in every compartment by selecting the /_Audit log group on the Search page.

For an overview of Audit, see[Overview of Audit](https://docs.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm).
Note  
  
This page replaces the classic Audit page features found in the Governance &amp; Administration portion of the Console, which will eventually be deprecated. As a result, a new and improved Audit experience is now part of Oracle Cloud Infrastructure Logging, and we recommend that you use this latest version of Audit instead.

## Required Permissions for Audit Logs

To view and search Audit logs, you must have the corresponding Audit-related permissions. For more information, see[Details for the Audit Service](https://docs.oracle.com/iaas/Content/Identity/Reference/auditpolicyreference.htm)and[Required Permissions for Searching Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm#required_permissions_for_searching_logs)for more information.

## Filtering Audit Logs

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Audit .

The Audit logs list page opens. All events in the selected compartment are displayed in a table.
- Select Edit to change the time range of the captured events.
The Edit time range panel opens.
- Select one of the preconfigured time range options. You can also select Custom and enter your own start and end date and times. Only a 14-day range is available when performing a Custom search. Select Update when done.
- Use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- Click within the Explore events box.
The following audit log filters appear that you can configure:
- User : Add one or more user filters.
- Resource : Add one or more resource filters.
- Action Type : Select one or more of the following actions:
- GET
- POST
- PUT
- PATCH
- DELETE
- Type : Add one or more type filters.
- To create a custom filter, select Advanced to the right of the search box.
The Advanced resource query box opens. Start entering text to automatically display filter settings, along with operators. For example, entering d displays filters starting with that letter. Use the up or down arrow keys to select from the list, or continue typing to enter what you want to filter on. This action functions the same as this field on the Logging Search page.

To find log events with a specific status code, include quotes (") around the code to avoid results that have those numbers embedded in a longer string.

## Exploring the Details of Events

On the Explore events tab, each log entry is organized in terms of the Event Time , User , Resource , Type , Action , and Status . Select and expand an audit log entry. Each entry displays the log data in a JSON field view, similar to the Search page, where you can collapse and expand nodes, or click the copy icon to copy the log entry to the clipboard.

To export log data, in Explore events , click Export Log Data (JSON) . This feature allows you to export the log data to a JSON file that you can save to your system.

## Exporting Audit Events

You can export audit events using[Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm).

## Audit Schema

For more information on the audit logging schema, see[Version 2 Audit Log Schema](https://docs.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm#schema)
