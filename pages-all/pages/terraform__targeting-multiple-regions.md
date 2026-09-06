# Targeting Multiple Regions
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/targeting-multiple-regions.htm
- Fetched: 2026-09-05 19:21 CDT

# Targeting Multiple Regions

Use the Oracle Cloud Infrastructure Terraform provider to create resources in multiple regions.

Use a single Terraform configuration to create Oracle Cloud Infrastructure (OCI) resources in multiple regions.

## Create a Provider for Each Region

A Terraform configuration may have only a single OCI Terraform provider block, but to apply configurations to multiple regions, you need to create multiple provider blocks.

A typical OCI Terraform provider block might look like the following:

```

```

Tip  
  
All parameters should be set using variables.

If you want to use more than one region within a single Terraform config, multiple providers are required. Each provider must be given an alias. For example:

```

```

If you want to use more than one region within a single Terraform config, multiple providers are required. Each provider must be given an alias. For example:

```

```

When you sign up for Oracle Cloud Infrastructure, Oracle creates a tenancy for you in one region, which is your home region . The home region has special properties. For example, IAM resources can only be created in your home region. For that reason, you should designate that region with an appropriate alias, like`home`. Use simple aliases for other regions so that users can easily map configurations to the regions that they want (for example,`region2`).
Note  
  
Specific regions (us-phoenix-1, us-ashburn-1, and so on) are not hardcoded into either the`region`or`alias`fields.

### Finding Your Home Region

When deploying to multiple OCI regions, you might want to look up your home region dynamically, so you don't have to explicitly pass the home region as a configuration variable.

One typical use case might require provisioning resources to a specific region using a Terraform configuration that also creates a compartment. Since the compartment must be created in your home region, you could use code like the following to automatically look up the home region:
```

```

## Provision a Resource

To provision a resource in a region, specify the aliased provider name in the resource.

For example:
```

```

## Modules and Multiple Regions

Typically, a module should use only a single region. If more regions are needed, you should use separate modules.

If the config contains multiple providers, the module should specify the provider to use by using the following format:
```

```
