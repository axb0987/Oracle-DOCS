# Tagging a Quota When Updating
- Source: https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/tag-quota-update.htm
- Fetched: 2026-09-05 02:53 CDT

# Tagging a Quota When Updating

Add metadata tags to an existing quota. This metadata enables you to define keys and values and associate them with resources.

For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/tag-quota-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/tag-quota-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/tag-quota-update.htm#)
- 

- On the Quota policies list page, select the quota policy that you want to work with. If you need help finding the list page, see[Listing Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/list-quota.htm).
- 
On the quota details page, select the Tags tab and add or edit tags as needed:
- To add one or more tags, select Add , and then enter the tag namespace (for a defined tag), key, and value.
- To edit or remove a tag, select the Actions menu (three dots) for the tag and then select the appropriate option.
- 

Use the`--defined-tags`or`--freeform-tags`options when running the[oci quota update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits/quota/update.html)command to tag a quota when you're updating it:

```

```
For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateQuota](https://docs.oracle.com/iaas/api/#/en/limits/latest/Quota/UpdateQuota)
