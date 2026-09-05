# Using Tag Variables
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/usingtagvariables.htm
- Fetched: 2026-09-05 03:07 CDT

# Using Tag Variables

You can use a variable to set the value of a defined tag. When you add the tag to a resource, the variable resolves to the data it represents. You can use tag variables in defined tags and default tags.

Note the following limitations:
- You can't use a tag variable as a predefined tag value. See[Using Predefined Values](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/usingpredefinedvalues.htm)for information on working with predefined variables
- You can't use tag variables in free-form tags.

## Required IAM Policy

Tag variables are a feature of defined tags. To allow users to work with tag variables, use the same IAM policy for working with tag namespaces and tags. For more information, see[Required Permissions for Working with Defined Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#Who).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). If you want to dig deeper into writing policies for groups or other IAM components, see[Details for IAM without Identity Domains](https://docs.oracle.com/iaas/Content/Identity/Reference/iampolicyreference.htm).

## Working with Tag Variables

Consider the following example:

Operations.CostCenter="`${iam.principal.name}`at`${oci.datetime}`"

Operations is the namespace, CostCenter is the tag key, and the tag value contains two tag variables`${iam.principal.name}`and`${oci.datetime}`. When you add this tag to a resource, the variables resolve to your user name (the name of the principal that applied the tag) and a time date stamp for when you added the tag.
```

```

The variable is replaced with data at the time that you apply the tag. If you later edit the tag, the variable is gone and only the data remains. You can edit the tag value in all the ways you would edit any other tag value.

To create a tag variable, you must use a specific format.
```

```

Type a dollar sign followed by open and close curly brackets. The tag variable goes between the curly brackets. You can use tag variables with other tag variables and with string values.

## Supported Tag Variables

The following tag variables are supported.

Variable Description
`${iam.principal.name}`The name of the principal that tagged the resource.
`${iam.principal.type}`The type of principal that tagged the resource.
`${oci.datetime}`
