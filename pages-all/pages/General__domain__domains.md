# Managing Your Domains
- Source: https://docs.oracle.com/en-us/iaas/Content/General/domain/domains.htm
- Fetched: 2026-09-05 02:11 CDT

# Managing Your Domains

Domain Management allows you to register your domains with Oracle Cloud Infrastructure, as being your legitimately owned domain, which blocks others from claiming that domain in the future using new cloud accounts. OCI customers can redirect new user sign-up attempts that use a corporate email address from that customer's domains.

For example, if you work at "Company A" and "companyA" is the domain name, for anyone who comes to Oracle Cloud Infrastructure and tries to create a tenancy with "companyA" in the email domain, such an attempt will be prevented and they will be directed instead to OCI.

As a result, with Domain Management , large enterprises can more easily control their environments, by knowing who is creating tenancies, and can apply corporate policy onto such tenancies. They can securely verify ownership of your domains, and more easily control spending and management of resources.

To learn more about Domain Management , see the following:
- [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/General/domain/domains.htm#domainmanage_required_IAM_policy)
- [Domain Management](https://docs.oracle.com/en-us/iaas/Content/General/domain/domain-management.htm)
- [Domain Governance Management](https://docs.oracle.com/en-us/iaas/Content/General/domain/domaingov-management.htm)
- [Domain Revocation](https://docs.oracle.com/en-us/iaas/Content/General/domain/domain_revocation.htm)

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

To use Domain Management , the following policies are required:
```

```
