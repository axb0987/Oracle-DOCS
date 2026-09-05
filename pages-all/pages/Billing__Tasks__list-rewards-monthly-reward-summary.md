# Listing Monthly Subscription Rewards
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-rewards-monthly-reward-summary.htm
- Fetched: 2026-09-05 01:43 CDT

# Listing Monthly Subscription Rewards

List the rewards for a subscription ID.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-rewards-monthly-reward-summary.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-rewards-monthly-reward-summary.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-rewards-monthly-reward-summary.htm#)
- 

To view the rewards summary and other details, open the navigation menu and select Billing &amp; Cost Management . Under Programs and Rewards , select Oracle Support Rewards . The Oracle Support Rewards page opens.
Note  
  
If the subscription and products are eligible for rewards but there is no associated usage, a message is displayed to indicate that no rewards data was found (because no rewards data has accrued yet).

You can view rewards by subscription, which you can select from the corresponding Subscription list. The following rewards summary is shown:
- Available Support Rewards : The total amount of accrued rewards that you can use.
- Redeemed Support Rewards : The total amount of rewards that you have redeemed.
- Current Contractual Accrual Rate : The rewards accrual rate. For example, customers can accrue rewards either at US$0.25 for every $1 of OCI usage, or $0.33 for every $1 of OCI usage if they have a ULA (Unrestricted License Agreement).
- Ending Soon : The rewards amount that expires within 30 days.

Following the rewards summary, a more detailed tabular view of the rewards is listed:
- Expiration Date : The date when rewards expire.
- Accrual Date : The date when the rewards were earned.
- Total Usage : The total usage amount evaluated for rewards ( Eligible Usage + Non-Eligible Usage = Total Usage ).
- Eligible Usage : The amount of usage that's eligible for rewards spending.
Note  
  

Eligible usage details aren't available for months where reward information was uploaded manually.
- Non-Eligible Usage : The amount of usage not eligible for rewards.
Note  
  

Not all usage accrues rewards. Consumption of third-party services and offerings, such as VMware, Microsoft, and Oracle Cloud Marketplace, aren't eligible to earn rewards. For more information, see[https://www.oracle.com/cloud/rewards/faq/](https://www.oracle.com/cloud/rewards/faq/).
- Accrued Rewards : The sum of any remaining rewards. Equivalent to the value of Available Support Rewards in the rewards summary.
- Redeemed : The amount of redeemed rewards. Equivalent to the value of Redeemed Support Rewards in the summary.
- Remaining : The amount of remaining ( Accrued Rewards - Redeemed ) rewards. Remaining rewards that are expiring soon are highlighted in red.
- 

Use the[oci usage rewards monthly-reward-summary list-rewards](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/usage/rewards/monthly-reward-summary/list-rewards.html)command and required parameters to list the rewards for a subscription ID:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ListRewards](https://docs.oracle.com/iaas/api/#/en/usage-proxy/latest/MonthlyRewardSummary/ListRewards)
