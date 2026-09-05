# Accessing Streaming Resources Across Tenancies
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/accessing-streaming-resources-across-tenancies.htm
- Fetched: 2026-09-05 03:05 CDT

# Accessing Streaming Resources Across Tenancies

Write policies that let your tenancy access Streaming resources in other tenancies.

If you're new to policies, see[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm). For information about Streaming permissions, see[Details for the Streaming Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/streamingpolicyreference.htm).

## Cross-Tenancy Policies

Share Streaming resources with another organization that has its own tenancy. This organization could be another business unit in your company, a customer of your company, a company that provides services to your company, and so on. In cases such as these, you need cross-tenancy policies in addition to standard user and service policies.

For general information about cross-tenancy policies, see[Cross-Tenancy Access Policies](https://docs.oracle.com/iaas/Content/Identity/policieshow/iam-cross-domain.htm).

### Source Policies for Streaming

Endorse a group to manage Streaming resources in the destination tenancy.

The source administrator creates policy statements that endorse a source IAM group allowed to manage resources in the destination tenancy.

Here is an example of a broad policy statement that endorses the IAM group`StreamingAdmins`group to do anything with all Streaming resources in any tenancy:

```

```

To write a policy that reduces the scope of tenancy access, the destination administrator must provide the destination tenancy OCID. Here is an example of policy statements that endorse the IAM group`StreamingAdmins`group to manage Streaming resources in the DestinationTenancy only:

```

```

### Destination Policies for Streaming

Admit a group to manage Streaming resources in the destination tenancy.

The destination administrator creates policy statements that:
- Define the source tenancy and IAM group that is allowed to access resources in your tenancy. The source administrator must provide this information.
- Admit those defined sources to access Streaming resources that you want to allow access to in your tenancy.

Here is an example of policy statements that endorse the IAM group`StreamingAdmins`in the source tenancy to do anything with all Streaming resources in your tenancy:

```

```

Here is an example of policy statements that endorse the IAM group`StreamingAdmins`in the source tenancy to manage Streaming resources only the`SharedStreams`compartment :

```

```
