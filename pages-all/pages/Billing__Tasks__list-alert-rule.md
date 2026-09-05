# Listing Budget Alert Rules
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-alert-rule.htm
- Fetched: 2026-09-05 01:43 CDT

# Listing Budget Alert Rules

View the alert rules for a budget in your tenancy in Billing and Cost Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-alert-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-alert-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-alert-rule.htm#)
- 

- On the Budgets list page, select the budget that contains the budget alert rules that you want to work with. If you need help finding the list page or the budget, see[Listing Budgets](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/../Tasks/list-budget.htm).
- On the details page, select the Budget Alert Rules tab.
All budget alert rules in the budget are displayed in a table.

## Filtering List Results

Use filters to limit the budget alert rules in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

To perform an action on a budget alert rule directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that budget alert rule:
- View/Edit :[Get details for the budget alert rule](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/get-alert-rule.htm)or[edit the budget alert rule](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-alert-rule.htm).
- Delete :[Delete the budget alert rule](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/delete-alert-rule.htm).

To[create a budget alert rule](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-alert-rule.htm), select Create Budget Alert Rule .
- 

Use the[oci budgets budget alert-rule list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/budgets/budget/alert-rule/list.html)command and required parameters to list the budget alert rules in the tenancy:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ListAlertRules](https://docs.oracle.com/iaas/api/#/en/budgets/latest/AlertRuleSummary/ListAlertRules)
