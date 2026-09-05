# Managing Tags
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/manage-tags.htm
- Fetched: 2026-09-05 03:03 CDT

# Managing Tags

Update or remove values for defined tags from resources. Assign new defined tag namespaces or tag keys to resources. Or, remove defined tags from resources in bulk.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/manage-tags.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/manage-tags.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/manage-tags.htm#)
- 

These steps assume that you already have resource results. You got resource results by doing one of the following:
- You accessed a resource collection from the home page or according to the instructions in[Getting a Resource Collection's Details](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/get-resource-collection.htm).
- You performed a free text search and selected the Resources category of results according to the instructions in[Performing a Free Text Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_perform_a_free_text_search.htm)
- You ran an advanced resource query according to the instructions in[Running a Custom, Free-Form Query](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_custom_freeform_query_to_find_a_resource.htm).

- (Optional) To further refine the list of resources for which you want to perform bulk actions, select the checkbox next to the resource name in the list of resource results.
- Select Actions .
- Select Manage tags .
- If any resources that you selected can't have their tags managed as part of this bulk action, the Console displays them and the reasons why. Review the list, and then select Next .
- Review the tags that already exist and then do one or more of the following:
- To update the value of a tag key, select Tag value , and then enter a new value.
- To apply a defined tag, remove a defined tag, or leave a defined tag unchanged, select Action , and then select Apply tag to all selected resources , Remove tag from all selected resources , or Do nothing , as appropriate.
- To add another defined tag to the selected resources, select + Another tag , and then select the Tag namespace , Tag key , Tag value , and Action .
- Depending on the option available, either select Review changes or Review .
- Review the list of resources and their proposed tag changes, and then select either Apply updates or Apply changes , depending on the option available.
- To confirm the changes, select Continue .
- Select Close .
- 

Use the[bulk-edit](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag/bulk-edit.html)command and required parameters to bulk edit tags on resources:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[BulkEditTags](https://docs.oracle.com/iaas/api/#/en/identity/latest/Tag/BulkEditTags)
