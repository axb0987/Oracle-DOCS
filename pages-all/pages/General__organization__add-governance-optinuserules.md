# Opting In Tenancies to Use Governance Rules
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-optinuserules.htm
- Fetched: 2026-09-05 02:11 CDT

# Opting In Tenancies to Use Governance Rules

Certain types of tenancies that are already part of the organization can opt in to use governance rules.

- A parent tenancy can opt itself in or out.
- A parent tenancy can request that a child tenancy agree to opt in, or it can opt out a child tenancy.
- A child tenancy can be opted in by the parent tenancy or opt itself in, but a child tenancy can't opt itself out.

You can opt in a child tenancy either while signed in as the parent tenancy, or while signed in as the child tenancy.

To opt in a child tenancy to governance rules while signed in as the parent tenancy :
- On the Tenancies list page, select the child tenancy to open its details page. If you need help finding the list page, see[Listing Organization Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/organizationtenancies-list.htm).
- On the tenancy details page, select Request to join organization governance .

The Request to join organization governance panel opens, where you can request the tenancy to opt in. The recipient must have access to the child tenancy, and has 14 days to respond before the request expires.
- (Optional) Enter the recipient email address, and then confirm it.
- To select governance rules now, select the option and then select the rules to use. Otherwise, select to skip now and select later.
- Select Send request .

A message is displayed indicating that your governance invitation request has been sent, and the child tenancy will use organization governance soon if they decide to accept the request.

On the sending tenancy's Invitations page, you can view the new governance invitation, which has Sent request in the Type field. Select the invitation to view the invitation details page, where you can view its status (initially Pending ), until the receiving tenancy accepts the governance invitation.

The Request field indicates that you requested the tenancy to join organization governance, and that after the recipient tenancy accepts the request, you can create and attach governance rules to the tenancy.

You can also choose to revoke the governance invitation by selecting Revoke . If you revoke the invitation, the invitation details page reloads and switches to a canceled state. The invitation's Status field on the Invitations page also changes to Canceled .
- While signed in as the recipient child tenancy, select the invitation that you want to work with. If you need help finding the list page, see[Listing Recipient Invitations](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-list.htm).

The new governance invitation has a status of Pending , and its type is Received request .
- Select the invitation to open the details page.

The invitation type is Received request , and the Request field indicates that by accepting the request, you're joining organization governance and agreeing to allow the parent tenancy to create and attach governance rules to the tenancy. After joining, only the parent tenancy can remove the tenancy from organization governance.
- On the invitation details page, select the Actions menu and then select Accept . Confirm the acceptance.

Note  
  
If you select Decline , the invitation is rejected and the sending tenancy can send another governance invitation later.

If you accept the invitation, after a few minutes the invitation status changes to Accepted . The invitation status can be viewed on both the sending (parent) tenancy, and the recipient (child) tenancy.

On the sending tenancy's Tenancies list page, the Organization governance field displays Joined , to indicate that the tenancy is now using governance rules. The Governance state field on the tenancy's details page also shows Organization governance , to indicate that the tenancy is using governance rules.

To opt in a child tenancy while signed in as the child tenancy :
- From the Tenancies page, select the tenancy to open its details page. If you need help finding the list page, see[Listing Organization Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/organizationtenancies-list.htm).
- Select Join organization governance .

The Join organization governance panel opens, where you can request the tenancy to opt in. By joining organization governance, you agree to allow the parent tenancy to create and attach governance rules to the child tenancy. After joining, only the parent tenancy can[opt the child tenancy out](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm)of governance rule usage.
- Select Join organization governance .

A notification message is displayed, indicating that your request to opt in to governance has been accepted, and that your tenancy will be joined and participate in organization governance soon.
-
