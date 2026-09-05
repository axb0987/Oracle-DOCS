# Getting a Sender Invitation's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-get.htm
- Fetched: 2026-09-05 02:12 CDT

# Getting a Sender Invitation's Details

Get information about an invitation sent to a tenancy inviting it to join an organization.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-get.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-get.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-get.htm#)
- 

You can view sender invitation details from both the parent tenancy that sent the invitation and the recipient tenancy that's been invited to join the organization as a child tenancy.

On the Invitations page, select the invitation that you want to work with. If you need help finding the list page, see[Listing Sender Invitations](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-list.htm).

The invitation details page displays the invitation status and other details about the invitation.

The Type field shows invitations (a parent tenancy wants another tenancy to become a child tenancy in the organization), or requests (to use[governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm)). For invitations sent from a parent tenancy inviting a child tenancy, Sent invitation is displayed.
- 

Use the[oci organizations sender-invitation get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/sender-invitation/get.html)command and required parameters to get details about a sender invitation:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetSenderInvitation](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SenderInvitation/GetSenderInvitation)
