# Tags and Tag Namespace Concepts
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm
- Fetched: 2026-09-05 03:07 CDT

# Tags and Tag Namespace Concepts

Oracle Cloud Infrastructure supports two kinds of tags: free-form tags and defined tags. By creating and applying tags, you can retrieve lists of resources tagged with specific keys from any service that supports tagging.
Tip  
  
Watch a video to introduce you to the concepts and features of tagging:[Introduction to Tagging](https://www.youtube.com/watch?v=7l5vQtxJFFE).

## Required IAM Policy

If you're in the Administrators group, then you have the required access for managing tag namespaces and tags.

For more policy samples specific to working with tags and tag namespaces, see[Required Permissions for Working with Defined Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#Who).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). If you want to dig deeper into writing policies for groups or other IAM components, see[Details for IAM without Identity Domains](https://docs.oracle.com/iaas/Content/Identity/Reference/iampolicyreference.htm).

## Overview of Tags and Tag Namespaces

Defined tags provide more features and control than free-form tags. Before you create a defined tag key, you first set up a tag namespace for it. You can think of the tag namespace as a container for a set of tag keys.

When you create the tag key definition, you must choose the type of value (which also determines how the user applying the tag adds the value):
- You can leave it empty so that a user can fill in the value.
- You can create a list of values so that the user must choose from those values.

Note  
  
The allowed characters for tag namespaces and keys are printable ASCII, except U+0020 space (" "), and U+002E full stop ("."). Namespace and key names cannot be empty.

Avoid entering confidential information.

To apply a defined tag to a resource, a user first selects the tag namespace, then the tag key within the namespace, and then they can assign the value. If the tag key contains a blank value, the user can type in a value or leave it blank. If the tag key contains a list, the user must select a value from the list.

Defined tags support policy to allow you to control who can apply your defined tags. The tag namespace is the entity to which you can apply policy. Administrators can control which groups of users are allowed to use each namespace.

The following diagrams illustrate defined tags. Two tag namespaces are set up: Operations and HumanResources. The tag keys are defined in the namespaces. Within each namespace, the tag keys must be unique, but a tag key name can be repeated across namespaces. In the example, both namespaces include a key named "Environment."

[

The first instance is tagged with two tags from the Operations tag namespace, indicating that it belongs to the Operations production environment and the Operations project "Alpha". The second instance is tagged with tags from both the HumanResources tag namespace and the Operations tag namespace, indicating that it belongs to the HumanResources "Production" environment, the HumanResources cost center "42", and also the Operations project "Beta".

[

## Working with Standard Tags

To reduce the complexities of creating and managing tags, Oracle Cloud Infrastructure Tagging provides you with templates of standard tag namespaces and tag definitions.

You can use this template to create a tag namespace and bring consistency across your tenancy.

For more information, see[Understanding Standard Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/../Concepts/understandingstandardtags.htm). To know how to import standard tags using the console, see[Import Standard Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_import-standard-tags.htm).

## Working with Defined Tags

You must set up the tag namespace and tag keys in your tenancy before users can apply a defined tag to a resource. As part of the setup process, you must also grant permissions to the user groups that need to use the namespace.
Note  
  
Tag namespaces and tag key definitions beginning with "oci" and "orcl" are reserved for internal use.

Features of defined tags include:
- Consist of a tag namespace, a key, and a value.
- The tag namespace and tag key definition must be set up in your tenancy before users can apply a defined tag to a resource.
- You can create the tag key with either a tag value type of string (for the user to add a value or leave blank) or a list of values (from which the user must choose).
- When applying a defined tag, users select from the list of tag keys.
- Users can apply a defined tag during resource creation or to an existing resource.
- Defined tag keys are case insensitive.
- Defined tag values are case sensitive. For example, "alpha" and "Alpha" are distinct values.
- You can use tag variables.
- You can create a list of predefined variables to associate with a tag key. Users that apply the tag to a resource must select a value from the list you create.

Tag administrators create and manage defined tags, and users apply these tags to resources. Use IAM policy to select tag administrators who can create tags. Grant all other users in the tenancy only the ability to apply tags.

### Required Permissions for Working with Defined Tags

To apply, update, or remove defined tags for a resource, a user must be granted permissions on the resource and permissions to use the tag namespace.

Users must be granted`use`access on the tag namespace to apply, update, or remove a defined tag for a resource.

Some example policies for tag namespaces:

To allow a group to simply view the tag namespaces in the tenancy (or in a compartment) requires`inspect`access:

```

```

Important  
  
To apply tags to a resource when using the Console, a user must have permissions to`inspect tag-namespaces in tenancy`. If the user does not have this permission, the list of tag namespaces cannot be presented to the user in the dialog menu.

To allow a group to read the tag definitions contained in tag namespaces requires`read`access:

```

```

To allow a group to apply, update, or remove a defined tag for a resource requires the`use`access on the tag namespace:

```

```

To allow usage of a specific tag namespace or namespaces, use a`where`clause with the`target.tag-namespace.name`variable. For example:

```

```

or to specify multiple tag namespaces:

```

```

To manage tag namespaces and the tag definitions in them, requires`manage`access:

```

```

In addition to the permissions to work with the tag namespace, to apply or remove defined tags on a resource you must have the update permission for the resource. For many resources, the update permission is granted with the`use`verb. For example, users who can[use instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)in CompartmentA can also apply, update, or remove defined tags for instances in CompartmentA.

Some resources don't include the update permission with the`use`verb. To allow a group to apply, update, or remove defined tags for these resources without granting the full permissions of`manage`, you can add a policy statement to grant only the &lt;RESOURCE&gt; _UPDATE permission from the`manage`verb. For example, to allow a group NetworkUsers to work with defined tags with VCNs in CompartmentA, you could write a policy like:

```

```

The`inspect`permission for a resource grants permissions to view defined tags for that resource. For example, users who can`inspect`instances can also view any defined tags applied to the instance.

For information about resource permissions, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference.htm).

### Example Scenario

Your company has an Operations department. Within the Operations department are several cost centers. You want to be able to tag resources that belong to the Operations department with the appropriate cost center.
- Create a tag namespace definition called Operations.
- In the Operations namespace, create a tag key definition called CostCenter.

Alice already belongs to the group[InstanceLaunchers](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). Alice can manage instances in CompartmentA. You want Alice and other members of the InstanceLaunchers group to be able to apply the Operations.CostCenter tag to instances in CompartmentA.

To grant the InstanceLaunchers group access to the Operations tag namespace (and only the Operations tag namespace), add the following statements to the[InstanceLaunchers policy](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm):

```

```

Alice can now apply the Operations.CostCenter tag to resources in CompartmentA.

## Inheriting Compartment Tags

The child compartments and their resources in metering services such as Cost Analysis, Usage Reports, and Budget, inherit the defined tags applied to a compartment. However, if there is a conflict between the inherited tags and the tags applied directly to the resources or the child compartments, the tags applied to the resources take precedence over the inherited tags. You can dynamically apply defined tags to resources in a compartment.

For example, consider a tenancy called TenancyA with TagKey1=TagValueP and a compartment called Compartment P with TagKey3=TagValueQ and TagKey4=TagValueS . You have a compute instance in Compartment P with TagKey2=TagValueR , TagKey3=TagValueT . When the tag inheritance logic is applied, the following tags are applied to the compute instance: TagKey2=TagValueR , TagKey3=TagValueT , TagKey4=TagValueS . The resource has inherited TagKey4=TagValueS from the parent compartment. However, the TagKey3 applied to the compute instance overrides the TagKey3 value applied to the parent compartment.

You can filter using inherited tags in Cost Analysis, create budgets with inherited tags, and view these tags in the Usage Reports.

## Retiring Key Definitions and Namespace Definitions

You can retire a tag key definition or a tag namespace definition.

When you retire a tag key definition, you can no longer apply it to resources. However, the tag is not removed from the resources that it was applied to. The tag still exists as metadata on those resources and you can still call the retired tag in operations (such as listing, sorting, or reporting).

## Reactivating Tag Key Definitions and Namespace Definitions

You can reactivate retired tag key definitions and tag namespace definitions.
- When you reactivate a tag key, it is again available for you to apply to resources.
- When you reactivate a tag namespace, you can create new tag key definitions in that namespace. However, if you want to use any of the tag key definitions that were retired with the namespace, you must explicitly reactivate each tag key definition.

## Moving Tag Namespaces to a Different Compartment

You can move a tag namespace to a different compartment. The tag namespace can be active or retired when you move it. When you move the tag namespace, all its tag key definitions are moved along with it.

This functionality is useful if you need to reorganize your compartment hierarchy, or if you need to delete a compartment that contains a retired tag namespace. Remember that you can't delete a compartment that contains resources. A retired tag namespace, even though it is retired, is still an existing resource. Moving the retired tag namespace to a different compartment can enable you to delete its original containing compartment.

To move a tag namespace, you must be allowed to`manage tag-namespaces`in both compartments.

See the procedure[Moving a Tag Namespace to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_move_a_tag_namespace_to_a_different_compartment.htm).

## Deleting Tag Key Definitions and Namespaces

You can delete tag key definitions and tag namespaces.

When you delete a tag key definition, you begin a process that removes the tag from all resources in your tenancy.

If the tag was used with dynamic groups, none of the rules that contain the tag will be evaluated against the tag.

The delete action is asynchronous and initiates a work request. Once you start the delete operation, the state of the tag changes to deleting, and tag removal from resources begins. This process can take up to 48 hours depending on the number of resources that were tagged as well as the regions in which those resources reside. When all tags are removed, the state changes to deleted. You cannot restore a deleted tag. After the tag state changes to Deleted, you can use the same tag name again.
