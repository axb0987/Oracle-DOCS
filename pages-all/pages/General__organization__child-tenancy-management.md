# Child Tenancy Management
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/child-tenancy-management.htm
- Fetched: 2026-09-05 02:12 CDT

# Child Tenancy Management

As the parent tenancy, you can create new child tenancies to be part of your organization.

Child tenancies that you create consume from your organization's default subscription. If you want a new child tenancy to consume from another subscription, you can remap the created tenancy to another subscription on the Subscription Mapping page.
Caution  
  

SaaS or Multicloud subscription services can be activated in either the parent tenancy or a child tenancy of an organization. Resources against the SaaS or Multicloud subscriptions, however, can only can be provisioned in the tenancy where they were activated.

Tenancies that only have SaaS or Multicloud subscriptions can be invited to become child tenancies of an organization.

You can also attach[governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm)to the new child tenancy during creation, or you can come back later and attach rules. To attach governance rules during child tenancy creation, you can create the governance rules first on the Governance Rules page so that they're available for selection during child tenancy creation.

Created child tenancies inherit the current default limits of the parent tenancy. Child tenancies receive their own set of limits, which aren't shared with other tenancies.
Note  
  
Free Tier or Trial tenancies can't add new child tenancies, or be invited to be part of an organization, unless they're converted to paid first. For more information about upgrading, see[Account Upgrade Overview](https://docs.oracle.com/iaas/Content/Billing/Tasks/changingpaymentmethod.htm#Upgrade).

The following table describes the child tenancy creation and invitation actions that you can perform based on pricing model:

Pricing Model Can Create Tenancies Can Invite Tenancies Can Be Invited
Pay As You Go Yes Yes Yes
Annual Commit Yes Yes Yes
Funded Allocation Yes Yes Yes
Custom Commit Yes Yes Yes
Trial/Free Tier No No No

For step-by-step instructions, see[Creating a Child Tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/child-tenancy-create.htm)
