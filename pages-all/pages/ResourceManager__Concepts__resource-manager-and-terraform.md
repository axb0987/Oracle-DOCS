# Resource Manager and Terraform
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resource-manager-and-terraform.htm
- Fetched: 2026-09-05 02:54 CDT

# Resource Manager and Terraform

Terraform is an Infrastructure as Code (IaC) tool supported by Resource Manager for provisioning, configuring, and managing Oracle Cloud Infrastructure (OCI) resources.

For information about IaC tools supported by Resource Manager, see[Supported Infrastructure as Code Tools](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/iac-tools.htm).

Each stack in Resource Manager is associated with a Terraform configuration and a Terraform state file. An understanding of[Hashicorp Terraform](https://developer.hashicorp.com/terraform)concepts is critical to manage resources successfully with Resource Manager.

## Terraform Configuration

Terraform configurations codify your infrastructure in declarative files that contain the steps required to provision your infrastructure and maintain its state. To manage OCI resources, the configuration must specify the`terraform-provider-oci`[Terraform provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#providers).

Resource Manager requires Terraform configurations to[create stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack.htm)for provisioning and managing OCI resources. Pre-defined Terraform configurations are available as[templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Reference/templates.htm), and you can also generate Terraform configurations[from existing compartments](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-compartment.htm)and[from resource creation pages (such as Create compute instance)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-resource.htm). After the initial provisioning of your OCI resources, Resource Manager uses the stack's Terraform configuration to[detect drift](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/detect-drift.htm)of resources (the difference between resource states and the configuration).

For a walkthrough that includes writing a sample Terraform configuration, see[Getting Started](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm).

For information about writing our own Terraform configurations, see[Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)and[Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm).

## Terraform State

Terraform state files are automatically generated and updated by Resource Manager. Resource Manager stores Terraform state files for stacks so you don't have to. The stack's state file (.tfstate, in JSON format) maps your stack's resources to your configuration and maintains essential configuration metadata, such as resource dependencies.

Multiple people can work on a stack concurrently because stack state is locked, allowing only one job at a time to run on a given stack.

For related instructions, see:
- [Getting a Stack's Terraform Configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-stack-tf-config.htm)
- [Getting a Job's State File](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-tf-state.htm)
- [Creating an Import Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-import.htm)

## Jobs

Resource Manager[jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__jobdefinition)use Terraform configuration and state files to manage your Oracle Cloud Infrastructure (OCI) resources through the following Terraform actions.
- Plan : Parses your Terraform configuration and creates an execution plan for the associated stack. The execution plan lists the sequence of specific actions planned to provision your OCI resources. The execution plan is handed off to the apply job, which then executes the instructions.
- Apply . Applies the execution plan to the associated stack to create (or modify) your OCI resources. Depending on the number and type of resources specified, a given apply job can take some time. You can check status while the job runs.
- Destroy . Releases resources associated with a stack. Released resources are not deleted. For example, terminates a Compute instance controlled by a stack. The stack's job history and state remain after running a destroy job. You can monitor the status and review the results of a destroy job by inspecting the stack's log files.
- Import State . Sets the provided Terraform state file as the current state of the stack. Use this job to migrate local Terraform environments to Resource Manager.

When you[run a job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job.htm), the stack's variable values are added as environment variables in the Resource Manager Terraform host. For example, the VCN specified in a stack for a given VCN variable is added as an environment variable.

For a walkthrough that includes running jobs for the Terraform actions Plan, Apply, and Destroy, see[Getting Started](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm).

For instructions related to jobs for Terraform actions, see[Managing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/jobs.htm)
