# SDK Troubleshooting
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_troubleshooting.htm
- Fetched: 2026-09-05 01:35 CDT

# SDK Troubleshooting

This section covers the most common errors that can occur with the OCI SDKs and how to troubleshoot them.

## Timeout Errors

Timeout errors happens when a request doesn't get a response from the server within the configured timeout period. These errors can happen for a number of reasons, and are raised differently, depending on the SDK:
- Java SDK: A`BmcException`is thrown with a status code of -1. This exception also has a timeout field with a`true`value.
- Go SDK: The returned error message contains "`(Client.Timeout exceeded while awaiting headers)`."
- .NET SDK: A`System.Threading.Tasks.TaskCanceledException`is thrown.
- TypeScript SDK: The error contains "`ETIMED`".
- Ruby SDK: A`NetworkError`is thrown with a status code of`0`.
- Python SDK: Either a`ConnectTimeout`exception is thrown with a message containing "`ConnectTimeoutError`", or a`RequestException`is thrown with a message containing "`Read timed out`".
Troubleshooting Suggestions
- Have you updated the SDK?
- If so, try reverting back to the original version used when the code was working.
- If the original version works, stay with the working version, and continue to Step 2 using the new (not working) version of the SDK.
- If the original version of SDK does not work anymore, continue to Step 2.
- If the SDK version did not change, check if there are other code changes since it worked last time.
- If there have been code changes, try reverting those changes and re-try the original working code.
- If the original working code stops working, continue to Step 2.
- If the original working code works, the issue was caused by the code change.
- If there have been no code changes since it worked last time, continue to Step 2.
- Does the timeout occur if you send the same request to a different OCI region from the same machine?
- If not, then the timeout came from the service. Contact support and be ready to provide the`opc-request-id`for the failing request.
- If the request still fails with a timeout, continue to Step 3.
- Try the same operation from another tool or SDK, such as the OCI CLI or curl. Does the timeout issue still occur?
- If not, please contact support or create an issue on Github.
- If so, the issue is either with the service or the network. Check network connectivity or contact support for help.
- Other possible causes:
- A timeout error might occur if your internet speed is not fast enough to send all of the content of the request body within the configured timeout period. Check your internet connection and timeout settings.
- Check your local network and proxy settings to make sure the hostname can be resolved.

## SSL Errors

If you receive an SSL certificate error (often raised as a`CERTIFICATE_VERIFY_FAILED`error), you might be missing additional certificates that the operation requires.

Troubleshooting Suggestions

The OCI CLI and each OCI SDK have unique methods to specify certifications in code.

CLI

```

```

Java
Import CA certificates to the Java Keystore:
- Import a certificate into the Apple Mac OS keychain:
```

```

- Import a Certificate into the Java Runtime Environment (JRE) Truststore:
```

```

Go
```

```

Python
```

```

Ruby
```

```

TypeScript
```

```

.NET

For the OCI .NET SDK, you need to trust the certificate file at the OS level:

Mac OS
- 

In the Keychain Access app on your Mac, select either the Login or System keychain.
- 

Drag the certificate file onto the Keychain Access app.
- 

If you're asked to provide a name and password, type the name and password for an administrator user on this computer.

Centos/RHEL/Oracle Linux
- 

Copy the .crt file to`/etc/pki/ca-trust/source/anchors`on your machine
- 

Run`update-ca-trust extract`

Debian/Ubuntu
- 

Copy the .crt file to`/usr/local/share/ca-certificates/`on your machine
- 

Run`update-ca-certificates`

Windows
- Click the search box on the taskbar or in the Start Menu, and type "mmc" to launch the Microsoft Management Console.
- Click the File menu and then click Add/Remove Snap-In .
- Click Certificates under Available Snap-ins then click Add .
- Click OK
- Click Computer Account , then click the Next button.
- Click Local Computer
- Click Finish .
- Double-click Certificates (Local Computer) in the tree menu, then right-click Trusted Root Certification Authorities Store .
- Click All Tasks in the pop-up menu, then select Import .
- Follow the instructions to find and import your certificate.

## Configuration or Authentication Errors

The OCI SDKs use a configuration file to authenticate on local machines. See[SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File)for more information.
This is an example configuration file:
```

```

Troubleshooting Suggestions
- If you get an error message similar to "did not find a proper configuration for user", ensure that you have a valid configuration file.
- If you're using instance principal or resource principal authorization, check that you're running in the correct environment and that the IMDS service is enabled. For more information on authentication methods, see[SDK Authentication Methods](https://docs.oracle.com/iaas/Content/API/Concepts/sdk_authentication_methods.htm)
