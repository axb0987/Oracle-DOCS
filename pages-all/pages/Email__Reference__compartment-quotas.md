# Managing Compartment Quotas
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/compartment-quotas.htm
- Fetched: 2026-09-05 02:00 CDT

# Managing Compartment Quotas

Use compartment quotas in Oracle Cloud Infrastructure Email Delivery to set granular limits on email sending within specific compartments in your tenancy.

Use Compartment Quotas in Email Delivery to set granular limits on email sending within specific compartments in your tenancy.

Using compartment quotas, you can:
- Control how many emails are sent from each compartment.
- Set limits to avoid exceeding your budget for email delivery.
- Restrict unauthorized email sending within compartments.

When sending an email, the Email Delivery service uses the compartment quotas functionality within OCI to check the compartment quotas for the sending compartment. If the quota is exceeded, the email send request is blocked.

For detailed information on existing email delivery limits on tenancies, see[Email Delivery Service Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#Email_Delivery_Limits).

## Email Delivery Quotas

The compartment quotas for the`email-delivery`family are listed below.

Email Delivery Quotas
Name Scope Description
approved-sender-count Regional Number of approved senders
email-domain-count Regional Number of email domains
email-private-endpoint-count Regional Number of private endpoints
max-emails-day Regional Maximum number of emails sent per day
max-message-size Regional Message size
sendrate Regional Number of emails sent per minute

### Example
```

```

## Creating a Quota Policy

Create an email quota policy for a compartment by defining a policy statement.

### Using the Console
- Open the navigation menu and click Governance &amp; Administration . Under Tenancy Management , click Limits, Quotas and Usage .
- Click the Actions menu to the right of the limit name you want to create a quota for, and click Create Quota Policy .
- In the Create Quota Policy dialog box, specify the following:
- Name: Enter a name for the quota. Avoid entering confidential information.
- Description: Enter a description.
- Quota Policy: Define the quota policy statement.
- Under Tags , add one or more tags to the quota policy by entering a tag namespace, key, and value.
- Optional: Select Save as stack to save the quota policy as a stack.
- Select Create Quota Policy .

Examples for defining quota policy:
```

```

For more information on creating quota policies and statements, see[Quota Policy Quick Start](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm#top__quickstart),[Sample Quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/sample_quotas.htm), and[Quota Policy Syntax](https://docs.oracle.com/iaas/Content/Quotas/Concepts/quota_policy_syntax.htm).
Note  
  

New quota policies can take up to 10 minutes to start working.

For more information about quotas, see[Managing Quota Policies](https://docs.oracle.com/iaas/Content/Quotas/Concepts/managing_quota_policies.htm)
