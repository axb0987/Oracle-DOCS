# How OCI Functions Works
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionshowitworks.htm
- Fetched: 2026-09-05 02:07 CDT

# How OCI Functions Works

Find out how OCI Functions works when you deploy a function, and when you invoke a function.

## What Happens When You Deploy a Function to OCI Functions?

When you have written the code for a function and it's ready to deploy, you can use a single Fn Project CLI command to perform all the deploy operations in sequence:
- building a Docker image from the function
- providing a definition of the function in a func.yaml file that includes:
- the maximum length of time the function is allowed to execute for
- the maximum amount of memory the function is allowed to consume
- pushing the image to the specified Docker registry
- uploading function metadata (including the memory and time restrictions, and a link to the image in the Docker registry) to the Fn Server
- adding the function to the list of functions shown in the Console

The above process of deploying a function to OCI Functions is shown in the diagram.

[

Note that once the image has been uploaded to the Docker registry, it is your responsibility to update the image. For example, when new language versions are supported (for more information, see[Function Development Kits (FDKs)](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionssupportedlanguageversions.htm)).

## What Happens When You Invoke a Function?

You can invoke a function that you've deployed to OCI Functions from:
- The Fn Project CLI.
- The Oracle Cloud Infrastructure SDKs.
- Signed HTTP requests to the function's invoke endpoint. Every function has an invoke endpoint.
- Other Oracle Cloud services (for example, triggered by an event in the Events service) or from external services.

When a function is invoked for the first time, OCI Functions first verifies the request with the IAM service. Assuming the request passes authentication and authorization checks, OCI Functions then passes the request to the Fn Server, which uses the function definition to:
- identify the Docker image of the function to pull from the Docker registry
- execute the function by running the function's image as a container on an instance in a subnet associated with the application to which the function belongs

When the function is executing inside the container, the function can read from and write to other resources and services running in the same subnet (for example, Database as a Service). The function can also read from and write to other shared resources (for example, Object Storage), and other Oracle Cloud Services. You can specify the maximum length of time the function is allowed to execute by setting a timeout in the func.yaml file or in the Console.

OCI Functions stores the function's logs in Oracle Cloud Infrastructure or in an external logging destination.

When the function has finished executing and after a period being idle, the Docker container is removed. If OCI Functions receives another call to the same function before the container is removed, the second request is routed to the same running container. If OCI Functions receives a call to a function that is currently executing inside a running container, OCI Functions scales horizontally to serve both incoming requests and a second Docker container is started.

OCI Functions shows information about function invocations in metric charts.

The above process of invoking a function is shown in the diagram.

[
