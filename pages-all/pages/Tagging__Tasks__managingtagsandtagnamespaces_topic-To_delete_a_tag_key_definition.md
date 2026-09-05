# Deleting a Tag Key Definition
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_delete_a_tag_key_definition.htm
- Fetched: 2026-09-05 03:07 CDT

# Deleting a Tag Key Definition

Delete retired tag key definitions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_delete_a_tag_key_definition.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_delete_a_tag_key_definition.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_delete_a_tag_key_definition.htm#)
- 

- On the Tag namespaces list page, select the namespace that you want to work with. If you need help finding the list page, see[Listing Tag Namespaces](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/../Common/../Concepts/list-tagnamespace.htm).
- On the Tag namespace details page, in the Tag key definitions section, select the tag key definitions you want to delete.
- From the Actions menu, select Delete .

Important  
  
The Delete option is enabled only for retired tag key definitions.
- In the Delete selected tag key definitions dialog box, select Delete .

The tag key definitions that are marked for deletion move to the Deleting state. To track the deletion progress, from the Actions menu at the top of the Tag namespace details page, select View work requests .
- 

Use the[delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag/delete.html)command and required parameters to delete a specified tag definition:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

To delete a tag key definition, use[DeleteTag](https://docs.oracle.com/iaas/api/#/en/identity/latest/Tag/DeleteTag)operation.

To delete multiple tag key definitions within a tag namespace, use[BulkDeleteTags](https://docs.oracle.com/iaas/api/#/en/identity/latest/Tag/BulkDeleteTags)
