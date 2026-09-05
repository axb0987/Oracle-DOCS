# Removing Domains
- Source: https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domain.htm
- Fetched: 2026-09-05 02:11 CDT

# Removing Domains

Release a domain, making it available to be claimed again by another tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domain.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domain.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domain.htm#)
- 

To remove a domain:
- On the Domain Management page, find the domain that you want to work with. If you need help finding the list page, see[Listing Domains](https://docs.oracle.com/en-us/iaas/Content/General/domain/list-domain.htm).
- From the Actions menu for the domain, select Remove Domain . A confirmation is displayed confirming which domain you're removing.
- Select Remove Domain . The Status field changes to Releasing . The status changes to Released after the[work request](https://docs.oracle.com/en-us/iaas/Content/General/domain/../Concepts/workrequestoverview.htm)is complete, and will be removed from the Domain Management page after seven days.
- 

Use the[oci organizations domain delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/domain/delete.html)command and required parameters to remove a domain:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteDomain](https://docs.oracle.com/iaas/api/#/en/organizations/latest/Domain/DeleteDomain)
