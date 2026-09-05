# Getting Started
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm
- Fetched: 2026-09-05 02:54 CDT

# Getting Started

This sample provides an end-to-end walkthrough of the tasks required to create and deploy an Oracle Cloud Infrastructure compute instance using Resource Manager.

This page helps you get started with Resource Manager. Use this end-to-end walkthrough of tasks to create and deploy an Oracle Cloud Infrastructure compute instance using either a prebuilt Terraform configuration or your own Terraform configuration. For a brief introduction to Resource Manager, see[Overview of Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm).

## Highlights

In addition to providing a prebuilt Terraform configuration for creating a Compute instance, this walkthrough provides samples that demonstrate how to write a Terraform configuration. Whichever configuration you use (prebuilt or your own), Resource Manager uses Terraform to provision the defined resources . The resources are organized into stacks, which you create and provision using jobs.

The walkthrough covers the following tasks:
- Select or create a Terraform configuration.
- Provision the infrastructure:
- Create a stack in which to provision your infrastructure.
- Run a plan job against your stack, which parses your configuration and creates an execution plan.
- Review the generated execution plan.
- Run an apply job against your stack, which provisions your resources. The apply job follows the execution plan, which is based on your Terraform configuration.
- Review the resulting infrastructure.
- Optionally provision the infrastructure in more environments, using the same Terraform configuration.

## Before You Begin

Ensure that you have installed, obtained, or created the prerequisites:
- An Oracle Cloud Infrastructure tenancy for each environment where you want to provision resources. For example, you might provision the resources defined in a Terraform configuration to development, staging, and production environments.
Note  
  
