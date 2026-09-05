# Specifying Versions
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/terraform-specifying-versions.htm
- Fetched: 2026-09-05 02:56 CDT

# Specifying Versions

Specify and pin versions of the OCI Terraform provider and modules for use with Resource Manager.

Terraform, the Oracle Cloud Infrastructure (OCI) Terraform provider, and Terraform modules you call in your configuration files all introduce changes or add new functionality periodically. As these changes are made, new versions are released.

To ensure that your configurations are applied consistently to OCI resources, you can explicitly set the version of these components in Terraform configuration files.

## Provider Version

You can control the version of the OCI Terraform provider that Terraform uses when interacting with OCI resources. This ability is especially helpful when your configuration relies on features introduced with a particular version of the provider or it has only been tested with a particular version of the provider.

You can use the`>=`or`=`operators to specify the version, depending on your use case.

For more information, see[Specifying Provider Requirements](https://developer.hashicorp.com/terraform/language/settings#specifying-provider-requirements).

### Using Terraform v0.12 or earlier

Terraform v0.12 or earlier allowed you to specify`version`within the`provider`block. For example:
```

```

### Using Terraform v0.13

Terraform v0.13 deprecated`version`within`provider`blocks. Instead, versions should be specified within a`required_providers`block. For example:
```

```

## Module Version

In addition to specifying the version of the Terraform CLI and the OCI Terraform provider, you can also specify the version of Terraform modules.

If a module has been upgraded to use a newer version of Terraform core, but you still use an earlier version of Terraform, you can specify a compatible version of the module. If your configurations have only been tested with a specific version of the module, you can specify that version to ensure compatibility.

Modules accept the`version`argument. For example:
```

```

For more information, see[Module Blocks](https://developer.hashicorp.com/terraform/language/modules/syntax)
