# OCI SDK Authentication Methods
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm
- Fetched: 2026-09-05 01:35 CDT

# OCI SDK Authentication Methods

The OCI SDK and CLI supports the following authentication methods:
- API key-based authentication
- Session token-based authentication
- Instance principal
- Resource principal

This section discusses each method in detail and provides examples.

## API Key-Based Authentication

In this authentication method, you create a configuration file and store it on the local disk. The configuration file contains details such as the user OCID, tenancy OCID, region, private key path, and fingerprint. This authentication method creates a permanent configuration file on your machine. It should be used if you are working from a secure network and are comfortable storing private keys and configuration locally.

### Examples

The following section shows examples of API key-based authentication.

[CLI](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

You can use the following CLI commands to set up API key-based authentication:

" oci setup bootstrap ": This command helps to set up a configuration file. You can login via a browser and your configuration file is automatically created and uploaded to the console. For more details, see[oci setup bootstrap](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/setup/bootstrap.html)

" oci setup config ": This command helps to set up a configuration file from a command line session without browser support via an interactive CLI command which prompts you for information (including a user OCID, a tenancy OCID, and region name) and create a private key. Once the file is created, you need to upload your public key to the console. For more information, see[oci setup config](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm#configfile)

[Python](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Python usage, see[this example on Github](https://github.com/oracle/oci-python-sdk/blob/master/examples/configuration_example.py).

[Java](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For a simple example of Java usage, see[this example on Github](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/SimpleAuthenticationDetailsProviderExample.java).

For an example of using a configuration file with the Java SDK, see[this example on Github](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/CopyObjectExample.java).

[.NET](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of .NET usage, see[this example on Github](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/AuditExample.cs).

[PowerShell](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

The`Set-OCIClientConfig`cmdlet in the Common module provides a guided walk-through for setting up a configuration file. See the[PowerShell Docs Configuration File](https://docs.oracle.com/iaas/Content/API/SDKDocs/powershellgettingstarted.htm#powershellsdkgettingstarted_topic_setup_configuraion_file)section for more information.

[Ruby](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Ruby usage, see[this example on Github](https://github.com/oracle/oci-ruby-sdk/blob/master/examples-oci/object_storage_getnamespace_example.rb).

[TypeScript](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of TypeScript usage, see[this example on Github](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/typescript/authentication.ts).

[Go](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Go usage, be sure to read the[README file](https://github.com/oracle/oci-go-sdk/blob/master/README.md#configuring), and then see[this example on Github](https://github.com/oracle/oci-go-sdk/blob/master/example/example_audit_test.go).

## Session Token-Based Authentication

Using session-token-based authentication, you create a local configuration file that contains information including the user OCID, tenancy OCID, region, private key path and a temporary session token file path. This method uses this information along with the temporary session token, which expires in an hour (by default). Session token-based authentication can be used when you need quick, temporary authentication.

### Examples

The following section shows examples of session token-based authentication.

[CLI](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

You can use the following CLI command to set up session token-based authentication:

" oci session authenticate ":This command sets a temporary session token. Sign in via a browser, and a session configuration file is automatically created that you can use to authenticate until the session expires (by default, expiration is in 60 minutes). After the session expires, you need to refresh the session token. For more information, see[oci session authenticate](https://docs.oracle.com/iaas/Content/API/SDKDocs/clitoken.htm).

[Python](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Python usage, see[Running Scripts on a Computer without a Browser](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../SDKDocs/clitoken.htm#Running_Scripts_on_a_Computer_without_a_Browser).

[Java](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Java usage, see[this example on Github](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/SessionTokenExample.java).

[.NET](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of .NET usage, see[this example on Github](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/SessionTokenAuthenticationDetailsProviderExample.cs).

[PowerShell](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

Not supported.

[Ruby](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

Not supported.

[TypeScript](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of TypeScript usage, see[this example on Github](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/typescript/session-auth.ts).

[Go](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Go usage, see[this example on Github](https://github.com/oracle/oci-go-sdk/blob/master/example/example_securityTokenBasedAuth_test.go).

## Instance Principal Authentication

Using instance principal authentication, you can authorize an instance to make API calls on Oracle Cloud Infrastructure services. After you set up the required resources and policies, an application running on an instance can call Oracle Cloud Infrastructure public services, removing the need to configure user credentials or a configuration file. For more details, see[instance principal](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).

Instance principal authentication can be used from an instance or VM where you don't want to store a configuration file.

### Examples

The following section shows examples of instance principal authentication.

[CLI](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

You can use the following CLI command to set up instance principal-based authentication:

" oci setup instance-principal " : This command helps you to set up instance principal authentication on an existing instance from a machine where you already have OCI CLI authentication configured. For example, you can run this command from Cloud Shell (which is authenticated using a delegation token) to set up instance principal on an instance. For more information, see[oci setup instance-principal](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/setup/instance-principal.html).

To setup instance principal dynamic groups and policies manually, see[Calling Services from Instances](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).

[Python](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Python usage, see[this example on Github](https://github.com/oracle/oci-python-sdk/blob/master/examples/instance_principals_examples.py).

[Java](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Java usage, see[this example on Github](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/InstancePrincipalsAuthenticationDetailsProviderExample.java).

[.NET](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of .NET usage, see[this example on Github](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/InstancePrincipalExample.cs).

[PowerShell](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

See[PowerShell Modules for OCI documentation](https://docs.oracle.com/iaas/Content/API/SDKDocs/powershellconcepts.htm#powershellconcepts_topic_instance_principals)for more information.

[Ruby](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Ruby usage, see[this example on Github](https://github.com/oracle/oci-ruby-sdk/blob/master/examples-oci/instance_principals_example.rb).

[TypeScript](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of TypeScript usage, see[this example on Github](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/typescript/instance-principal.ts).

[Go](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of how you can create and configure instance principal authentication using the Go SDK, see[this example on Github](https://github.com/oracle/oci-go-sdk/blob/master/example/example_instance_configs_test.go).

For an example that uses instance principal authentication, see[this example on Github.](https://github.com/oracle/oci-go-sdk/blob/master/example/example_instance_principals_test.go)

## Resource Principal Authentication

Resource principal authentication is very similar to instance principal authentication, but is intended to be used for resources that are not instances, such as server-less functions.

### Examples

The following section shows examples of resource principal authentication.

[CLI](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For CLI examples, visit[Accessing OCI Resources with Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm).

[Python](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Python usage, see[this example on Github](https://github.com/oracle/oci-python-sdk/blob/master/examples/resource_principals_example.py).

[Java](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Java usage, see[this example on Github](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/FunctionsEphemeralResourcePrincipalAuthenticationDetailsProviderExample.java).

[.NET](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of .NET usage, see[this example on GitHub](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/FunctionsEmphemeralResourcePrincipalsExample.cs).

[PowerShell](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

Example not available.

[Ruby](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Ruby usage using RPv1.1, see[this example on Github](https://github.com/oracle/oci-ruby-sdk/blob/master/examples-oci/resource_principals_1_1_example.rb).

For an example of Ruby usage using RPv2.2, see[this example on Github](https://github.com/oracle/oci-ruby-sdk/blob/master/examples-oci/resource-principal-v2.2/func.rb).

[TypeScript](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of TypeScript usage, see[this example on Github](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/typescript/resource-principal.ts).

[Go](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#)

For an example of Go usage, see[this example on Github](https://github.com/oracle/oci-go-sdk/tree/master/example/example_resource_principal_function)
