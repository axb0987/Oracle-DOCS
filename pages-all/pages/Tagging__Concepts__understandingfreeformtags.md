# Understanding Free-form Tags
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm
- Fetched: 2026-09-05 03:06 CDT

# Understanding Free-form Tags

Oracle Cloud Infrastructure supports two kinds of tags: free-form tags and defined tags. This topic describes free-form tags.

Because free-from tags are limited in functionality, Oracle recommends that you only use them to try out the tagging feature in your system when you are first getting started with tagging. For more information about the features and limitations of free-form tags, see[Working with Free-form Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm#workfreeform).

## Required IAM Policy

If you're in the Administrators group, then you have the required access for free-form tags. For more policy samples specific to working with free-form tags, see[Required Permissions for Working with Free-form Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm#IAM-free-form).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). If you want to dig deeper into writing policies for groups or other IAM components, see[Details for IAM without Identity Domains](https://docs.oracle.com/iaas/Content/Identity/Reference/iampolicyreference.htm).

## Overview of Free-form Tags

Free-form tags consist of a key and a value, for example:

Environment: Production

where "Environment" is the key and "Production" is the value.

You can apply multiple free-form tags to a single resource, up to the[limit](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/taggingoverview.htm#limits).

[

## Working with Free-form Tags

Free-form tags consist of a key-value pair and have limited features. To experience the full feature set of tagging, use[defined tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/managingtagsandtagnamespaces.htm).

Features of free-form tags include:
- Consist of a key and a value. Free-form tags do not belong to a namespace.
- You can apply free-form tags during resource creation or to an existing resource.
- Free-form tag keys are case sensitive. For example, "Project" and "project" are distinct keys.
- Free-form tag values are case sensitive. For example, "alpha" and "Alpha" are distinct values.

Limitations of free-form tags include:
- When applying a free-form tag, you can't see a list of existing free-form tags, so you don't know what tags and values have already been used.
- You can't see a list of existing free-form tags in your tenancy.
- You can't use free-form tags to control access to resources. That is, you can't include free-form tags in IAM policies.
- You can't use tag variables in free-form tags.
- You can't use predefined values in free-form tags.

### Required Permissions for Working with Free-form Tags

To apply, update, or remove free-form tags for a resource, you must have the update permission on the resource. For many resources, the update permission is granted with the`use`verb. For example, users who can[use instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)in CompartmentA can also apply, update, or remove free-form tags for instances in CompartmentA.

Some resources do not include the update permission with the`use`verb. To allow a group to apply, update, or remove free-form tags for these resources without granting the full permissions of`manage`, you can add a policy statement to grant only the &lt;RESOURCE&gt; _UPDATE permission from the`manage`verb. For example, to allow a group NetworkUsers to work with free-from tags with VCNs in CompartmentA, you could write a policy like:

```

```

The`inspect`verb for a resource grants permissions to view free-form tags for that resource. Therefore, users who can`inspect`instances in CompartmentA can also view any free-form tags applied to the instance.

For information about resource permissions, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference.htm)
