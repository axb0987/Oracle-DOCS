# Examples, Templates, and Solutions
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/examples-templates.htm
- Fetched: 2026-09-05 19:20 CDT

# Examples, Templates, and Solutions

See examples of OCI infrastructure descriptions using the Hashicorp Configuration Language format (HCL) in Terraform configuration files.

The OCI Terraform provider uses Terraform configuration files to manage your OCI infrastructure.

Referring to existing example configurations, sample solutions, and templates can help you understand HashiCorp Configuration Language format (HCL) and see how it is used to define OCI resources.

You can also modify examples or entire solution sets to meet your needs.

## Example Configurations

Tip  
  
Quickly create stacks with example OCI Terraform configurations. Go to[Terraform Oracle Cloud Infrastructure Provider Examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples), navigate to the folder for the configuration you want (such as`adm`), and then select the Deploy to Oracle Cloud button under "Magic Button" in the readme.

We provide many[example Terraform configuration files](https://github.com/oracle/terraform-provider-oci/tree/master/examples)that show you how to create specific OCI resources. These examples are intended to be as simple as possible. In most cases, they contain only the specific resource and any dependencies required for it to run.

Examples are grouped by service, including Compute, Database, Networking, Load Balancer, and several others.

These don't represent production configurations or real world scenarios, but they can serve as a starting point and be modified and combined as necessary.

## Templates

Oracle also provides[templates](https://docs.oracle.com/iaas/Content/ResourceManager/Reference/templates.htm)for[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm). Resource Manager uses Terraform to automate deployment and operations for OCI resources.

Templates can help those new to infrastructure-as-code and those who are updating production configurations. Use templates to try out Resource Manager and inspect the underlying[oracle-terraform-modules](https://github.com/oracle-terraform-modules)to familiarize yourself with Terraform configuration files.

## Architecture Center

The[Oracle Architecture Center](https://docs.oracle.com/solutions/)contains reference architectures, solution playbooks, and best practices. You can filter the content to see[Terraform-specific information](https://docs.oracle.com/solutions/?q=&cType=reference-architectures&technologies=Terraform&sort=date-desc)that you can use with the OCI Terraform provider or[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)
