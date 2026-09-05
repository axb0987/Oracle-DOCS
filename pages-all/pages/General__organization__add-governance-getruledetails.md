# Getting a Governance Rule's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-getruledetails.htm
- Fetched: 2026-09-05 02:11 CDT

# Getting a Governance Rule's Details

Get information about a governance rule in an organization.

On the Governance rules list page, select the rule that you want to view details for. If you need help finding the list page, see[Listing Governance Rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/list-governancerules.htm).

On the details page, the Details tab shows the following information under General information :
- OCID : OCID of the governance rule.
- Created : Created time in UTC format.
- Targeted tenancies : The number of targeted tenancies.
- Attachment method : Attached to specific tenancies or the entire organization.

Under Rule configuration , some information changes depending on whether the rule is for allowed regions, quota policies, or tags:
- Rule type
- (Allowed region rule only) Allowed regions : Lists the allowed regions in the rule.
- (Quota policy rule only) Statement : Shows the quota policy statements for the rule.
- (Tags rule only) Tag namespace : Lists the namespace.
- (Tags rule only) Tag key : Lists the tag key value if one was selected.
- (Tags rule only) Default value : Lists the tag's default value if one was defined.
- (Tags rule only) Cost tracking : Indicates whether the tag is a cost-tracking tag.

The Tenancies tab or section of the governance rule details page lists the following information for every tenancy:
- Tenancy : The tenancy name.
- Rule status : The rule status, whether Not attached or Attached .
- Organization governance : Indicates whether the tenancy has joined organization governance. Only tenancies that have joined organization governance can be attached to rules.

For information about attaching a governance rule to a tenancy, see[Attaching a Governance Rule to a Tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-attachruletenancy.htm)
