# Moving a Tag Namespace to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_move_a_tag_namespace_to_a_different_compartment.htm
- Fetched: 2026-09-05 03:07 CDT

# Moving a Tag Namespace to a Different Compartment

Move a tag namespace from one compartment to another.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_move_a_tag_namespace_to_a_different_compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_move_a_tag_namespace_to_a_different_compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_move_a_tag_namespace_to_a_different_compartment.htm#)
- 

- On the Tag namespaces list page, find the namespace that you want to work with. If you need help finding the list page, see[Listing Tag Namespaces](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/../Common/../Concepts/list-tagnamespace.htm).
- From the Actions menu for the tag namespace, select Move tag namespace .
- In the Move resource dialog box, select the destination compartment.
- Select Move tag namespace .
- 

Use the[change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag-namespace/change-compartment.html)command and required parameters to move the tag namespace to the specified compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

To move a Tag Namespace to a different compartment, use the[ChangeTagNamespaceCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagNamespace/ChangeTagNamespaceCompartment)