It is a best practice to locate each environment in its own tenancy.
- The OCID for the compartment where you wish to create your stack.
- A user account that includes the following:
- An API signing key. For guidance, see[Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm).
- Required IAM permissions. For more information, see[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm)and[Details for Resource Manager](https://docs.oracle.com/iaas/Content/Identity/policyreference/resourcemanagerpolicyreference.htm).
- If you want to use the Oracle Cloud Infrastructure CLI, install and configure the CLI first. See[Quickstart](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm)and[Configuring the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliconfigure.htm)

## Task 1a: Select a prebuilt Terraform Configuration

You can select the compute instance[template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Reference/templates.htm)with its prebuilt Terraform configuration instead of writing your own configuration. These steps guide you through the stack creation process.
- Select the following link to launch the Create stack page with the compute instance template already selected.

[Launch stack with Compute Instance template](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=computeinstance)
- In the Create stack page, enter a Name for the new stack (or accept the default name provided). Avoid entering confidential information.
- 

From the Create in compartment drop-down, select the compartment where you want to create the stack.

A compartment from the list scope is set by default.
- 

Select Next .

The Configure variables panel displays variables from the Terraform configuration.
- 

Review the variables and make changes as necessary.
Important  
  
Do not add your private key or other confidential information to configuration variables.
- Select Next .
- In the Review panel, verify your stack configuration.

For purposes of this walkthrough, leave Run apply blank. (Use this option to automatically provision the infrastructure when the stack is created.)
- Select Create to create your stack.

The stack details page for the new stack appears.

Congratulations! You have created a stack with the prebuilt Terraform configuration from the compute instance template. The next step is to[provision the infrastructure](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#build).

## Task 1b: Create Your Own Terraform Configuration

If you didn't select a prebuilt Terraform configuration, then follow these steps to write your own.

A Terraform configuration is a file that codifies your infrastructure. The configuration defines your Terraform provider, the resources you intend to provision, variables, and specific instructions for provisioning the resources.

This page guides you through selecting the compute Instance[template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Reference/templates.htm)with its prebuilt Terraform configuration or alternatively writing your own configuration using several .tf files within a .zip file.

For more information about writing configurations for use with Resource Manager, see[Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)and[Terraform Language Documentation](https://developer.hashicorp.com/terraform/language).
Caution  
  
Do not provide user credentials or other confidential information in your Terraform configuration.

[Create an Oracle Cloud Infrastructure Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

The following code sample creates a basic Oracle Cloud Infrastructure Terraform provider. You can provide values as variables that are defined either in a variables file or in the provider definition (.tf) file. For more information, see[Provider Configuration](https://developer.hashicorp.com/terraform/language/providers/configuration).

```

```

[Define Variables](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Define the variables you want to use when provisioning your resources. A best practice is to create a "variables" file in the configuration package that you upload. Following is an example from a configuration file that we've named`variables.tf`. For more information about using variables, see[Define input variables](https://developer.hashicorp.com/terraform/tutorials/oci-get-started/oci-variables). See also[Input Variables](https://developer.hashicorp.com/terraform/language/values/variables).

```

```

For more information about variables declared in the preceding examples, see the following:
- `InstanceImageOCID`:[Platform Images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm)
- `InstanceShape`:[Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm)
- `region`and`localAD`:[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)

[Define a Schema Document (Optional)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

With a[schema document](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm), you can reuse one, unedited Terraform configuration in development, staging, and production environments. Resource Manager prompts you for variable values when you create a stack with a Terraform configuration that includes a schema document.

Schema documents are recommended for Terraform configurations when using Resource Manager. Including a schema document allows you to extend pages in the Oracle Cloud Infrastructure Console. Facilitate variable entry in the Create stack page by surfacing SSH key controls and by naming, grouping, dynamically prepopulating values, and more. Define text in the Application Information tab of the Stack details page that opens for a created stack.

Following are contents of an example schema document (`schema.yaml`) that covers the basic details in this scenario.
Note  
  
To easily reuse this schema document,[specify default values](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__default)for each variable.

```

```

[Create a Virtual Cloud Network (VCN)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

The following code sample creates an Oracle Cloud Infrastructure virtual cloud network (VCN) named "ExampleVCN."

```

```

[Create a Subnet in Your VCN](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

The following code sample creates a subnet named "ExampleSubnet" in the VCN defined in the previous code sample.

```

```

[Create an Internet Gateway](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

The following code sample creates an internet gateway named "ExampleIG" in the VCN that we created.

```

```

[Create a Core Route Table](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

The following code sample creates a Oracle Cloud Infrastructure core route table in the VCN and then applies two route rules.

```

```

[Create a Compute Instance](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

The following extended code example creates an Oracle Cloud Infrastructure compute instance. The code also references the image on which the compute instance is created, sets boot volume size, adds essential metadata, and applies both free-form and defined tags.

```

```

[Finalize the Configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Ensure that all of the configuration files are in a single directory. You can store your Terraform configuration file locally or in a source code control system. For more information on storing your file in a source code control system, see[Managing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/managingconfigurationsourceproviders.htm). Wherever your file is stored, you can select it when creating a stack using the CLI or Console.
Important  
  
Make sure your Terraform configuration file is valid. See[Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm)and[Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm).

## Task 2: Provision the Infrastructure

Use your Terraform configuration to build and deploy your infrastructure by taking the following actions:
- 

If you created your own Terraform configuration, follow these steps to create a stack in a tenancy compartment of your choosing. (If you selected a prebuilt configuration, skip this step.)

For Terraform configuration sources supported with Resource Manager, see[Where to Store Your Terraform Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#sources).

A stack is a collection of resources that you can act on as a group. All of the resources that you specify in your configuration are provisioned in the stack that you create.

You can create a stack from a remote, versioned file in a source code control system (such as[Git](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-git.htm)), an[Object Storage bucket](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-bucket.htm), or a locally accessed .zip file that you upload. Following are instructions for a local file.

[To create a stack from your .zip file (Console)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

- Open the navigation menu and select Developer Services . Under Resource Manager , select Stacks .
- 

Under List Scope , select a compartment that you have permission to work in.
- 

Select Create stack .

The Create stack page opens, with the Stack information tab selected.
- 

On the Create stack page, under Choose the origin of the Terraform configuration , select My configuration .
- 

Under Stack configuration , select .Zip file and add the Terraform configuration.

You can either drag and drop your Terraform configuration .zip file onto the control or select Browse and navigate to the location of the .zip file.

You can also store your configuration remotely. For example, store the configuration in[Git](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-git.htm)or an[Object Storage bucket](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-bucket.htm).

The page is populated with information contained in the Terraform configuration.
- Enter values for the remaining fields.

Name Description
Use custom providers Select this option to use[custom providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/update-stack-custom-providers.htm), and then select the bucket that contains the custom providers.
Name Stack name. You can accept the default name provided. Avoid entering confidential information.
Description Stack description (optional).
Create in compartment Compartment where you want to create the stack. A compartment from the list scope is set by default.
Terraform version Version that you want for the Terraform configuration.
Tags Optionally apply[tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)to the stack.
- 

Select Next .

The Configure variables panel lists variables from the Terraform configuration.
- 

Review the variables and change as needed. Don't add your private key or other confidential information to configuration variables.
- 

Select Next .
- 

In the Review panel, verify the stack configuration.
- 

To automatically provision resources on creation of the stack, select Run apply .
- 

Select Create to create the stack.

The stack is created and its details page opens.

If you selected Run apply , then Resource Manager runs the apply action on the new stack.

[To create a stack from your .zip file (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Use the command related to your file location.

[To create a stack from a remote, versioned file](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create-from-git-provider.html)oci resource-manager stack create-from-git-provider`command and required parameters to create a stack from Git.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

[Example Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

```

```

[To create a stack from your .zip file](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Note  
  
On Windows, be sure the zip file and variables.json files are in the same directory from which you're running the CLI. The CLI currently has a limitation on Windows that prevents correct handling of the files if either one is in a subdirectory.

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create.html)oci resource-manager stack create`command and required parameters to create a stack from a local zip file.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

[Example Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

```

```

[Example Response](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

```

```

- 

Generate an execution plan.

The plan job parses your configuration to create an "execution plan," which is a step-by-step representation of the planned deployment in job log entries. Once the plan job has completed, you can evaluate the execution plan by viewing the job's log entries to confirm that it performs the expected operations, and in the intended sequence.
Note  
  
You can skip this step if you selected Run apply when you[created the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#build__createStack). In this case, the resources have already been provisioned.

[To run a plan job (Console)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

- Open the navigation menu and select Developer Services . Under Resource Manager , select Stacks .
- 

Under List Scope , select a compartment that you have permission to work in.
- 

Select the name of the stack that you want.

The Stack details page opens.
- 

Select Plan .
- 

In the Plan panel, review the Name and optionally change it.
- 

Select Plan .

The plan job is created. The new job is listed under Jobs .

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-logs-content.htm).

[To run a plan job (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-plan-job.html)oci resource-manager job create-plan-job`command and required parameters to run a plan job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-logs-content.htm).
- 

Review the execution plan to confirm that it represents your intentions.

The execution plan is represented in the log for the plan job you ran previously.
Note  
  
You can skip this step if you selected Run apply when you[created the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#build__createStack). In this case, the resources have already been provisioned.

[To review an execution plan (the log for the plan job) (Console)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

- 

Open the navigation menu and select Developer Services . Under Resource Manager , select Jobs .

You can also access jobs from a stack detail page. Select Stacks and then select the name of the stack you want.
- 

Under List Scope , select a compartment that you have permission to work in.
- 

Select the name of the plan job that you ran.

The Job details page opens. Logs are visible (in the Logs section under Resources ).

For plan jobs, the log file is the execution plan. View the log file for the plan job and note the "message" fields in the sequence of log entries of the log file. These values represent the sequence of operations specified in your configuration.
- 

(Optional) Select Download logs (in the Logs section under Resources ).

If changes are needed,[update your stack to use a revised configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/update-stack-tf-config.htm)and then[run another plan job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-plan.htm)to obtain an updated execution plan.

[To review an execution plan (the log for the plan job) (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-logs.html)oci resource-manager job get-job-logs`command and required parameters to get logs for a job as a paged list of entries.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

[Example Response for a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

The command returns JSON objects that describe log entries. Each object has a message member with a property that displays one line of the execution plan. In this example, the plan job creates a single virtual cloud network (VCN); the remaining members show details about the VCN.
```

```

If changes are needed,[update your stack to use a revised configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/update-stack-tf-config.htm)and then[run another plan job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-plan.htm)to obtain an updated execution plan.
- 

Provision your resources by running an apply job against the execution plan.

When satisfied with the execution plan, you're ready to do the work of provisioning the stack with the resources that you've defined. The apply job takes the execution plan and "applies" it to the stack. The result is a fully provisioned stack.
Note  
  
You can skip this step if you selected Run apply when you[created the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#build__createStack). In this case, the resources have already been provisioned.

[To run an apply job (Console)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

- 

Open the navigation menu and select Developer Services . Under Resource Manager , select Stacks .
- 

Under List Scope , select a compartment that you have permission to work in.
- 

Select the name of the stack that you created.

The Stack details page opens.
- 

Select Apply .
- 

(Optional) In the Apply panel, review the apply job Name and[other settings](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-apply.htm#console)and update if needed.
- 

Select Apply .

The apply job is created. The new job is listed under Jobs .

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-logs-content.htm).

To confirm existence of newly provisioned resources,[inspect resources in the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/inspect-resources.htm).

[To run an apply job (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-apply-job.html)oci resource-manager job create-apply-job`command and required parameters to run an apply job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

[Examples](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Example 1: Reference a plan job.

```

```

Example 2: Automatically approve (don't reference a plan job).

```

```

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-logs-content.htm).

To confirm existence of newly provisioned resources,[inspect resources in the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/inspect-resources.htm).
- Review the log entries and state file for the apply job you just ran.
- 

See the entries in the job log for more details about the job.

[To view the job log (Console)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

- 

Open the navigation menu and select Developer Services . Under Resource Manager , select Jobs .

You can also access jobs from a stack detail page. Select Stacks and then select the name of the stack you want.
- 

Under List Scope , select a compartment that you have permission to work in.
- 

Select the name of the apply job that you ran.

The Job details page opens. Logs are visible (in the Logs section under Resources ).
- 

(Optional) Select Download logs (in the Logs section under Resources ).

[To view the job log (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

View the log file and note the "message" fields in the sequence of log entries of the log file. You can view the log file for the specified job as either a paged list of entries or in its raw form.

[To view a paged list of entries](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-logs.html)oci resource-manager job get-job-logs`command and required parameters to get logs for a job as a paged list of entries.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

[Example Response for a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

The command returns JSON objects that describe log entries. Each object has a message member with a property that displays one line of the execution plan. In this example, the plan job creates a single virtual cloud network (VCN); the remaining members show details about the VCN.
```

```

[To view logs in raw form](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-logs-content.html)oci resource-manager job get-job-logs-content`command and required parameters to get logs content for a job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

The job state file represents the job's output in JSON format.

The state file maps your stack's resources to your configuration and also maintains essential configuration metadata, such as resource dependencies. Resource Manager generates and updates state files automatically when you run jobs.

The Resource Manager supports state locking by allowing only one job at a time to run on a given stack. For more information about state files, see[State](https://developer.hashicorp.com/terraform/language/state).

[To view the state of the job (Console)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

- 

Open the navigation menu and select Developer Services . Under Resource Manager , select Jobs .

You can also access jobs from a stack detail page. Select Stacks and then select the name of the stack you want.
- 

Under List Scope , select a compartment that you have permission to work in.
- 

Select the name of the job.

The Job details page opens.
- 

Select Download Terraform configuration .

[To view the state of the job (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-tf-state.html)oci resource-manager job get-job-tf-state`command and required parameters to get a job's state.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

Example response:

```

```

Note  
  
You can also[import state files](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-import.htm)for resources already managed by Terraform.
- 

When you need to release the resources that you provisioned, run a destroy job on the stack.

A destroy job tears down the stack that you created and then cleans up associated resources without deleting them. For example, the destroy job terminates Compute instances associated with the stack.
Note  
  

We recommend running a destroy job before deleting a stack to release associated resources first. When you delete a stack, its associated state file is also deleted; therefore, you lose track of the state of its associated resources. Cleaning up resources associated with a deleted stack can be difficult without the state file, especially when those resources are spread across multiple compartments. To avoid difficult cleanup later, we recommend that you release associated resources first by running a destroy job.

Data cannot be recovered from destroyed resources.

[To run a destroy job (Console)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

- 

Open the navigation menu and select Developer Services . Under Resource Manager , select Stacks .
- 

Under List Scope , select a compartment that you have permission to work in.
- 

Select the name of the stack that you want.

The Stack details page opens.
- Select Destroy .
- 

(Optional) In the Destroy panel, review the apply job Name and[other settings](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-destroy.htm#console)and update if needed.
- 

Select Destroy .

The destroy job is created. The new job is listed under Jobs .

After running a destroy job, get the job to check its status. You can optionally view the Terraform state file, view the logs, and confirm deletion of the resources. You can also re-create destroyed resources.

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-logs-content.htm).

To view the Terraform state file (shows the state of your resources after running the job), select the name of the job to display the Job details page, then select View state under Resources . Optionally select Show changes in this version .

To view the logs for the job, select the job to open its details page, then select Logs under Resources .

To confirm deletion of the resources,[inspect resources in the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/inspect-resources.htm).

To re-create a stack's resources after the resources are destroyed,[run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-apply.htm). The new resources differ from previously destroyed resources by their unique[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)and other metadata.

[To run a destroy job (CLI)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#)

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-destroy-job.html)oci resource-manager job create-destroy-job`command and required parameters to run a destroy job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

After running a destroy job, get the job to check its status.

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-logs-content.htm).

You can optionally[view the Terraform state file](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-tf-state.htm),[view the logs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-logs.htm), and confirm deletion of the resources. You can also re-create destroyed resources.

To confirm deletion of the resources,[inspect resources in the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/inspect-resources.htm).

To re-create a stack's resources after the resources are destroyed,[run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-apply.htm). The new resources differ from previously destroyed resources by their unique[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)and other metadata.

## Task 3: Repeat in More Environments

This section describes how to build and deploy infrastructure in multiple environments.

In this scenario, you use the same[Terraform configuration .zip file](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#config)to provision a Compute instance in your development, staging, and production environments.
Note  
  
This scenario assumes that the Terraform configuration includes[a schema document](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#schema), which allows you to change variable values when creating a stack in the Console.
- 

Access the tenancy for the new environment where you want to provision the infrastructure defined in your Terraform configuration.

For example, access the tenancy for your staging or production environment.
- Open the Create stack page:
- Open the navigation menu and select Developer Services . Under Resource Manager , select Stacks .
- 

Under List Scope , select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
- Select Create stack .
- 

Using the same Terraform configuration as for the first environment, complete the Stack information tab:
- 

On the Create stack page, select My configuration .
- 

Under Stack configuration , select .Zip file and add the Terraform configuration.

You can either drag and drop your Terraform configuration .zip file onto the control or select Browse and navigate to the location of the .zip file.
- Enter a Name for the new stack (or accept the default name provided). Avoid entering confidential information.
- Optionally enter a Description .
- 

From the Create in compartment drop-down, select the compartment where you want to create the stack.
- 

Select Next .

The Configure variables panel displays variables from the selected Terraform configuration file.
- 

Specify the variable values for this environment:
- 

In the Configure variables panel, review the variables and make changes as necessary.

[Default values](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__default)are provided when specified in the[schema document](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#schema).
Important  
  
Do not add your private key or other confidential information to configuration variables.
- Select Next .
- In the Review panel, verify your stack configuration.
- To automatically provision resources on creation of the stack, select Run apply .
- 

Select Create to create your stack.

The stack details page for the new stack appears.

If you selected Run apply , then Resource Manager runs the apply action on the new stack.

Congratulations, you have reused your Terraform configuration to create a stack in a new environment. If you selected Run apply , then you also provisioned resources in the new environment.

You can now generate and review an execution plan (and provision resources, if Run apply wasn't selected). To complete these items, repeat the steps from[Task 2: Provision the Infrastructure](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm#build)
