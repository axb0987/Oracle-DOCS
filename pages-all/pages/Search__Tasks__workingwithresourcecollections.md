# Working With Resource Collections
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/workingwithresourcecollections.htm
- Fetched: 2026-09-05 03:03 CDT

# Working With Resource Collections

Save searches that you perform often so that you can access their results more quickly later.

Resource collections show you the results of a saved search. The search criteria that you specify at the time you create the resource collection remains as you saved it. Meanwhile, results update dynamically as resources are added to or removed from the tenancy or when resource attributes change to meet the saved search criteria. Consult the resource collection at any time to see the latest results.

You can keep resource collections personal or publish them in a compartment where others with permissions can access them. You can also perform certain bulk actions on the resources in the resource collection.

Search supports the following tasks for working with resource collections:
- [Listing Resource Collections](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/list-resource-collections.htm)
- [Creating a Resource Collection](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/create-resource-collection.htm)
- [Getting a Resource Collection's Details](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/get-resource-collection.htm)
- [Updating a Resource Collection](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/update-resource-collection.htm)
- [Copying a Resource Collection](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/copy-resource-collection.htm)
- [Deleting a Resource Collection](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/delete-resource-collection.htm)

For more information about performing bulk actions on resources, including those in resource collections, see[Performing Bulk Resource Actions](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/performingbulkresourceactions.htm).

## Required IAM Policy

To use Oracle Cloud Infrastructure resource collections in a compartment, you must be granted security access in a policy (IAM) by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which compartment you should work in. By contrast, resource collections that are personal require no special access. Only the user who created a personal resource collection can do anything with it.

The following policy gives permission to the example group ResourceCollectionAdmins to manage resource collections in the tenancy. The policy gives permission to do anything with the`resource-collections`resource-type in any compartment.
```

```

This statement provides the least restrictive access needed to complete administrative tasks with resource collections, as described later in this section.

You might want to provide access to a group to work with resource collections in specific compartments only. The following policy gives permission to the example group ResourceCollectionUsers to read and update resource collections in a compartment. Access is limited to resources in the specified example compartment.
```

```

For more information about permissions or if you need to write more or less restrictive policies, see[Details for Search](https://docs.oracle.com/iaas/Content/Identity/policyreference/searchpolicyreference.htm). If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm)
