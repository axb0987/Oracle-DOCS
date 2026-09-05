# Function Development Kits (FDKs)
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionssupportedlanguageversions.htm
- Fetched: 2026-09-05 02:09 CDT

# Function Development Kits (FDKs)

Find out about the Function Development Kits (FDKs) used by OCI Functions to support different languages.

OCI Functions uses Fn Project Function Development Kits (FDKs) to support popular languages - Java, Node.js, Python, Go, Ruby, and C#. An FDK is a set of helper libraries that handle system internals (such as protocols, parsing input and output, and logic for function containers). Each language FDK consists of three components:
- A build-time base image, containing language-specific libraries and tools to build executable functions.
- A runtime base image, to provide a language-specific runtime environment in which to run executable functions.
- An FDK library (in the case of Java, the FDK library is included in the build-time and runtime base images).

FDKs are specific to particular versions of a given language. Oracle regularly publishes new FDK build-time and runtime base images for supported languages (for example, to issue a patch, or to support a newly released version of the language). In the case of Java, an FDK update always includes all three components (the builld-time and runtime base images, as well as the FDK library). In the case of other languages, an FDK update might include one or more of the components.

When you first create a function using the Fn Project CLI`fn init`command, you specify the language in which the function's source code is written using the`--runtime`command option. As well as specifying a language, you can optionally specify a version of the language. If you don't specify the language version, the Fn Project CLI assumes you want to use the most recent version of the language FDK that's available. The Fn Project CLI records the value of the`--runtime`command option as the value of the`runtime:`parameter in the function's func.yaml. The Fn Project CLI also adds values for the`build_image:`and`run_image:`parameters in the func.yaml file according to the`--runtime`command option you specify, as follows:
- If you specify simply a language as the value of the`--runtime`command option, the Fn Project CLI adds the most recent versions of that language's FDK build-time and runtime base images as values for the`build_image:`and`run_image:`parameters. For example, if you enter`fn init --runtime python helloworld-func`and Python 3.11 is the most recent version available, the Fn Project CLI adds the following:
```

```

- If you specify both a language and a version as the value of the`--runtime`command option, the Fn Project CLI adds the corresponding version of the language's FDK build-time and runtime base images as values for the`build_image:`and`run_image:`parameters. For example, if you enter`fn init --runtime python3.9 helloworld-func`, the Fn Project CLI adds the following:
```

```

When you build a function using using`fn build`or`fn deploy`, the Fn Project CLI creates a Docker image (and in the case of`fn deploy`, pushes the image to a Docker registry). The Docker image contains the function's runtime dependencies. If the function is written in a language for which an FDK is available, the Fn Project CLI:
- Uses the build-time base image specified by the`build_image:`parameter to build an executable version of the function, and includes the executable function in the Docker image.
- Includes the runtime base image specified by the`run_image:`parameter in the Docker image, to provide the runtime environment in which to run the executable function.

The Fn Project CLI uses cached versions of the FDK's build-time and runtime base images, if these are available. If cached versions of the base images are not available, the Fn Project CLI pulls the language FDK's build-time and runtime base images from Docker Hub.

Note that if a new version of a language FDK is released , the values for the`build_image:`and`run_image:`parameters in an existing function's func.yaml file are not automatically updated. The initial versions of the language FDK's build-time and runtime base images that were previously specified as values for the`build_image:`and`run_image:`parameters when the function was created are still used to build the function executable, and to provide the runtime environment. Using the initial values of the`build_image:`and`run_image:`parameters helps to ensure the function code remains compatible with the language FDK's build-time and runtime base images.

If you want to re-build an existing function with a different language version, and include a different runtime in the function's Docker image, change the values of the`build_image:`and`run_image:`parameters in the function's func.yaml file to reference a different version of the language FDK. For consistency and to avoid confusion, update the value of the`runtime:`parameter to correspond to the`--runtime`command option for the version of the language FDK. In the case of Java functions, you also have to change the FDK version in the function's pom.xml file.

## Examples

The examples in this section assume you are using Fn Project CLI version 0.6.7 (or later), and that Python 3.11 is the most recent version of Python supported by the Python FDK.

### Example 1: Create a new function with Python 3.11

If you want to create a new function with Python 3.11, run either of the following commands:

```

```

```

```

In the case of`fn init --runtime python helloworld-func`, the Fn Project CLI records the value of the`--runtime`command option as the value of the`runtime:`parameter in the function's func.yaml, and adds the most recent version numbers of the Python FDK's build-time and runtime base images as values for the`build_image:`and`run_image:`parameters:
```

```

In the case of`fn init --runtime python3.11 helloworld-func`, the Fn Project CLI records the value of the`--runtime`command option as the value of the`runtime:`parameter in the function's func.yaml, and adds the Python 3.11 FDK's build-time and runtime base images as values for the`build_image:`and`run_image:`parameters:
```

```

