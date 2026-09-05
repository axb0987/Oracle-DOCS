# Managing Tag Defaults
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults.htm
- Fetched: 2026-09-05 03:06 CDT

# Managing Tag Defaults

This topic describes how to you can specify tags to be automatically applied to resources at creation time.

## Required IAM Policy

If you're in the Administrators group, then you have the required access for managing tag defaults and tag namespaces. For specific policy information for this feature, see[Required Permissions for Working with Tag Defaults](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults.htm#requriedIAM).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). If you want to dig deeper into writing policies for tagging or other IAM components, see[Details for IAM without Identity Domains](https://docs.oracle.com/iaas/Content/Identity/Reference/iampolicyreference.htm).

## Overview of Tag Defaults

Tag defaults let you specify tags that are applied automatically to all resources at the time of creation in a specific compartment. This feature allows you to ensure that appropriate tags are applied at resource creation without requiring the user creating the resource to have access to the tag namespaces. Consider the following example:

Alice is a finance administrator and has access to the restricted tag namespace Finance. Alice can set up a tag default to apply the Finance.CostCenter tag with a value of W1234 to all resources. Eli can create resources but does not have access to the Finance tag namespace. When Eli creates a resource, the Finance.CostCenter tag is automatically applied with a value of W1234. Eli cannot change this tag, and Alice is confident that it is always applied correctly and not changed by the users who create or edit resources.

Tag defaults allow tenancy administrators to create secure permissions boundaries between users concerned with governance and users who need to create and administer resources.

## Where to Manage Tag Defaults

Tag defaults are defined for a specific compartment. In the Console, you manage tag defaults on the Compartment Details page.

## Required Permissions for Working with Tag Defaults

To create or edit a tag default for a compartment, you must be granted the following combination of permissions:
- `manage tag-defaults`access on the compartment where you are adding the tag default
- `use tag-namespaces`access on the compartment where the tag namespace resides
- `inspect tag-namespaces`access on the tenancy

For the full mapping of permissions to API operations, see[Details for IAM without Identity Domains](https://docs.oracle.com/iaas/Content/Identity/Reference/iampolicyreference.htm).

For example, assume you created a set of tag namespaces in CompartmentA. To give a group named TagAdmins access to add tag defaults to CompartmentA, write a policy with the following statements:

```

```

Now assume you also want to allow TagAdmins to create tag defaults in CompartmentA using tag namespaces that reside in CompartmentZ. Add a statement to allow TagAdmins to use tag namespaces in CompartmentZ:

```

```

Now when TagAdmins create tag defaults in CompartmentC, they can use tag namespaces that reside in either CompartmentA or CompartmentZ.

## Limits on Tag Defaults

A maximum of 20 tag defaults can be defined per compartment.
Note  
  
When you delete a tag key definition, existing tag defaults based on that tag key definition are not removed from the compartment. Until you delete the tag default in the compartment, the tag default continues to count against your limit of 20 tag defaults per compartment.

See[Limits on Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/../Concepts/taggingoverview.htm#limits)for more limits on tags.

## Working with Tag Defaults

You can only use tag defaults with defined tags. Free-form tags aren't supported for tag defaults.

You can define up to 20 tag defaults per compartment.

After a tag default is created in a compartment:
- The default tag is applied to any new resources created in that compartment.
- Previously existing resources in the compartment aren't tagged retroactively.
- If you change the default value of the tag default, existing occurrences aren't updated.

## Deleting Tag Defaults

- If you delete the tag default from the compartment, existing occurrences of the tag aren't removed from resources.
- When you delete a tag key definition, existing tag defaults based on that tag key definition aren't removed from the compartment. Until you delete the tag default in the compartment, the tag default continues to count against the limit of 20 tag defaults per compartment.

## Required Tag Values

For tag defaults, you must include a tag value, but you have a choice about how the value is applied.
- Default value
- User-applied value

If you use a default value, then you must create it. This value is applied to all resources.

If you specify that a user-applied value is required, then the user creating the resource must enter the value for the tag at the time of resource creation. Users cannot create resources without entering a value for the tag.
Tip  
  
You can use predefined values and user-applied values to ensure that users only apply a value that you trust. See[Using Predefined Values](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/usingpredefinedvalues.htm).
Important  
  

If users try to create resources in the Console without`use`or`manage`permissions for`tag-namespaces`, the Console returns an error message stating "The following tag namespaces / keys are not authorized or not found: 'oracle-tags'."

## Tag Inheritance

The default tag is applied to all resources created in the compartment, including child compartments and the resources created in the child compartments.

Example:
- 

In CompartmentA, you create a tag default, TagA.

Resources (and compartments) created in CompartmentA are automatically tagged with TagA.
- 

In the subcompartment, CompartmentB, you create tag default, TagB.

Resources and compartments created in CompartmentB are automatically tagged with TagA and TagB.
- 

In the sub-subcompartment, CompartmentC, you create tag default TagC.

Resources created in CompartmentC are automatically tagged with TagA, TagB, and TagC.

This example is illustrated in the following graphic:

[

## Overriding Tag Defaults

Tag defaults can be overridden at the time of resource creation by users who have the appropriate permissions to both create the resource and to use the tag namespace.

Example: CompartmentA has a tag default defined to apply CostCenter.Operations="42". Pradeep belongs to a group that grants him permissions to create instances in CompartmentA and also to use tag namespaces in CompartmentA. He creates an instance in CompartmentA, and in the Create Instance dialog, he applies the tag CostCenter.Operations="50". Because he has the appropriate permissions, when the instance is created, the tag default is overridden, and the instance is tagged with CostCenter.Operations="50".

After a resource is created and tagged, users with the appropriate permissions to both update the resource and to use the tag namespace can modify the default tags that were applied at resource creation.

## Tag Defaults and Retired Tags

Retired tags can't be applied to new resources. Therefore, if the tag namespace or tag key specified in a tag default is retired, when new resources are created, the retired tag is not applied. As a best practice, you should delete the tag default that specifies the retired tag.

## Tag Defaults and Tag Variables

You can use tag variables in tag defaults. Tag variables dynamically resolve at resource creation time. For example, you enter a tag variable for principal name as the tag default in a particular compartment.

Operations.CostCenter="`${iam.principal.name}`"

Davis and Garcia each create buckets in that compartment. The buckets that Davis creates include default tags that contain his name as the value, while the buckets that Garcia creates have his name.
```

```

Meanwhile, the tag default still contains the original variables. See[Using Tag Variables](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/usingtagvariables.htm)
