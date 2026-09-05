# Disabling Domain Governance
- Source: https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domaingov.htm
- Fetched: 2026-09-05 02:11 CDT

# Disabling Domain Governance

Disable domain governance on a claimed domain.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domaingov.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domaingov.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domaingov.htm#)
- 

The domain must already be active before you can disable governance.

- On the Domain Management page, find the domain that you want to work with. If you need help finding the list page, see[Listing Domains](https://docs.oracle.com/en-us/iaas/Content/General/domain/list-domain.htm).
- From the Actions menu , select Disable Governance . A Turn off Domain Governance confirmation is displayed, indicating which domains are to be disabled.
- Select Confirm . After refreshing the page, the Status field changes to Disabled to indicate the domain is verified but not governed.

To enable governance, see[Enabling Domain Governance](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domaingov.htm).
- 

Use the[oci organizations domain-governance delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/domain-governance/delete.html)command and required parameters to remove domain governance from a claimed domain:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteDomainGovernance](https://docs.oracle.com/iaas/api/#/en/organizations/latest/DomainGovernance/DeleteDomainGovernance)
