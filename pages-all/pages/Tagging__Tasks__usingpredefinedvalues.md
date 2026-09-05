# Using Predefined Values
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/usingpredefinedvalues.htm
- Fetched: 2026-09-05 03:07 CDT

# Using Predefined Values

You can create a list of values and associate that list with a tag key definition. When users then apply the tag to a resource, they must select a value from the list of predefined values. Use lists of predefined values to impose limits on the values that users can apply to tags. You can use predefined values with defined tags and default tags.

Note the following limitations:
- You can't create lists of predefined values for free-form tags. See[Understanding Free-form Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/../Concepts/understandingfreeformtags.htm)for information on working with free-form tags.
- Tag variables can't be added to a list of predefined values. See[Using Tag Variables](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/usingtagvariables.htm)for information on working with tag variables.

## Required IAM Policy

Predefined values are a feature of defined tags. To allow users to work with predefined values, use the same IAM policy for working with tag namespaces and tags. For more information, see[Required Permissions for Working with Defined Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#Who).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). If you want to dig deeper into writing policies for groups or other IAM components, see[Details for IAM without Identity Domains](https://docs.oracle.com/iaas/Content/Identity/Reference/iampolicyreference.htm).

## Working with Predefined Values

You can update existing tags to use predefined values.

Every list of predefined values that you create must contain at least one value. Lists can't contain duplicate values or blank entries. With predefined values, users applying tags can't set the value of a tag to`null`. For more information, see[Using the Console](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/usingpredefinedvalues.htm#predefvalconsole).

## Predefined Values and Default Tags

You can use predefined values and default tags to impose limits on the values that users can apply to tags.

Here's how it works:
- You define a list of predefined values for a tag key.
- You create a default tag that uses the key with the list of predefined values and requires that users who create resources in the compartment add the value to the tag.
- Oracle prompts all users creating resources in the compartment to enter a tag value. Because the tag key contains a predefined list that you created, the value the user applies is a value that you trust.

These features help to ensure that new resources contain the values you expect. For more information, see[Managing Tag Defaults](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults.htm).

## Using the Console

You can use predefined values when you create or update a tag key definition. For more information, see[Creating a Tag Key Definition](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/Create_tag_key_definition.htm)and[Updating a Tag Key Definition](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/Update_tag_key_definition.htm).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
- [CreateTag](https://docs.oracle.com/iaas/api/#/en/identity/latest/Tag/CreateTag)- creates a tag key definition
- [UpdateTag](https://docs.oracle.com/iaas/api/#/en/identity/latest/Tag/UpdateTag)
