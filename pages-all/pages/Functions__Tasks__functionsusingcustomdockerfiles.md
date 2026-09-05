# Using Custom Dockerfiles
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingcustomdockerfiles.htm
- Fetched: 2026-09-05 02:09 CDT

# Using Custom Dockerfiles

Find out how to use your own custom Dockerfile with OCI Functions.

When you build or deploy a function with OCI Functions, a Docker image is created and pushed to a Docker registry. As with any Docker image, the instructions to build the image are contained in a Dockerfile.

If the function is written in one of the languages supported by an Fn Project FDK (Functions Development Kit), OCI Functions uses the`runtime:`,`build_image:`and`run_image:`settings in a func.yaml file to determine the language (and therefore the build-time and run-time dependencies) to include in the Docker image. If you use the`fn init`command to initialize the function, a func.yaml file is created for you. For example, a func.yaml might look like:
```

```

When you build or deploy the function, OCI Functions uses the settings in the func.yaml file to create a temporary Dockerfile containing the instructions from which to build the Docker image. For example, a temporary Dockerfile is shown below.
```

```

Having created the Docker image, OCI Functions deletes the temporary Dockerfile.

If you want more control over the Docker image that is created, you can modify the Dockerfile that OCI Functions creates. Alternatively, you can create your own Dockerfile entirely from scratch. In both cases, the Dockerfile is referred to as a 'custom Dockerfile'. This workflow is sometimes referred to as Bring-Your-Own-Dockerfile, or BYOD.

When you build or deploy the function, OCI Functions uses the instructions in the custom Dockerfile to build the Docker image.

To have OCI Functions use a custom Dockerfile when building a Docker image:
- 

Make a copy of the Dockerfile you want to use as a custom Dockerfile.
- 

Save the new file to the directory containing the func.yaml file.
- 

Give the new file the name`Dockerfile`.

Note that you must name the file`Dockerfile`.
- 

Open the file named`Dockerfile`in an editor of your choice.

For example, the`Dockerfile`file might contain the following lines to install the Oracle Instant Client from an oraclelinux:7-slim base image:
```

```

- 

Include the following lines in the file named`Dockerfile`(as described in[Permissions Granted to Containers Running Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsrunningasunprivileged.htm)):

```

```

For example:
```

```

- 

Save the file named`Dockerfile`. You can now use the`Dockerfile`file as a custom Dockerfile.
- 

In the func.yaml file, change the value of the`runtime:`parameter to`runtime: docker`.

For example, if the func.yaml file contains`runtime: java`, change it to`runtime: docker`.
- 

Use the`fn build`or`fn deploy`commands to build or deploy the function.

OCI Functions uses the instructions in the custom Dockerfile (the file named`Dockerfile`) to build the Docker image for the function, and push it to the Docker registry. Using the`fn build`or`fn deploy`command ensures the image includes the necessary dependencies to make it compatible with the application's shape (see[Specifying the Compute Architecture on Which to Run Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm)
