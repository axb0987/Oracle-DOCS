# Managing Identity Domains
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/overview.htm
- Fetched: 2026-09-05 02:21 CDT

# Managing Identity Domains

An identity domain is a container for managing users and roles, federating and provisioning of users, secure application integration through Oracle Single Sign-On (SSO) configuration, and SAML/OAuth based Identity Provider administration. It represents a user population in Oracle Cloud Infrastructure and its associated configurations and security settings (such as MFA).

## Overview

Identity domains are similar to other OCI resources. As an administrator, you can create, move, tag, and delete an identity domain. OCI access policies can be written to allow users in a specific domain to access resources in other domains. You can also assign user accounts to predefined administrator roles to delegate administrative responsibilities within a domain. For more information about administrator roles and the privileges associated with each role, see[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../roles/understand-administrator-roles.htm).

You manage identity domains (for example, creating or deleting a domain) using the user interface or the IAM API. You manage resources (for example, users and groups) within an identity domain using the user interface or with the SCIM-based IAM Identity Domains API.

Each tenancy includes a Default identity domain created in the root compartment that contains the initial tenant administrator user and group and a default Policy that allows administrators to manage any resource in the tenancy. The Default identity domain lives with the life cycle of the tenancy and can't be deleted.

You can create additional identity domains within a tenancy. Multiple identity domains are useful when you need separate environments for a single cloud service or application (for example, one environment for development and one for production). For added security, you can configure each identity domain to have its own credentials (for example, Password and Sign-On policies). You can also configure an identity domain for consumer-facing applications and allow consumer users to perform self-registration and social login.

Each identity domain type is associated with a different set of features and object limits. For information to help you decide which domain type is appropriate for what you want to do, see[IAM Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../sku/overview.htm).

Users in identity domains can request access to groups and applications. Users can also perform self-service tasks such as updating profile information, changing passwords, and configuring settings for 2-Step Verification.

## Information for Existing IAM and IDCS Administrators
If you're an existing IAM or IDCS administrator and you don't see identity domains in your regions, read the following information to learn what to expect when the update happens.
- [OCI IAM Identity Domains: What OCI IAM customers need to know](https://www.oracle.com/a/ocom/docs/security/what-oci-iam-customers-should-expect.pdf)
- [OCI IAM Identity Domains: What Oracle IDCS customers need to know](https://www.oracle.com/a/ocom/docs/security/what-idcs-customers-should-expect.pdf)
If you're an existing IAM or IDCS administrator and your region has been updated recently, read the following information to learn about what to expect post update.
- [OCI IAM Identity Domains: What OCI IAM customers need to know](https://www.oracle.com/a/ocom/docs/security/what-oci-iam-customers-should-expect-post-migration.pdf)
- [OCI IAM Identity Domains: What Oracle IDCS customers need to know](https://www.oracle.com/a/ocom/docs/security/what-idcs-customers-should-expect-post-migration.pdf)

This section includes the following overview topics:
- [Introduction](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/introduction-identity-domains.htm)
- [Using Implicit Access for Default Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/implicitManagedAccess-defaultdomain.htm)

You can perform the following tasks related to identity domains:
- [Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm)
- [Listing License Types](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-list-license-types.htm)
- [Creating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm)
- [Getting an Identity Domain's Details](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-details-of-an-identity-domain.htm)
- [Editing an Identity Domain's Details](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-edit-domain-details.htm)
- [Moving an Identity Domain Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-move-resources-to-a-different-compartment.htm)
- [Activating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-activate-a-domain.htm)
- [Deactivating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-deactivate-a-domain.htm)
- [Changing an Identity Domain's Type](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-change-identity-domain-type.htm)
- [Copying an Identity Domain's OCID](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-copy-an-identity-domain-ocid.htm)
- [Replicating an Identity Domain to Multiple Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm)
- [Resetting All Passwords for an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-reset-all-passwords-for-domain.htm)
- [Deleting an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-delete-a-domain.htm)

## Required Policy or Role

To manage identity domain settings, you must have one of the following access grants:
- Be a member of the Administrators group
- Be granted the Identity Domain Administrator role
- Be a member of a group granted`manage`domains

To understand more about policies and roles, see[The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../getstarted/identity-domains.htm#The),[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../roles/understand-administrator-roles.htm), and[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../policieshow/Policy_Basics.htm)
