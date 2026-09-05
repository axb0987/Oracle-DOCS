# Overview of Compartment Quotas
- Source: https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas.htm
- Fetched: 2026-09-05 02:52 CDT

# Overview of Compartment Quotas

Use Compartment Quotas in Oracle Cloud Infrastructure to control resource consumption within compartments.

Compartment quotas give tenant and compartment administrators better control over how resources are consumed in Oracle Cloud Infrastructure, enabling administrators to easily allocate resources to compartments using the Console. Along with[compartment budgets](https://docs.oracle.com/iaas/Content/Billing/Concepts/budgetsoverview.htm), compartment quotas create a powerful toolset to manage your spending in Oracle Cloud Infrastructure tenancies. You can start using compartment quotas from any compartment detail page in the Console.

Compartment quotas are similar to[service limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm). The biggest difference is that service limits are set by Oracle, and compartment quotas are set by administrators, using policies that allow them to allocate resources with a high level of flexibility.

Compartment quotas are set using policy statements written in a simple declarative language that is similar to the IAM policy language.

Three types of quota policy statements are available:

- `set`: Sets the maximum number of a cloud resource that can be used for a compartment.
- `unset`: Resets quotas back to the default service limits.
- `zero`: Removes access to a cloud resource for a compartment.

For an explanation of the anatomy of quota statements, see[Quota Policy Syntax](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/quota_policy_syntax.htm)for more information on quota policy syntax. Also see[Sample Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/sample_quotas.htm)for more information on usage examples.

Some common questions about quotas are the following:
- Question : What are service family names, and where can I find them?

Answer : See[Available Quotas by Service](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Available_Quotas_by_Service.htm). Under each service, the family name is listed.
- Question : What are all the quota names and where can I find them?

Answer : See[Available Quotas by Service](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Available_Quotas_by_Service.htm), which lists all quota names under each service.

Compartment quotas are available on the Console's Limits, Quotas and Usage page, which you can use to automatically generate quota statements.

## Quota Policy Quick Start

As a prerequisite, ensure you have the appropriate permissions to create quotas. See[Authentication and Authorization](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_authentication_and_authorization.htm)for more information.

You can quickly create a quota policy for any resource by using the Console's Limits, Quotas and Usage page.
- On the Limits, Quotas and Usage page, select the service, scope, resource, or compartment that you want to create a quota policy for.
- In the table, select the Actions menu (three dots) and select Create Quota Policy Stub .

This selection allows you to automatically generate a quota policy statement that you can use to create quota policies in the Console's Limits, Quotas and Usage page. For more information, see[Managing Quota Policies](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/managing_quota_policies.htm)and[Sample Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/sample_quotas.htm)
