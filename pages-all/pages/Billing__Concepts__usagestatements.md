# Usage Statements
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagestatements.htm
- Fetched: 2026-09-05 01:43 CDT

# Usage Statements

Use the Usage Statements page to view monthly statements of your subscription usage in Oracle Cloud.
Note  
  
Usage statements differ from[Invoices](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm)in the following ways: usage statements don't include taxes, and the usage period might not match the invoice period.

Monthly usage statements show usage for the previous calendar month, and are available in XLSX format. The statements are available only from a[parent tenancy](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm).

Usage statement generation starts on the second day of each month. Customers receive their statements as early as the second day, but always by the third day of every the month.

If a usage statement needs to be updated because of delayed usage, costs, or other changes, a new statement is generated for that month. If a subscription has no usage for a particular month, no usage statement is generated for that month.

## Using the Console

On the Usage Statements page, you can filter by the subscription and usage period, download statements, and specify the email addresses of the users who are authorized to view the statements.
- Open the navigation menu and select Billing &amp; Cost Management . Under Billing , select Usage Statements .
- On the Usage Statements list page, you can filter the displayed usage statements, as needed, by using the Subscription and Usage period filters:
- Subscription : Filter by the subscription ID. By default, all subscriptions are shown.
- Usage period : Filter by the last 3 months, last 6 months, or last 1 year.

Usage statements are listed in the table by file name, format, subscription, usage period, and published date.
- 

To download a statement, select the Actions menu (three dots) and select Download report .

Downloaded statements show the plan number, subscription ID, account type (for example, Pay As You Go), usage period, and total contract value. The statements list active commitments and usage for the parent tenant by product SKU. Active commitments show the commitment ID, total value, starting and ending balance in the usage period, and the start and end date. The parent tenant usage table lists the product SKU, usage metric, unit cost, quantity, expected usage, overage, and the net amount.
- To specify the email addresses of users who are authorized to view the usage statements, select Manage email recipient .
- 

In the Edit email recipients panel, enter the email addresses of up to five users and then select Update .

## Using the API

You can use the following API operations to manage email recipients for usage statements:
- [CreateEmailRecipientsGroup](https://docs.oracle.com/iaas/api/#/en/usage/latest/EmailRecipientsGroup/CreateEmailRecipientsGroup)
- [DeleteEmailRecipientsGroup](https://docs.oracle.com/iaas/api/#/en/usage/latest/EmailRecipientsGroup/DeleteEmailRecipientsGroup)
- [GetEmailRecipientsGroup](https://docs.oracle.com/iaas/api/#/en/usage/latest/EmailRecipientsGroup/GetEmailRecipientsGroup)
- [ListEmailRecipientsGroups](https://docs.oracle.com/iaas/api/#/en/usage/latest/EmailRecipientsGroup/ListEmailRecipientsGroups)
- [UpdateEmailRecipientsGroup](https://docs.oracle.com/iaas/api/#/en/usage/latest/EmailRecipientsGroup/UpdateEmailRecipientsGroup)

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
