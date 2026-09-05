# SDK for .NET Cloud Shell Quick Start
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cloudshellquickstart_dotnet.htm
- Fetched: 2026-09-05 01:35 CDT

# SDK for .NET Cloud Shell Quick Start

This topic explains how to quickly get started with the Oracle Cloud Infrastructure SDK for .NET using Cloud Shell.
- Sign in to the Console.
- Click the Cloud Shell icon in the Console header. Note that Cloud Shell runs commands against the region selected in the Console's Region selection menu when Cloud Shell was started.
- Create a working directory and move to it:

```

```

- Create a new .NET Console application project:

```

```

- Add the`OCI.DotNetSDK.Objectstorage`package to the project.

```

```

Optionally, you can include the`--source`parameter, which falls back to retrieving the package from the pre-installed location (`/usr/lib/dotnet/NuPkgs/`) if it can't be downloaded from nuget.org.
Note  
  
To bypass nuget.org and force usage of the pre-installed .NET SDK, you can use the`nuget.config`provided in step 2a of the instructions[here](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../SDKDocs/dotnetsdkgettingstarted.htm#installing_modules_with_yum).
- Add the following code to the`Program.cs`file:

```

```

- Run the example:

```

```
