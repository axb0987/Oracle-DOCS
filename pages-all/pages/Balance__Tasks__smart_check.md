# Diagnosing Load Balancer Issues Using Smart Check
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/smart_check.htm
- Fetched: 2026-09-05 01:41 CDT

# Diagnosing Load Balancer Issues Using Smart Check

Use Smart Check to diagnose and fix a load balancer's configuration and environment issues.

Your load balancer includes Smart Check, which runs in the background to detect issues with the load balancer configuration and operating environment. Access the results of Smart Check activities through the Oracle Cloud Infrastructure Console as a resource of the load balancer.

Smart Check evaluates the load balancer approximately every 10 seconds. Each check reviews configuration issues such as the following:
- Load balancer's backend servers are in a drain or offline state.
- Protocol mismatches exist on the HTTP listener.
- Port mismatches exist on the HTTP backend servers.

Smart Check results are presented in tabular format within the load balancer's Details page. Each category of issues has an assigned status of High , Medium , Low , and OK . You can display details of each check, including recommendations for corrective actions where necessary. An Informational tab is also available to provide best practices and recommendations on how to make your load balancer work optimally.

## Using the Console

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Monitoring and find the Smart check section.

All Smart Check diagnostic entries are listed in a table. The Last checked indicator displays the UTC-based date-time group the load balancer was last diagnosed. Checks occur every 10 seconds.

Each entry contains the following columns and associated values:
- Category : Displays the area of the load balancer to which the Smart Check entry pertains, for example:

Backend Timeout
- Details : Displays details on the issue, for example:

Set the listener idle timeout to at least 10 seconds less than backend's keep-alive timeout.
- Recommended action : Describes corrective action you can take for the issue, for example:

Edit the listener and change the idle timeout.
- Select next to the entry to display details, including links to where you can perform corrective or preemptive actions.

Find the Informational section to display a list of best practices and recommendations to follow. Select the "down" arrow at the end of the entry to display details, including recommended fixes to any warnings or critical issues detected by Smart Check.

### Filtering List Results

Use filters to limit the Smart Check diagnostic entries in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list)
