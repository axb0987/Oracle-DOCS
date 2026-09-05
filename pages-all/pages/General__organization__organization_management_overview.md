# Organization Management Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_management_overview.htm
- Fetched: 2026-09-05 02:12 CDT

# Organization Management Overview

Use Organization Management to centrally manage many tenancies, invite and create child tenancies, view and map subscriptions, and create and attach governance rules to tenancies in an organization.

With Organization Management, you can add tenancies to an organization, and have those tenancies consume from the primary funded subscription. You can create an isolated tenancy to build workloads, without needing to book a new order.
Two types of tenancies are involved when mapping and using a subscription in Organization Management:
- Parent : Tenancy that's associated with the primary funded subscription, which must be a paid Oracle PaaS and IaaS Universal Credits subscription. The Parent isn't an irreversible administrator nomination. Standalone tenancies are also called Parent. An existing tenancy can be invited later to join the organization as a child and change its default subscription.
- Child : Tenancies that join an organization, whereby the parent manages the child's cost and governance. Child tenancies can either be created as entirely new tenancies, or, existing tenancies can be invited to join the same organization and to change your default subscription.

An organization can have multiple child tenancies, which are managed by the parent tenancy. The parent tenancy can use[Subscription Mapping](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-management.htm)to assign subscriptions to any child tenancy in the organization.

Benefits of Organization Management include the following:
- Share a single commitment to help avoid cost overages and[enable multitenancy cost management](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_cost_reporting.htm). You can analyze, report, and monitor across all linked tenancies in an organization. The parent tenancy can analyze and report across each of its tenancies through[Cost Analysis](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm)and[Cost and usage reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm), and you can receive alerts through[Budgets](https://docs.oracle.com/iaas/Content/Billing/Concepts/budgetsoverview.htm).
- Customers with strict data isolation requirements can use a multitenancy strategy to isolate data and restrict resources across their tenancies.
- Use[governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm)to enforce and govern resources on specific child tenancies, or the entire organization.
Important  
  
SaaS subscription services can be provisioned in the tenancy where the SaaS subscription was activated, which also includes child tenancies.

The remainder of this topic provides an overview of how to use Organization Management to create child tenancies, invite existing tenancies, view and revoke invitations, and how to remap subscriptions to tenancies. Cost reporting features are also described, which you can use to centrally manage cost and usage information across all tenancies in an organization. Using these features you can better manage a multitenancy environment.

To learn more about Organization Management, see the following:
- [Planning Considerations](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_planning.htm)
- [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_required_iam_policy.htm)
- [Assigned Subscription Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/assigned-subscription-management.htm)
- [Child Tenancy Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/child-tenancy-management.htm)
- [Link Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/link-management.htm)
- [Order Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/order-management.htm)
- [Organization Entity Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-entitymanagement.htm)
- [Organization Tenancy Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-tenancy-management.htm)
- [Sender Invitation Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-management.htm)
- [Recipient Invitation Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-management.htm)
- [Subscription Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-management.htm)
- [Subscription Line Item Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-lineitem-management.htm)
- [Subscription Mapping Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-management.htm)
- [Work Request Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-management.htm)
- [Cost Reporting Integration](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_cost_reporting.htm)
- [Support](https://docs.oracle.com/en-us/iaas/Content/General/organization/organizations_support.htm)
- [Troubleshooting Organization Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-troubleshooting.htm)
