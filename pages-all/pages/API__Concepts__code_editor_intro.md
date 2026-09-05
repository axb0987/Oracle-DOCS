# Code Editor
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/code_editor_intro.htm
- Fetched: 2026-09-05 01:35 CDT

# Code Editor

This section describes how to use Oracle Cloud Infrastructure (OCI) Code Editor, an in-console editing environment that enables you to edit code and update service workflows and scripts.

Oracle Cloud Infrastructure (OCI) Code Editor provides a rich, in-console editing environment that enables you to edit code and update service workflows and scripts without having to switch between the Console and your local development environment. Code Editor provides a convenient way to perform common code updates for various services, such as creating and deploying Functions, editing Terraform configurations used with Resource Manager stacks, or creating and editing an API.

For more information, see[the Code Editor product page](https://www.oracle.com/devops/code-editor/).
Tip  
  
Watch a[video introduction](https://apexapps.oracle.com/pls/apex/f?p=44785:265:0:::265:P265_CONTENT_ID:32715)to Code Editor.

## Code Editor Features

Code Editor includes the following features:
- 

Rich native support for over a dozen programming languages, including syntax highlighting, intelligent completions, bracket matching, linting, code navigation (go to method definition, find all references), and refactoring.
- 

Managed OCI service plug-ins that provide a native, integrated experience for supported OCI services, offering specific functionality and coding workflows for each supported service. For example, the Functions plugin allows developers to edit deploy and invoke functions from within the Code Editor window.
- 

Git integration that enables you to clone any Git-based repository, track changes made to files, and commit, pull and push code directly from within the Code Editor, allowing you to contribute code and revert code changes with ease.
- Direct integration with Cloud Shell allows you to read and edit code files stored in the Cloud Shell home directory and have direct access to the 30+ cloud-based tools pre-installed with Cloud Shell.
- Comprehensive workspace and user management control enables you to manage your code projects as independent workspaces. For example, you can modify and set persistent settings that apply to folders in a workspace instead of modifying environment configurations each time.
- Complete personalization of fonts, color schemes, screen layouts, keyboard shortcuts, and language localization.
- Persistant state across sessions auto-saves progress and persists state across multiple user sessions, so Code Editor automatically opens the last edited page on startup.

## Required IAM Policy

Code Editor uses the same IAM policies as Cloud Shell. For more information, see[Cloud Shell Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cloudshellintro.htm#Required_IAM_Policy).
If you will be using any service plugins within Code Editor, you need the following policy in addition to any policies required by the underlying service:
```

```

For example, if you wish to manage Functions resources using the Functions plugin in Code Editor, you need the policy listed above and the policies listed[here](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#Create_Policies_to_Control_Access_to_Network_and_FunctionRelated_Resources).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)
