# Issues deploying applications and functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-deploying-applications-and-functions.htm
- Fetched: 2026-09-05 02:09 CDT

# Issues deploying applications and functions

Find out how to troubleshoot problems when deploying applications and functions with OCI Functions.

You might encounter these issues when deploying applications and functions with OCI Functions.

## Deploying an application returns an "unauthorized: incorrect username or password" message

When deploying an application, you might see a message similar to the following:
```

```

The message indicates an unnecessary and unsuccessful attempt to log in to Docker Hub. To resolve this situation, log out from Docker using the following command:

```

```

Having logged out from Docker, re-run the command to deploy the application.

## Deploying a function returns an "error running docker push, are you logged into docker?" message

If you see a message similar to the following when deploying a function, double-check that your development environment doesn't have the FN_REGISTRY environment variable set to your Docker username:
```

```

If you have used the open source Fn Project platform, you might have followed instructions in the[Fn Project documentation](https://github.com/fnproject/docs/blob/master/fn/operate/private_registries.md)to set the FN_REGISTRY environment variable to your Docker username to enable interaction with the official Docker registry (docker.io).

The FN_REGISTRY environment variable overrides the value of the registry option in your Fn Project CLI context.

To use the Fn Project CLI with OCI Functions, do one of the following:
- Unset the FN_REGISTRY environment variable.
- Override the FN_REGISTRY environment variable using the`--registry`global option whenever you enter an Fn Project CLI command that interacts with Oracle Cloud Infrastructure Registry.

## Deploying a function returns a ListTriggers message and a 500 error

When deploying a function that you've previously created using an earlier version of the Fn Project CLI, you might see a message similar to the following:
```

```

This message indicates that the function's func.yaml file contains one or more HTTP trigger definitions. OCI Functions does not currently support HTTP triggers. To deploy the function, remove the`triggers:`section from the func.yaml file.

To avoid creating new func.yaml files containing trigger definitions, follow the instructions in[Installing the Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstallfncli.htm)to upgrade the Fn Project CLI to the most recent version.

## Deploying a function returns an "Image does not exist or you do not have access to use it" message

When deploying a function using an Oracle Cloud Infrastructure compute instance as your OCI Functions development environment, you might see a message similar to the following:
```

```

This message indicates that the compute instance does not have access to Oracle Cloud Infrastructure Registry.

Double-check that a policy statement (similar to the one below) exists in the tenancy's root compartment to allow a dynamic group that includes the compute instance's OCID to access Oracle Cloud Infrastructure Registry:

```

```

For more information about using an Oracle Cloud Infrastructure compute instance as your development environment, see[Different Options for Function Development Environments](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfiguringclient_topic-Different_Options_for_Function_Development_Environments.htm).

## Deploying a function to OCI Functions returns "Fn: Missing subnets annotation" message

When you deploy a function to OCI Functions, you might see the following message:
```

```

If you see the`Fn: Missing subnets annotation`message, confirm that you entered the correct application name. For example:
- the application might not be in the compartment currently specified by the Fn Project CLI context
- the application might have existed previously, but has subsequently been deleted

## Deploying a function returns a "Getting image source signatures Error: trying to reuse blob ... at destination: checking whether a blob ... exists in .... :StatusCode: 403, Fn: error running docker push: exit status 125" message

When you deploy a function to OCI Functions, you might see the following message:
```

```

This message indicates that although your tenancy is federated with Oracle Identity Cloud Service, the username that you provided when you logged in to Oracle Cloud Infrastructure Registry did not include an identity domain name.

You probably provided a username in the format`<tenancy-namespace>/<user-name>`, in a command such as:
```

```

For example:
```

```

However, because your tenancy is federated with Oracle Identity Cloud Service, you have to use a slightly different command format that includes the name of the identity domain, in the format`<tenancy-namespace>/<domain-name>/<user-name>`.

For example:
```

```

To successfully deploy the function, re-enter the`docker login`command and specify the username in the correct format including the identity domain name.

For more information, see[Logging in to Oracle Cloud Infrastructure Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionslogintoocir.htm).

## Deploying a function to OCI Functions returns "Function's image architecture 'x86' is incompatible..." message

When you deploy a function to OCI Functions, you might see a message similar to the following:
```

```

This message indicates that the function's image does not include the necessary dependencies (child images) for the application's shape. A likely cause of the message is the use of Fn Project CLI version 0.6.24 (or earlier) to deploy a function with an x86 image to:
- an application that has a multi-architecture shape (such as Generic_X86_ARM)
- an application that has a single architecture shape that is not compatible with an x86 image (such as Generic_ARM)

From Fn Project CLI version 0.6.25 onwards, when you use the command`fn deploy --app <app-name>`to build a function and deploy it to OCI Functions, the Fn Project CLI builds the function's Docker image with the necessary dependencies for the application's shape. If the application has a multi-architecture shape (such as Generic_X86_ARM, the default application shape since September, 2023), the Fn Project CLI builds a multi-architecture image for the function. The function's image and the application's shape are always compatible.

However, Fn Project CLI version 0.6.24 (and earlier) always builds Docker images with the necessary dependencies for a single architecture, the x86 architecture. As a single architecture image, such an x86 image is only compatible with applications that have the Generic_X86 single architecture shape. The x86 image is incompatible with applications that have:
- a multi-architecture shape (such as Generic_X86_ARM, the default application shape since September, 2023)
- a single architecture shape that is not Generic_X86 (such as Generic_ARM)

To deploy the function successfully, you have to provide an image that is compatible with the application's shape. Do one of the following:
- Use Fn Project CLI version 0.6.25 or later (recommended).
- Deploy the function to a different application that has a shape that is compatible with the function's image (create a new application if necessary). Assuming you are using Fn Project CLI version 0.6.24 or earlier, always deploy the function to an application that has a Generic_X86 shape.
- Use Docker to build an image that is compatible with the application's architecture shape.

For more information, see[Specifying the Compute Architecture on Which to Run Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm).

## Deploying a function to OCI Functions in Cloud Shell returns "OL8 Cloud Shell does not support cross-compilation and multi-arch functions builds..." message

When you deploy a function to OCI Functions in the Cloud Shell development environment, you might see a message similar to the following:
```

```

This message indicates that the function is based on a multi-architecture image, or that the application has a multi-architecture shape, or that the Cloud Shell session and the application have a different architecture.

In the Cloud Shell development environment, OCI Functions does not support the creation and deployment of functions based on multi-architecture images, nor applications with multi-architecture shapes. In addition, the Cloud Shell session's architecture must be the same as the application's architecture.

For more information:
- About creating a function based on a single architecture image, in an application that has a compatible single architecture shape, see[Specifying the Compute Architecture on Which to Run Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm).
- About selecting the Cloud Shell session's architecture, see[Cloud Shell Architecture](https://docs.oracle.com/iaas/Content/API/Concepts/cloudshellintro.htm#Cloud_Shell_Architecture).

## Deploying a function returns an "Invalid or unsupported image manifest. Unable to get architecture from the OCIR Manifest/Headers…" message

When you deploy a function to OCI Functions, you might see a message similar to the following:
```

```

There are a number of possible causes and solutions, as described in this section.

### Possible cause: Incorrect Docker version

The Docker version you are using might be unsupported.

If you are using Docker to build function images, you must use a supported version of Docker (at the time of writing, version 17.10 or later).

To confirm the version of Docker that you are using, enter:
```

```

If the version of Docker is not supported, install a more recent version. For more information, see[Installing Docker for Use with OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstalldocker.htm).

### Possible cause: Manifest is incorrectly formatted, or is missing required information

The image manifest might be incorrectly formatted, or might not contain all of the required information. The error message provides additional details.

Specifically, the image manifest:
- Must be in valid JSON format.
- Must include an image digest.
- Must specify a valid image architecture (either`amd64`or`arm64`, or both).

To inspect the image manifest, enter:
```

```

For example:
```

```

Verify that the image manifest:
- Is in valid JSON format.
- Includes a`digest`field.
- Includes a`platform`field that specifies a valid image architecture. In the case of a single architecture image, the`platform`field must specify either`amd64`or`arm64`. In the case of a multi-architecture image, the`platform`field must specify both`amd64`and`arm64`. For more information, see[Specifying the Compute Architecture on Which to Run Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm).

If the image manifest is incorrectly formatted, or is missing required information, update the manifest and rebuild the image.

### Possible cause: Image is invalid

The image built from the image manifest might be invalid (for example, because the image manifest is missing required information).

In this situation, you have to rebuild the image. How to rebuild the image depends on whether you are rebuilding a single architecture image or a multi-architecture image, and on the tool you want to use.

Rebuilding a single architecture image:

You can rebuild single architecture images in different ways, including:
- Using the Fn Project CLI (Recommended):

In the function's directory, enter the following Fn Project CLI command to build the function and its dependencies as a single architecture image, push the image to the specified Docker registry, and deploy the function to OCI Functions:
```

```

where`<app-name>`is the name of the application with the single architecture shape, in which you want to create the function.

For more information, see[Using the Fn Project CLI to build a single architecture image](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm#functionsbuildingsinglearchimages-fnprojectcli).
- Using the Docker build command or the Docker buildx plugin:

To build an image for the same architecture as your current platform, use the`docker build`command. For example, to build an image to deploy on an application with`amd64`as the single architecture shape, enter:
```

```

To build an image for a different architecture than your current platform, use the`docker buildx build`command. For example, to build an image to deploy on an application with`amd64`as the single architecture shape, enter:
```

```

Be sure to specify either`amd64`or`arm64`, and not to specify both. Also be sure not to specify any other architecture.

Having built the image, enter the following command to push the image to the Docker registry:
```

```

For more information, see[Using the Docker build command to build a single architecture image](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm#functionsbuildingsinglearchimages-dockerbuild).

Rebuilding a multi-architecture image:

You can rebuild multi-architecture images in different ways, including:
- Using the Fn Project CLI (Recommended):

In the function's directory, enter the following Fn Project CLI command to build the function and its dependencies as a multi-architecture image, push the image to the specified Docker registry, and deploy the function to OCI Functions:
```

```

where`<app-name>`is the name of the application with the multi-architecture shape, in which you want to create the function.

For more information, see[Using the Fn Project CLI to build a multi-architecture image (recommended)](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm#functionsbuildingmultiarchimages-fnprojectcli)..
- Using the Docker buildx plugin:

To build a multi-architecture image on which to base a function to deploy to an application with a multi-architecture shape, enter the following`docker buildx build`command:
```

```

Be sure to specify both`amd64`and`arm64`, and not to specify any other architecture.

Having built the image, enter the following command to push the image to the Docker registry:
```

```

For more information, see[Using the Docker buildx plugin to build a multi-architecture image](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm#functionsbuildingmultiarchimages-dockerbuildx)..

## Building or deploying a function returns "toomanyrequests: You have reached your unauthenticated pull rate limit" error message

When building or deploying a function with OCI Functions, you might see an error message similar to the following:
```

```

This message indicates that Docker Hub has throttled image pulls and prevented the download of an image referenced by the function. The error typically occurs because your environment is not authenticated with Docker Hub (that is, not logged in), or because you have exceeded Docker Hub's pull rate limits for unauthenticated users (which are enforced per IP address or per account).

To pull the image successfully, do one or both of the following:
- Log in to Docker Hub, if not logged in already.
-
