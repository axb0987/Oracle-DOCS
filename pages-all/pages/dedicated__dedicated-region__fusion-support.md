# Fusion Support
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/fusion-support.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/fusion-support.htm#dcoc-content-body)

# Fusion Support

Use this section to learn how support representatives use Fusion Support to locate, process, create, escalate, update, and close Service Requests (SRs) for Dedicated Region support operations.

Use Fusion Support when a customer request must be managed in the operator support workflow or when an Oracle-facing SR must be created for technical, billing, limit, security, or access-log support. SRs created directly in Fusion Support are not visible to the customer. Use the customer-facing SR or another approved communication path when the customer must receive updates about an Oracle-facing request.

## Fusion Support Operating Model

Use the Fusion Console Service Requests page as the working area for operator-managed SRs and Oracle-facing escalation records. Access Fusion Support from the Operator Console, or sign in directly to the Fusion Console when direct access has already been configured.

Operating Area Use Operational Guidance
Customer-facing SR handling Review and process SRs that customers submit through the Customer Console. Use the SR record to track customer communication, status, attachments, and closure requests. Keep the customer-visible status aligned with the work being performed.
Oracle-facing SR creation Create an SR to contact Oracle Support when the work is not an escalation of an existing customer SR. Select the correct problem type, severity, service or resource details, region context, optional additional details, and a clear problem description.
Oracle-facing escalation Escalate an existing technical, billing, or limit SR when Oracle assistance is required. Use Escalate from the originating SR. After submission, open the Oracle-facing escalation from View Escalation on the original SR.
Security routing Create a Security SR when a technical issue is security-related or when Oracle Support identifies a vulnerability. Do not keep security matters only in a Technical SR. Use the Security problem type so the dedicated security support team is alerted.
Data handling Prevent customer-identifiable information from being submitted to Oracle Support. Review the SR payload, attachments, and problem description before submission, then confirm that no customer-identifiable information is included.

## Locate and Review Service Requests

Locate the SR from the email notification link when available. If the link is not available, open Fusion Support, select Service Requests, and use Find, List, or Advanced Search to locate the request.

Search Method When to Use It Guidance
Find Use when the SR number is known. Enter the support request reference number and open the matching SR from the SR Number column.
List Use when the SR number is not known and a standard queue view is sufficient. Review lists such as All Open Service Requests, My Open Service Requests, Open Service Requests Created by Me, Open Service Requests Not Assigned to a Queue, Open Service Requests Where I Am on the Team, or Unassigned Open Service Requests in My Queue.
Advanced Search Use when a saved search, queue-specific search, or broader record-set filter is required. Create or edit saved searches, select the record set that matches the required status scope, then search or save the search for later use.

## Create Oracle-Facing Service Requests

Create an Oracle-facing SR in Fusion Support when you need Oracle Support assistance and the work is not an escalation from an existing customer SR. Select the problem type that matches the request before entering the remaining fields.

Problem Type When to Use It Required Guidance
Technical Use for technical issues that require Oracle Support and are not security-related. Select the service, service category, service issue type, severity, optional region and availability domain, and a complete problem description. Leave Tenancy OCID and User OCID empty for a new technical SR.
Billing Use for billing issues that require Oracle Support and are not escalated from an existing billing SR. Select Billing as the problem type, select the severity, leave Tenancy OCID and User OCID empty, and provide the billing issue details and regression or reproduction context when available.
Limit Use for a limit request that must be created directly in Fusion Support. Select the limit service category, limit resource item, limit increase value, approval status, severity, optional region and availability domain, and a clear request description. Tenancy OCID and User OCID are prepopulated and not editable.
Security Use when the issue involves a security matter or when a technical SR must be routed to the security support team. Select Security as the problem type, select the affected service details and severity, verify prepopulated OCID fields, and include only the details needed for security triage.
Access logs Use when a customer requests access logs from Oracle Support. Create a Technical SR with Low severity, leave attachments empty, and include access-log template in the problem description.

## Severity Values in Fusion Support

Use the Fusion Support severity values to reflect the operational impact of the request.

Fusion Severity Typical Condition
Critical A critical production system or critical business function is unavailable or unstable, and a contact is available to work the issue 24x7 if needed.
High A critical system or business function has severe loss of service, but operations can continue in a restricted manner and a contact is available during business hours.
Medium A functionality, error, or performance issue affects some operations.
Low A product or service usage question, setup question, or documentation clarification has no immediate operational effect.

## Escalate Customer Service Requests to Oracle Support

Escalate an existing customer SR when Oracle assistance is required to resolve a technical, billing, or limit issue. Open the customer SR in Fusion Support, select Escalate, complete the Oracle-facing Create Service Request form, and submit the escalation.

