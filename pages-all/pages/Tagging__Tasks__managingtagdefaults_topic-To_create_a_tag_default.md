# Creating a Tag Default
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults_topic-To_create_a_tag_default.htm
- Fetched: 2026-09-05 03:06 CDT

# Creating a Tag Default

Create tag defaults so that they can be applied automatically to all the resources that are created in a specific compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults_topic-To_create_a_tag_default.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults_topic-To_create_a_tag_default.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults_topic-To_create_a_tag_default.htm#)
- 

- On the Compartments list page, select the compartment you want to work with, then select the Tag defaults tab. If you need help finding the list page, see[Listing Tag Defaults](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/../Common/../Concepts/list-tag-defaults.htm).
- On the Tag defaults page, select Create tag default .
- On the Create tag default page, provide the following information:

- Tag namespace : Select the tag namespace.
- Tag key : Select the tag key.
- In the Required Tag Value Options section, select the type of value you want this tag to have. The available options are:

- Default value : Select this option to enter the default value you want this tag to have.
- User-applied value : Select this option if you want users to enter the value when the resources are created.
- Click Create tag default .
- 

Use the[create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag-default/create.html)command and required parameters to create a tag default in a specified compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

To create a tag default, use the[CreateTagDefault](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagDefault/CreateTagDefault)
