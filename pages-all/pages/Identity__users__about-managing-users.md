# Managing Users
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/users/about-managing-users.htm
- Fetched: 2026-09-05 02:30 CDT

# Managing Users

Create and manage user accounts, including updating and deleting them.

For information about the number of users you can have, see[IAM Identity Domain Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../sku/overview.htm#iam-object-limits).
- [Listing Users](https://docs.oracle.com/en-us/iaas/Content/Identity/users/list-user-accounts.htm)
- [Lifecycle for Managing Users](https://docs.oracle.com/en-us/iaas/Content/Identity/users/lifecycle-managing-users.htm)
- [Creating a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/create-user-accounts.htm)
- [Viewing User Details](https://docs.oracle.com/en-us/iaas/Content/Identity/users/view-user-account.htm)
- [Editing a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/edit-user-account.htm)
- [Deleting a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/delete-user-accounts.htm)
- [Unlocking a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/unlock-user-accounts.htm)
- [Resetting a User Password](https://docs.oracle.com/en-us/iaas/Content/Identity/users/reset-passwords-user-accounts.htm)
- [Resending an Invitation to a User to Activate their Account](https://docs.oracle.com/en-us/iaas/Content/Identity/users/resend-invitations.htm)
- [Editing a User's Capabilities](https://docs.oracle.com/en-us/iaas/Content/Identity/users/edit-users-capabilities.htm)
- [Listing Users](https://docs.oracle.com/en-us/iaas/Content/Identity/users/list-user-accounts.htm)
- [Searching for a User Account](https://docs.oracle.com/en-us/iaas/Content/Identity/users/search-user-accounts.htm)
- [Changing a User's Status](https://docs.oracle.com/en-us/iaas/Content/Identity/users/change-status-user-account.htm)
- [Clearing All Keep Me Signed-In Sessions for a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/clear-signed-in-sessions-for-users.htm)
- [Linking a User to a My Oracle Cloud Support Account](https://docs.oracle.com/en-us/iaas/Content/Identity/users/link-to-mos.htm)
- [Assigning Applications to a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/assign-applications-users.htm)
- [Removing Applications from a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/remove-applications-user-account.htm)
- [Assigning Users to Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/users/assign-users-roles.htm)
- [Adding a User to a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/users/assign-groups-user-account.htm)
- [Removing Users from Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/users/remove-groups-user-account.htm)
- [Resetting Authentication Factors for User Accounts](https://docs.oracle.com/en-us/iaas/Content/Identity/users/reset-authentication-factors-user-accounts.htm)
- [Generating a Bypass Code for a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/generate-bypass-codes-user-accounts.htm)

## Required Policy or Role

To manage identity domain settings, you must have one of the following access grants:
- Be a member of the Administrators group
- Be granted the Identity Domain Administrator role or the Security Administrator role
- Be a member of a group granted`manage`domains

To give this permission to non administrators, you'll need to additionally write policies like the following:

```

```

where you replace GroupA with the name of the group you want to grant the permission to.

To understand more about policies and roles, see[The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../getstarted/identity-domains.htm#The),[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../roles/understand-administrator-roles.htm), and[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../policieshow/Policy_Basics.htm)
