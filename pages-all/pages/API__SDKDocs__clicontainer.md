# Working with the OCI CLI Container Image
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clicontainer.htm
- Fetched: 2026-09-05 01:36 CDT

# Working with the OCI CLI Container Image

This section covers how to install and use the OCI CLI Container Image.

The Oracle Cloud Infrastructure (OCI) Command Line Interface (CLI) Container Image is a Docker image that has the OCI CLI tools pre-installed. This section covers how to install and use the OCI CLI Container Image.

## Requirements

To use the OCI CLI container image, you must have:
- A standards-compliant container runtime engine, such as[Docker](https://www.docker.com/), or[Podman](https://podman.io/)
- An Oracle Cloud Infrastructure tenancy
- A user account in that tenancy that belongs to a group to which appropriate policies have been assigned to grant the required permissions.
- A keypair used for signing API requests, with the public key uploaded to Oracle. Only the user calling the API should possess the private key. For more information, see[Configuring the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#Required_Keys_and_OCIDs).

For examples of how to set up a new user, group, compartment, and policy, see the[Adding Users](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm#Adding_Users). For a list of other typical OCI policies, review the[list of common policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#top).

## Using the OCI CLI container image

To use the container image, pull the latest version from the GitHub Container Registry:
```

```

Consider tagging the image as`oci`to make it a more seamless drop-in replacement:
```

```

For added convenience, you can create an shell alias that runs the container for you:
```

```

## API Signing Key Authentication

This is the default authentication method used by all OCI SDKs and the OCI CLI. To use this method, mount a location on the host system to the`/oracle/.oci`directory inside the container.

If you have previously configured the OCI CLI on the host machine, the easiest way to provide access to your API signing key is to map your`$HOME/.oci`directory to`/oracle/.oci/`inside the container.
For example:
```

```

You can also pass the`OCI_CLI_CONFIG_FILE`environment variable to use a different location for the OCI CLI`config`file.
Note  
  
Ensure that the`key_file`field in`$HOME/.oci/config`uses the`~`character so that the path resolves both inside and outside the container; for example:`key_file=~/.oci/oci_api_key.pem`.
If you have not configured the OCI CLI, create the`$HOME/.oci`directory:
```

```

Next, start the OCI CLI interactive setup process:
```

```

For more information, see[Setting Up the Configuration File](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm#configfile).

## Session token authentication

To use token-based authentication, map port 8181 to the container:
```

```

For more information, see[Token-based Authentication for the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/clitoken.htm).

## Instance principal authentication

To enable instance principal authentication, you can use the`--auth instance_principal`command-line parameter:
```

```

You can also pass the`OCI_CLI_AUTH`environment variable:
```

```

If you created a shell alias, add it to the alias definition.

For more information, see[OCI SDK Authentication Methods](https://docs.oracle.com/iaas/Content/API/Concepts/sdk_authentication_methods.htm).

## Local file access

The simplest way to allow the OCI CLI running inside the container to access files on the host is to bind mount a directory from the host into the container.
In the following example, the`$HOME/scratch`directory is bind mounted as`/oracle/scratch`in the container so that the files inside that directory can be bulk uploaded to OCI Object Storage using the OCI CLI:
```

```

## Building from Source

The source code required to build the OCI CLI container image can be found at[https://github.com/oracle/docker-images/tree/main/OracleCloudInfrastructure/oci-cli](https://github.com/oracle/docker-images/tree/main/OracleCloudInfrastructure/oci-cli)
