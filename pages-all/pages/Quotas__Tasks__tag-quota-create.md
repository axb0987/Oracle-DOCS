# Tagging a Quota at Creation
- Source: https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/tag-quota-create.htm
- Fetched: 2026-09-05 02:53 CDT

# Tagging a Quota at Creation

Add metadata to a quota when you first create one. You can define keys and values, and associate them with resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/tag-quota-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/tag-quota-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/tag-quota-create.htm#)
- 

- Begin the steps for creating a quota using the Oracle Cloud Infrastructure Console as described in[Creating a Quota](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/create-quota.htm).
- In the Create quota policy panel, select Add tag and provide values for the following fields. See[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm)for descriptions of these fields.

- Namespace
- Key
- Value

Select Add tag to add another tag. Select X to remove the associated tag.
- 

Use the`--defined-tags`or`--freeform-tags`options when running the[oci quota create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits/quota/create.html)command to tag a quota when you create it:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateQuota](https://docs.oracle.com/iaas/api/#/en/limits/latest/Quota/CreateQuota)
