# Specifying the Compute Architecture on Which to Run Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm
- Fetched: 2026-09-05 02:09 CDT

# Specifying the Compute Architecture on Which to Run Functions

Find out about specifying the processor architecture on which to run a function with OCI Functions.

When deploying a function to OCI Functions, you can specify the processor architecture of the compute instances on which you want to run the function. You can limit the function to running on a single architecture (such as Arm), or you can enable the function to run on multiple architectures (such as both Arm and x86).

There are three steps to specifying the processor architecture on which to run a function:
- Create an application and select a shape for the application that supports the architecture on which you want to run the function. See[Selecting a Single Architecture or Multi-Architecture Application Shape on which to run a Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm#functionsspecifyingapplicationfunctionarchitectures).
- Build an image that contains the necessary dependencies (child images) for the architecture on which you want to run the function. See[Building Multi-Architecture (Multi-Arch) Images](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm#functionsbuildingmultiarchimages)and[Building Single Architecture Images](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm#functionsbuildingsinglearchimages).
- Create the function based on the image you've built, in the application with the appropriate shape. See[Creating Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfunctions-about.htm).

Depending on how you choose to create functions using OCI Functions, you can complete and combine these steps in several different ways. For example:
- You can use the Console to create an application with the appropriate shape first, and then use the Fn Project CLI`fn deploy`command to create and deploy the function (which automatically builds a suitable image containing the necessary dependencies).
- You can use a Docker command to build an image containing the necessary dependencies first, use the OCI CLI to create an application with the appropriate shape, and then use the Console to create a function in the application based on the image.

## Selecting a Single Architecture or Multi-Architecture Application Shape on which to run a Function

Find out how selecting an application's shape influences the processor architecture of the compute instances on which functions run with OCI Functions.

When you define an application in OCI Functions, you select the processor architecture of the compute instances on which to deploy and run functions in the application. All the functions in the application are deployed and run on compute instances with the same architecture.

You specify the compute instance architecture on which you want to run functions in an application by selecting a shape for the application as follows:
- If you always want functions in the application to run on compute instances with an Arm-based architecture, select the Generic_ARM shape. If you select this single architecture shape for the application, every function's image must contain the necessary dependencies for the Arm architecture (in either a single architecture image, or a multi-architecture image).
- If you always want functions in the application to run on compute instances with an x86-based architecture, select the Generic_X86 shape. If you select this single architecture shape for the application, every function's image must contain the necessary dependencies for the x86 architecture (in either a single architecture image, or a multi-architecture image).
- If you want functions to run on compute instances with whichever architecture has sufficient capacity, select the Generic_X86_ARM shape. In this case, OCI Functions selects the architecture on which to run functions based on available capacity. If you select this multi-architecture shape for the application, every function's image must contain the necessary dependencies for both the Arm architecture and the x86 architecture (in a multi-architecture image).

When you create a function in an application, the image on which the function is based must include the necessary dependencies for the application's shape:
- If you select a single architecture shape for the application, the function's image must contain the necessary dependencies for the corresponding architecture (in either a single architecture image, or a multi-architecture image).
- If you select a multi-architecture shape for the application, the function's image must contain the necessary dependencies for both architectures (in a multi-architecture image).

To use the same image to deploy and run a function on multiple different architectures, you use a multi-architecture image (also known as a manifest list, or as a 'multi-arch image'). You build multi-architecture images from a single source tree, with one image tag that includes images for both x86 and Arm architectures.

If you use the Fn Project CLI command`fn -v deploy --app <app-name>`to build a function and its dependencies as a Docker image, the image is built with the necessary dependencies for the application's shape. If the application has a multi-architecture shape, the function's image is built as a multi-architecture image. You can also build multi-architecture images using[Docker Buildx](https://github.com/docker/buildx)and[Podman](https://github.com/containers/podman). If you use a tool other than the Fn Project CLI to build a multi-architecture image, it is your responsibility to verify the image is compatible with the application's shape.

When you select a multi-architecture shape for an application, OCI Functions assesses available capacity and determines the architecture in which to deploy and run functions accordingly. Since a function might be deployed in different architectures, the function must be based on a multi-architecture image. It is your responsibility to verify that a function based on a multi-architecture image can be successfully invoked in both x86 and Arm architectures. To enable you to do so, we recommend that as well as creating such a function in an application with a multi-architecture shape, you also create functions based on a multi-architecture image in applications with single architecture shapes. To aid with debugging, Oracle also recommends that a function's logs include details of the architecture of the compute instance on which the function is running.

Having created an application, note that you cannot subsequently change the application's shape. If you want a particular function to run on a different architecture, create the function in a different application (create a new application if necessary) and provide the appropriate single architecture or multi-architecture image. For example:
- If you select a single architecture shape (Arm or x86) for an application but you want a particular function to run on a different architecture, create the function in a different application that has the appropriate architecture shape.
- If you select a multi-architecture shape for an application, but you want a particular function to always run on a specific architecture, create the function in a different application that has the appropriate single architecture shape.
- If you select a single architecture shape (Arm or x86) for the application but you want a particular function to run on any compute instance regardless of architecture, create the function in a different application that has a multi-architecture shape.

## Building Multi-Architecture (Multi-Arch) Images

Find out how to build multi-architecture images for functions in applications that have multi-architecture shapes.

You can build multi-architecture images in different ways, including:
- using the Fn Project CLI (for more information, seee[Using the Fn Project CLI to build a multi-architecture image (recommended)](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm#functionsbuildingmultiarchimages-fnprojectcli))
- using[Docker Buildx](https://github.com/docker/buildx)(for more information, see[Using the Docker buildx plugin to build a multi-architecture image](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm#functionsbuildingmultiarchimages-dockerbuildx))
- using[Podman](https://github.com/containers/podman)

You can create functions based on a multi-architecture image both in applications that have a multi-architecture shape and in applications that have a single architecture shape, provided the multi-architecture image includes the necessary dependencies (child images) for the application's shape.
Note  
  

Note that in the Cloud Shell development environment, OCI Functions does not support the creation and deployment of functions based on multi-architecture images, nor applications with multi-architecture shapes. In addition, the Cloud Shell session's architecture must be the same as the application's architecture (for more information about selecting the Cloud Shell session's architecture, see[Cloud Shell Architecture](https://docs.oracle.com/iaas/Content/API/Concepts/cloudshellintro.htm#Cloud_Shell_Architecture)).

### Using the Fn Project CLI to build a multi-architecture image (recommended)

You can use the Fn Project CLI to build a multi-architecture image when deploying a function in an application with a multi-architecture shape:
- Log in to your development environment as a functions developer.
- If a suitable application with a multi-architecture shape in which to create the function does not exist already, create such an application now. See[Creating Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingapps.htm).
- If you haven't already initialized the function, follow the instructions in[Using Fn Project CLI Commands](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsuploading.htm#usingfncli)to initialize the function now.
- In the function's directory, enter the following Fn Project command to build the function and its dependencies as a Docker multi-architecture image, push the image to the specified Docker registry, and deploy the function to OCI Functions:

```

```

where`<app-name>`is the name of the application with the multi-architecture shape, in which you want to create the function.

The multi-architecture image is created, and includes the necessary dependencies for the architectures specified by the application's multi-architecture shape.

### Using the Docker buildx plugin to build a multi-architecture image

Prerequisite: Before you can use the Docker buildx plugin, you have to download and install the plugin. For download and installation instructions, see the[Docker buildx documentation on github](https://github.com/docker/buildx).

Having downloaded and installed the Docker buildx plugin, you can use the plugin to build a multi-architecture image on which to base a function to deploy to an application with a single or multi-architecture shape. For more information about using the Docker buildx plugin, see the[Docker buildx documentation on github](https://github.com/docker/buildx).

For example, you might build a multi-architecture image for a Python hello-world image as follows:
- Log in to your development environment as a functions developer.
- In a terminal window, create a directory in which to store functions. For example:
```

```

- Change directory to the newly created directory. For example:
```

```

- Create a helloworld Python function by entering:
```

```

A directory called`helloworld-func`is created, containing:
- `func.yaml`: The function definition file, containing the minimum amount of information required to build and run the function. See the[Fn Project documentation](https://github.com/fnproject/docs/blob/master/fn/develop/func-file.md)to find out about the additional parameters you can include in a func.yaml file.
- `requirements.txt`: A list of required Python libraries.
- `func.py`: The actual function file.
- Create a new file named`Dockerfile`in the same directory.

Note that you must name the file`Dockerfile`.
- Open the file named`Dockerfile`in an editor of your choice and add the following lines:
```

```

- Save the file named`Dockerfile`. You can now use the`Dockerfile`file as a custom Dockerfile.
- In the func.yaml file, change the value of the`runtime:`parameter to`runtime: docker`.

For example, change:
```

```

to:
```

```

- Use the`docker buildx`command to build x86 and Arm-based images and generate a multi-architecture image from them, by entering:
```

```

For example:
```

```

- Push the multi-architecture image to Oracle Cloud Infrastructure Registry. For example, by entering:
```

```

You can now base a function on the multi-architecture image.
- (Optional) Create a new function and set the function's Image property to the name of the multi-architecture image. For example:
- When using the Console, specify`my-manifest-name:1.0.0-SNAPSHOT-X86-ARM`in the Image field.
- When using the Fn Project CLI, specify`my-manifest-name:1.0.0-SNAPSHOT-X86-ARM`as the value of the image argument. For example:
```

```

## Building Single Architecture Images

Find out how to build single architecture images for functions in applications that have single architecture shapes.

You can build single architecture images in different ways, including:
- Using the Fn Project CLI. See[Using the Fn Project CLI to build a single architecture image](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm#functionsbuildingsinglearchimages-fnprojectcli).
- Using the Docker build command. See[Using the Docker build command to build a single architecture image](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm#functionsbuildingsinglearchimages-dockerbuild).

When you create a function based on a single architecture image, you must create the function in an application that has a compatible single architecture shape.

### Using the Fn Project CLI to build a single architecture image

You can use the Fn Project CLI to build a single architecture image when deploying a function in an application with a single architecture shape:
- Log in to your development environment as a functions developer.
- If a suitable application with a single architecture shape in which to create the function does not exist already, create such an application now. See[Creating Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingapps.htm).
- If you haven't already initialized the function, follow the instructions in[Using Fn Project CLI Commands](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsuploading.htm#usingfncli)to initialize the function now.
- In the function's directory, enter the following Fn Project command to build the function and its dependencies as a single architecture image, push the image to the specified Docker registry, and deploy the function to OCI Functions:

```

```

where`<app-name>`is the name of the application with the single architecture shape, in which you want to create the function.

The single architecture image is created, and includes the necessary dependencies for the architecture specified by the application's single architecture shape.

### Using the Docker build command to build a single architecture image

You can use the Docker build command to build a single architecture image on which to base a function that you want to deploy to an application with a single architecture shape. For more information, see the[docker build command in the Docker documentation](https://docs.docker.com/engine/reference/commandline/build/).

Note that when you use the Docker build command to build an image, the image includes the necessary dependencies for the architecture of the current platform on which you run the command. So if you run the Docker build command on an AMD platform (an x86 architecture), the image includes the necessary dependencies for the x86 architecture. If you want to build a single architecture image for an architecture different to the current platform, use the Docker buildx plugin and specify the single target architecture as the value of the`--platform`argument. See[Using the Docker buildx plugin to build a multi-architecture image](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsspecifyingcomputearchitectures.htm#functionsbuildingmultiarchimages-dockerbuildx)
