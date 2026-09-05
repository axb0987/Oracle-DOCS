# Canceling a Sender Invitation
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-cancel.htm
- Fetched: 2026-09-05 02:12 CDT

# Canceling a Sender Invitation

Cancel an invitation sent to a tenancy to join an organization.

A parent tenancy that sends an invitation to another tenancy to join the organization can decide to later revoke the invitation.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-cancel.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-cancel.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-cancel.htm#)
- 

- Sign in to the parent tenancy as a user who has permissions to manage invitations and subscription sharing.
- On the Invitations page, select the invitation that you want to work with. If you need help finding the list page, see[Listing Sender Invitations](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-list.htm).
- On the details page, select Revoke .
- Confirm the revocation.

On the Invitations list page, the invitation's status changes to Canceled .
- 

Use the[oci organizations sender-invitation cancel](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/sender-invitation/cancel.html)command and required parameters to cancel a sender tenancy invitation:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CancelSenderInvitation](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SenderInvitation/CancelSenderInvitation)
