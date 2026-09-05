# Tagging a Log Saved Search When Updating
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-update-log-saved-search.htm
- Fetched: 2026-09-05 02:38 CDT

# Tagging a Log Saved Search When Updating

Add metadata to an existing saved search in Logging. This metadata enables you to define keys and values and associate them with resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-update-log-saved-search.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-update-log-saved-search.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-update-log-saved-search.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Saved Searches .
- Under List scope , select the compartment that contains the saved search that you want to tag.
- On the Saved Searches page, select the name of the saved search.
- On the saved search details page, add or edit tags as needed:
- To add one or more tags, select Add tags and enter the tag namespace (for a defined tag), key, and value.
- To edit or remove a tag, select the Tags tab, select the edit icon next to a tag, and change its value or remove it.
- 

Use the`--defined-tags`or`--freeform-tags`options when running the[oci logging log-saved-search update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log-saved-search/update.html)command to tag a log saved search when you update an existing one:

```

```

- 

Run the[UpdateLogSavedSearch](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogSavedSearch/UpdateLogSavedSearch)operation to edit a log saved search. Include the`definedTags`and`freeformTags`
