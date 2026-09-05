# Managing Dynamic Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm
- Fetched: 2026-09-05 02:21 CDT

# Managing Dynamic Groups

Dynamic groups allow you to group compute instances and other resources as "principal" actors (similar to user groups). You can then create policies to permit the resources to[make API calls against services](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/../callresources/callingservicesfrominstances.htm). When you create a dynamic group, rather than adding members explicitly to the group, you instead define a set of matching rules to define the group members. Resources that match the rules are members of the group. For example, a rule could specify that all instances in a particular compartment are members of the dynamic group. The members can change dynamically as instances are launched and terminated in that compartment.

You can perform the following dynamic group management tasks:
- [Working with Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Working_with_Dynamic_Groups.htm)
- [Listing Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/listing-dynamnicgroups.htm)
- [Creating a Dynamic Group](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/To_create_a_dynamic_group.htm)
- [Updating Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Updating_Dynamic_Groups.htm)
- [Updating a Dynamic Group's Description](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/To_update_a_dynamic_groups_description.htm)
- [Updating a Dynamic Group's Matching Rules](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/To_update_a_dynamic_groups_matching_rules.htm)
- [Assigning a Domain Role](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/assign-domain-role.htm)
- [Writing Matching Rules to Define Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm)
- [Using the Rule Builder](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Using_the_Rule_Builder.htm)
- [Deleting a Dynamic Group](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/To_delete_a_dynamic_group.htm)

## Required Policy or Role

To manage identity domain settings, you must have one of the following access grants:
- Be a member of the Administrators group
- Be granted the Identity Domain Administrator role or the Security Administrator role
- Be a member of a group granted`manage`domains

To understand more about policies and roles, see[The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/../getstarted/identity-domains.htm#The),[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/../roles/understand-administrator-roles.htm), and[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/../policieshow/Policy_Basics.htm)