From now on, when you build the function, the Fn Project CLI continues to use those initial versions of the build-time and runtime base images to build the function executable, and to provide the runtime environment.

### Example 2: Create a new function with Python 3.9

If you want to create a new function with Python 3.9, run the following command:

```

```

The Fn Project CLI records the value of the`--runtime`command option as the value of the`runtime:`parameter in the function's func.yaml, and adds the version of the Python FDK's build-time and runtime base images that are appropriate for Python 3.9 as values for the`build_image:`and`run_image:`parameters, as shown:
```

```

From now on, when you build the function, the Fn Project CLI continues to use those initial Python 3.9 versions of the build-time and runtime base images to build the function executable, and to provide the runtime environment.

### Example 3: Rebuild an existing function with Python 3.8

If you want to rebuild an existing function that was initially built with Python 3.8, and you want to continue to build it with Python 3.8, run the following command:

```

```

The`build_image:`and`run_image:`parameters in the func.yaml file were originally set to versions of the Python FDK's build-time and runtime base images appropriate for Python 3.8. When you build the function, the Fn Project CLI continues to use the same Python 3.8 build-time and runtime base images to build the function executable, and to provide the runtime environment.

### Example 4: Rebuild an existing Python 3.8 function with Python 3.11
If you want to rebuild an existing function that was initially built with Python 3.8, and you now want to build it with Python 3.11:
- Change the values of the`build_image:`and`run_image:`parameters in the function's func.yaml to reference the latest FDK version for Python 3.11 (see[How to find out the latest FDK build-time and runtime base image versions for a particular supported language version](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionssupportedlanguageversions.htm#functionssupportedlanguageversions_topic_How_to_find_out_latest_supported_FDK)):
```

```

- For consistency and to avoid confusion, update the value of the`runtime:`parameter to correspond to the`--runtime`command option for Python 3.11.
```

```

- Run the following command:

```

```

The Fn Project CLI uses the versions of the Python FDK's build-time and runtime base images specified by the`build_image:`and`run_image:`parameters in the func.yaml file to build the function executable, and to provide the runtime environment. From now on, when you build the function, the Fn Project CLI uses those versions of the build-time and runtime base images.

## Behavior in Earlier Versions of the Fn Project CLI (prior to version 0.6.7)

Using versions of the Fn Project CLI prior to version 0.6.7, every time you built or rebuilt a function written in a language supported by an FDK (with the exception of Java, see below), the Fn Project CLI used cached versions of the language FDK's build-time and runtime base images, if these were available. If cached versions of the base images were not available, the Fn Project CLI pulled the most recent versions of the base images from Docker Hub. As a result, you could not be certain that the function code was compatible with the language FDK's build-time base image used to build the function executable, or with the runtime base image used to provide the runtime environment.

You can continue to build existing functions exactly as before, by not explicitly specifying the version of the language FDK when you build a function. The Fn Project CLI will continue to use cached versions of the FDK's build-time and runtime base images (if available), or pull the most recent versions of the base images from Docker Hub (if cached images are not available).

Starting with Fn Project CLI version 0.6.7:
- If you explicitly specify the version of the language FDK when you create a function, the Fn Project CLI adds that version as the value of the`build_image:`and`run_image:`parameters in the function's func.yaml file.
- If you build or deploy a function and the function's func.yaml file does not already contain`build_image:`and`run_image:`parameters because it was created with an earlier Fn Project CLI version, the Fn Project CLI adds the parameters to the func.yaml file. The values of the`build_image:`and`run_image:`parameters record the versions of the FDK build-time and runtime base images that the Fn Project CLI is currently using.

Unless you explicitly specify a different version when you re-build the function later, the Fn Project CLI continues to use the FDK version specified by the`build_image:`and`run_image:`parameters.

Note that in the case of Java functions, previous versions of the Fn Project CLI did add the`runtime:`,`build_image:`, and`run_image:`parameters to func.yaml files, to help ensure the function code remained compatible with the Java FDK's build-time and runtime base images.

If you want to re-build an existing function with a different language version, and include a different runtime in the function's Docker image, change the values of the`build_image:`and`run_image:`parameters in the function's func.yaml file to reference a different version of the language FDK. For consistency and to avoid confusion, update the value of the`runtime:`parameter to correspond to the`--runtime`command option for the version of the language FDK. In the case of Java functions, you also have to change the FDK version in the function's pom.xml file.

## How to find out the language versions supported by FDKs

