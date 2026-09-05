# Editing a Configuration Using Visual Studio Code
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/vscode.htm
- Fetched: 2026-09-05 02:57 CDT

# Editing a Configuration Using Visual Studio Code

Work with stacks and Terraform configurations in Visual Studio Code using the OCI Resource Manager extension for VS Code.

OCI Resource Manager is an extension of[OCI Toolkit for Visual Studio Code .

## Prerequisites

Either install[OCI Toolkit for Visual Studio Code or install both[OCI Toolkit Core and OCI Resource Manager .

As with any Oracle client, obtain an API signing key. For guidance, see[Generating an API Signing Key (Console)](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#apisigningkey_topic_How_to_Generate_an_API_Signing_Key_Console).

## Installing the Extension

For instructions on installing the OCI Resource Manager extension for VS Code, see the following.

- [Visual Studio Code Plugin for Resource Manager (Visual Studio | Marketplace)](https://marketplace.visualstudio.com/items?itemName=Oracle.rms)
- [Visual Studio Code Plugin for Resource Manager (GitHub)](https://github.com/oracle-samples/oci-vscode-toolkit)

## Listing Stacks

In the tree navigation on the left side, expand the node for the compartment that you want.

## Opening a Terraform Configuration for Editing

- In the tree navigation on the left side, expand the node for the compartment that you want.
- Expand the node for the stack that you want.
- Double-click the node for the Terraform configuration that you want.
The Terraform configuration file opens.

## Saving Changes

- In the tree navigation on the left side, expand the node for the compartment that you want.
- Right-click the stack that you want, and then select Save changes .
If the configuration is stored in Git, then a prompt for using the Git command line appears. If the configuration is stored outside Git, then a prompt appears for overwriting the existing file.
- Follow the prompts.

## Running the Plan Action

Note  
  
You can run the plan action on a stack outside Visual Studio Code. See[Creating a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm)and[Editing a Configuration Using Code Editor](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/code-editor.htm).

- In the tree navigation on the left side, expand the node for the compartment that you want.
- Right-click the stack that you want, and then select the relevant option.
- Run Plan action on stack (displayed if the configuration is stored in Git)
- Save changes and run Plan action on stack (displayed if the configuration is stored elsewhere; for example, locally, or in an Object Storage bucket)
The status of the action is shown on the lower right corner. If the configuration is stored outside Git, then you are prompted to accept overwriting the existing file.
- Follow the prompts.
You can go to the Console to check status. Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-logs-content.htm).

## Running the Apply Action

Note  
  
You can run the apply action on a stack outside Visual Studio Code. See[Creating an Apply Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)and[Editing a Configuration Using Code Editor](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/code-editor.htm).

- In the tree navigation on the left side, expand the node for the compartment that you want.
- Right-click the stack that you want, and then select the relevant option.
- Run Apply action on stack (displayed if the configuration is stored in Git)
- Save changes and run Apply action on stack (displayed if the configuration is stored elsewhere; for example, locally, or in an Object Storage bucket)
The status of the action is shown on the lower right corner. If the configuration is stored outside Git, then a prompt appears for overwriting the existing file.
- Follow the prompts.

## Downloading the Terraform Configuration

- In the tree navigation on the left side, expand the node for the compartment that you want.
- Right-click the stack that you want, and then select Download configuration .
If the configuration is stored in Git, then a prompt for the Git URL appears at the top of the window, followed by prompts for credentials. If the configuration is stored outside Git, then a prompt might appear for overwriting the existing file.
-
