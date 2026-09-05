# Issues setting up and running OCI Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-setting-up-and-running-Oracle-Functions.htm
- Fetched: 2026-09-05 02:09 CDT

# Issues setting up and running OCI Functions

Find out how to troubleshoot problems when setting up and running OCI Functions.

You might encounter these issues when setting up and running OCI Functions.

## Running Fn Project CLI commands returns a 401 error

If you see a message similar to the following when running an Fn Project CLI command, double-check that the credentials specified for your current profile in the ~/.oci/config file are authenticating you correctly:
```

```

For example:
- Does`user`specify the OCID of your Oracle Cloud Infrastructure user account?
- Does`fingerprint`specify the fingerprint of the public API key value uploaded to the Console?
- Does`key_file`specify the full path to the private key file?

See[Creating a Profile in the Oracle Cloud Infrastructure CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfigureocicli.htm). Also see[API Errors](https://docs.oracle.com//iaas/Content/API/References/apierrors.htm).

## Running Fn Project CLI commands returns a 404 error

If you see a message similar to the following when running an Fn Project CLI command, double-check that you are authorized to access function-related and network resources:
```

```

For example:
- Does`oracle.compartment-id`in your current context correctly specify the OCID of the compartment that owns deployed functions?
- Have policies been set up correctly to give group access to function-related and network resources?
- If you are using a local machine as your OCI Functions development environment, has your user account been included correctly in the group to which access to function-related and network resources has been granted?
- If you are using an Oracle Cloud Infrastructure compute instance as your OCI Functions development environment, has the compute instance's OCID been included correctly in the dynamic group that has been granted access to Oracle Cloud Infrastructure Registry?
- Has a policy been set up to give OCI Functions access to network resources?

See[Different Options for Function Development Environments](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfiguringclient_topic-Different_Options_for_Function_Development_Environments.htm),[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm), and[Creating Policies to Control Access to Network and Function-Related Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm). Also see[API Errors](https://docs.oracle.com//iaas/Content/API/References/apierrors.htm).

## Running Fn Project CLI commands returns an X509: decryption password incorrect error

If you see a message similar to the following when running an Fn Project CLI command, double-check that the pass_phrase specified for your current profile in the ~/.oci/config file is correct:
```

```

See[Creating a Profile in the Oracle Cloud Infrastructure CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfigureocicli.htm).

## Performing Docker-related operations with the Fn Project CLI displays an "Error response from daemon... unknown: Unauthorized" message

To enable the Fn Project CLI to access the Docker registry specified in the Fn Project CLI context, the local Docker client (the Docker daemon on Linux) in your development environment must be logged in to that Docker registry. If the Docker client is not logged in to the Docker registry, you see a message similar to the following:
```

```

Follow the instructions in[Logging in to Oracle Cloud Infrastructure Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionslogintoocir.htm)to log the Docker client in to the appropriate Oracle Cloud Infrastructure Registry, an Oracle-managed Docker registry available in a number of different regions.

## Running an Fn Project CLI command displays an "Fn: asn1:structure error: tags don't match" message

When running an Fn Project CLI command, you might see a message similar to the following:
```

```

This message indicates a problem with the format of the private key. Double-check the private key is PEM-encoded by opening the private key file in the ~/.oci directory and confirming that the private key starts with`BEGIN RSA PRIVATE KEY`. For more information about generating keys, see[Setting up an Oracle Cloud Infrastructure API Signing Key for Use with OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionssetupapikey.htm).

## Running fn version shows that a more recent version of the Fn Project CLI is available

If you see a message similar to the following when you enter the`fn version`command, a more recent version of the Fn Project CLI is available:
```

```

To upgrade the Fn Project CLI to the most recent version, reinstall the Fn Project CLI by following the instructions in[Installing the Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstallfncli.htm)
