# Updating Default Value of a Tag Default
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults_topic-To_update_the_default_value_of_a_tag_default.htm
- Fetched: 2026-09-05 03:07 CDT

# Updating Default Value of a Tag Default

Update the default value of a tag default.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults_topic-To_update_the_default_value_of_a_tag_default.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults_topic-To_update_the_default_value_of_a_tag_default.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults_topic-To_update_the_default_value_of_a_tag_default.htm#)
- 

- On the Compartments list page, select the compartment you want to work with, then select the Tag defaults tab. If you need help finding the list page, see[Listing Tag Defaults](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/../Common/../Concepts/list-tag-defaults.htm).
- On the Tag defaults page, select the Actions menu (three dots) to the right of the tag default that you want to update and select Edit tag default .
- In the Edit tag default dialog box, select the type of value you want this tag to have. The available options are:

- Default value : Enter the new default value you want this tag to have.
- User-applied value : Select this option if you want users to enter the value when the resources are created.
- Select Edit tag default .
- 

Use the[update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag-default/update.html)command and required parameters to update a tag default value:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

To update the tag default, use[UpdateTagDefault](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagDefault/UpdateTagDefault)
