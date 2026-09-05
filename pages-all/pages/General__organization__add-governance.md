# Adding Governance to Tenancies
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm
- Fetched: 2026-09-05 02:11 CDT

# Adding Governance to Tenancies

Use governance rules to configure and attach controls to tenancies in your organization. When a governance rule is attached to a tenancy, a corresponding resource is created and then locked in the target tenancy.

A governance rule is a type of enforcement that a parent tenancy creates that allows governing a resource on the child tenancy. The parent tenancy creates the governance rules, whereby they can be targeted to one or more child tenancies. After being set, the governance rule enforcements become locked , so that users within the child tenancy aren't permitted to modify the rule. As a result, a lock icon appears in the interface of such resources.

For example, if a parent tenancy created an allowed regions governance rule for a child tenancy, the child tenancy is prevented from subscribing to other regions on the Region Management page. For quota policies, on the child tenancy's Quota Policies page the quota name has an adjacent lock icon, and on the quota policy details page, a message indicates that the resource was created and locked by the parent tenancy using governance rules. To change the rule, the parent must unlock it and change it. For more information, see[Resource Locking](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resource_locking.htm).

Using governance rules, you can enforce the following controls:
- Allowed regions : One or more regions that the targeted tenancies are allowed to subscribe to. Set an allowable list of regions as permitted by your compliance standards.
Note  
  
If a targeted tenancy is already subscribed to a region not on the allowed regions list, the tenancy remains subscribed to that region, and resources can still be deployed in that region.
- Quota policies : Set a resource quota to limit the number of resources within a service, or disable certain services. Such quotas can be set at the tenancy level, for example:
```

```

- Tags : Define[tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm)throughout your organization. You can share a tag namespace for consistent tagging, or define a tag default to ensure that all resources are tagged.
Note  
  
When you update a resource (such as a tag namespace) in a parent tenancy that was used to create a governance rule, you must also update the governance rule for the changes to propagate to child tenancies.

## Using the Console

You can perform the following governance rules tasks:
- [Creating a Governance Rule and Attaching It to a Tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-createattachrule.htm)
- [Attaching a Governance Rule to a Tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-attachruletenancy.htm)
- [Getting a Governance Rule's Details](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-getruledetails.htm)
- [Editing a Governance Rule](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-editrule.htm)
- [Deleting a Governance Rule](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-deleterule.htm)
- [Changing the Governance Rule Attachment Method from the Parent Tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-changeattachmethod.htm)
- [Detaching a Governance Rule from a Tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-detachrule.htm)
- [Opting In Tenancies to Use Governance Rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-optinuserules.htm)

## Using the CLI

Use the[oci organizations governance organization-tenancy add](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/governance/organization-tenancy/add.html)command and required parameters to add governance rules to a tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Using the API

Run the[AddGovernance](https://docs.oracle.com/iaas/api/#/en/organizations/latest/OrganizationTenancy/AddGovernance)
