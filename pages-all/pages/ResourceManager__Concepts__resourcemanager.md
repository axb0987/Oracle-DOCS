# Overview of Resource Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm
- Fetched: 2026-09-05 02:54 CDT

# Overview of Resource Manager

Automate deployment and operations for Oracle Cloud Infrastructure resources using Resource Manager. With supported Infrastructure as Code (IaC) tools, DevOps engineers can develop and deploy their infrastructure anywhere.

A Terraform configuration codifies your infrastructure in declarative configuration files. Resource Manager allows you to share and manage infrastructure configurations and state files across multiple teams and platforms. This infrastructure management can't be done with local Terraform installations and Oracle Terraform modules alone. For more information about the Oracle Cloud Infrastructure Terraform provider, see[Terraform Provider](https://docs.oracle.com/iaas/Content/dev/terraform/home.htm). For a general introduction to Terraform and the "infrastructure-as-code" model, see[Terraform Community](https://www.terraform.io/).

Resource Manager is compliant with[Federal Information Processing Standard (FIPS)](https://www.nist.gov/standardsgov/compliance-faqs-federal-information-processing-standards-fips). For more information about OCI in US government regions, see[Oracle US Government Cloud and Oracle US Defense Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govoverview.htm).
Tip  
  
Watch a[video introduction](https://apexapps.oracle.com/pls/apex/f?p=44785:265:0:::265:P265_CONTENT_ID:31978)to the service.

## Key Concepts

Following are brief descriptions of key concepts and the main components of Resource Manager. configuration Information to codify your infrastructure. Use your configuration to specify the Oracle Cloud Infrastructure resources in a given stack. For example, specify resource metadata, data source definitions, and variable declarations. Each Terraform configuration file is either HashiCorp Configuration Language (HCL) format or JSON format. HCL-formatted files use the file extension`.tf`. JSON-formatted files use the file extension`.tf.json`. For Terraform configuration sources supported with Resource Manager, see[Where to Store Your Terraform Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#sources). For example configurations, see[Terraform Oracle Cloud Infrastructure Provider Examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples)and[Oracle-Provided Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Reference/templates.htm). For more information, see[Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)and[Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm); see also[Terraform Language Documentation](https://developer.hashicorp.com/terraform/language). configuration source provider Connection information to a source code control system where your Terraform configuration files are stored. Use a configuration source provider to create a stack from a remote, versioned Terraform configuration file. A configuration source provider has the following types:

A configuration source provider can be one of the following types:
- Bitbucket
- GitHub
- GitLab

Following are the supported products for each type of configuration source provider.
- Bitbucket:
- Bitbucket Cloud
- Bitbucket Server
- GitHub:
- [GitHub Enterprise](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/githubs-products#github-enterprise)
- GitHub Enterprise Server
- GitHub Enterprise Cloud
- [GitHub Free for organizations](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/githubs-products#github-free-for-organizations)
- [GitHub Free for user accounts](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/githubs-products#github-free-for-user-accounts)
- [GitHub Team](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/githubs-products#github-team)
- GitLab:
- GitLab Community Edition
- GitLab Enterprise Edition
- GitLab.com A configuration source provider has the following lifecycle states:
- Active : The configuration source provider is available for use. For more information, see[Managing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/managingconfigurationsourceproviders.htm)and[Creating a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack.htm).

For a walk-through using CLI for cloud provisioning in a CI/CD pipeline, see[IaC in the Cloud: Integrating Terraform and Resource Manager into your CI/CD Pipeline - Building With the OCI CLI](https://blogs.oracle.com/developers/iac-in-the-cloud%3a-integrating-terraform-and-resource-manager-into-your-cicd-pipeline-building-with-the-oci-cli). drift Difference between the actual, real-world state of your infrastructure, and the stack's last executed configuration. For example, drift occurs when a team member adds a production tag to your resources, or when a resource fails. You can[run drift detection reports](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/detect-drift.htm)to determine if provisioned resources have different states than those resources defined in the stack's last executed configuration. You can also[view detailed drift status for each resource](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/list-drift.htm). job Instructions to perform the actions defined in your configuration. Only one job at a time can run on a given stack; further, you can have only one set of Oracle Cloud Infrastructure resources on a given stack. To provision a different set of resources, you must create a separate stack and use a different configuration. Jobs store history about their associated stack. For example, plan jobs store generated execution plans and apply jobs store configurations (snapshots) and state files. Jobs reside in the same compartment as the stack they are associated with. An OCID is assigned to each job. For information about Resource Manager job types, see[Creating a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job.htm). A job has the following lifecycle states:
- Accepted (`ACCEPTED`): The job was accepted for processing.
- In progress (`IN_PROGRESS`): The job is running (executing).
- Failed (`FAILED`): The job did not complete execution.
- Succeeded (`SUCCEEDED`): The job has completed successfully.
- Canceling (`CANCELING`): The job is being canceled; a notification has been sent, but the job has not yet stopped running.
- Canceled (`CANCELED`): The job was canceled and has stopped running. Default retry policy: A job might fail because of a downstream service issue. For example, an apply job for creating a compute instance might fail because of a temporary connectivity issue in the Compute service. When a job fails because of downstream service issue, the job retries according to the Go SDK default retry policy. See[Go SDK for Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/tools/go/latest/). module A group of related resources. Use modules to create lightweight and reusable abstractions, so that you can describe your infrastructure in terms of its architecture. For more information, see[Creating Modules](https://developer.hashicorp.com/terraform/language/modules/develop). package Typically a .zip file to a Terraform configuration that is stored in a[supported provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/deploybutton.htm#deploybutton-supportedproviders), such as GitHub. For more information, see[Using the Deploy to Oracle Cloud Button](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/deploybutton.htm). private endpoint Network information for connecting to a nonpublic resource. For more information, see[Managing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/private-endpoints.htm). resource discovery A feature to capture deployed Oracle Cloud Infrastructure resources as Terraform[configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__ConfigurationConcept)and[state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__statedefinition)files. For more information, see[Resource Discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resource-discovery.htm). stack The collection of Oracle Cloud Infrastructure resources corresponding to a given[Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm). Each stack resides in the compartment you specify, in a single region; however, resources on a given stack can be deployed across multiple regions. An OCID is assigned to each stack. For steps on creating stacks, see[Creating a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack.htm). For Terraform configuration sources supported with Resource Manager, see[Where to Store Your Terraform Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#sources). A stack has the following lifecycle states:
- Creating : The stack is being created.
- Active : The stack is available for use.
- Deleting : The stack is being deleted.
- Deleted : The stack was deleted.
- Failed : The stack could not be created. state The state of your resource configuration, stored in JSON format in a state file (`.tfstate`). For more information, see[State Management](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#features__state). template A prebuilt[Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__ConfigurationConcept)that provisions a set of resources used in a common scenario. The template can be provided by either Oracle or someone in your tenancy, as a private template. To create stacks from templates, see[Creating a Stack from a Template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-template.htm). For reference, see[Oracle-Provided Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Reference/templates.htm).

To create private templates, see[Managing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/managingprivatetemplates.htm).

## Features

[Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#)

A template is a[Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)that you can use to manage infrastructure. Templates can help customers who are new to infrastructure as code and who are updating production workflow configurations. Use templates to try out Resource Manager and to apply proven best practices to your production workflow configuration. For information about Oracle-provided templates, see[Oracle-Provided Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Reference/templates.htm).

Create your own[private templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/managingprivatetemplates.htm)to share with others in the tenancy.

[Start with a Resource Creation Page](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#)

Save your configuration from a resource configuration page to a stack. Use the stack to install, configure, and manage the resource through the "infrastructure-as-code" model. For more information, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-resource.htm).

[CI/CD with Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#)

Remotely store your Terraform configurations using integrated source code control systems, such as Bitbucket Cloud , Bitbucket Server , DevOps , GitHub, and GitLab. This integration helps you achieve continuous integration and continuous delivery (CI/CD).

For more information, see:

- [Creating a Stack from Bitbucket Cloud](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-bitbucket-cloud.htm)
- [Creating a Stack from Bitbucket Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-bitbucket-server.htm)
- [Creating a Stack from DevOps](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-devops.htm)
- [Creating a Stack from Git](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-git.htm)
- [Managing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/managingconfigurationsourceproviders.htm)

For a walk-through using CLI for cloud provisioning in a CI/CD pipeline, see[IaC in the Cloud: Integrating Terraform and Resource Manager into your CI/CD Pipeline - Building With the OCI CLI](https://blogs.oracle.com/developers/iac-in-the-cloud%3a-integrating-terraform-and-resource-manager-into-your-cicd-pipeline-building-with-the-oci-cli).

In addition, we also allow storing Terraform configurations in Object Storage buckets. For more information, see[Creating a Stack from a Bucket](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-bucket.htm).

[Resource Discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#)

A feature to capture deployed resources as Terraform[configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__ConfigurationConcept)and[state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__statedefinition)files. With this feature, you can:
- Move from manually managed infrastructure to Resource Manager-controlled infrastructure.
- Learn how Terraform uses HashiCorp Configuration Language (HCL) syntax to represent Oracle Cloud Infrastructure resources.
- Duplicate or rebuild existing infrastructure in another compartment.
For more information, see[Resource Discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resource-discovery.htm)and the following instructions:
- [Creating a Stack from an Existing Compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack-compartment.htm)
- [Recreating Infrastructure from an Existing Compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/recreate-infra.htm)

[State Management](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#)

Resource Manager stores Terraform state files for stacks so you don't have to. Multiple people can work on a stack concurrently because Resource Manager locks the stack state, allowing only one job at a time to run on a given stack. Resource Manager automatically generates and updates the stack's state file (`.tfstate`, in JSON format). This file maps your stack's resources to your configuration and maintains essential configuration metadata, such as resource dependencies.
For related instructions, see:
- [Getting a Stack's State File](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-stack-tf-state.htm)
- [Getting a Job's State File](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-tf-state.htm)
- [Creating an Import Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-import.htm)

For more information about Terraform state files, see[State](https://developer.hashicorp.com/terraform/language/state).

[Drift Detection](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#)

Find out if provisioned resources have different states than those resources defined in the stack's last run configuration and view detailed drift status for each resource.

You can optionally limit the drift detection to specified resources. Each resource is identified by a resource address, which is a string derived from the resource type and name specified in the stack's Terraform configuration plus an optional index. For example, the resource address for the fourth Compute instance with the name "test_instance" is`oci_core_instance.test_instance[3]`. The resource type is`oci_core_instance`, a period acts as delimiter, the resource name is`test_instance`, and the index is`3`in bracket. For more details and examples of resource addresses, see the Terraform documentation at[Examples](https://developer.hashicorp.com/terraform/cli/state/resource-addressing#examples).
For more information about drift detection, see[drift](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__driftdefinition)and the following instructions:
- [Detecting Drift in a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/detect-drift.htm)
- [Listing Drift Status for a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/list-drift.htm)

[Deploy to Oracle Cloud Button](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#)

The Deploy to Oracle Cloud button allows you to launch your remote Terraform configuration using the Create Stack workflow available in Resource Manager.

For more information, see[Using the Deploy to Oracle Cloud Button](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/deploybutton.htm).

[Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#)

With private endpoints, you can access nonpublic cloud resources in your tenancy from Resource Manager. For example, use Remote Exec with a private instance or access a Terraform configuration in a private GitHub server.

For more information, including common scenarios, see[Managing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/private-endpoints.htm).

[Custom Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#)

You can supply custom Terraform providers using Object Storage. To add custom providers to buckets, see[Putting Data into Object Storage](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingbuckets.htm). To fetch custom providers from buckets, see[Using Custom Providers with a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/update-stack-custom-providers.htm).

[Dependency Lock Files](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#)

[Dependency lock files](https://developer.hashicorp.com/terraform/language/files/dependency-lock)are automatically managed for new and updated stacks. You decide when to retrieve the latest versions available from the configured source of Terraform providers. Providers are updated within the version constraints of the Terraform configuration. For instructions, see[Retrieving the Latest Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-lock-file.htm).

[Roll Back Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#)

Roll back a stack to a previous known state. Rolling back is a good alternative to spending time troubleshooting a stack's unknown state.

To roll back, first identify the successful apply job that you want. This "target job" uses a different Terraform configuration.[Create a plan rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-plan-rollback.htm)for this target job, and then[create an apply rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-apply-rollback.htm)using the generated execution plan.

## Availability

The Resource Manager service is available in all Oracle Cloud Infrastructure commercial regions. See[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About)for the[list](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About__The)of available regions, along with associated locations, region identifiers, region keys, and availability domains.

## Generalized Workflow

The following image represents a generalized view of the Resource Manager workflow.
[
- 

[Create a Terraform configuration.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)
Note  
  
For Terraform configuration sources supported with Resource Manager, see[Where to Store Your Terraform Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#sources).
- [Create a stack.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-stack.htm)
- [Run a plan job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-plan.htm), which produces an execution plan.
- [Review the execution plan (job logs).](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-logs.htm)
- If changes are needed in the execution plan,[update the configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/update-stack-tf-config.htm)and run a plan job again.
- [Run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-apply.htm)to provision resources.
- Review[state files](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-tf-state.htm)and[log files](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/get-job-logs.htm), as needed.
- You can optionally reapply your configuration, with or without making changes, by running an apply job again.
- Optionally, to release the resources running on a stack,[run a destroy job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/create-job-destroy.htm).

For a detailed walkthrough of the Resource Manager workflow, see[Getting Started](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/samplecomputeinstance.htm).

## Ways to Access Resource Manager

You can access the Resource Manager service using the Console or the[Resource Manager REST API](https://docs.oracle.com/iaas/api/#/en/resourcemanager/). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Console: To access Resource Manager using the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password. Open the navigation menu and select Developer Services . Under Resource Manager , select Overview .

API: To access Resource Manager through APIs, use[Resource Manager API](https://docs.oracle.com/iaas/api/#/en/resourcemanager/).

CLI: See[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

## Default Provider

By default, Resource Manager supports`terraform-provider-oci`, the Terraform provider for Oracle Cloud Infrastructure.

For supported third-party Terraform providers, see[Supported Terraform Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/providers.htm).

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.
Important  
  
Policies for managing Oracle Cloud Infrastructure resources are also required for Resource Manager operations that access resources. For example,[running an apply job](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)on a stack that includes Compute instances and subnets requires policies that grant you permissions for those resource types, in the compartments where you want to provision the resources. To see examples of policies for managing Oracle Cloud Infrastructure resources, see[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

Administrators: For common policies that give groups access to Resource Manager resources, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/resourcemanager_security.htm#iam-policies)(Securing Resource Manager).

## Security

In addition to creating IAM policies, follow these security best practices for Resource Manager.
- Limit the use of sensitive information in configuration and output files
- Perform a security audit
- Use[private endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/private-endpoints.htm)to securely access resources without exposing network traffic to the public

See[Securing Resource Manager](https://docs.oracle.com/iaas/Content/Security/Reference/resourcemanager_security.htm).

## Limits on Resource Manager Resources

See[Resource Manager Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#Resource_Manager_Limits).

For a list of applicable limits and[instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm), see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm). To set compartment-specific limits on a resource or resource family, administrators can use[compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm)
