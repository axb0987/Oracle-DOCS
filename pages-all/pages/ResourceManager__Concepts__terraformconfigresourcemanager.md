# Terraform Configurations for Resource Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm
- Fetched: 2026-09-05 02:54 CDT

# Terraform Configurations for Resource Manager

Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.

For basic information about Terraform configurations, see[Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm). For instructions on using configurations with stacks and jobs, see[Managing Stacks and Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/managingstacksandjobs.htm).

For Terraform configuration sources supported with Resource Manager, see[Where to Store Your Terraform Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#sources).

In addition to writing your own Terraform configuration file, you also have the option to generate a Terraform configuration from either an existing compartment using[resource discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resource-discovery.htm)or a[sample template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Reference/templates.htm).
Caution  
  
Do not provide user credentials or other confidential information in your Terraform configurations.

## Requirements

Terraform configuration files used with Resource Manager must meet the following requirements.

### Terraform Provider

When using Resource Manager, the`region`field in the`provider "oci"`block is the only required field. For more information about defining providers, see[Configuration File Requirements](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm#configuration-file-requirements).

### File Structure

Resource Manager requires the following file structure for the Terraform configuration:
- 

The working directory must contain at least one`.tf`file. The working directory cannot contain a`.terraform`directory.

The working directory is the path from which to run Terraform. By default, the working directory is the root directory of your configuration (for an uploaded configuration, the root of your`.zip`file). When using the API, you can specify a different location for the working directory by setting the`workingDirectory`parameter.
- The configuration must follow guidelines specified in[Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm).
- No Terraform state files (`.tfstate`) can exist in the configuration.
- If you plan to upload the configuration locally, then bundle all files into a`.zip`file.

### Modules

Resource Manager supports the following[Terraform module sources](https://developer.hashicorp.com/terraform/language/modules/sources):
- 

[Local paths](https://developer.hashicorp.com/terraform/language/modules/sources#local-paths)
- 

[Terraform Registry](https://developer.hashicorp.com/terraform/language/modules/sources#terraform-registry)
- 

[GitHub](https://developer.hashicorp.com/terraform/language/modules/sources#github)
- 

[Bitbucket](https://developer.hashicorp.com/terraform/language/modules/sources#bitbucket)
- 

Generic[Git](https://developer.hashicorp.com/terraform/language/modules/sources#generic-git-repository)repositories
- [HTTP URLs](https://developer.hashicorp.com/terraform/language/modules/sources#http-urls)

### Variables

We recommend using a[schema document](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)with your Terraform configuration to facilitate user entry in the Oracle Cloud Infrastructure Console.

Resource Manager does not have requirements for variables in Terraform configurations. Resource Manager supports the native Terraform behavior for handling variables. Terraform sets variables from[your variable definitions](https://developer.hashicorp.com/terraform/language/values/variables#variable-definition-precedence)that use[supported type constraints](https://developer.hashicorp.com/terraform/language/values/variables#type-constraints). When you[run a job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job.htm), the stack's variable values are added as environment variables in the Resource Manager Terraform host. For example, the VCN specified in a stack for a given VCN variable is added as an environment variable.
Note  
  

When defined in the Terraform configuration, the following variables automatically prepopulate with values on the Console pages used to[create and edit the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack.htm). The stack's values are used when you select the Terraform actions[Plan](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-plan.htm),[Apply](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-apply.htm), and[Destroy](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-destroy.htm).
- `tenancy_ocid`(tenancy OCID)
- `compartment_ocid`(compartment OCID)
- `region`(region)
- `current_user_ocid`(OCID of the current user)

## Third-party Provider Configuration

Reference third-party Terraform providers in Terraform configurations used with Resource Manager.

By default, new Resource Manager stacks fetch third-party providers from[Terraform Registry](https://registry.terraform.io/browse/providers). (Unless[updated](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/update-stack-tf-reg.htm), certain older stacks fetch from[Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/providers.htm#third-party-older)).[Custom providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/update-stack-custom-providers.htm)are also available for new and updated stacks.

As with any provider configuration, we recommend specifying versions.[Dependency lock files](https://developer.hashicorp.com/terraform/language/files/dependency-lock)are automatically managed for new and updated stacks. Providers are updated within the version constraints of the Terraform configuration. For instructions, see[Retrieving the Latest Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-lock-file.htm).

For more information about adding providers to Terraform configurations, see[Provider Configuration](https://developer.hashicorp.com/terraform/language/providers/configuration).

## Example Terraform Configuration for Resource Manager

The following example shows a Terraform configuration that's contained in a single file. This basic sample defines only one Terraform provider, one Oracle Cloud Infrastructure resource, and a set of variables.
```

```

More often, Terraform configurations consist of two or more files bundled together (for an uploaded configuration, the files would be bundled in a .zip file). To see more complex Terraform configurations that include multiple files, explore the examples at[Terraform Oracle Cloud Infrastructure Provider Examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples).
Tip  
  
Quickly create stacks with example OCI Terraform configurations. Go to[Terraform Oracle Cloud Infrastructure Provider Examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples), navigate to the folder for the configuration you want (such as`adm`), and then select the Deploy to Oracle Cloud button under "Magic Button" in the readme.

## Where to Store Your Terraform Configurations

When[creating a stack with Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack.htm), you can select your Terraform configuration from the following sources.
- Local .zip file
- Local folder
- Object Storage bucket

The most recent contents of the bucket are automatically used by any job running on the associated stack.
- [Source code control system, such as Git](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/managingconfigurationsourceproviders.htm)

The latest version of your configuration is automatically used by any job running on the associated stack.
- [Template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Reference/templates.htm)(prebuilt Terraform configuration from Oracle or a[private template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/managingprivatetemplates.htm))
- Existing compartment ([Resource Discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resource-discovery.htm))

## Schema Documents

Schema documents are recommended for Terraform configurations when using Resource Manager. See[Extend Console Pages Using Schema Documents](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
