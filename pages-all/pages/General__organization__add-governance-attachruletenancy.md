# Attaching a Governance Rule to a Tenancy
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-attachruletenancy.htm
- Fetched: 2026-09-05 02:11 CDT

# Attaching a Governance Rule to a Tenancy

Attach an existing governance rule to one or more tenancies.

For more information about governance rules, see[Adding Governance to Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm).
- On the Governance Rules list page, select the governance rule that you want to attach to a tenancy. If you need help finding the list page, see[Listing Governance Rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/list-governancerules.htm).

The Tenancies tab or section of the details page lists the following information for every tenancy in the organization:
- Tenancy : The tenancy name.
- Rule status : The rule status, whether Not attached or Attached .
- Organization governance : Indicates whether the tenancy has joined or not joined organization governance. Only tenancies that have joined organization governance can be attached to rules.
- Select one or more tenancies and then select Attach tenancies .

A confirmation is displayed to confirm that you want to attach the rule to the tenancy.
- Select Attach rule .

The governance rule detail page reloads and a new work request is started. After the work request completes, the rule is attached to the tenancy, and the Rule status changes to Attached .

The governance rule now enforces its restrictions on the child tenancies. You can also view the associated governance rules by accessing the Tenancies page in Organization Management . On the Tenancies page, select the tenancy name to open the tenancy details page.
