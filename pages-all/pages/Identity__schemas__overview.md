# Customizing Schemas
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/overview.htm
- Fetched: 2026-09-05 02:28 CDT

# Customizing Schemas

Learn how to add, edit, or remove custom schema attributes and change user permissions for out-of-the-box (base) schema attributes.

If you're creating your own user interface for IAM and you don't find a schema attribute that you need from the list of base schema attributes, create one and extend it to the existing schema.

## Required Policy or Role

To customize schemas, you must have one of the following access grants:
- Be a member of the Administrators group
- Be granted the Identity Domain Administrator role or the Security Administrator role
- Be a member of a group granted`manage`domains

To understand more about policies and roles, see[The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/../getstarted/identity-domains.htm#The),[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/../roles/understand-administrator-roles.htm), and[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/../policieshow/Policy_Basics.htm).
You can perform the following schema management tasks:
- [Listing User Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/listing-schema.htm#list-attrib)
- [Creating a Custom User Attribute](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/add-custom-schema-attributes.htm)
- [Editing a User Attribute](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/edit-custom-schema-attributes.htm)
- [Editing a User's Permission for a Base Schema Attribute](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/change-user-permissions-base-schema-attribute.htm)
- [Deleting a Custom Attribute](https://docs.oracle.com/en-us/iaas/Content/Identity/schemas/remove-custom-schema-attribute.htm)
