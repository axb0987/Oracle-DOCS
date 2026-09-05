# Creating a Budget Alert Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-alert-rule.htm
- Fetched: 2026-09-05 01:43 CDT

# Creating a Budget Alert Rule

Create an alert rule for a budget in Billing and Cost Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-alert-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-alert-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-alert-rule.htm#)
- 

- On the Budgets list page, select the budget that you want to create a budget alert rule for. If you need help finding the list page or the budget, see[Listing Budgets](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/../Tasks/list-budget.htm).
- On the details page, select the Budget Alert Rules tab.
- Select Create Budget Alert Rule .
- In the Create Budget Alert Rule panel, enter the following information:
- Threshold Metric : Select a threshold for the alert:
- 

Actual Spend watches the actual amount you spent in the compartment per month.
- 

Forecast Spend watches resource usage and alerts you when it appears that the budget will be exceeded.

The forecast algorithm is of linear extrapolation and the formula is as follows:

`(Actual Spend / Days processed from the start of the budget period) * Days of the budget period`

The forecast algorithm requires at least three days of consumption to trigger, and the forecast spend is evaluated hourly.
- Threshold Type : Select a type:
- Percentage of Budget : A percentage of the monthly budget, which must be greater than 0 but no greater than 10,000.
- Absolute Amount : A fixed amount.
- Threshold % or Threshold Amount : Enter a value.

The label of this field depends on the selected threshold type.
- (Optional) Email Recipients : Enter one or more email addresses to receive the alerts. Separate multiple addresses by using a comma, semicolon, space, tab, or new line.
- (Optional) Email Message : Enter the body of the email alert. The text of the email message can't exceed 1,000 characters. This message is included with metadata about the budget, including the budget name, the compartment, and the amount of the monthly budget. You can use this message, for example, to provide instructions to the recipient, that explain how to request a budget increase or to remind users about corporate policies.
- Select Create .

The new rule appears in the list of budget alert rules.
- 

Use the[oci budgets budget alert-rule create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/budgets/budget/alert-rule/create.html)command and required parameters to create a budget alert rule:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateAlertRule](https://docs.oracle.com/iaas/api/#/en/budgets/latest/AlertRule/CreateAlertRule)
