# Listing Sender Invitations
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-list.htm
- Fetched: 2026-09-05 02:12 CDT

# Listing Sender Invitations

View a list of invitations sent to tenancies inviting them to join an organization.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-list.htm#)
- 

You can view sender invitations from both the parent tenancy that sent the invitation and the recipient tenancy that's been invited to join the organization as a child tenancy.

To view sent invitations, open the navigation menu and select Governance &amp; Administration . Under Organization Management , select Invitations .

The Invitations list page displays the following information:
- Invitation Name : Select the invitation name to go to the invitation details page.
- 

Status : Displays the invitation status. For example, the status is Active when the invitation is received but not yet accepted, and Pending for an invitation that has been sent but not yet accepted.

Following are the possible status states for a sender and recipient invitation:
- Active
- Pending
- Canceled
- Accepted
- Expired
- Failed
- Type : Displays Sent invitation for invitations to join an organization. Sent request or Received request indicates that a request to join[organization governance](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm)was sent or received.
- Created : The UTC creation date and time of the invitation.
- 

Use the[oci organizations sender-invitation list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/sender-invitation/list.html)command and required parameters to view the list of sender tenancy invitations:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListSenderInvitations](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SenderInvitation/ListSenderInvitations)
