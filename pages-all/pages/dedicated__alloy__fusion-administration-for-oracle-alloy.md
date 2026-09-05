# Oracle Alloy and Fusion
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-administration-for-oracle-alloy.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-administration-for-oracle-alloy.htm#dcoc-content-body)

# Oracle Alloy and Fusion

Fusion extends the Oracle Alloy operating model into Oracle-managed applications that support user administration, commercial processing, invoicing, and Oracle-facing support workflows. Use Fusion when a task requires Fusion security administration, customer-account maintenance, order processing, or receivables review that is not completed directly in the Operator Console.

## Fusion Console and Access

Users who have the required access can sign in to Fusion directly by using the provisioned URL and credentials, or they can open Fusion from the Operator Console. From the Operator Console home page, Fusion Orders, Fusion Invoicing, and Fusion Support open the relevant Fusion work areas in a separate authenticated window. After the initial launch, bookmark the Fusion URL for direct access.

Within Fusion, Security Console under Tools is the control point for user accounts, role membership, and related account-administration actions. The Users page provides search, review, edit, lock, delete, and password-reset workflows for existing accounts. Use the Users page to create implementation users.

## User Administration and Data Access

When you create or update a Fusion user, assign the Oracle Alloy roles that match the operating responsibility, such as billing, pricing, order management, or customer support. If a new user needs the same role set as an existing user, copy the existing user instead of re-creating role assignments manually.

For users who need to open Fusion from the Operator Console, create the corresponding account in the Customer Console as part of the same onboarding flow.

Role assignment alone is not sufficient for Fusion work areas that depend on business-unit or reference-data access. After roles are assigned, complete data access configuration in Setup and Maintenance by using Manage Data Access for Users. Oracle Alloy roles use Alloy Business Unit access. Roles that depend on reference data also require the applicable Common Set or Enterprise Set values before the user can work with the related records.

## Customer, Order, and Subscription Administration

Fusion supports individual customer creation and bulk customer onboarding from a spreadsheet template. Customer setup must establish the customer account, account sites, and bill-to, ship-to, and sold-to address purposes before order entry. Set payment terms on the customer account so that orders can be processed without avoidable validation errors.

Subscription orders are created in the Order Management work area by using Alloy Business Unit and the Subscription Services order type. The order flow captures the customer, item B88206, quantity, contract dates, billing frequency, administrator email, commit model, price list change policy, and rate card price list.

Validate the order before submission. Use the Manage Orders work area to retrieve existing orders or copy an order when a new request closely follows an earlier configuration.

When you renew a commitment subscription or convert a pay-as-you-go subscription to a commitment subscription, use an extension order and provide the existing subscription OCID in the additional information for the order line. Set the extension start date at least 48 hours in the future. Reuse the same rate card price list as the existing subscription unless a planned commercial change requires a different pricing arrangement.

## Invoicing and Account Maintenance

Receivables in Fusion is used to review invoices after invoice data is generated in the Operator Console and finalized in Fusion with tax calculation. Use Billing to review invoice records. Use Manage Transactions to search by customer, transaction, or other invoice attributes.

Fusion also supports account-maintenance actions that affect the downstream commercial workflow. For example, terminate a customer account by setting an account termination date while preserving the record for historical reporting. This approach helps keep billing and audit history intact after the commercial relationship ends.

## Fusion Support Operations

Fusion Support is used for operator-to-Oracle support and for operator administration of customer-originated service requests when the workflow requires Fusion. Service requests created directly in Fusion are not visible to end customers. Customer communications remain in the customer-facing support path while Oracle escalations are managed as separate records.

This separation preserves the operator as the primary point of contact and limits the spread of customer-identifiable information.

Fusion supports direct creation of technical, billing, limit, and security service requests. Fusion also supports escalation of an existing customer request into a separate Oracle support record. When escalation is required, review the title, severity, service categorization, tenancy context, and problem description before submission.

Attachments from the originating request are not forwarded automatically into the Oracle escalation. Download and attach supporting files again when they are needed for diagnosis.

Message handling and status discipline are part of case quality. Use customer responses for end-customer communication and internal notes for Oracle support communication. Keep the service-request status aligned with the current handoff state, and move the case between In Progress, Pending with Customer, Close Requested, Resolved, and Closed as work progresses.

Attachments are limited to supported nonexecutable file types up to 10 MB. Request attachments are deleted 7 days after a request is resolved or closed.

Fusion also supports higher-volume service-request administration, including saved searches, quick edits across multiple requests, list export, and targeted requests for access logs. Submit access-log requests as low-severity technical requests, and specify the requested time range and business justification.

Requested log windows can cover no more than 30 days, must fall within the previous 12 months, and can be requested no more than once per week.

- [Oracle Alloy and Fusion](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-administration-for-oracle-alloy.htm#oracle-alloy-and-fusion)
- [Fusion Console and Access](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-administration-for-oracle-alloy.htm#fusion-console-and-access)
- [User Administration and Data Access](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-administration-for-oracle-alloy.htm#user-administration-and-data-access)
- [Customer, Order, and Subscription Administration](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-administration-for-oracle-alloy.htm#customer-order-and-subscription-administration)
- [Invoicing and Account Maintenance](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-administration-for-oracle-alloy.htm#invoicing-and-account-maintenance)
- [Fusion Support Operations](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-administration-for-oracle-alloy.htm#fusion-support-operations)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
