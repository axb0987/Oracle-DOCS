# Accepting an Invitation to Join an Organization
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-accept.htm
- Fetched: 2026-09-05 02:12 CDT

# Accepting an Invitation to Join an Organization

Accept an invitation from a parent tenancy to join an organization.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-accept.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-accept.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-accept.htm#)
- 

To accept an invitation, follow these steps:

- On the Invitations page, select the invitation that you want to work with. If you need help finding the list page, see[Listing Recipient Invitations](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-list.htm).
- On the details page, select the Actions menu and then select Accept . Confirm the acceptance.

By joining the organization, the parent tenancy can manage cost management and reporting (oversee spending), governance rules (create and attach governance rules to the tenancy), and subscription mapping (map and unmap subscriptions to the tenancy).

See the final step of the[Inviting a Tenancy to Join an Organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-create.htm)Console topic for more information on the invitation acceptance process.
- 

Use the[oci organizations recipient-invitation accept](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/recipient-invitation/accept.html)command and required parameters to accept a recipient tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AcceptRecipientInvitation](https://docs.oracle.com/iaas/api/#/en/organizations/latest/RecipientInvitation/AcceptRecipientInvitation)
