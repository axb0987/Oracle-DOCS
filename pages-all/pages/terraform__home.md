# Terraform Provider
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/home.htm
- Fetched: 2026-09-05 19:20 CDT

# Terraform Provider

Install, configure, and use the OCI Terraform provider with the Terraform tool.

[Hashicorp Terraform](https://developer.hashicorp.com/terraform)is an Infrastructure as Code (IaC) tool that lets you programmatically manage, version, and persist infrastructure. Terraform configurations codify infrastructure in declarative files that contain the steps required to provision infrastructure and maintain its state. You can share these files among team members, treat them as code, edit, review, and version them.

Terraform uses providers to interface between the Terraform engine and the supported cloud platform. The Oracle Cloud Infrastructure (OCI) Terraform provider is a component that connects Terraform to the OCI services that you want to manage.
Caution  
  
Terraform state files contain all resource attributes that are specified as part of configuration files. If you manage any sensitive data with Terraform, such as database or user passwords or instance private keys, treat the state file itself as sensitive data. For more information, see[Storing Sensitive Data](https://docs.oracle.com/iaas/Content/dev/terraform/storing-sensitive-data.htm).

You can use the OCI Terraform provider to manage OCI resources wherever you use a Terraform distribution, including[Terraform Cloud](https://www.terraform.io/docs/cloud/index.html)and the OCI[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm). The OCI Terraform provider is at[GitHub](https://github.com/oracle/terraform-provider-oci).
Tip  
  
To migrate an existing Terraform state file to Resource Manager, use an[import job](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-import.htm).

To begin using this provider to manage OCI resources, see[Getting Started](https://docs.oracle.com/iaas/Content/dev/terraform/getting-started.htm).

Licensing: This provider and samples are licensed under the Mozilla Public License 2.0; third-party content is separately licensed as described in the code.

## Availability

The Oracle Cloud Infrastructure Terraform provider is region agnostic. You can use the Terraform provider to work with[supported services](https://docs.oracle.com/iaas/Content/dev/terraform/supported-services.htm#list)in all Oracle Cloud Infrastructure regions where they're available.[Oracle US Government Cloud and Oracle US Defense Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govoverview.htm)customers: Use the[FIPS-compatible OCI Terraform provider](https://docs.oracle.com/iaas/Content/dev/terraform/fips-compatible.htm).

See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for the[list](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About__The)of available regions, along with associated locations, region identifiers, region keys, and availability domains.

## Contributions

Got a fix for a bug, or a new feature you'd like to contribute? The OCI Terraform provider is open source and accepting pull requests on[GitHub](https://github.com/oracle/terraform-provider-oci).

## Notifications

To be notified when a new version of the OCI Terraform provider is released, subscribe to the[Atom feed](https://github.com/oracle/terraform-provider-oci/releases.atom).

## Questions or Feedback

Refer to[Troubleshooting Basics](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting-basics.htm)and[a list of common issues](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm)to see if your question has an answer.

You can also use[GitHub](https://github.com/oracle/terraform-provider-oci/issues)
