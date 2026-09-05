# Creating Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfunctions-about.htm
- Fetched: 2026-09-05 02:08 CDT

# Creating Functions

Find out about creating functions.

You can create a new function definition in the OCI Functions server in different ways:
- Using the Console, a CLI command, or an API operation to create a new function based on an existing Docker image that has already been pushed to the Docker registry (as described in this topic).
- Using the single Fn Project CLI command`fn deploy`to build a new Docker image, push the image to the Docker registry, and create a new function based on the image in one step (as described in[Creating and Deploying Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsuploading.htm)).
- Using Code Editor (see[Creating Functions Using Code Editor](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionscreatingfunctions-usingcodeeditor.htm)).
- Using pre-built functions (see[Creating Functions Using Pre-Built Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functions_pbf_creating_prebuilt.htm)).

When creating a new function based on an existing Docker image, you specify function metadata to store in the OCI Functions server. For example, the maximum length of time the function is allowed to execute for.

The existing image on which you base a new function must be suitable for use with OCI Functions. Typically, to build and push a suitable image, you or somebody else will use Fn Project CLI commands and/or Docker CLI commands. For example, having written your function code and a func.yaml file containing function metadata (perhaps based on the template helloworld function and func.yaml created using`fn init`), you can:
- Use`fn build`to build a new Docker image from the function.
- Use`docker push`to push the image to the Docker registry.

With the image in the Docker registry, you can then use the Console, a CLI command, or an API operation to create a function based on the image, as described in this topic.

See[Creating a Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfunction-task.htm)
