# Upgrading Configurations to Terraform v0.12
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/upgrading.htm
- Fetched: 2026-09-05 19:21 CDT

# Upgrading Configurations to Terraform v0.12

Upgrade OCI Terraform provider configurations for Terraform v0.12.

With the release of Terraform v0.12, Oracle Cloud Infrastructure Terraform providers need to be upgraded and some existing configurations might need to be updated as well.

## Upgrading the Terraform Provider

Oracle Cloud Infrastructure (OCI) Terraform provider versions 3.26.0 and below are not compatible with Terraform v0.12. OCI Terraform provider version 3.27.0 is the earliest version that supports Terraform v0.12.
Note  
  
All OCI Terraform provider versions remain compatible with Terraform v0.11 and v0.10.
The simplest way to begin using the latest v0.12-compatible provider from the HashiCorp provider registry is to place an explicit version requirement in your[provider configuration block](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm#provider-definitions), as shown here:

```

```

For guidance using additional version configuration options, see[Provider Versions](https://www.terraform.io/docs/configuration/providers.html#provider-versions).

## Upgrading Terraform Configurations

Some users may find that no changes are needed to run existing Terraform configurations with v0.12.

For configurations that do need to be upgraded, see[Upgrading Terraform configuration](https://www.terraform.io/upgrade-guides/0-12.html#upgrading-terraform-configuration).

### Upgrading configurations while preserving v0.11 compatibility

As recommended in[Upgrading Terraform configuration](https://www.terraform.io/upgrade-guides/0-12.html#upgrading-terraform-configuration), the simplest way to upgrade your configurations is to use the`terraform 0.12upgrade`command. Using the`terraform 0.12upgrade`command to upgrade your configurations, however, renders them incompatible with Terraform v0.11 and earlier.
Caution  
  
Prior to making configuration changes, it is strongly recommended that configuration and state files are backed up using version control or another preferred mechanism.

It may be possible to manually upgrade configurations to work with v0.12 while preserving compatibility with v0.11. Not all possible configurations can be made compatible with both v0.11 and v0.12. This method should only be used as a best-effort to preserve compatibility with v0.11.

The following cases detail where it is possible to convert existing v0.11 usage to be compatible with both v0.11 and v0.12.

[Attributes vs. Blocks](https://docs.oracle.com/iaas/Content/dev/terraform/upgrading.htm#)

In v0.11, it was possible to treat attributes and nested blocks interchangeably. Note how the attribute`metadata`and the nested block`source_details`are both assigned using only braces.
```

```

In v0.12, attributes need to be assigned using the`=`operator while blocks need to be assigned using only braces. Note how the attribute`metadata`is now assigned with`=`. This usage is still compatible with v0.11.
```

```

[Nested blocks with multiple elements](https://docs.oracle.com/iaas/Content/dev/terraform/upgrading.htm#)

In v0.11, it was possible to wrap lists of nested blocks inside`[]`like this example.
```

```

In v0.12, it is required to specify each nested block individually without wrapping it in`[]`. This usage is still compatible with v0.11.
```

```

[Quotes around attribute names](https://docs.oracle.com/iaas/Content/dev/terraform/upgrading.htm#)

In v0.11, it was possible to put quotation marks`"`around attribute names. Note how the`min`and`max`attributes have quotation marks around them.
```

```

In v0.12, quotation marks`"`around attribute names are no longer allowed.
```

```

[Variable names starting with non-alphabetical characters](https://docs.oracle.com/iaas/Content/dev/terraform/upgrading.htm#)

In v0.11, it was possible to specify variable names that begin with non-alphabetical characters.
```

```

In v0.12, variable names must begin with alphabetical characters.
```

```

[Computing list index values](https://docs.oracle.com/iaas/Content/dev/terraform/upgrading.htm#)

In v0.11, division operations often resulted in integer values that could be used as a valid index in a list.
```

```

In v0.12, division operations can result in floating point values that may no longer be valid. To avoid this situation, use the`floor`interpolation to convert floating point values to an index.
```

```
