# Removing an Identity Domain Administrator
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/securing/iam-identity-removeadmin.htm
- Fetched: 2026-09-05 02:28 CDT

# Removing an Identity Domain Administrator

Remove a user as an administrator in an identity domain in IAM.
Each identity domain requires at least one administrator which is granted the identity domain administrator role directly and not indirectly. In a direct grant, the role is assigned to the user post creation. The user isn't part of any group which grants the role. In an indirect grant, the role is granted through a group mapping to the Administrator Group.
Important  
  
Before you remove an identity domain administrator, ensure that the identity domain has at least one administrator which is granted the identity domain administrator role directly. If you need to grant a user the identity domain administrator role directly, see[Adding Identity Domain Administrators](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/iam-identity-adding-admin.htm).

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/../domains/to-view-identity-domains.htm).
- Select Administrators .
- On the Administrators list page, select the Actions menu (three dots) next to the user to remove.
- Select Remove .
-
