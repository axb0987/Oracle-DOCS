# Creating a Budget
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-budget.htm
- Fetched: 2026-09-05 01:43 CDT

# Creating a Budget

Create a budget to set soft limits on infrastructure spending in Billing and Cost Management.
For more information about budgets, see[Budgets](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/../Concepts/budgetsoverview.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-budget.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-budget.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-budget.htm#)
- 

- On the Budgets list page, select Create Budget . If you need help finding the list page or the budget, see[Listing Budgets](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/../Tasks/list-budget.htm).
- In the Create Budget window, for Budget Scope , select the type of target for the budget:
- Child Tenancy : Available only when you're signed in to a parent tenancy in an[organization](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm).
- Compartment : Available for both parent and child tenancies.
- Tags : Available for both parent and child tenancies. For more information, see[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).
- Enter a name for the budget. The name can contain only alphanumeric characters, dashes, and the underscore character, and can't begin with a number. Avoid entering confidential information.
- Enter a description for the budget. Avoid entering confidential information.
- Select the target for the budget:
- For budgets that target a child tenancy , select the tenancy name from the Target Tenancy list.
- For budgets targeting a compartment , select the compartment from the Target Compartment list.
Important  
  

Although the budget tracks spending in the specified target compartment, you must have permissions to manage budgets in the root compartment of the tenancy to create and use the budgets.

You also can't create a budget in a compartment that already has a budget. You can create multiple alert rules within an existing budget. For more information about creating budget alert rules, see[Creating a Budget Alert Rule](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-alert-rule.htm).
- For budgets that target a tag :
Important  
  
Only a single budget is allowed per tag.
- Select a tag namespace.
- Select a target tag key.
- Enter a tag value.
- Under Schedule , select either Monthly for a recurring budget, or Custom (non-recurring) for a budget that's used only a single time.

(Monthly) In the Budget Amount field, enter a monthly amount for the budget.

(Custom) In the Budget Amount field, enter an amount for the budget.

The minimum allowed value for the budget is 1. The maximum allowed value is 999,999,999,999 in the chosen currency.

The Budgets page[lists](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-budget.htm)both Monthly and Custom (non-recurring) budget types, while the Status field indicates whether a budget is Active , Scheduled , or Expired .
- 

(Monthly) From Day of the month to begin budget processing , select the day of the month that you want budget processing to periodically begin on each month.

Setting this value allows you to create a budget that aligns with your billing cycle date, and to receive more meaningful budget alerts. Below this field, Current Budget Processing Period Based on Selection reflects the budget processing period, according to the day of the month you chose. When viewing or editing a budget on its details page, the Budget Processing Period field also displays this information.

Note  
  
If you select 29, 30, or 31 as the day of the month, budget processing begins on the last day of the month for months that have fewer days than the date you selected.
(Custom) Select the start date and end date (in UTC) for the non-recurring budget, up to a maximum of one year.
Note  
  
The start and end date can only be edited before the budget is active, and can't be changed when[editing](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-budget.htm)a budget.
- You can optionally create an alert for the budget by creating a budget alert rule. In Budget Alert Rule (optional) , configure the alert rule:
- For Threshold Metric , select a threshold for the alert:
- 

Actual Spend watches the actual amount you spent in the compartment per month.
- 

Forecast Spend watches resource usage and alerts you when it appears that the budget will be exceeded.

The forecast algorithm is of linear extrapolation and the formula is as follows:

`(Actual Spend / Days processed from the start of the budget period) * Days of the budget period`

The forecast algorithm requires at least three days of consumption to trigger, and the forecast spend is evaluated hourly.
- Select an option for Threshold Type :
- Percentage of Budget : A percentage of the monthly budget, which must be greater than 0 but no greater than 10,000.
- Absolute Amount : A fixed amount.

The label of the next text field changes depending on which option you select.
- Enter a value for either Threshold % or Threshold Amount .
- Optionally, in the Email Recipients field, enter one or more email addresses to receive the alerts. Separate multiple addresses by using a comma, semicolon, space, tab, or new line.
- Optionally, enter the body of the email alert in the Email Message field. The text of the email message can't exceed 1,000 characters. This message is included with metadata about the budget, including the budget name, the compartment, and the amount of the monthly budget. You can use this message, however, to provide instructions to the recipient that explains how to request a budget increase, or to remind users about corporate policies.
- (Optional) In the tags section, add one or more tags to the budget.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .
- 

Use the[oci budgets budget budget create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/budgets/budget/budget/create.html)command and required parameters to create a budget:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateBudget](https://docs.oracle.com/iaas/api/#/en/budgets/latest/Budget/CreateBudget)
