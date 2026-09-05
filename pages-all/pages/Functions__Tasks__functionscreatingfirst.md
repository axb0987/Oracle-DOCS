# Creating, Deploying, and Invoking a Helloworld Function
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfirst.htm
- Fetched: 2026-09-05 02:08 CDT

# Creating, Deploying, and Invoking a Helloworld Function

Find out how to create, deploy, and invoke a helloworld function with OCI Functions.

You can start off using OCI Functions by using Fn Project CLI commands to:
- create a simple helloworld function written in java
- push the image to the Docker registry that's configured for OCI Functions
- deploy the function to an application in OCI Functions
- invoke the function
Tip  
  
If you aren't able to successfully complete one of the steps in this topic, review the solutions for common problems (see[Troubleshooting OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting.htm)).

To get started with OCI Functions:
- Confirm that you have completed the steps in the[Functions QuickStart Guides](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartguidestop.htm).
- Sign in to the Console as a functions developer.
- 

Use the Console to create a new application in OCI Functions:
- Open the navigation menu and select Developer Services . Under Functions , select Applications .
- Select the region you intend to use for OCI Functions.

We recommend that you use the same region as the Docker registry specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)).
- 

Select the compartment specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)).

The Applications page shows the applications already defined in the compartment.
- 

Select Create Application and specify:
- The name for the new application as helloworld-app.
- 

The VCN and subnet (or subnets, up to a maximum of three) in which to run the function. For example, a VCN called acme-vcn-01 and a public subnet called Public Subnet IHsY:US-PHOENIX-AD-1). Note that a public subnet requires an internet gateway in the VCN, and a private subnet requires a service gateway in the VCN. If a regional subnet has been defined, best practice is to select that subnet to make failover across availability domains simpler to implement. If a regional subnet has not been defined and you need to meet high availability requirements, select multiple subnets. We recommend that subnets are in the same region as the Docker registry specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)).
- Select Create .
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, create a helloworld java function by entering:

```

```

A directory called helloworld-func is created, containing:
- A function definition file called func.yaml, containing the minimum amount of information required to build and run the function. See the[Fn Project documentation](https://github.com/fnproject/docs/blob/master/fn/develop/func-file.md)to find out about the additional parameters you can include in a func.yaml file.
- A /src directory containing source files and directories for the helloworld function (including /src/main/java/com/example/fn/HelloFunction.java).
- A Maven configuration file called pom.xml that specifies the project artifacts and dependencies required to compile the function from the source files.
- Change directory to the newly created helloworld-func directory.
- 

Enter the following single Fn Project command to build the function and its dependencies as a Docker image called helloworld-func, push the image to the specified Docker registry, and deploy the function to OCI Functions in the helloworld-app:

```

```

The`-v`option simply shows more detail about what Fn Project commands are doing (see[Using the Fn Project CLI with OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingwithfncli.htm)).
- (Optional) Assuming the specified Docker registry is Oracle Cloud Infrastructure Registry, use the Console to confirm that the helloworld-func image has been pushed to Oracle Cloud Infrastructure Registry successfully:
- Open the navigation menu and select Developer Services . Under Containers &amp; Artifacts , select Container Registry .
- 

Choose the registry's region.

You see all the repositories in the registry to which you have access. The image you pushed is in a new repository with a name constructed from:
- the repository name prefix in the address of the Docker registry in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm))
- the name of the helloworld-func image

For example, the new repository might be called`acme-repo/helloworld-func`.
- Select the name of the new repository. You see details of the helloworld-func image that's been pushed to Oracle Cloud Infrastructure Registry.
- 

(Optional) Use the Console to confirm that the function has been deployed to OCI Functions successfully:
- Open the navigation menu and select Developer Services . Under Functions , select Applications .
- 

Select the compartment specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)).

The Applications page shows that an application called helloworld-app has been created.
- 

Select the helloworld-app application to see the functions within it.

The Functions tab shows that the helloworld-func function has been deployed to OCI Functions.
- 

In a terminal window, invoke the helloworld-func function by entering:

```

```

The 'Hello World !' message is displayed.
