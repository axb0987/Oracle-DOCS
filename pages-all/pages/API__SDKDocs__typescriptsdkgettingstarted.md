# Getting Started
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/typescriptsdkgettingstarted.htm
- Fetched: 2026-09-05 01:37 CDT

# Getting Started

This topic describes how to install and configure the SDK for TypeScript and JavaScript.

This topic describes how to install and configure the SDK for TypeScript and JavaScript.

To use the Oracle Cloud Infrastructure SDK for TypeScript and JavaScript in your project, import any service from`./oci-typescript-sdk/index.ts`. For example:

```

```

## Downloading the SDK from GitHub

You can download the SDK for TypeScript and JavaScript as a zip archive from[GitHub](https://github.com/oracle/oci-typescript-sdk). It contains the SDK, all of its dependencies, documentation, and examples.

## Installing with yum

If you're using Oracle Linux 7 or 8, you can use yum to install the OCI SDK for TypeScript and JavaScript.

For Oracle Linux 8:
```

```

For Oracle Linux 7:

OS Management System needs to be enabled for the compute instance. See the[OS Management documentation](https://docs.oracle.com/iaas/os-management/osms/osms-getstarted.htm)for more information.

Node version 14 or 16 needs to be added in the software source list by OS Management. See the[Software Source documentation](https://docs.oracle.com/iaas/os-management/osms/osms-software-sources.htm#osms-console-add-software-sources)for more information on adding Nodejs 14 or 16 to the Software Source.
After the software source is added, run:
```

```

The`oci-typescript-sdk`yum package will only work for Node version 14 or 16. The`oci-sdk`package will be installed into the`global node_modules`folder. To use the`oci-sdk`package in a project, link the`oci-sdk`global package to your local project.
For example:
```

```
Because the`oci-sdk`package is globally installed, you must update the import statements for`oci-sdk`'s sub-packages when running the`oci-typescript-sdk`examples on GitHub. For example:

```

```

```

```

## Using the SDK for TypeScript and JavaScript with NPM

[NPM](https://www.npmjs.com/package/oci-sdk).

## Configuring the SDK

The SDK services need two types of configuration: credentials and client-side HTTP settings.

### Configuring Credentials

First, you need to set up your credentials and config file. For instructions, see[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm).

The default configuration location is "~/.oci/config" and "DEFAULT" profile is used. You can use`ConfigFileAuthenticationDetailsProvider`with or without specifying the configuration location and profile name:

```

```

```

```

### Configuring Custom Options

In the configuration file, you can insert custom key-value pairs that you define, and then reference them as necessary. For example, you could specify a frequently used compartment ID in the config file:

```

```

Then you can retrieve the value:

```

```

```

```
