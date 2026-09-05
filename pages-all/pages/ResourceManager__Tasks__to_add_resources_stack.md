# Adding Unmanaged Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm
- Fetched: 2026-09-05 02:56 CDT

# Adding Unmanaged Resources

Add existing resources to a stack in Resource Manager.
Note  
  
Some steps in these instructions use[Terraform CLI](https://developer.hashicorp.com/terraform/cli); most steps use the Oracle Cloud Infrastructure Console.
- 

Gather information about the unmanaged resources that you want to add: Note their[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Unmanaged resources are created outside Resource Manager.
Tip  
  
You can generate a Terraform configuration that lists all resources in a compartment. For instructions, see[Creating a Stack from an Existing Compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm).
- 

[Gather stack information](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm#)

- 

In the Console, access the details page for the stack that you want to add the resources to.
- Open the navigation menu and select Developer Services . Under Resource Manager , select Stacks .
- 

Under List Scope , select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
- 

Select the name of the stack to display its details page.
- 

Confirm that managed resources are up-to-date: Generate a drift detection report.
- 

Go to More actions and select Run drift detection .
- 

In the Run drift detection panel, select All resources .
- 

Select Run drift detection .

A work request is started. When the work request is complete, the drift status appears in the Stack information tab.
- 

Go to More actions and select View drift detection report .

A panel lists the drift status of the specified resources defined by the stack. Resources are identified by resource names.
- 

To view details of drift status for a resource, expand the resource.

Actual and expected properties are listed.
- 

If differences between actual and expected properties are reported, make your resources match the properties of your Terraform configuration:[run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm). In the Stack Details page, select Apply .

You can alternatively address these differences when manually editing the Terraform configuration later.
- 

Download the stack's Terraform configuration file: In the Stack information tab, to the right of Terraform configuration , select Download .
- 

Download the stack's state file:
- Go to the details page for the most recent apply job: Select the job link under Jobs .
- On the job details page, select Download Terraform state .
- 

[Update the state file using Terraform CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm#)

- 

Set up Terraform CLI on your local machine.

For instructions, see[Terraform CLI](https://developer.hashicorp.com/terraform/cli).
- 

On your local machine, go to Terraform CLI and navigate to the directory containing the downloaded Terraform configuration and state file.
- 

For each[unmanaged resource previously identified](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm#top__unmanaged-resources), import the state file by running the`terraform import`command:
```

```

Example:
```

```

For more information about this command, see[Terraform Import CLI Command](https://developer.hashicorp.com/terraform/cli/commands/import).
- 

Refresh the state file by running the`terraform refresh`command:
Note  
  
To refresh for a specific resource, use the refresh target`-target=<resource>`.

For more information about this command, see[Terraform Refresh CLI Command](https://developer.hashicorp.com/terraform/cli/commands/refresh).
- 

Manually update the downloaded Terraform configuration to include the[unmanaged resource previously identified](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm#top__unmanaged-resources).

If any unresolved drift remains in[the drift detection report](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm#top__drift), address those differences in your manual update.
- 

[Update the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm#)

- 

Access the stack's details page again.
- Open the navigation menu and select Developer Services . Under Resource Manager , select Stacks .
- 

Under List Scope , select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
- 

Select the name of the stack to display its details page.
- 

Import the refreshed state file to the stack.
- 

Go to More actions and select Import state .
- 

In the Import state dialog, add your Terraform state file, either by dragging and dropping it onto the dialog's control, or by selecting Browse and navigating to the file location.
- 

Select Import .
- 

Upload the[manually edited Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm#top__config)to the stack.
- 

In the Stack information tab, next to Terraform configuration , select Upload .
- 

In the Edit stack dialog, under Stack configuration , select .Zip file and add your revised Terraform configuration.

You can either drag and drop your Terraform configuration .zip file onto the control or select Browse and navigate to the location of the .zip file.
- 

Select Next as needed and then select Save changes .
- 

[Confirm that infrastructure is up-to-date](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/to_add_resources_stack.htm#)

- 

Select Plan .
- 

In the Plan dialog, review the plan job Name and update it if needed.
- 

Select Plan .

The new plan job is listed under Jobs , with an initial state of Accepted . Soon the status changes to In progress . When the job is complete, view the job log to confirm no changes.

Example of a job log reporting no changes:
```

```
