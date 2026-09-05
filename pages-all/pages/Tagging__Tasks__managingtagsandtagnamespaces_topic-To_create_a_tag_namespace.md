# Creating a Tag Namespace
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_create_a_tag_namespace.htm
- Fetched: 2026-09-05 03:07 CDT

# Creating a Tag Namespace

Create a tag namespace using the Console, CLI, or API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_create_a_tag_namespace.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_create_a_tag_namespace.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_create_a_tag_namespace.htm#)
- 

- On the Tag namespaces list page, select Create tag namespace . If you need help finding the list page, see[Listing Tag Namespaces](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/../Common/../Concepts/list-tagnamespace.htm).
- On the Create tag namespace page, provide the following information:

- Create in compartment : The compartment in which you want to create the namespace definition.
- Namespace definition name : A unique name for this set of tags. The name must be unique within a tenancy. Tag namespace is case insensitive. You can't change this value later. Avoid entering confidential information.
- Description : A friendly description. You can't change this value later.
- Select Create .
- 

Use the[create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag-namespace/create.html)command to create a tag namespace.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateTagNamespace](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagNamespace/CreateTagNamespace)
