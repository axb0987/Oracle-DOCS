# Applying Configurations
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/applying.htm
- Fetched: 2026-09-05 19:20 CDT

# Applying Configurations

Use the OCI Terraform provider to apply configurations.

After the Oracle Cloud Infrastructure (OCI) Terraform provider is[installed](https://docs.oracle.com/iaas/Content/dev/terraform/installing.htm)and[configured](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm), and you have created Terraform configurations that include the provider and a resource or data source, you can run Terraform against your OCI infrastructure.
Tip  
  
See[Terraform Provider Tutorials](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials.htm)for step-by-step instructions and examples.

## Initializing Terraform

Run the following command from a directory that contains your Terraform configuration files to initialize Terraform:

```

```

Example output:
```

```

If the command results in an error, verify that the OCI Terraform provider is[configured properly](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm).

## Reviewing Changes

Without making any changes to your existing OCI resources, Terraform can return a list of changes that will be made based on your configurations if you choose to apply them. This list is called an execution plan . To view the execution plan, run the following command:

```

```

Example output:
```

```

Review the plan and check whether the changes shown in the plan match your expectations.

### Destructive Changes

Some OCI resources have properties that cannot be updated by Terraform without destroying the existing resource and re-creating it with the new property value. When you run`terraform plan`and attempt to modify a non-updatable property, Terraform indicates what resource will be replaced and what property or properties cannot be updated.

For example, the following execution plan prefixes a resource that will be deleted and re-created with`-/+`and appends the`# forces replacement`comment to the property that cannot be updated:
```

```

Caution  
  
A forced deletion and re-creation of a resource might also result in the replacement of a parent resource. Always run`terraform plan`before you run`terraform apply`to see what resources will be affected.

The full reference of the OCI Terraform provider's supported resources and data sources contains usage, argument, and attribute details. The full reference is available at[docs.oracle.com](https://docs.oracle.com/iaas/tools/terraform-provider-oci/latest/)and[Terraform Registry](https://registry.terraform.io/providers/oracle/oci/latest/docs). For releases of the OCI Terraform Provider, see[oracle/terraform-provider-oci](https://github.com/oracle/terraform-provider-oci/releases).

The reference indicates which properties are updatable.

## Applying Changes

Once you're confident that your configurations will result in your expected changes, you can apply your Terraform configurations by running the following command:

```

```

When prompted for confirmation, enter`yes`, for your resource to be created. After you run the`apply`comand, the output is displayed in the terminal. Example output:
```

```

Caution  
  
If you make changes to resources you manage with Terraform outside of Terraform , those changes will be overwritten the next time you use Terraform to apply configurations. Add the`ignore_changes`
