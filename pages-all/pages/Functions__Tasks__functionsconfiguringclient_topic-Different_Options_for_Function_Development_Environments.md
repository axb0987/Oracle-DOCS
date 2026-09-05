# Different Options for Function Development Environments
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfiguringclient_topic-Different_Options_for_Function_Development_Environments.htm
- Fetched: 2026-09-05 02:07 CDT

# Different Options for Function Development Environments

Find out about the different OCI Functions development environments you can set up.

When setting up your OCI Functions development environment, you have different options:
- 

Option 1: Setting up Cloud Shell. (Recommended) For users trying out OCI Functions for the first time, this is the recommended way to get started quickly. By copying and pasting a few commands from the Console into the Cloud Shell window, you can set up an OCI Functions development environment in just a few minutes. If you set up Cloud Shell, two ready-made Fn Project CLI contexts are provided (if you want to create your own Fn Project CLI context, you'll have to specify`--provider oracle-cs`when you create the context).

This option enables you to experiment creating, deploying, and invoking new functions. You can also explore OCI Functions using the samples on Git Hub (see[Oracle Functions Samples](https://github.com/oracle/oracle-functions-samples)). Note that Cloud Shell allocates 5GB for each user’s home directory, which cannot be expanded or mounted to external storage. It is your responsibility to perform regular housekeeping to keep space usage below 5GB (see[Freeing Up Cloud Shell Storage By Removing Unused Images](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscloudshellcleanup.htm)).

Use the[Functions QuickStart on Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm)if you want to set up Cloud Shell as your OCI Functions development environment.
- 

Option 2: Setting up a local machine. For most users (especially Mac and Linux users), this will be the way to work with OCI Functions. If you set up a local machine, you'll have to specify`--provider oracle`when you create a new Fn Project CLI context.

This option enables OCI Functions to perform authentication and authorization using Oracle Cloud Infrastructure request signing, private keys, user groups, and policies that grant permissions to those user groups.

Use the[Functions QuickStart on Local Host](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm)if you want to set up a local machine as your OCI Functions development environment.
- 

Option 3: Setting up an Oracle Cloud Infrastructure compute instance. For some users, this will be more convenient than setting up a local machine. If you set up an Oracle Cloud Infrastructure compute instance, you'll have to specify`--provider oracle-ip`when you create a new Fn Project CLI context.

This option enables OCI Functions to perform authentication and authorization using instance OCIDs, dynamic groups, and policies granting permissions to those dynamic groups. This approach removes the requirement for users to manage private keys. Note that to set up an OCI Functions development environment on an Oracle Cloud Infrastructure compute instance, you must:
- have permission to create dynamic groups
- create a new dynamic group that includes the compute instance's OCID
- create a policy to give the new dynamic group access to function resources, network resources, and Oracle Cloud Infrastructure Registry
- specify`--provider oracle-ip`when you create a new Fn Project CLI context

Use the[Functions QuickStart on an OCI Compute Instance](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartocicomputeinstance.htm)if you want to set up an Oracle Cloud Infrastructure compute instance as your OCI Functions development environment.

## Setting Fn Project CLI context for different development environments

The Fn Project CLI uses a context to connect to your Oracle Cloud Infrastructure tenancy. The context specifies OCI Functions endpoints, the OCID of the compartment to which deployed functions will belong, and the address of the Docker registry to and from which to push and pull images.

When setting up a local machine development environment, or an Oracle Cloud Infrastructure compute instance development environment, you have to create your own Fn Project CLI context. The Cloud Shell development environment provides two ready-made contexts, although you can create your own.

When you create an Fn Project CLI context, you use the`fn create context`command, and you specify an authentication provider. The provider to specify depends on the development environment you are using, as shown in the following table:

Development Environment Command to create Fn Project CLI context
Cloud Shell`fn create context <my-context> --provider oracle-cs`
Local Machine`fn create context <my-context> --provider oracle`
OCI Compute Instance`fn create context <my-context> --provider oracle-ip`
