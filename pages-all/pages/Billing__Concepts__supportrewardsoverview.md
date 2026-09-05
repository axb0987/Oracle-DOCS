# Oracle Support Rewards Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/supportrewardsoverview.htm
- Fetched: 2026-09-05 01:43 CDT

# Oracle Support Rewards Overview

With Oracle Support Rewards, you can earn rewards when using Oracle Cloud Infrastructure services, and those rewards can be applied to pay for support contracts that customers have for other eligible on-premises Oracle products.

For example, a customer can be both an OCI customer, and have an on-premises Oracle database enterprise license that they invoice for monthly. The customer's OCI usage allows them to earn rewards that they can apply to pay the Oracle database enterprise support contract invoice. These invoices are paid in a separate Billing Center system outside of OCI. As a result, Oracle Support Rewards can help lower your support bill.

Oracle Support Rewards are tied to your subscription, if your subscription is enrolled. Support rewards are accrued at the rate specified in your Oracle Universal Credits order document, and can be redeemed against support invoices for eligible products. Customers can accrue Oracle Support Rewards for their[Multicloud](https://docs.oracle.com/iaas/Content/multicloud/Oraclemulticloud.htm)subscriptions as well.

Oracle Support Rewards also integrates with[Organization Management](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm). Namely:
- Both parent and standalone tenancies can see their rewards.
- Parent tenancies can view their own rewards, plus their child tenancy rewards.
- Child tenancies can't see their rewards. Child tenancies viewing the Oracle Support Rewards page only see a message indicating that they're signed in to a child tenancy, because Oracle Support Rewards are only visible from the parent tenancy.

Using the Oracle Support Rewards page, an OCI administrator can view what rewards have accrued, and they can also drill into what specific usage earned them their rewards.

You can perform the following support rewards tasks:
- [Listing Monthly Subscription Rewards](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/list-rewards-monthly-reward-summary.htm)
- [Listing Product Information for a Subscription](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/list-products-product-summary.htm)
- [Creating a Redeemable User for a Subscription](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/create-redeemable-user.htm)
- [Deleting a Redeemable User from a Subscription](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/delete-redeemable-user.htm)
- [Listing the Redeemable Users for a Subscription](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/list-redeemable-users-redeemable-user-summary.htm)
- [Listing the Redemption History for a Subscription](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/list-redemptions-redemption-summary.htm)
- [Viewing the Redemption Code for Support Rewards](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/viewing-redemption-code.htm)
- [Redeeming Rewards](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/redeem_rewards.htm)

Also see the following instructional videos about Oracle Support Rewards:
- [Overview: Summary of the end-to-end process (3:44)](https://www.oracle.com/cloud/rewards/?ytid=ZiRvOvFBXF8)
- [Administration: How to view and share available rewards in the Console (3:16)](https://www.oracle.com/cloud/rewards/?ytid=BYbbk6tKOOM)
- [Redemption: How to redeem rewards in the Billing Center (7:07)](https://www.oracle.com/cloud/rewards/?ytid=oVUOyYyiTdE)

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

To use Oracle Support Rewards, the following policy statements are required. To view rewards:
```

```

To view and authorize users to redeem rewards in the Billing Center:
```

```
