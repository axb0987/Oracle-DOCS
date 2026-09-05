# Required IAM Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_replicate_vault_required_policies.htm
- Fetched: 2026-09-05 02:35 CDT

# Required IAM Policy

Learn about the policies required to replicate an external key management vault.

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: for a typical policy that gives access to vaults, keys, and secrets, see[Let security admins manage vaults, keys, and secrets](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#sec-admins-manage-vaults-keys). Besides policies for users and groups, you must also write a policy that gives the Vault service the ability to do everything with vaults so it can create and manage vaults on your behalf during replication. For example, the following policy gives permission to the service in all regions realm-wide:

```

```

To restrict permissions to specific compartments, specify the compartment instead. For more information about permissions or if you need to write more restrictive policies, see[Details for the Vault Service](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)
