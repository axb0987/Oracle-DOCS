# Subscriptions
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/subscriptions.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/subscriptions.htm#dcoc-content-body)

# Subscriptions

Use this section to learn how operators view, export, and manage Dedicated Region subscriptions in the Operator Console, including lifecycle status, subscription resources, commitments, usage statements, and local CSV exports.

Use the Subscriptions workspace when an internal customer subscription must be reviewed, exported, suspended, reinstated, terminated, or reconciled with usage and commitment data. Open Subscriptions from the Operator Console home page under My tools, or use the navigation menu and select Business operations, then Subscriptions. When reviewing the full subscription list, set List Scope to the root compartment.

Subscription Area Use Primary Operator Actions
Subscription list and export Review subscription records and create a local export for reconciliation or operational reporting. Open Subscriptions, set List Scope to the root compartment, review the list, and select Export as CSV when a local copy is required.
Subscription details and resources Inspect subscription-level resources and supporting information for a selected subscription. Select the subscription, open the Subscription details page, and use the Resources menu to review Usage, Rate card, Usage statements, and other available subscription resources.
Usage statements Review customer billing details based on usage charges and download statements when local analysis is required. Open Usage statements, search by statement text or filter by published date, and download the statement as a CSV file when needed.
Commitments Review committed consumption and understand whether usage is covered by active commitments or has moved into overage. Open Commitments, review total active commitments, current usage, and overage, and export the commitment list as a CSV file when required.
Lifecycle status Understand whether a subscription is active, suspended, or terminated and determine the next operational action. Review the status from the Subscriptions page. Reinstate a suspended subscription only when reinstatement criteria are met or the suspension was applied in error.

### Access Subscriptions

Access Subscriptions when subscription status, billing-related subscription data, commitments, usage statements, or exports must be reviewed.
- 

Open the Operator Console.
- 

On the Operator Console home page, under My tools, select Subscriptions. Alternatively, open the navigation menu, select Business operations, and then select Subscriptions.
- 

Under List Scope, select the root compartment when the task requires the full subscription list.
- 

Select a subscription to open the Subscription details page and review the resources available for that subscription.

### View Subscription Resources

Use the Subscription details page to review the resources associated with a specific subscription.
- 

Open Subscriptions from My tools or from Business operations.
- 

Under List Scope, select the root compartment.
- 

Select the subscription that must be reviewed.
- 

On the Subscription details page, use the Resources menu to review Usage, Rate card, and Usage statements. Review other available resources, such as Commitments, when they are present for the subscription.

### View and Export Usage Statements

Use usage statements to review the details of a customer bill that are based on usage charges.
- 

Open Subscriptions from My tools or from Business operations.
- 

Select the subscription.
- 

Under Resources, select Usage statements.
- 

Search for a specific statement by using the search field, or narrow the list by published date.
- 

Download the usage statement as a CSV file when local review, reconciliation, or recordkeeping is required.

### View and Export Commitments

Use Commitments to review the commitment position for a subscription and determine how much usage is covered by active commitments.
- 

Open Subscriptions from My tools or from Business operations.
- 

Select the subscription.
- 

Under Resources, select Commitments.
- 

Review total active commitments, current usage, and overage. Current usage shows consumption covered by active commitments. Overage shows usage that is not covered by active commitments and has been charged as extra consumption.
- 

Export the commitments list as a CSV file when a local copy is needed for reconciliation, chargeback, or audit support.

### Export Subscriptions

Export subscriptions when subscription records must be reviewed locally or shared with approved operational stakeholders.
- 

Open Subscriptions from My tools or from Business operations.
- 

Under List Scope, select the root compartment.
- 

Select Export as CSV to export the subscription data to the local default downloads location.
- 

Use the subscriptions.csv file as a local copy of the subscription list. Exported values include subscription name, subscription number, payment model, status, start date, and end date.

### Manage Subscription Status

Use subscription status to determine whether a customer subscription is in normal operation, under suspension controls, or no longer recoverable through subscription reinstatement.

Status Operational Meaning Operator Guidance
Active The subscription is in the normal operating state. The customer is in compliance and has paid for services. Use this status as the expected baseline for subscriptions that are operating normally.
Suspended The subscription is suspended, commonly because of fraud or nonpayment. Invoices are paused. During the initial five-day grace period, customer resources remain running, but the customer cannot create more resources and cannot access the cloud portal. After the grace period, resources are shut down in a disruptive but recoverable state until the suspension period ends. Reinstate the subscription only when the customer meets reinstatement criteria or when the suspension was applied in error. When reinstated, an automated email notification is sent to impacted customers. If a subscription remains suspended for 30 days, it automatically becomes terminated.
Terminated The subscription has not been reinstated within the suspension period. Customer resources are terminated and reclaimed within 5 to 30 days, depending on the service. Treat termination as nonrecoverable by OCI. Verify that required notifications and internal records are complete before communicating final status to the customer.

Each subscription lifecycle transition sends email notifications to the customer so that suspension, reinstatement, and termination actions remain transparent.

### Subscription Guardrails

Keep subscription administration aligned with customer transparency, auditability, and restricted operational access.

Guardrail Implementation Guidance
Root compartment scope Use the root compartment for full subscription list review and export tasks so the operator can reconcile against the complete subscription inventory.
Status verification Verify the current status on the Subscriptions page before initiating or communicating any lifecycle action. Lifecycle transitions can affect portal access, resource creation, invoicing, and eventual resource reclamation.
Customer notification awareness Account for automated customer email notifications when suspending, reinstating, or terminating a subscription. Coordinate internal communication so messages are consistent with the lifecycle event.
Export control Treat subscriptions.csv, usage statement CSV files, and commitment exports as operational records. Share them only with approved billing, support, or operations stakeholders.
Reconciliation context When reconciling subscription data, retain the subscription name, subscription number, payment model, status, start and end dates, usage statement date, commitment values, and any export filters used.

- [Subscriptions](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/subscriptions.htm#subscriptions)
- [Access Subscriptions](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/subscriptions.htm#access-subscriptions)
- [View Subscription Resources](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/subscriptions.htm#view-subscription-resources)
- [View and Export Usage Statements](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/subscriptions.htm#view-and-export-usage-statements)
- [View and Export Commitments](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/subscriptions.htm#view-and-export-commitments)
- [Export Subscriptions](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/subscriptions.htm#export-subscriptions)
- [Manage Subscription Status](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/subscriptions.htm#manage-subscription-status)
- [Subscription Guardrails](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/subscriptions.htm#subscription-guardrails)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
