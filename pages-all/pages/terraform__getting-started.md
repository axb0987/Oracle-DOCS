# Getting Started with the Terraform Provider
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/getting-started.htm
- Fetched: 2026-09-05 19:20 CDT

# Getting Started with the Terraform Provider

Learn about Terraform software and the OCI Terraform provider.

Terraform is "infrastructure-as-code" software that lets you define OCI resources in files that you can persist, version, and share. These files describe the steps required to provision infrastructure and maintain its state:
- Resources create OCI infrastructure objects, such as virtual cloud networks or compute instances. The first application of the configuration creates the objects, and later applications update or delete them.
- Data sources represent read-only views of existing OCI infrastructure.
- Variables represent parameters for Terraform.
Caution  
  
Terraform state files contain all resource attributes that are specified as part of configuration files. If you manage any sensitive data with Terraform, such as database or user passwords or instance private keys, treat the state file itself as sensitive data. For more information, see[Storing Sensitive Data](https://docs.oracle.com/iaas/Content/dev/terraform/storing-sensitive-data.htm).

## First Steps

To get started, you can visit our[Terraform provider tutorials](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials.htm)for detailed walkthroughs and examples, or see the following pages for steps to install and configure the OCI Terraform provider:
- [Install or access a distribution of Terraform and the OCI Terraform provider](https://docs.oracle.com/iaas/Content/dev/terraform/installing.htm).
- [Configure the OCI Terraform provider](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm).
- [Describe your infrastructure as code](https://docs.oracle.com/iaas/Content/dev/terraform/describing-infra.htm).
- [Apply your configurations using Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/applying.htm).

## Example Usage

Terraform executes the steps and builds out the infrastructure that you describe in configuration files.

For example, when the following configuration is applied, Terraform connects to your tenancy and retrieves a list of its availability domains. Because no resources are defined in this configuration, no infrastructure is created or modified.

```

```

For more information about Terraform configuration requirements, see[Authoring Configurations](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm)
