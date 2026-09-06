# Installing the Provider
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/installing.htm
- Fetched: 2026-09-05 19:20 CDT

# Installing the Provider

Install the OCI Terraform provider.

To use the Oracle Cloud Infrastructure (OCI) Terraform provider, you must install both Terraform and the OCI Terraform provider. You can[directly download](https://docs.oracle.com/iaas/Content/dev/terraform/installing.htm#hashicorp)Terraform and the OCI Terraform provider from HashiCorp.

[Government Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govoverview.htm)customers: follow the installation and configuration steps in[Enabling FIPS Compatibility](https://docs.oracle.com/iaas/Content/dev/terraform/fips-compatible.htm).
Tip  
  
Use[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)to[preinstall the Oracle Cloud Development Kit on a compute instance in your compartment](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/devtools.htm). The Oracle Cloud Development Kit includes Terraform and the OCI Terraform provider, and preconfigures the required authorization.

After downloading and installing, you must[configure the Terraform provider](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm)so that Terraform can interact with OCI resources.

## Prerequisites for Installing and Using the Provider

- An Oracle Cloud Infrastructure (OCI) account that has the required user credentials to execute a Terraform plan.
- A user in that account.
- Required keys and OCI IDs (OCIDs). For guidance, see[Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm).
- The correct Terraform binary file for your OS. We recommend using Terraform version 0.12.20 or greater.

## Installing from HashiCorp

Terraform and the OCI Terraform provider can be downloaded directly from HashiCorp.

### Download and Install Terraform

Terraform is available for direct download from the[HashiCorp download page](https://www.terraform.io/downloads.html). Ensure that you download the correct binary file for your system.

### Download and Install the Provider

To use the latest version of the OCI Terraform provider, run`terraform init`from the directory that contains a[configuration file](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm)with the`provider "oci" { ...`configuration block. The provider is automatically downloaded. Terraform configurations also allow you to[specify a particular version](https://docs.oracle.com/iaas/Content/dev/terraform/specifying-versions.htm#provider)of the OCI Terraform provider.

You can also[download the Terraform provider directly](https://releases.hashicorp.com/terraform-provider-oci/)to a location of your choice.

## Test the Terraform Installation

Open a terminal window and run the following command to test your installation:

```

```
