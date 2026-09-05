# SDK and CLI Configuration File
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
- Fetched: 2026-09-05 01:35 CDT

# SDK and CLI Configuration File

Oracle Cloud InfrastructureSDKs and CLI require basic configuration information, like user credentials and tenancy OCID. You can provide this information by:
- Using a configuration file
- Declaring a configuration at runtime
Note  
  
You can use the Console to help generate a configuration file. For more information, see[Generating an API Signing Key (Console)](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#apisigningkey_topic_How_to_Generate_an_API_Signing_Key_Console).

The SDKs fully support both options. Refer to the documentation for each SDK for information about the config object and any exceptions when using a configuration file:
- [Oracle Cloud InfrastructureSDK for Java Configuration](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../SDKDocs/javasdkgettingstarted.htm#Configur)
- [Oracle Cloud InfrastructureSDK for Python Configuration](https://docs.oracle.com/iaas/tools/python/latest/configuration.html)
- [Oracle Cloud InfrastructureSDK for Ruby Configuration](https://docs.oracle.com/iaas/tools/ruby/latest/index.html#label-Configuring+the+SDK)
- [Oracle Cloud InfrastructureSDK for Go Configuration](https://github.com/oracle/oci-go-sdk/blob/master/README.md#configuring)
- [Oracle Cloud InfrastructureSDK for TypeScript and JavaScript Configuration](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../SDKDocs/typescriptsdkgettingstarted.htm#configuring)
- [Oracle Cloud InfrastructureSDK for .NET Configuration](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../SDKDocs/dotnetsdkgettingstarted.htm#Configure)

The CLI requires a configuration file, but also allows you to set environment variables to provide certain information. See[CLI Environment Variables](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../SDKDocs/clienvironmentvariables.htm)for more information.

## File Name and Location

On macOS and Git Bash on Windows the default OCI CLI config file location is`~/.oci/config`. Here,`~`refers to the current user's home directory, for example,`/Users/username/.oci/config`. On Windows PowerShell (native Windows shell) the config file location is`"$($Env:UserProfile)\.oci\config"`. This expands to`C:\Users\YourUsername\.oci\config`.

## File Entries

The following table lists the basic entries that are required for the configuration file, as well as where to get the required information.

Entry Description and Where to Get the Value Required?
`user`

OCID of the user calling the API. To get the value, see[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm).

Example:`ocid1.user.oc1..<unique_ID>`(shortened for brevity) Yes
`fingerprint`

Fingerprint for the public key that was added to this user. To get the value, see[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm). Yes
`key_file`

Full path and filename of the private key.

Important: The key pair must be in PEM format. For instructions on generating a key pair in PEM format, see[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm).

Example (Linux/Mac OS):`~/.oci / oci_api_key.pem`

Example (Windows):`~/.oci/oci_api_key.pem`

This corresponds to the file`%HOMEDRIVE%%HOMEPATH%\.oci\oci_api_key.pem`. Yes
`pass_phrase`

Passphrase used for the key, if it is encrypted.

Caution: This entry is deprecated, and is included for backward compatibility only. Avoid saving confidential information in the configuration file. For additional security, pass the passphrase to the SDK/CLI at run time. Yes, if key is encrypted and passphrase has not been configured to be passed to at runtime
`tenancy`

OCID of your tenancy. To get the value, see[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm).

Example:`ocid1.tenancy.oc1..<unique_ID>`Yes
`region`

An Oracle Cloud Infrastructure region. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

Example:`us-ashburn-1`Yes
`security_token_file`

If[session token authentication](https://docs.oracle.com/iaas/Content/API/Concepts/sdk_authentication_methods.htm#sdk_authentication_methods_session_token)is being used, then this parameter is required.

Using this authentication method makes fingerprint , user , and pass_phrase not required. Starting a session with the OCI CLI will populate all of the required parameters for this authentication method. See[Starting a Token-based CLI Session](https://docs.oracle.com/iaas/Content/API/SDKDocs/clitoken.htm#Starting). Conditional

### Custom Values

Some Oracle Cloud Infrastructure SDKs support defining custom values in the configuration file. Refer to the documentation for each SDK for more information.

### Profiles and Inheritance

You can create multiple profiles with different values for these entries, then you can specify which profile to load.

Some Oracle Cloud Infrastructure SDKs require a DEFAULT profile and support profile inheritance. This means that any value that isn't explicitly defined for a given profile is inherited from the DEFAULT profile. Refer to the documentation for each SDK for more information.

## Example Configuration

The following example (for Linux and Mac OS) shows key values in a configuration file and how to set profiles for a SDK that supports profile inheritance.

```

```

This example is for Windows:
```

```
