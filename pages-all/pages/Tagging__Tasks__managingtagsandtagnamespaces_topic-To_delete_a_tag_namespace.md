# Deleting a Tag Namespace
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_delete_a_tag_namespace.htm
- Fetched: 2026-09-05 03:07 CDT

# Deleting a Tag Namespace

Delete a retired tag namespace.

When you delete a tag namespace, the tag key definitions associated with the tag namespace are also deleted. The tag key definitions are removed from any resources that have the tags.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_delete_a_tag_namespace.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_delete_a_tag_namespace.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_delete_a_tag_namespace.htm#)
- 

- On the Tag namespaces list page, find the namespace that you want to work with. If you need help finding the list page, see[Listing Tag Namespaces](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/../Common/../Concepts/list-tagnamespace.htm).
- From the Actions menu for the tag namespace, select Delete tag namespace .

Important  
  
The Delete tag namespace action is enabled only for a retired tag namespace.
- In the Delete tag namespace dialog box, select Delete .
- 

Use the[delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag-namespace/delete.html)command and required parameters to delete a specified tag namespace:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

To delete the tag namespace, you must first delete all of the tag key definitions contained in the tag namespace. Use[DeleteTagNamespace](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagNamespace/DeleteTagNamespace)operation.

To delete a Tag Namespace and all if its tag key definitions, you must first retire the tag namespace. Use[CascadeDeleteTagNamespace](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagNamespace/CascadeDeleteTagNamespace)
