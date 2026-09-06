# Migrating a Legacy Provider Source Configuration to the Supported Configuration
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/migrating-legacy.htm
- Fetched: 2026-09-05 19:20 CDT

# Migrating a Legacy Provider Source Configuration to the Supported Configuration

Migrate providers from the legacy`hashicorp/oci`source configuration to`oracle/oci`.

The`required_providers`block of a[Terraform configuration file](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm)might use the legacy`hashicorp/oci`source configuration.

Example:
```

```

This legacy`hashicorp/oci`source configuration won't be supported in the future.

Migrate any legacy source configuration to the current`oracle/oci`source configuration.

- Update the`required_providers`block in the Terraform configuration.

Example:
```

```

To specify a version, add a`version`line.

Example (version 4.55.0):
```

```

- If you use modules, then add the following block to each module.

```

```

To specify a version, add a`version`line (see example in previous step).

For information on providers in modules, see[Providers Within Modules](https://developer.hashicorp.com/terraform/language/modules/develop/providers).
- Run`terraform init`.

The state of the migration attempt is indicated by the response:
- Successful command indicates successful migration.
- The following error indicates failed migration.
```

```

- If the migration failed, then do the following:
- Run`terraform state replace-provider -auto-approve hashicorp/oci oracle/oci`.
- Run`terraform init`
