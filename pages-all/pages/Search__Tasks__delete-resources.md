# Deleting Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/delete-resources.htm
- Fetched: 2026-09-05 03:03 CDT

# Deleting Resources

Delete found resources in bulk rather than individually.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/delete-resources.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/delete-resources.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/delete-resources.htm#)
- 

These steps assume that you already have resource results. You got resource results by doing one of the following:
- You accessed a resource collection from the home page or according to the instructions in[Getting a Resource Collection's Details](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/get-resource-collection.htm).
- You performed a free text search and selected the Resources category of results according to the instructions in[Performing a Free Text Search](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_perform_a_free_text_search.htm)
- You ran an advanced resource query according to the instructions in[Running a Custom, Free-Form Query](https://docs.oracle.com/en-us/iaas/Content/Search/Tasks/queryingresources_topic-To_run_a_custom_freeform_query_to_find_a_resource.htm).

- Do one of the following:
- To delete all resources in the list of results, select the checkbox in the table header in the leftmost column. Repeat this for any remaining pages of results. (You can navigate to the next page of results by selecting the lower right arrow at the bottom of the table.)
- To delete only some resources in the list of results, select the checkbox in the leftmost column next to the display name of each result you want to delete.
- Select Actions .
- Depending on the option available, either select Delete or Delete resources .
- If any resources that you selected can't be deleted as part of a bulk action, the Console displays them and the reasons why. Review the list, and then select Next .
- Review the list of resources that can be deleted as part of the bulk action, and then select Delete resources .
- To confirm, select either Continue or Delete , depending on the option available.
- 

Use the[bulk-delete-resources](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/bulk-delete-resources.html)command and required parameters to delete resources in bulk:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[BulkDeleteResources](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/BulkDeleteResources)
