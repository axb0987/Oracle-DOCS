# Managing Defined Tags for Multiple Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-managing-defined-tags-multiple-resources.htm
- Fetched: 2026-09-05 02:11 CDT

# Managing Defined Tags for Multiple Resources

You can add, update, and remove multiple defined tags for multiple existing resources by using Tenancy Explorer.

To manage defined tags for a resource, you must have permission to use the namespace. See[Required Permissions for Working with Defined Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#Who). For more information about how tagging works and tagging concepts, see[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-managing-defined-tags-multiple-resources.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-managing-defined-tags-multiple-resources.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-managing-defined-tags-multiple-resources.htm#)
- 

- Open the navigation menu and select Governance &amp; Administration . Under Tenancy Management , select Tenancy Explorer .
- Select the resources whose tags you want to update. Optionally, use the Filter by resource type drop-down menu to narrow the list of resources.
- From the Actions menu, select Manage Tags .

The Manage Tags panel opens. The first table displays the tags currently applied to the selected resources. The second table displays the selected resources.
- To add one or more defined tags to the resources: Under the table of existing tags, select Additional Tag and enter the following information:

- Namespace: Select the tag namespace to use.
- Key: Select a key that’s associated with the tag namespace.
- Value: Enter a value or select one from the list. Values are case sensitive.
- To update one or more of the defined tags: Find the tag that you want to update and enter a new value. For Action , select Apply tag to all selected resources.
- To remove one or more of the defined tags: In the list of tags, find the tag that you want to remove. For Action , select Remove tag from all selected resources.
- When you’re done managing tags, select Next .
- Confirm changes, and then select Submit .

The Work Request page launches to show you the status of the work request to add, update, or delete the tags for the resources.
- 

Use the[bulk-edit](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag/bulk-edit-tags-resource-type/list.html)command to add, update, or remove multiple tag key definitions on selected resources:

```

```

Use the[bulk-edit-tags-resource-type](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag/bulk-edit.html)

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

To add, update, or remove multiple tag key definitions on selected resources, see[BulkEditTags .

To list the resource types that support bulk tag editing, see[ListBulkEditTagsResourceTypes .

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm)
