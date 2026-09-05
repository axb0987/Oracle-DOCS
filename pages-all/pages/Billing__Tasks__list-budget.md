# Listing Budgets
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-budget.htm
- Fetched: 2026-09-05 01:43 CDT

# Listing Budgets

View the tenancy's budgets in Billing and Cost Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-budget.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-budget.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-budget.htm#)
- 

Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Budgets .

The Budgets page opens. All budgets in the tenancy are displayed in a table.

Both Monthly and Custom (non-recurring) budget types are included. The Status value indicates whether a budget is Active , Scheduled , or Expired .

## Filtering List Results

Use filters to limit the budgets in the list. For example, filter by budget scope (compartment or tag). Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a budget to open its details page, where you can view its status and perform other tasks.

To perform an action on a budget directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that budget:
- View details : Open the details page for the budget.
- Edit :[Edit the budget](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-budget.htm).
- Manage Tags : Add one or more tags to the budget. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Add tags : Add one or more tags to the budget. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- View tags : View existing tags for the budget. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete :[Delete the budget](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/delete-budget.htm).

To[create a budget](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-budget.htm), select Create Budget .
- 

Use the[oci budgets budget budget list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/budgets/budget/budget/list.html)command and required parameters to list the budgets in the tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListBudgets](https://docs.oracle.com/iaas/api/#/en/budgets/latest/BudgetSummary/ListBudgets)
