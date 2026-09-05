# Declining an Invitation to Join an Organization
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-ignore.htm
- Fetched: 2026-09-05 02:12 CDT

# Declining an Invitation to Join an Organization

Decline an invitation from a parent tenancy to join an organization.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-ignore.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-ignore.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-ignore.htm#)
- 

- On the Invitations list page, select the pending invitation that you want to decline. If you need help finding the list page, see[Listing Recipient Invitations](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-list.htm).
- On the details page, select the Actions menu and then select Decline .
- Confirm that you want to decline the invitation.

On the prospective child tenancy, the received invitation details page reloads and updates the status to Ignored .
- 

Use the[oci organizations recipient-invitation ignore](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/recipient-invitation/ignore.html)command and required parameters to decline a recipient child tenancy invitation:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[IgnoreRecipientInvitation](https://docs.oracle.com/iaas/api/#/en/organizations/latest/RecipientInvitation/IgnoreRecipientInvitation)
