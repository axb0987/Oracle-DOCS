# Understanding Standard Tags
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/understandingstandardtags.htm
- Fetched: 2026-09-05 03:06 CDT

# Understanding Standard Tags

Standard tags are tag namespace templates defined and managed by Oracle which customers can import into a tenancy's root compartment and get started with commonly used tags.

## Required IAM Policy

If you are part of the Administrators group, then you have the required access for managing standard tags. Otherwise, you need permission to manage tags to import and update standard tags. For more policy samples specific to working with tags and tag namespaces, see[Required Permissions for Working with Defined Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/managingtagsandtagnamespaces.htm#Who).

If you are new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). If you want to dig deeper into writing policies for groups or other IAM components, see[Details for IAM without Identity Domains](https://docs.oracle.com/iaas/Content/Identity/Reference/iampolicyreference.htm).

## Standard Tag Namespaces

The following tag namespaces are currently available to import along with their intended use case. For the latest list of tag namespaces, check the import standard tags section on the console. To import standard tags using the console, see[Import Standard Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/managingtagsandtagnamespaces_topic-To_import-standard-tags.htm).

Tag Namespaces Use case Example
Oracle-ApplicationName This tag mentions the type of Oracle workload the resource is being used for
Oracle-Standard Tags are recommended by Oracle to have a consistency across your tenancy
Oracle-Vendor Oracle vendor tags

## Tag Types

Regularly defined tags are of two types - String and Enum. Whereas standard tags have three types of Enum tags:

- String: Accepts any string as a value.
- Immutable Enum: Oracle controls the value list and users cannot modify this list.
- Appendable Enum: The existing values cannot be altered but new ones can be added to the list.
-
