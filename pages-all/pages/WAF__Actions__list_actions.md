# Listing Web Application Firewall Actions
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/list_actions.htm
- Fetched: 2026-09-05 03:09 CDT

# Listing Web Application Firewall Actions

View a list of the actions contained within a web application firewall policy.

## Using the Console

- On the Policies list page, select the policy that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/../Policies/list_waf-policy.htm#top).
The policy's details page opens.
- From the details page, select Actions .
- To view the actions in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
The Actions list opens. All actions are displayed in a table. The Actions list shows the name, action type ( Allow , Check , Return HTTP Response ), and rule usage (attached load balancer name).

### Filtering List Results

Use filters to limit the actions in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

### Actions

In the list table, select the name of an action to open its details page, where you can view its status and perform other tasks.

To perform a task on an directly from the list table, select an available option from the Actions menu in the row for that request protection rule.
- View details :[Open the details page for the action](https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/get_action.htm#top).
- Edit :[Edit the action](https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/update_action.htm#top).
- Delete :[Delete the action](https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/delete_action.htm#top)from the policy.

To add an action, select Add action from the Actions menu .
