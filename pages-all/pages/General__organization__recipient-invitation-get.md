# Getting a Recipient Invitation's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-get.htm
- Fetched: 2026-09-05 02:12 CDT

# Getting a Recipient Invitation's Details

Get information about an invitation sent to a tenancy inviting it to join an organization.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-get.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-get.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-get.htm#)
- 

You can view recipient invitation details from both the parent tenancy that sent the invitation and the recipient tenancy that's been invited to join the organization as a child tenancy.

On the Invitations list page, select the invitation that you want to work with. If you need help finding the list page, see[Listing Recipient Invitations](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-list.htm).

The invitation details page displays the invitation status, and other details about the invitation.

The Type field shows invitations (a parent tenancy wants another tenancy to become a child tenancy in the organization), or requests (to use[governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm)). For invitations received from a parent tenancy inviting a child tenancy, Received invitation is displayed.
- 

Use the[oci organizations recipient-invitation get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/recipient-invitation/get.html)command and required parameters to get the details of a recipient child tenancy invitation:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetRecipientInvitation](https://docs.oracle.com/iaas/api/#/en/organizations/latest/RecipientInvitation/GetRecipientInvitation)
