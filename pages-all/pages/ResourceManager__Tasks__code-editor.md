# Editing a Configuration Using Code Editor
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/code-editor.htm
- Fetched: 2026-09-05 02:54 CDT

# Editing a Configuration Using Code Editor

Use Code Editor to edit the Terraform configuration associated with a stack in Resource Manager.

Note  
  
Ensure that you have policy access to Code Editor. Code Editor uses the same IAM policies as Cloud Shell. For more information, see[Required IAM Policy (Cloud Shell)](https://docs.oracle.com/iaas/Content/API/Concepts/devcloudshellintro.htm#Required_IAM_Policy). For more information about Code Editor features and functionality, see[Code Editor](https://docs.oracle.com/iaas/Content/API/Concepts/code_editor_intro.htm).

In the Console, you can open a Terraform configuration from the Stack details page, or browse the Code Editor tree view to find the Terraform configuration that you want.

## Opening a Configuration from Stack Details

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- Go to Edit and then select Edit Terraform configuration in code editor .
The Terraform configuration opens in Code Editor. Tree navigation on the left side of Code Editor lists the selected Terraform configuration under RESOURCE MANAGER , Compartments , the compartment name, Stacks , the stack name, and the name of the Terraform configuration.
- Edit the Terraform configuration.
- To save changes, go to the Code Editor tree navigation, right-click the associated stack, and select Save changes .
- To run a plan job using the changes, go to the Code Editor tree navigation, right-click the associated stack, and select the relevant option.
- Run Plan action on stack (displayed for configurations stored in Git)
- Save changes and run Plan action (displayed for configurations stored elsewhere)
- To run an apply job using the changes, go to the Code Editor tree navigation, right-click the associated stack, and select the relevant option.
- Run Apply action on stack (displayed for configurations stored in Git)
- Save changes and run Apply action (displayed for configurations stored elsewhere)

## Opening a Configuration from Code Editor

- Go to the Developer Tools icon in the top of the Console (next to the region indicator) and then select Code Editor .
- In the tool bar on the left of the Code Editor window, select the Oracle Cloud Infrastructure icon.
- Select RESOURCE MANAGER .
- Expand the tenancy, the Compartments folder, and the subfolder for the compartment that contains the stack that you want.
- Expand Stacks and then expand the stack that you want.
- Select the name of Terraform configuration file that you want to edit.
The file opens.
- Edit the file.
- To save changes, go to the Code Editor tree navigation, right-click the associated stack, and select Save changes .
- To run a plan job using the changes, go to the Code Editor tree navigation, right-click the associated stack, and select the relevant option.
- Run Plan action on stack (displayed for configurations stored in Git)
- Save changes and run Plan action (displayed for configurations stored elsewhere)
- To run an apply job using the changes, go to the Code Editor tree navigation, right-click the associated stack, and select the relevant option.
- Run Apply action on stack (displayed for configurations stored in Git)
-
