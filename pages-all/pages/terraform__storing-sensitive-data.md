# Storing Sensitive Data
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/storing-sensitive-data.htm
- Fetched: 2026-09-05 19:21 CDT

# Storing Sensitive Data

Store sensitive data when using the OCI Terraform provider.
Caution  
  
Terraform configuration files and state files might contain sensitive data.

When configuring the OCI Terraform provider,[use variables to define your provider](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm#provider-definitions)instead of including sensitive information within the file.

Terraform state files contain all resource attributes that are specified as part of configuration files. If you manage any sensitive data with Terraform, such as database or user passwords or instance private keys, treat the state itself as sensitive data. For more information, see[Sensitive Data in State](https://www.terraform.io/docs/state/sensitive-data.html)
