# Editing a Quota
- Source: https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/update-quota.htm
- Fetched: 2026-09-05 02:53 CDT

# Editing a Quota

Edit a quota's description or policy statement.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/update-quota.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/update-quota.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/update-quota.htm#)
- 

- On the Quota policies list page, select the quota policy that you want to work with. If you need help finding the list page, see[Listing Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/list-quota.htm).
- 

On the quota details page, select Manage quota policy .
- 

In the Manage quota policy panel, edit the description and change the policy, as needed. For more information, see[Quota Policy Quick Start](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/../Concepts/resourcequotas.htm#top__quickstart),[Sample Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/../Concepts/sample_quotas.htm), and[Quota Policy Syntax](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/../Concepts/quota_policy_syntax.htm).
- Select Update .
- 

Use the[oci quota update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits/quota/update.html)command and required parameters to update a quota:

```

```

For example, to update a created quota to allow notifications in a tenancy:

```

```

Where`statements.json`is:
```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateQuota](https://docs.oracle.com/iaas/api/#/en/limits/latest/Quota/UpdateQuota)
