# Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm
- Fetched: 2026-09-05 02:07 CDT

# Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure

Find out how create an Fn Project CLI context to connect to Oracle Cloud Infrastructure for use with OCI Functions.

Before using OCI Functions, you have to configure the Fn Project CLI to connect to your Oracle Cloud Infrastructure tenancy.

When the Fn Project CLI is initially installed, it's configured for a local development 'context'. To configure Fn Project CLI to connect to your Oracle Cloud Infrastructure tenancy instead, you have to create a new context. The context specifies OCI Functions endpoints, the OCID of the compartment to which deployed functions will belong, and the address of the Docker registry to and from which to push and pull images.

You can define multiple contexts, each stored in a different context file in .yaml format. By default, the individual context files are stored in the`~/.fn/contexts`directory. The`~/.fn/config.yaml`file specifies which context file Fn Project uses.

To create a new context, you can create a new context file manually and edit the`~/.fn/config.yaml`file by hand to point to that file. Alternatively, you can use the Fn Project CLI to interactively create the new context file and instruct the Fn Project CLI to start using that file, as described below.

If you are using Cloud Shell as your development environment, two Fn Project CLI contexts have already been created for you (a default context and a context for the current region). For more information, see[OCI Functions on Cloud Shell QuickStart Guide](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#functionsquickstartcloudshell_topic_setup_CloudShell_dev_env_Setup_Fn_Project_CLI_context). You simply have to copy and paste commands from the Getting Started page into the Cloud Shell window:
- to instruct the Fn Project CLI to use the context for the current region
- to provide the OCID of the compartment that will own deployed functions
- to provide the Oracle Cloud Infrastructure Registry address that you want to use with OCI Functions

The instructions in this topic assume:
- you are not using Cloud Shell as your development environment
- you are using Linux
- you have already completed the steps in[Installing the Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstallfncli.htm)

To create a new context file using the Fn Project CLI:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, create the new Fn Project CLI context for Oracle Cloud Infrastructure by entering:

```

```

where &lt;my-context&gt; is a name of your choosing. For example:

```

```

Note that you specify`--provider oracle`to enable authentication and authorization using Oracle Cloud Infrastructure request signing, private keys, user groups, and policies that grant permissions to those user groups.
- 

Specify that the Fn Project CLI is to use the new context by entering:

```

```

where &lt;my-context&gt; is the name you specified in the previous step. For example:

```

```

- 

Configure the new context with the OCID of the compartment that you want to own the deployed functions (you might have created a new compartment specifically for this purpose, see[Creating Compartments to Own Network Resources and OCI Functions Resources in the Tenancy, if they don't exist already](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingcompartment.htm)) by entering:

```

```

For example:

```

```

- 

Configure the new context with the api-url endpoint to use when calling the API by entering:

```

```

where`<api-endpoint>`is one of the endpoints in the list of Functions endpoints in the[Functions API](https://docs.oracle.com/iaas/api/#/en/functions/latest/), in the format`https://functions.<region-identifier>.oci.oraclecloud.com`. The`<region-identifier>`in`<api-endpoint>`is the identifier of the Oracle Cloud Infrastructure region in which you'll be creating and deploying functions. For example,`us-phoenix-1`.

For example:

```

```

- 

Configure the new context with the address of the Docker registry (for example, Oracle Cloud Infrastructure Registry) that you want to use with OCI Functions by entering:

```

```

where:
- 

`<region-key>`is the key of the Oracle Cloud Infrastructure Registry region. For example,`phx`for Phoenix. See[Availability by Region](https://docs.oracle.com/iaas/Content/Registry/Concepts/registryprerequisites.htm#regional-availability).

We recommend that the Docker registry you specify is in the same region as the subnet on which you intend functions to run.
- `<tenancy-namespace>`is the auto-generated Object Storage namespace string of the tenancy in which to create repositories (as shown on the Tenancy Information page). For example, the namespace of the`acme-dev`tenancy might be`ansh81vru1zp`. Note that for some older tenancies, the namespace string might be the same as the tenancy name in all lower-case letters (for example,`acme-dev`).
- `<repo-name-prefix>`is (optionally) a repository name prefix to pre-pend to the names of functions that you deploy, to specify the names of repositories to which to push function images. Using a repository name prefix can make it easier to organize and control access to repositories in the registry. See[Notes about repository names and repository name prefixes](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm#Create_an_Fn_Project_CLI_Context_to_Connect_to_Oracle_Cloud_Infrastructure__section_repository_name_notes).

For example:

```

```

- 

(Optional) Configure the new context with the OCID of the compartment for repositories to and from which you want OCI Functions to push and pull function images, by entering:

```

```

For example:
```

```

If you do not specify a value for`oracle.image-compartment-id`, OCI Functions pushes and pulls images to and from repositories in the root compartment. In both cases, a suitable policy statement must exist to allow you to manage repositories in the compartment (either the compartment specified by`oracle.image-compartment-id`, or the root compartment). See[Policy Statements to Give OCI Functions Users Access to Oracle Cloud Infrastructure Registry Repositories](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#userregistrypolicy).

OCI Functions constructs the name of the repository for a function image by pre-pending the repository name prefix to the function name. Repository names are unique across all compartments in the entire tenancy. Note that OCI Functions behaves as follows with regards to compartments and`oracle.image-compartment-id`when pushing an image to a named repository:
- If a repository with that name already exists in the compartment specified by`oracle.image-compartment-id`, OCI Functions successfully pushes the image to that repository.
- If a repository with that name does not exist in any compartment (including in the root compartment) in the tenancy, OCI Functions creates a new repository with that name in the compartment specified by`oracle.image-compartment-id`and successfully pushes the image to it.
- If a repository with that name already exists in the tenancy but in a different compartment to the one specified by`oracle.image-compartment-id`, OCI Functions issues an error. For OCI Functions to successfully push the image, you have to either set`oracle.image-compartment-id`to the OCID of the compartment of the existing repository, or specify a different repository name (by renaming the function, or by specifying an alternative repository name prefix).
- 

(Optional) Verify the Fn Project CLI context you've created by viewing the context file. For example, by entering:

```

```

The context file contains:
```

```

When you have completed the steps in this topic, go on to[Setting the Context for the Fn Project CLI Using the oracle.profile Parameter](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionssetoracleprofile.htm).

## Notes about repository names and repository name prefixes

When deploying a function, the function image is pushed to a repository in the registry specified by the`registry:`setting in the Fn Project CLI context. The name of the repository is either the same as the name of the function (that is,`<function-name>`), or the name of the function with a repository name prefix pre-pended to it (that is,`<repo-name-prefix>/<function-name>`).

When deploying a function, note the following. If a repository named`<function-name>`(or`<repo-name-prefix>/<function-name>`if you've specified a`<repo-name-prefix>`) does not already exist in the registry:
- If the registry's Create repository on first push in root compartment property is set to true, a new private repository is created in the root compartment
- If the registry's Create repository on first push in root compartment property is set to false, a new repository cannot be created, and the attempt to push the function image fails.

If the registry's Create repository on first push in root compartment property is set to false and a suitable repository does not already exist, do one of the following before deploying a function:
- Create a new repository with the same name as the function, and do not specify a`<repo-name-prefix>`in the Fn Project CLI context. For example, if the function is named`hello-world`, create a new repository named`hello-world`.
- Create a function with the same name as an existing repository, and do not specify a`<repo-name-prefix>`in the Fn Project CLI context. For example, if the existing repository is called`hello-galaxy`, name the new function`hello-galaxy`.
- If you want to use a repository name prefix to organize and control access to repositories, specify a`<repo-name-prefix>`in the Fn Project CLI context, and also create a repository with a name that includes both the repository name prefix and the function name. For example, to store images for a function named`hello-world`in a repository named`acme-repo/hello-world`, specify`phx.ocir.io/ansh81vru1zp/acme-repo`in the Fn Project CLI context, and also create a repository named`acme-repo/hello-world`
