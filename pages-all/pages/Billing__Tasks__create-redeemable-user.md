# Creating a Redeemable User for a Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-redeemable-user.htm
- Fetched: 2026-09-05 01:43 CDT

# Creating a Redeemable User for a Subscription

Add a user who is authorized to redeem rewards for a subscription ID, based on their email address.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-redeemable-user.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-redeemable-user.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-redeemable-user.htm#)
- 

- Open the navigation menu and select Billing &amp; Cost Management . Under Programs and Rewards , select Oracle Support Rewards .
- On the Oracle Support Rewards page, select Manage authorized users .

The Manage Authorized Users panel opens.

Authorizing a user to[redeem rewards](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/redeem_rewards.htm)gives the user full permission to redeem your accrued rewards balance, as a form of payment against on-premises support invoices for Oracle Technology Programs. Authorized users can apply awards according to your order terms.
- Select + Another User , and then enter an email address. Optionally, enter a first and last name for the email address.

Authorized users receive emails that are personally addressed to them using the supplied first and last name.
- Select Save .

A message is displayed that the email addresses were saved successfully.

Note  
  
Email addresses are transferred outside Oracle Cloud Infrastructure to the Billing Center system. The email addresses for authorized rewards users must be the same as the email addresses the authorized users use to sign in to the Billing Center, where[rewards are redeemed](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/redeem_rewards.htm).
- 

Use the[oci usage rewards redeemable-user create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/usage/rewards/redeemable-user/create.html)command and required parameters to create and add a user who can redeem rewards to a subscription ID:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateRedeemableUser](https://docs.oracle.com/iaas/api/#/en/usage-proxy/latest/RedeemableUser/CreateRedeemableUser)
