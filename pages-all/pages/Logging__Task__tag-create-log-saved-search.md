# Tagging a Log Saved Search at Creation
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-create-log-saved-search.htm
- Fetched: 2026-09-05 02:38 CDT

# Tagging a Log Saved Search at Creation

Add metadata to a log saved search when you first create it. This metadata enables you to define keys and values and associate them with resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-create-log-saved-search.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-create-log-saved-search.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-create-log-saved-search.htm#)
- 

This task can't be performed using the Console.
- 

Use the`--defined-tags`or`--freeform-tags`options when running the[oci logging log-saved-search create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log-saved-search/create.html)command to tag a log saved search when you create it:

```

```

- 

Run the[CreateLogSavedSearch](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogSavedSearch/CreateLogSavedSearch)operation to create a log saved search. Include the`definedTags`and`freeformTags`
