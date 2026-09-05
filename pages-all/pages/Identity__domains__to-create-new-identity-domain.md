# Creating an Identity Domain
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm
- Fetched: 2026-09-05 02:21 CDT

# Creating an Identity Domain

To create an identity domain in IAM, administrators need to know which identity domain type they want to create, in which compartment to create it, and the new identity domain administrator's sign-in credentials, if needed. The domain types that you're allowed to create are based on your subscription.

The default groups created in a new identity domain are All Domain Users, and Domain Administrators. During identity domain creation, if you create an administrative user for the identity domain, that administrator is placed in the Domain Administrators group. The Domain Administrators group can't be deleted and there must be at least one user in the group. Administrators can hide any identity domain that they create from the sign-in page.

When you create an identity domain, the selected region in the Console becomes the identity domain's home region. For example, if the selected region in the Console is Germany Central (Frankfurt) and you create an identity domain, the identity domain is created in the Frankfurt region as the home region.
Note  
  
Unlike the Default identity domain, additional identity domains aren't automatically replicated to all subscribed regions. If users in these identity domains need to interact with OCI resources in other regions, ensure that you[enable replication for those domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm). Many Oracle services and applications automatically provision an Oracle Apps identity domain which lets you to use IAM to manage access to the subscribed services. For example, if you order a Fusion App, you also get an Oracle Apps identity domain. You can't create Oracle Apps or Oracle Apps Premium identity domains directly.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm#)
- 

- On the Domains list page, select Create domain . If you need help finding the list page, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm).
- On the Create domain panel, enter a display name for the domain using only letters, numerals, hyphens, periods, or underscores. The name can contain up to 100 characters.

Note  
  
Select the display name carefully. Changing the identity domain display name has consequences; for example, bookmarked URLs must be updated to use the new name.
- Enter a description.
- Select one of the available domain types. For information to help you decide which domain type is appropriate for what you want to do, see[IAM Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../sku/overview.htm).
- Select Create an administrative user for this domain to use an administrative user account for this identity domain. Enter the details of the user who you want to administer this identity domain.

Note  
  
Granting users or groups the identity domain administrator role for domains other than the default domain grants them full administrator permissions to only that domain (not to the tenancy). At least one administrator for the identity domain must be granted the identity domain administrator role directly. This is in addition to any identity domain administrator roles granted by group membership. For more information, see[Understanding Administrator Roles](https://docs.oracle.com/iaas/Content/Identity/roles/understand-administrator-roles.htm).
- Verify that the correct compartment is selected.
- Perform one of the following actions depending on what you see:
- Expand Tags and add one or more tags to the domain.
- Select Show advanced options and add one or more tags to the domain.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Next .
- (Optional) Select Enable remote region disaster recovery to enable remote region disaster recovery. Select Next to review the information that you entered for the domain.
You must be subscribed to the paired region to enable remote region disaster recovery. For example, if your home region is US East (Ashburn), then you must be subscribed to US West (Phoenix). For more information, see[Disaster Recovery Region Pairings](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/disaster_recovery_and_domains.htm#disaster_recovery_region_pairings).
- Select Create .
Ensure that the identity domain status is Creating .
- 

Use the[oci iam domain create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/create.html)command and required parameters to create an identity domain:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/CreateDomain)