Escalation Type Required Information Operational Guidance
Technical escalation Severity, service, service category, service issue type, optional region and availability domain, additional details, and problem description. Attachments from the originating SR are not forwarded automatically. Download required files from the original SR and attach them to the escalated SR when forwarding is appropriate.
Billing escalation Severity, attachments when allowed by the workflow, optional additional details, prepopulated Tenancy OCID and User OCID, and problem description. Use when billing assistance or a software issue requires Oracle Support involvement.
Limit escalation Severity, limit service category, limit resource item, limit increase value, optional region and availability domain, attachments when appropriate, additional details, and problem description. Use when Oracle approval, resource review, or support assistance is required for the limit request.
Security escalation path Security problem type, service details, severity, prepopulated OCID fields, optional attachments, additional details, and problem description. Create a Security SR instead of keeping the issue in a Technical SR when the subject is security-related.

After an escalation is submitted, use View Escalation on the original SR to open the Oracle-facing escalation record.

## Manage Status, Messages, and Closure

Maintain the Fusion Support SR status as the request moves between support work, customer action, and closure. Customer Console status values depend on the Fusion Support status selected in the SR.

Fusion Support Status Customer Console Status Use
New PENDING WITH SUPPORT Initial state after a customer submits the SR.
In Progress PENDING WITH SUPPORT Use when support is actively working toward resolution.
Pending With Customer PENDING WITH CUSTOMER Use after sending a customer message and waiting for the customer response.
Close Requested CLOSE REQUESTED Appears after the customer selects Close Ticket. The customer cannot continue interacting with the SR in this state.
Resolved CLOSED Use only when the issue can be treated as closed from the customer perspective, because the customer cannot continue interacting with the SR.
Closed CLOSED Use when the customer has requested closure and the SR is ready to be closed.

To communicate with the customer, open the SR, select Messages, select Compose, select Response, enter the message, keep the Channel value unchanged, and send the response. To communicate with an Oracle Support Engineer on an escalated SR, select Compose, select Internal Note, enter the message, keep the Channel value unchanged, and send the note.

## Manage Attachments

Use attachments only when diagnostic files, screenshots, logs, or supporting documentation are required for technical troubleshooting.

Attachment Area Guidance
Attachment eligibility Attach files only to technical SRs. Do not attach files to limit or billing-related SRs when the workflow does not support attachments.
File size and file type Upload one file at a time. Each file must be 10 MB or smaller. Do not upload unsupported file types such as.exe,.bat,.aspx, or.com.
Private or sensitive files Use the private attachment option when a file contains personal information or protected health information. Submit only the data required for triage.
Retention SR-specific attachments are deleted 7 days after the SR is closed or resolved, even if they still appear in the Operator Console or Fusion Console.
Download and forward Download customer-provided attachments before viewing or forwarding them to an escalated Oracle-facing SR. Attachments from an originating SR are not automatically forwarded to Oracle Support.

## Export Lists and Apply Quick Edits

Use list export and quick edit actions when SR review or queue management requires a saved list or a bulk field update.

Action Use Guidance
Export SR list Export up to 2,000 service requests from the current Find, List, or Advanced Search results. Select Actions, then Export List up to 2000 Records. Fusion Support downloads a ServiceRequests.xls file.
Apply quick edits Update one or more SRs without opening each SR individually. Select the SRs, select Update, add field-value pairs, and submit the update. Available fields include Category Name, Product Description, Severity, and Status.
Saved searches Reuse a filtered SR view for recurring operational review. Create or edit lists from Advanced Search, then save the search after verifying the record set and filters.

## Request Access Logs

Request access logs by creating a Technical SR in Fusion Support with Low severity. Use the access-log request path only when the customer request meets the timing and frequency limits.

Access Log Requirement Guidance
Delivery target Access logs are provided in 3 to 5 business days after the SR is submitted.
Date range Request a maximum duration of one month. The start and end dates cannot be more than 30 days apart.
Lookback limit The requested start date cannot be more than 12 months before the request date.
Frequency A customer can request access logs once per week.
Problem description template Include Access-Log: Request for Access Logs, the justification, log start date, and log end date in the problem description.
Returned fields Completed access logs include values such as User OCID, Service Name, and Event Time UTC.

- [Fusion Support](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/fusion-support.htm#fusion-support)
- [Fusion Support Operating Model](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/fusion-support.htm#fusion-support-operating-model)
- [Locate and Review Service Requests](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/fusion-support.htm#locate-and-review-service-requests)
- [Create Oracle-Facing Service Requests](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/fusion-support.htm#create-oracle-facing-service-requests)
- [Severity Values in Fusion Support](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/fusion-support.htm#severity-values-in-fusion-support)
- [Escalate Customer Service Requests to Oracle Support](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/fusion-support.htm#escalate-customer-service-requests-to-oracle-support)
- [Manage Status, Messages, and Closure](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/fusion-support.htm#manage-status-messages-and-closure)
- [Manage Attachments](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/fusion-support.htm#manage-attachments)
- [Export Lists and Apply Quick Edits](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/fusion-support.htm#export-lists-and-apply-quick-edits)
- [Request Access Logs](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/fusion-support.htm#request-access-logs)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
