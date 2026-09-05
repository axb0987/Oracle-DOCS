# Creating a Governance Rule and Attaching It to a Tenancy
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-createattachrule.htm
- Fetched: 2026-09-05 02:11 CDT

# Creating a Governance Rule and Attaching It to a Tenancy

Create a governance rule and attach it to one or more child tenancies in your organization.

You can also attach an existing governance rule to a tenancy. See[Attaching a Governance Rule to a Tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-attachruletenancy.htm). For more information about governance rules, see[Adding Governance to Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm).

- Open the navigation menu and select Governance &amp; Administration . Under Organization Management , select Governance Rules .
- Select Create rule .
- On the Create rule panel, enter a name for the governance rule. Avoid entering confidential information.
- From Type , select a governance rule type: Allowed regions , Quota policy , or Tags .
- In the Rule configuration section, enter the following information based on the type of rule you selected:

- If you selected Allowed regions , select one or more regions that the targeted tenancies are allowed to subscribe to. In Description , enter a name for the allowed region rule configuration. Avoid entering confidential information.
- If you selected Quota policy , create a quota policy to attach to the targeted tenancies by adding quota policy statements. For more information about quota creation, syntax, and samples, see[Managing Quota Policies](https://docs.oracle.com/iaas/Content/Quotas/Concepts/managing_quota_policies.htm),[Quota Policy Syntax](https://docs.oracle.com/iaas/Content/Quotas/Concepts/quota_policy_syntax.htm), and[Sample Quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/sample_quotas.htm). In Description , enter a name for the quota policy rule configuration. Avoid entering confidential information.
- If you selected Tags , select a tag namespace from the root compartment to clone onto the targeted tenancies.

To add a default tag to the rule, select the Add default tag checkbox and then select a tag key from the list.

To set a required tag value, select Default value and then enter the value in the Default value field. If the user can set their own tag value, select User-applied value .
- In the Attach rule section, select whether to attach the rule to specific tenancies, or to all current and future tenancies that have joined organization governance (using governance rules).

- If you select Attach to specific tenancies , select one or more tenancies from the Tenancies field. You can also choose to not select any tenancies at this point (such rules have 0 in the Targeted tenancies field on the associated governance rule details page).
- If you select Attach to entire organization , the rule is attached to your tenancy and all your organization's tenancies that join organization governance. The rule attachment applies to both current and future tenancies.
- Select Create rule .

A new governance rule details page opens for the rule you created.

This page shows the overall rule status. You can edit or delete the rule, change the attachment method (target specific tenancies or the entire organization), add tags, view rule details, and attach or detach the rule from tenancies. For each tenancy, you can also view the rule attachment[work request](https://docs.oracle.com/en-us/iaas/Content/General/organization/../Concepts/workrequestoverview.htm)progress. If the attachment failed, select Retry attaching from the Actions menu (three dots) .

The governance rule is now configured and enforces its restrictions on the child tenancies (or if specified, the entire organization and future tenancies that join the organization). You can also view the associated governance rules by accessing the Tenancies page in Organization Management . On the Tenancies page, select the tenancy name to open the tenancy details page.

Under Governance rules , you can view the list of governance rules attached to the tenancy (to include their name and rule type). Select the governance rule name to go to the associated governance rule details page.

Meanwhile, the child tenancy that has attached governance rules can also view the rules on the Governance rules page, but can't interact with the rule, and can only view basic information about it, because the parent tenancy controls the rule configuration.

After the governance rule is created, you can[edit](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-editrule.htm)or[delete](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-deleterule.htm)the rule,[attach](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-attachruletenancy.htm)or[detach](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-detachrule.htm)the rule, or[change](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-changeattachmethod.htm)the rule attachment method (specific tenancies or entire organization). From the parent tenancy, you can also choose to[opt a tenancy in to](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-optinuserules.htm)or[out of organization governance](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm), or from a child tenancy, you can request to[opt in to organization governance](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-optinuserules.htm).

For more information on opting out existing tenancies from governance rules, see[Removing Governance from Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm)
