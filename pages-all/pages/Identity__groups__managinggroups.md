# Managing Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/groups/managinggroups.htm
- Fetched: 2026-09-05 02:22 CDT

# Managing Groups

Use groups with identity domains in IAM to manage user access to applications and resources.

To give a group permissions, you must perform one of the following actions:
- Write at least one policy that gives that group permission to either the tenancy or a compartment. When writing the policy, you can specify the group by using either the unique name or the group's OCID. For information about writing policies, see[Managing Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/../policymgmt/managingpolicies.htm).
- Assign the group to an application.
Note  
  

The All-Domain-Users group is a group that's created by IAM. All identity domain users are assigned to this group by default. If you assign this group to any of your applications, then all users are assigned to these applications indirectly.

For a user, the All-Domain-Users group doesn't appear in the Groups tab because this group is assigned automatically when a new user is created. Also, because this group is created by IAM, and not by an administrator, you can't delete this group.

For information about the number of groups you can have, see[IAM Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/../sku/overview.htm#iam-object-limits).
- [Listing Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/list-groups.htm#enter-topic-id-first-task)
- [Creating a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/create-groups.htm)
- [Adding Users to a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/add-users-to-groups.htm)
- [Removing Users from a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/remove-users-from-groups.htm)
- [Assigning Applications to a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/assign-applications-group.htm)
- [Removing Applications from a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/remove-applications-group.htm)
- [Deleting a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/delete-groups.htm)

## Required Policy or Role

To manage identity domain settings, you must have one of the following access grants:
- Be a member of the Administrators group
- Be granted the Identity Domain Administrator role or the Security Administrator role
- Be a member of a group granted`manage`domains

To understand more about policies and roles, see[The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/../getstarted/identity-domains.htm#The),[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/../roles/understand-administrator-roles.htm), and[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/../policieshow/Policy_Basics.htm)
