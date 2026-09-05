# Configuring IAM Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_configuring_iam_policies.htm
- Fetched: 2026-09-05 02:34 CDT

# Configuring IAM Policies

Configure IAM policies for management External KMS private endpoint, vault and keys.

External KMS enables you to configure IAM policies to manage (create, modify, or delete) External KMS private endpoints, vaults, and keys in a tenancy or specific compartment.

Policy example to manage External KMS private endpoint

Create a policy to manage (create, update and delete) External KMS private endpoints in the tenancy or a specific compartment.
```

```

Examples
```

```

Policy example to manage virtual networks

The External KMS private endpoints need a policy to manage Virtual Networks too. You must create a policy to manage virtual network in the tenancy or a specific compartment.
```

```

```

```

Policy example to read External KMS private endpoints in a tenancy or specific compartment

Create a policy that allows you to read external KMS private endpoints in the tenancy or a specific compartment.
```

```

Examples
```

```

Policy example to list External KMS private endpoints in a tenancy or specific compartment

Create a policy that allows you to list external KMS private endpoints in the tenancy or a specific compartment.
```

```

Examples
```

```

Policy example to manage Vaults

Create a policy that allows a user to manage vaults in a specific compartment.
```

```

Examples
```

```

Policy example to manage Keys

Create a policy that allows a user to manage keys in a specific compartment.
```

```

Examples
```

```

For policies related to vaults and key remain same as OCI KMS. For more information, see[Key Management Service Policies](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

For information about how admins can use IAM policy to manage vaults and keys, see[Configure IAM Policies for Vault and Keys](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)
