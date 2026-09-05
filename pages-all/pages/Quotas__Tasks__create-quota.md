# Creating a Quota
- Source: https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/create-quota.htm
- Fetched: 2026-09-05 02:53 CDT

# Creating a Quota

Create a quota for a compartment by defining a policy statement.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/create-quota.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/create-quota.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/create-quota.htm#)
- 

- On the Quota policies list page, select Create quota . If you need help finding the list page, see[Listing Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/list-quota.htm).
- 

In the Create quota policy panel, specify the following information:
- 

Name : Enter a name for the quota. Avoid entering confidential information.
- 

Description : Enter a description.
- 

(Optional) Search for and select the compartment from the list of compartments. The policy is created in that compartment.
- 

Quota policy : Define the quota policy statement. For more information on creating quota policies and statements, see[Quota Policy Quick Start](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/../Concepts/resourcequotas.htm#top__quickstart),[Sample Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/../Concepts/sample_quotas.htm), and[Quota Policy Syntax](https://docs.oracle.com/en-us/iaas/Content/Quotas/Tasks/../Concepts/quota_policy_syntax.htm).
- (Optional) In the Tags section, add one or more tags to the quota policy.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .
Note  
  
New quota policies can take up to 10 minutes to start working.
- 

Use the[oci quota create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits/quota/create.html)command and required parameters to create a quota:

```

```

For example, to create a quota policy that disallows use of outbound email or notification for a tenancy:

```

```

Where`statements.json`is:
```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateQuota](https://docs.oracle.com/iaas/api/#/en/limits/latest/Quota/CreateQuota)
