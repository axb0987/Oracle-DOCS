# Creating and Deploying Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsuploading.htm
- Fetched: 2026-09-05 02:09 CDT

# Creating and Deploying Functions

Find out how to create and deploy functions to OCI Functions using Fn Project CLI commands.

You use Fn Project CLI commands to create and deploy functions to OCI Functions.
Tip  
  
If you aren't able to successfully complete one of the steps in this topic, review the solutions for common problems (see[Troubleshooting OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting.htm)).

## Using Fn Project CLI Commands

Tip  
  
From time to time, new versions of the Fn Project CLI are released. We recommend you regularly check that the latest version is installed. For more information, see[Steps to upgrade the Fn Project CLI](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm#functionsupgradingfncli_topic-Steps-to-upgrade-Fn-Project-CLI).

To create and deploy a function to OCI Functions using Fn Project CLI commands:
- Confirm that you have completed the steps in the[Functions QuickStart Guides](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartguidestop.htm).
- 

If the application to which you want to add the function doesn't yet exist in OCI Functions, create it now using the Fn Project CLI or the Console. For example, you might create a new application called acmeapp. See[Creating Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingapps.htm).
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, change directory to the directory containing the function code.
- 

Initialize the function by entering:

```

```

where:
- `<runtime-language>`is one of the supported runtime languages (currently go, java, node, python, ruby, and dotnet (for C#) are supported)
- `<function-name>`is the name to use as the function name. If you don't specify a function name, the name of the current directory (in lower case) is used. Avoid entering confidential information.

For example:

```

```

A directory is created with the function name you specified, containing:
- A function definition file called func.yaml, containing the minimum amount of information required to build and run the function. See the[Fn Project documentation](https://github.com/fnproject/docs/blob/master/fn/develop/func-file.md)to find out about the additional parameters you can include in a func.yaml file.
- A /src directory containing source files and directories.
- A Maven configuration file called pom.xml that specifies the project artifacts and dependencies required to compile the function from the source files.

Note that depending on the runtime language you specify, the`fn init`command might create an /example directory containing code for a helloworld application. As a matter of good practice, you'll probably want to delete the /example directory.
- Change directory to the newly created directory.
- 

Enter the following single Fn Project command to build the function and its dependencies as a Docker image, push the image to the specified Docker registry, and deploy the function to OCI Functions:

```

```

where`<app-name>`is the name of the application in OCI Functions to which you want to add the function. For example:

```

```

The`-v`option simply shows more detail about what Fn Project commands are doing (see[Using the Fn Project CLI with OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingwithfncli.htm)).

Note that you can build, push, and deploy the function using separate Fn Project commands, instead of the single`fn deploy`command.

Also note that if you are adding the function to an application that has a signature verification policy enabled, you have to specify additional options. See[Signing Function Images and Enforcing the Use of Signed Images from Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsenforcingsignedimagesfromocir.htm).
- (Optional) Assuming the specified Docker registry is Oracle Cloud Infrastructure Registry, use the Console to confirm that the image has been pushed to Oracle Cloud Infrastructure Registry successfully:
- Open the navigation menu and select Developer Services . Under Containers &amp; Artifacts , select Container Registry .
- 

Choose the registry's region.

You see all the repositories in the registry to which you have access. The image you pushed is in a new private repository with a name constructed from:
- the repository name prefix in the address of the Docker registry in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm))
- the name of the image you pushed

For example, the new repository might be called`acme-repo/acme-func`.
- Select the name of the new repository. You see details of the image that's been pushed to Oracle Cloud Infrastructure Registry
- 

(Optional) Use the Console to confirm that the function has been deployed to OCI Functions successfully:
- Open the navigation menu and select Developer Services . Under Functions , select Applications .
- 

Select the compartment specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)).

The Applications page shows the applications in the compartment, including the one you specified in the`fn deploy`command.
- 

Select the name of the application you specified in the`fn deploy`command to see the functions within it.
