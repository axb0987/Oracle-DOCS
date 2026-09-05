# Troubleshooting the CLI
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clitroubleshooting.htm
- Fetched: 2026-09-05 01:36 CDT

# Troubleshooting the CLI

This topic describes how to resolve issues that you might encounter when installing Python or the CLI, or when using the CLI.

## Installation Errors

If you see an error similar to this when installing with pip:

```
[](https://pypi.org/project/oci-cli/)[](http://pypi.org/)
```

Your machine may not be connected to external internet, or your network settings are blocking access to pypi. Consult with your network administrator to fix your network settings, or try performing an[Offline Installation](https://docs.oracle.com/iaas/Content/API/SDKDocs/climanualinst.htm#InstallingCLI_Offline)or using the[Container Image](https://docs.oracle.com/iaas/Content/API/SDKDocs/clicontainer.htm).

## Upgrade Errors

If you are seeing an outdated version number after performing a CLI upgrade, you should try uninstalling the previous version of the CLI.
You can find the package locations using the command:
```

```

Note  
  
Note that this command is not available in CLI versions 3.4.0 and earlier. Remove the packages listed by the command above using the instructions in[Uninstalling the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliuninstall.htm), and then install the latest OCI CLI version following the instructions for your environment found in the[Quickstart](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm).

## Service Errors

Any operation resulting in a service error causes an error of type "ServiceError" to be returned by the CLI. For information about common service errors that Oracle Cloud Infrastructure returns, see[API Errors](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../References/apierrors.htm).

401 Error - Not Authenticated

A service error has a status of`401`and a code of`NotAuthenticated`might indicate an invalid configuration file.

Please follow the instructions in[Setting up the Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#configfile)to set up and verify your configuration file.

## SSL Errors

Request Exception
A request exception like the following may indicate an invalid configuration file:
```

```

Please follow the instructions in[Setting up the Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#configfile)to set up and verify your configuration file.

Certification Verify Failed Using a Local Certification

A`CERTIFICATE_VERIFY_FAILED`exception might indicate that the CLI cannot find the additional certification your operation requires.
To resolve this, locate your local certification file:
```

```
This will return output similar to the following:
```

```

Set an environment variable so the CLI can find your local certification. For example:
```

```

Certification Verify Failed Using a Certification in an Instance

A`CERTIFICATE_VERIFY_FAILED`exception might indicate that the CLI cannot find the additional certification your operation requires. In some cases, the certification file may already be provisioned in the host.
To resolve this, set the location of your certification in an environment variable for the CLI to use:
```

```

If the certification file was not provisioned in the host, locate your certification file within the instance and set the variable to the correct path. For example:
```

```

Certification Verify Failed: URL Error If your machine is running a macOS variant of python 3.6 or 3.7, and you see the following message despite setting your certification path correctly:
```

```

To resolve this, locate and run the Certificates.command file. Your command may look like::
```

```

Run the CLI installer after the Certificates command runs successfully.

## Oracle Linux Permissions Issues

On Oracle Linux 7.3, if you encounter permission issues when running`pip install`, you might need to use`sudo`.

## oci Command Not Found

If the`oci`command isn't found, this can be caused by one of the following reasons:
- pip installed the package to a different virtual environment than your active one.
- You switched to a different active virtual environment after you installed the CLI.

To determine where the CLI is installed, run the`which pip`and`which oci`commands.

## ERROR: Could not find config file at /root/.oci/config

This error can occur when running a CLI command such as the following:
```

```

If the`config`file isn't found, use one of the following options:
- [Use the Console to create a CLI session](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clitoken.htm#Starting).
- Use the[Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cloudshellintro.htm).
- Create a`config`file using one the options in[Setting up the Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#configfile).

## Wheel File Won't Install

If the wheel file won't install, verify that pip is up to date. To update pip, run the`pip install -U pip`command. Try to install the wheel again.

## Windows Issues

If the`oci`command isn't found, make sure that the`oci.exe`location is in your path (for example, the`Scripts`directory in your Python installation).

## No Matching Distribution Found

Error:`No matching distribution found for oci-cli==3.x.x`

This error occurs if you are attempting to install the CLI in a Python 2 environment. Support for Python 2 was deprecated as of August 1, 2021.

To resolve this issue, update your Python to version 3.6.5 or later. If you require Python 2, any CLI version starting with 2.x.x will still support Python 2.

## Silent Data Corruption Using put Command

Issue: Users using the`oci os object put`command with data from STDIN might see silent data corruption in FIPS mode or in an environment which uses a FIPS-compliant OpenSSL version. The CLI reports that the upload operation was successful, but no data is uploaded.

To mitigate this issue, update the OCI CLI version to 3.4.1 or greater.
Tip  
  

Users initially setting up FIPS for the CLI should follow the instructions in[Using FIPS-validated Libraries](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliconfigure.htm#fips)

## Contact Information

If you want to search for an issue not listed here, contribute ideas, report a bug, get notified about updates, or have questions or feedback, use one of the following links.

### Contributions

Got a fix for a bug, or a new feature you'd like to contribute? The CLI is open source and accepting pull requests on[GitHub.](https://github.com/oracle/oci-cli)

### Notifications

To be notified when a new version of the CLI is released, subscribe to the[Atom](https://github.com/oracle/oci-cli/releases.atom)feed.

### Questions or Feedback

Ways to get in touch:
- [GitHub](https://github.com/oracle/oci-cli/issues): To search for issues or to file bugs and feature requests.
- [Stack Overflow](https://stackoverflow.com/): Use the[oracle-cloud-infrastructure](https://stackoverflow.com/questions/tagged/oracle-cloud-infrastructure)and[oci-cli](https://stackoverflow.com/questions/tagged/oci-cli)tags in your post.
- [Developer Tools section](https://community.oracle.com/community/oracle-cloud/cloud-infrastructure/content?filterID=contentstatus%5Bpublished%5D~category%5Bdeveloper-tools%5D)of the Oracle Cloud forums
- [My Oracle Support](https://support.oracle.com)
