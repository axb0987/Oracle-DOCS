# Getting Started
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/dotnetsdkgettingstarted.htm
- Fetched: 2026-09-05 01:36 CDT

# Getting Started

This topic describes how to install and configure the SDK for .NET.

This topic describes how to install and configure the SDK for .NET.

To use a specific Oracle Cloud Infrastructure service in your project, you can use the dotnet add package command from the root directory of your project workspace that contains the project file. The syntax for the add package command is:

```

```

If you do not specify a version number, the`add package`command will install the latest version.

This example installs the latest version of the Core Service package:

```

```

This example installs version 1.0.0 of the Identity Service package:

```

```

Note  
  
To avoid dependency conflicts, you should use the same versions of all OCI. NET SDK Nuget packages within an application.

## Downloading the SDK from GitHub

You can download the SDK for .NET as a zip archive from[GitHub](https://github.com/oracle/oci-dotnet-sdk). It contains the SDK, all of its dependencies, documentation, and examples.

## Installing the SDK with Yum

If you're using Oracle Linux 7 or 8, you can use yum to install the OCI SDK for .NET.
- To install the OCI SDK for .NET using yum:
- 

For Oracle Linux 7:
```

```

- 

For Oracle Linux 8:
```

```

The OCI Dotnet SDK service packages and its dependencies are located in`/usr/lib/dotnet/NuPkgs/`.
- So the dotnet CLI can find the installed packages, you must do one of the following:
- Create a file named`nuget.config`in the root of your .NET application project and add the following content:
```

```
...or...
- Use the`--source`option with the dotnet CLI commands, passing in the directory`/usr/lib/dotnet/NuPkgs/`. For example:
```

```

- To get information about the installed package, run the following command:
```

```

- Add the OCI Service packages to your project using the dotnet command line:
```

```

- You can now import namespaces into your project. For example:
```

```

## Using the SDK for .NET with Nuget

[Nuget](https://www.nuget.org/profiles/oci-dotnet-sdk).

## Configuring the SDK

The SDK services need two types of configuration: credentials and client-side HTTP settings.

### Configuring Credentials

First, you need to set up your credentials and config file. For instructions, see[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm).

Next, you need to set up the client to use the credentials. The credentials are abstracted through an`IAuthenticationDetailsProvider`interface that the client needs to implement.

These examples shows implementations of`ConfigFileAuthenticationDetailsProvider`and`SimpleAuthenticationDetailsProvider`.

[Using a Standard Configuration](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/dotnetsdkgettingstarted.htm#)

If you use standard config file keys and the standard config file location, you can use`ConfigFileAuthenticationDetailsProvider`:

```

```

[Using a Custom Configuration](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/dotnetsdkgettingstarted.htm#)

If you are using custom key names in the config file, you can use`SimpleAuthenticationDetailsProvider`

To load a config with or without a profile:

```

```

Next, create an`Auth`provider using`SimpleAuthenticationDetailsProvider`:

```

```

### Configuring Client-Side Options

Create a client-side configuration through the`ClientConfiguration`class. If you do not provide your own configuration, the SDK for .NET uses a default configuration.

The following example shows how to provide your own configuration:

```

```

### Configuring Custom Options

In the configuration file, you can insert custom key-value pairs that you define, and then reference them as necessary. For example, you could specify a frequently used compartment ID in the config file:

```

```

Then you can retrieve the value:

```

```

### Enabling Logging

The OCI SDK for .NET uses the`NLog`package for logging.`NLog`is automatically installed with the .NET SDK, so no additional installation is required.
To enable logging in your project:
- Add an`NLog.config`file at the project's root directory. You can find an example NLog.config file[here](https://github.com/NLog/NLog/wiki/Configuration-file#nlog-config-xml)
- Add an`ItemGroup`section in the project file. For example:
```

```

- To log from an application, create a`Logger`and use the`Info()`method. For example:
```

```

Note
