# Managing Account Upgrades and Payment Method
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/changingpaymentmethod.htm
- Fetched: 2026-09-05 01:43 CDT

# Managing Account Upgrades and Payment Method

On the Upgrade and Manage Payment page, you can: upgrade to a paid account, request to upgrade a paid account to corporate, update address or contact info for a corporate account, change your payment method, and request a sales call.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

To upgrade to a paid account or change your credit card, you must be a member of the Administrators group. See[The Administrators Group and Policy](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm#The).

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

## Account Upgrade Overview

Most new customers in the United States who create new accounts after January 28, 2019 can use the Upgrade and Manage Payment page tools.
Note  
  
If you created your account before January 28, 2019 or from outside the United States, use the following links:
- To upgrade to a paid account, see[Upgrade Your Free Oracle Cloud Promotion](https://docs.oracle.com/iaas/Content/GSG/Tasks/buysubscription_topic-Upgrade_Your_Free_Promotion.htm).
- To change your credit card, see[Updating Your Billing Details](https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/mmocs/updating-your-billing-details.html).

When you sign up for the[Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm), your credit card is authorized for $1 USD (or its equivalent in your country) at the time of sign-up.

When upgrading your free account, however, your credit card is authorized for $100 USD (or its equivalent in your country) at the time of the upgrade.

For both cases, the credit card authorizations are immediately reversed on the Oracle side. The vendor/banking institution at your location, however, decides how long it takes for the reversal to be processed.

## Upgrade to Pay As You Go

Note  
  
The credit card you used to sign up for Oracle services is shown as a default payment method, and can be used for an upgrade to a paid account. If you want you use a different credit card for an upgrade, click Change Payment Method .

To upgrade a trial account to Pay As You Go:
- Open the navigation menu and select Billing &amp; Cost Management . Under Billing , select Upgrade and Manage Payment . The Upgrade page is displayed.
- Under Subscription Information , the Plan Reference , Plan Type (Free Tier), and Start Date are indicated.

Under Account Details , the name, email address, and physical address you used during signup are also indicated.
- 

The credit card you used to sign up for the Free Trial is already shown as your default payment method. You can use this credit card for the upgrade, or enter another credit card by clicking Change Payment Method , and then do the upgrade. To change your payment details, see[Change Payment Method Before or After an Upgrade](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/changingpaymentmethod.htm#To_change_your_payment_method).
- Under Pay As You Go , you can review the Pay As You Go upgrade description, and view whether the account type is Corporate or Individual .

By default, all accounts are set as Individual . To change the customer account type to Corporate , you must[request a sales call](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/changingpaymentmethod.htm#To_request_a_sales_call). A payment method is also required.

Note  
  

Individual accounts can be upgraded to a Corporate account by[requesting a sales call](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/changingpaymentmethod.htm#To_request_a_sales_call), but accounts that start out as Corporate can't go back to being an Individual account.
- After specifying the account type preference, select the check box to agree to the terms and conditions.
- Click Upgrade your account .

(If applicable for your country) The Configure tax dialog opens, where you can optionally specify country-specific tax details. For example, for Chile, enter the required RUT (Rol Unico Tributario) value in the field, and select the GIRO payment transfer value from the list.
- Click Next . The Confirm account upgrade confirmation is displayed. Review the upgrade confirmation and click Upgrade account .
- A notification is displayed that your account upgrade is in progress. The upgrade can take a day or two to complete.

You receive a confirmation email upon completion of the upgrade, and the Upgrade page later indicates that the upgrade was successful. Also, at the top of the page under Subscription Information , the Plan Type field changes from Free Tier to Pay As You Go , and the page title changes to Manage Payment , where you can[update the address for corporate accounts](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/changingpaymentmethod.htm#updateaddress-corpacct), or[manage your payment method](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/changingpaymentmethod.htm#To_change_your_payment_method).

## Upgrade Pay As You Go to Corporate

To upgrade a Pay As You Go individual customer account type to a corporate account, you must request a sales call. For more information, see[Request a Sales Call](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/changingpaymentmethod.htm#To_request_a_sales_call).

## Update Address and Contact Info for a Corporate Account

Corporate customer account types can update their address at any time on the Manage Payment page.
- Open the navigation menu and select Billing &amp; Cost Management . Under Billing , select Upgrade and Manage Payment . The Manage Payment page is displayed.
- Under Subscription Information , the Plan Reference , Plan Type (Pay As You Go), and Start Date are indicated.

Under Corporate Account , the name, email address, and physical address you used during signup are also indicated.
- To update the address, click Update Account Details . The Update Account Details panel opens.

Corporate is already selected, and the Individual option isn't available, because you can't change the account type back to Individual .

Legal Company Name can't be changed, but you can change your address and contact details under Billing Address and Contact Information .
- After updating address and contact information, click Submit .

## Request a Sales Call

To request a sales call on the Upgrade and Manage Payment page:
- Open the navigation menu and select Billing &amp; Cost Management . Under Billing , select Upgrade and Manage Payment .
- On the Upgrade and Manage Payment page under Request a sales call , select Request a sales call .
- In the Request a sales call panel, enter your contact information, such as first and last name, email address, and phone number.
- Agree to the terms specific to the selected country.
- Select Submit .

## Change Payment Method Before or After an Upgrade

If you have a Free Tier account that you are[upgrading](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/changingpaymentmethod.htm#To_upgrade_to_PayasYouGo)to Pay As You Go, or already upgraded to a Pay As You Go account, you can change your payment method information.
Note  
  
Only Pay As You Go accounts, or Free Tier accounts that are upgrading to Pay As You Go, are allowed to update credit card information.
- Open the navigation menu and select Billing &amp; Cost Management . Under Billing , select Upgrade and Manage Payment . The Manage Payment page is displayed.
Note  
  
If you already upgraded to Pay As You Go, the Manage Payment page title is displayed. Although the left menu always is Upgrade and Manage Payment , the page title shows Upgrade if your account is a Free Tier account, or Manage Payment if you have already upgraded.
- Under Payment Method , click Change Payment Method . The Oracle Payment method box is displayed.
- Under Add a new payment method , click Credit Card .
- Enter your credit card details and click Finish . A confirmation is displayed.
- Click Close . A notification is displayed that your payment details were updated.

## Deleting Your Account

You can[delete your account](https://docs.oracle.com/iaas/Content/General/Tasks/deleting_tenancy.htm)
