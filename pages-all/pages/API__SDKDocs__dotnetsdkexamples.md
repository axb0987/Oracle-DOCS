# Examples
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/dotnetsdkexamples.htm
- Fetched: 2026-09-05 01:36 CDT

# Examples

This topic describes how to find, download, and run OCI .NET SDK examples.

GitHub

Examples of SDK usage can be found on[GitHub](https://github.com/oracle/oci-dotnet-sdk), including:
- [Example: Create an instance](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/CreateInstanceExample.cs)
- [Example: Invoke Oracle Function](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/FunctionsExample.cs)
- [Example: Move Compartment](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/MoveCompartments.cs)

The examples are also in the downloadable .zip file for the SDK. Examples for older versions of the SDK are in the downloadable .zip for the specific version, available on[GitHub](https://github.com/oracle/oci-dotnet-sdk/releases).
If you'd like to see another example not already covered, file a[GitHub issue](https://github.com/oracle/oci-dotnet-sdk/issues).

SDK Reference

In addition to the examples found on GitHub, the[SDK for .NET API reference](https://docs.oracle.com/iaas/tools/dotnet/latest/api/index.html)contains code examples that you can copy and modify to run in your own environment.

## Running Examples

- Use git to clone the OCI SDK for .NET repository:`git clone https://github.com/oracle/oci-dotnet-sdk.git`
- Create a configuration file in your home directory (`~/.oci/config`). See[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm)for more information.
- Change directory into the .NET Examples folder. For example:`cd ./oci-dotnet-sdk/Examples/`
- 

All of the examples require the environment variable`OCI_COMPARTMENT_ID`populated with the tenant ID or compartment ID.
- 

From the command line, run`dotnet run`. The[Audit example](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/AuditExample.cs)runs by default.
- 

To run any other example, make sure it has a`Main()`
