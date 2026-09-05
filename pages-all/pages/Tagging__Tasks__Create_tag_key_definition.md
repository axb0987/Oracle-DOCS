# Creating a Tag Key Definition
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/Create_tag_key_definition.htm
- Fetched: 2026-09-05 03:06 CDT

# Creating a Tag Key Definition

Create a tag key definition using the Console, CLI, or API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/Create_tag_key_definition.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/Create_tag_key_definition.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/Create_tag_key_definition.htm#)
- 

- On the Tag namespaces list page, select the namespace that you want to work with. If you need help finding the list page, see[Listing Tag Namespaces](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/../Common/../Concepts/list-tagnamespace.htm).
- On the Tag namespace details page, in the Tag key definitions section, select Create tag key definition .
- In the Create tag definition panel, provide the following information:

- Tag key : Enter the key. The key can be up to 100 characters in length. Tag keys are case insensitive and must be unique within the tag namespace. Avoid entering confidential information.
- Description : Enter a friendly description.
- In the Tag value type section, select one of the following options:

- Static value : Indicates that users can specify any value for this key.
- A list of values : Indicates that users must apply a value from a list you create. When you select this option, the Values box appears. Type the values. Separate multiple values with new lines. You must have at least one value. You can't have blank lines or duplicate values.
- Select Create .
- 

Use the[create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag/create.html)command to create a new tag in specified tag namespace:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

To create a tag key definition, use[CreateTag](https://docs.oracle.com/iaas/api/#/en/identity/latest/Tag/CreateTag)
