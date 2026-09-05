# Manage Approvals
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-approvals.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage Approvals

You can manage your approvals using the Oracle Access Governance Console.

## Filter and Sort Approvals

You can filter by request type and sort approvals by requestor name or approval end date. You can also sort approvals by name in the ascending or descending order.

### Filter Approvals

Use the Request type filter to quickly locate approvals by access requests or revision requests.

Access Requests : Within this category, you can select whether it is an extension access request or an access request.

Revision Request : For revision requests, you can apply additional filters based on the type of resource associated with the revision. For example, Identity collections, Organizations, Active identities, or Consumer identities.

### Sort by

Sort approval requests by Respond By date or by Requestor name.

## Approve or Reject Access Requests with Approvals

You can approve or reject access requests as a approver using the Approvals module in Oracle Access Governance. Depending on the use case, you can either approve request indefinitely or limit access by days or hours.

### Approve or Reject a Request

You can approve, reject, or request further clarification on pending access requests.
- In your browser, navigate to the Oracle Access Governance Console.
- Click the Navigation icon, and select My Stuff →Approvals to navigate to the Approvals page. The Approvals page displays the pending access requests requiring approvals.
- For individual request approval,
- To Approve a request, select the tick icon corresponding to a request that you want to approve. A confirmation box is displayed. Alternatively, you can:
- Click the View Details icon for a specific request, and then select Approve . .
- Select the check box corresponding to the request and then select Approve or Reject .
- (Conditional) Select Request information in case additional information is required for this request.
- Select the maximum duration for which you want to grant access for approval:
- Indefinitely : Allows permanent access with no time limits. Access is revoked only if manually revoked or the account is disabled.
- Maximum number of days [1-365] : Enter the maximum number of days to grant access. Access will be revoked after this period.
- Maximum number of hours [1-24] : Enter the maximum number of hours to grant access. Access will be revoked after the specified hours.
- Specific date and time range : Select access start time and access end time to grant access.
- Select Reset to what was requested to approve the original requested access time.

### Approve or Reject Requests in Bulk

You can approve or reject multiple requests in a single action. If applicable, the expiration date for an access remains unchanged. You cannot approve requests tagged as Violations in bulk. You need to individually perform actions on those requests.
- In the My Stuff →Approvals page, select one or more check boxes corresponding to the requests you want to approve or reject.
- Select Approve or Reject .
- Add a justification before confirming your decision.

## Approve Access Requests with Violations

If you have access requests with segregation of duties or low risk access guardrails violations, these will be flagged with the tag Violations .
For access request with Violations , access will be revoked based on the access guardrails configuration or the time limit you set—whichever is less. For example, if you choose a 20-day access period but the access guardrails only allow 2 days for low-risk violations, access will be revoked after 2 days. If the access is revoked due to time limit settings, the Violations remediation behavior doesn't change.

- Go to the My Stuff →Approvals page.
- For access request with the Violations tag, select the View details icon to view request details
- Click the View details link in the Insights section to review the violations.
- In the Time Limits section, select the maximum duration for which you want to grant access for approval:
- Indefinitely : Allows permanent access with no time limits. Access is revoked only if access is manually revoked or the account is disabled.
- Maximum number of days [1-365] : Enter the maximum number of days to grant access. Access will be revoked after this period.
- Maximum number of hours [1-24] : Enter the maximum number of hours to grant access. Access will be revoked after the specified hours.
- Specific date and time range : Select access start time and access end time to grant access
- Select Reset to what was requested to approve the original requested access time.
- Select Approve or Reject .
- For approving, add a justification and select the I understand and accept the violations check box. Violations will be snoozed for the pre-defined number of days. If the violation persists beyond this period, access will be revoked.
- Select Confirm .

## Approve Extension Request

When access is about to expire, users receive a expiring-soon notification based on the Access Bundle settings. If eligible, they can request an extension from the My Access page. Extension requests are marked with the tag Extension request .
You can view the prior approved access and take actions accordingly.

- Go to the My Stuff →Approvals page.
- For access request with the Extension request tag, select the View details icon to view extension request details.
- In the Time Limits section, select the specific date till which you want to extend the access.
- Select Reset to what was requested to approve the original extension time requested.
- Select Approve or Reject .
-
