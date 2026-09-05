# Importing Standard Tags
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_import-standard-tags.htm
- Fetched: 2026-09-05 03:07 CDT

# Importing Standard Tags

Import standard tags using the Console, CLI, or API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_import-standard-tags.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_import-standard-tags.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_import-standard-tags.htm#)
- 

- On the Tag namespaces list page, from the Actions menu, select Import standard tag . If you need help finding the list page, see[Listing Tag Namespaces](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/../Concepts/list-tagnamespace.htm).

On the Import standard tags panel, you can expand the standard tag namespace to view the tag definitions present in that template.
- Select the namespaces that you want to import and select Import . You can import up to five namespaces at a time.
A work request is created. To monitor import status, from the Actions menu, select View work requests .

Note  
  
You can reimport a tag namespace to get the new and updated tag definitions. However, even if a tag definition or the tag namespace is removed from the template, it remains in the tenancy while reimporting the tag namespace.
- 

Use the[import-standard-tags](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag/import-standard-tags.html)command and required parameters to import standard tags:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ImportStandardTags](https://docs.oracle.com/iaas/api/#/en/identity/latest/Tag/ImportStandardTags)
