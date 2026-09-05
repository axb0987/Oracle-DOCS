# Enabling Domain Governance
- Source: https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domaingov.htm
- Fetched: 2026-09-05 02:11 CDT

# Enabling Domain Governance

Enable domain governance for a claimed domain.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domaingov.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domaingov.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domaingov.htm#)
- 

When you first[add a new domain](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domain.htm), governance is disabled by default, and its status is set to Pending . After the status has changed to Active , you can then enable or disable governance.
Note  
  
Activating Enable Governance prevents others from creating an OCI account with your verified domain. Oracle notifies you when someone tries to create an account with your domain using[Notifications](https://www.oracle.com/devops/notifications/). If you need to allow others to create an account with your domain, select Disable Governance from the Actions menu . For more information, see[Disabling Domain Governance](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domaingov.htm).

- On the Domain Management page, find the domain that you want to work with. If you need help finding the list page, see[Listing Domains](https://docs.oracle.com/en-us/iaas/Content/General/domain/list-domain.htm).
- From the Actions menu , select Enable Governance . A Turn on Domain Governance confirmation is displayed.
- Agree to the Oracle Notification service rates. For more information, see[Notifications](https://www.oracle.com/devops/notifications/).
- Select Yes, turn on . After refreshing the page, the status changes to Active to indicate the domain is verified and governance is enabled.
- 

Use the[oci organizations domain-governance create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/domain-governance/create.html)command and required parameters to add domain governance to a claimed domain:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateDomainGovernance](https://docs.oracle.com/iaas/api/#/en/organizations/latest/DomainGovernance/CreateDomainGovernance)
