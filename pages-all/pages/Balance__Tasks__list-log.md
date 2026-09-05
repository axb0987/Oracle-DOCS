# Listing Load Balancer Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-log.htm
- Fetched: 2026-09-05 01:41 CDT

# Listing Load Balancer Logs

List the access or error logs for a load balancer.

## Using the Console

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Monitoring and find the Logs section.
All logs are displayed in a table. Each load balancer can have a single access log and error log.
- To view the Load Balancer logs in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

### Filtering List Results

Use filters to limit the Load Balancer logs in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

### Actions

In the list table, select the name of a Load Balancer log to open its details page, where you can view its status and perform other tasks.

To perform an action on a Load Balancer log directly from the list table, select an available option from the Actions menu in the row for that Load Balancer log:
- View details : Open the details page for the log.
- Disable/Enable log :[Enable](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_log.htm)a disabled log, or[disable](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/disable_log.htm)a log that's enabled.
- Delete :[Delete the log](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_log.htm).