To find out the versions of languages supported by FDKs (Java, Node.js, Python, Go, Ruby, and C#):
- If it hasn't already been upgraded, upgrade the Fn Project CLI to the most recent version. See[Upgrading the Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm).
- In a terminal window, enter:

```

```

For example:

```

```

In the above example, you can see that different FDKs support:
- three versions of dotnet (for C#), Java, Python and Node.js
- two versions of Go, and Ruby
- one version of Kotlin

For more details about the supported versions, see[Languages Supported by OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/languagessupportedbyfunctions.htm).

## How to find out the version of the FDK build-time and runtime base images used for an existing function

To find out the version of the FDK build-time and runtime base images that the Fn Project CLI is currently using to build the function executable, and to provide the runtime environment:
- If it hasn't already been upgraded, upgrade the Fn Project CLI to the most recent version. See[Upgrading the Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm).
- In a terminal window, change to the directory containing the function code.
- Use the`fn build`or`fn deploy`commands to build or deploy the function.

The`build_image:`and`run_image:`parameters are added to the function's func.yaml file, if they aren't already present. The parameter values show the version of the FDK build-time and runtime base images that the Fn Project CLI is currently using to build the function executable, and to provide the runtime environment.

## How to find out the default FDK build-time and runtime base image versions for a given language

To find out the default FDK build-time and runtime base image versions that the Fn Project CLI is currently using to build function executables, and to provide the runtime environment, for functions written in a given language:
- If it hasn't already been upgraded, upgrade the Fn Project CLI to the most recent version. See[Upgrading the Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm).
- In a terminal window, create a new helloworld function by entering:

```

```

where`<language>`is the particular language you're interested in (one of`java`,`python`,`node`,`ruby`,`go`,`kotlin`, or`dotnet`(for C#)).

For example:

```

```

- Change to the`/hello-func`directory created for the new function, and open the func.yaml file in a text editor.

The default FDK build-time and runtime base image versions for the language you specified are shown as values of the`build_image:`and`run_image:`parameters.

## How to find out the latest FDK build-time and runtime base image versions for a particular supported language version

To find out the latest FDK build-time and runtime base image versions that the Fn Project CLI is currently using to build executables, and to provide the runtime environment, for functions in a particular version of a given language.
- If it hasn't already been upgraded, upgrade the Fn Project CLI to the most recent version. See[Upgrading the Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm).
- 

To see the supported language versions available, run:

```

```

For example:

```

```

Note the valid values of the`--runtime`command option for the particular language you're interested in, which include the numbers of supported versions. For example:
- `java17`,`java11`,`java8`
- `python3.11`,`python3.9`,`python3.8`
- `node18`,`node16`,`node14`
- `ruby2.7`,`ruby3.1`
- `go1.19`,`go1.18`
- `dotnet3.1`,`dotnet6.0`,`dotnet8.0`(for C#)
- In a terminal window, create a new helloworld function by entering:

```

```

where`<language-version>`is the particular language and version you're interested in.

For example:

```

```

- Change to the`/hello-func`directory created for the new function, and open the func.yaml file in a text editor.

The latest supported FDK build-time and runtime base image versions for the language version you specified are shown as values of the`build_image:`and`run_image:`parameters.

## How to upgrade an existing function to use the latest FDK build-time and runtime base image version for a supported language

To upgrade an existing function so that the Fn Project CLI uses the latest FDK build-time and runtime base image versions for a supported language to build the function executable, and to provide the runtime environment:
- If it hasn't already been upgraded, upgrade the Fn Project CLI to the most recent version. See[Upgrading the Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm).
- In a terminal window, change to the directory containing the function code and open the func.yaml file in a text editor.
The`build_image:`and`run_image:`parameters show the FDK build-time and runtime base image versions currently being used by the Fn Project CLI to build the function executable, and to provide the runtime environment. For example:
```

```

If the`build_image:`and`run_image:`parameters are not present in the func.yaml file, use the`fn build`or`fn deploy`commands to build the function. Doing so will add the`build_image:`and`run_image:`parameters to the func.yaml file, set to the FDK build image and runtime image versions currently being used by the Fn Project CLI.
- 

Find out the FDK build-time image and runtime base image versions for the version of the language you want the Fn Project CLI to use (see[How to find out the latest FDK build-time and runtime base image versions for a particular supported language version](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionssupportedlanguageversions.htm#functionssupportedlanguageversions_topic_How_to_find_out_latest_supported_FDK)).
- Open the func.yaml file in a text editor (if it's not already open), and update it as follows:
- Change the values of the`build_image:`and`run_image:`parameters to the FDK build-time and runtime base image versions you identified in the previous step.

For example, you might change:
```

```

to
```

```

- For consistency and to avoid confusion, change the value of the`runtime:`parameter to correspond to the`--runtime`command option for the version of the language. For example:
```

```

- For Java functions only, open the pom.xml file in a text editor and update the`<fdk.version>`element to correspond to the version specified in the func.yaml.

For example, you might change`<fdk.version>1.0.105</fdk.version>`to`<fdk.version>1.0.130</fdk.version>`.
-
