# Editing a Budget
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-budget.htm
- Fetched: 2026-09-05 01:44 CDT

# Editing a Budget

Edit a budget in Billing and Cost Management.

When you edit a budget, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-budget.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-budget.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-budget.htm#)
- 

- 

On the Budgets list page, find the budget that you want to work with. If you need help finding the list page or the budget, see[Listing Budgets](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/../Tasks/list-budget.htm).
- 

From the Actions menu (three dots) for the budget, select Edit .
- 

In the Edit Budget panel, update the settings as needed. Avoid entering confidential information.

The fields that are editable depend on the type of budget:
- For monthly recurring budgets, you can change the name of the budget, the description, the budget amount, or the day of the month to begin budget processing. Avoid entering confidential information.
- For custom non-recurring budgets, you can change the name of the budget, the description, or the budget amount. The time period can't be edited. Avoid entering confidential information.

For descriptions of the settings, see[Creating a Budget](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-budget.htm).
- Select Save Changes .
- 

Use the[oci budgets budget budget update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/budgets/budget/budget/update.html)command and required parameters to edit a budget:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateBudget](https://docs.oracle.com/iaas/api/#/en/budgets/latest/Budget/UpdateBudget)
