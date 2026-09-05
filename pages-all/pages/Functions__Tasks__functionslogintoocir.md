# Logging in to Oracle Cloud Infrastructure Registry
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionslogintoocir.htm
- Fetched: 2026-09-05 02:08 CDT

# Logging in to Oracle Cloud Infrastructure Registry

Find out how to log in to Oracle Cloud Infrastructure Registry for use with OCI Functions.

Before using OCI Functions, you have to log Docker in to the Docker registry in which you are going to store your functions as Docker images. This is the Docker registry specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)).

You can store functions in public and private repositories in Oracle Cloud Infrastructure Registry, an Oracle-managed registry built on top of Oracle Cloud Infrastructure.

When you log Docker into a Docker registry, you have to provide the appropriate authentication details. For example, in the case of Oracle Cloud Infrastructure Registry, you have to provide the tenancy Object Storage namespace, the user name, and the user's auth token.

If you are using Cloud Shell as your development environment, you simply have to copy and paste commands from the Getting Started page into the Cloud Shell window. For more information, see[OCI Functions on Cloud Shell QuickStart Guide](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm#functionsquickstartcloudshell_topic_setup_CloudShell_dev_env_Log_in_to_registry).

The instructions in this topic assume:
- you are not using Cloud Shell as your development environment
- you are using Linux
- you have already completed the steps in[Starting Docker](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsstartdocker.htm)

To log Docker into Oracle Cloud Infrastructure Registry:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, log in to Oracle Cloud Infrastructure Registry by entering:

```

```

where`<region-key>`is the key for the Oracle Cloud Infrastructure Registry region specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)). For example,`phx`for Phoenix. See[Availability by Region](https://docs.oracle.com/iaas/Content/Registry/Concepts/registryprerequisites.htm#regional-availability).

For example:

```

```

- 

When prompted for Username , enter the name of the user you will be using with OCI Functions to create and deploy functions, in the format:

`<tenancy-namespace>/<username>`

where`<tenancy-namespace>`is the auto-generated Object Storage namespace string of the tenancy in which to create repositories (as shown on the Tenancy Information page). For example,`ansh81vru1zp/jdoe@acme.com`.

Note that for some older tenancies, the namespace string might be the same as the tenancy name in all lower-case letters (for example,`acme-dev`).

If your tenancy is federated with Oracle Identity Cloud Service, use the format`<tenancy-namespace>/<domain-name>/<username>`. For federated users, the`<domain-name>/<username>`is displayed in the Profile menu in the Console. For example, if the namespace string of your tenancy is`ansh81vru1zp`, and your tenancy is federated with Oracle Identity Cloud Service, and your username is`jdoe@acme.com`, then enter`ansh81vru1zp/oracleidentitycloudservice/jdoe@acme.com`.

You must have already generated an Oracle Cloud Infrastructure auth token for the user you specify (see[Generating an Auth Token to Enable Login to Oracle Cloud Infrastructure Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsgenerateauthtokens.htm)).
- When prompted for Password , enter the user's Oracle Cloud Infrastructure auth token. Having entered the password, Docker might warn you that the password is stored unencrypted in the Docker configuration file. The warning includes a[link to the Docker documentation](https://docs.docker.com/engine/reference/commandline/login/#credentials-store)where you can find out how to configure a credential helper. We recommend you review the information in the[Docker documentation](https://docs.docker.com/engine/reference/commandline/login/#credentials-store)and consider using an external credentials store for increased security.

When you have completed the steps in this topic, you have completed the configuration tasks for your client environment. Go on to[Verifying Your Configuration for Function Development](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsverifyingconfig.htm)
