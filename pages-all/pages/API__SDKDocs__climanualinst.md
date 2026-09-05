# Manual and Offline Installations
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm
- Fetched: 2026-09-05 01:36 CDT

# Manual and Offline Installations

This section covers how to perform manual and offline installations of the OCI Command Line Interface (CLI):
- [To perform a manual installation](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#climanualinst_intro)
- 

[To perform an offline installation.](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#InstallingCLI_Offline)

## Manual Installation

Instead of using the installation methods described in the[Quickstart](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm)or[using the OCI CLI Container image](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clicontainer.htm), you can manually install the CLI and its dependencies using`pip`. Before proceeding, be sure you meet the[Requirements](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cliconcepts.htm#Requirements).

Prior to manually installing the CLI:

- Make sure your Python path is set correctly
- Run "python --version" or "python3 --version" and make sure you have the required version
- If installing on Oracle Linux or CentOS, have the following installed:
- gcc
- zlib-devel
- python3-devel
- the latest version of OpenSSL 1.1.1
Note  
  
You can also download the CLI installation files and perform an[offline installation](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#InstallingCLI_Offline).

### Step 1: Installing Python

Python installation instructions vary for[each operating system that the CLI supports](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cliconcepts.htm#Requirements__SupportedPythonVersionsandOperatingSystems).
Note  
  
The CLI supports only the Python versions listed in the[CLI Requirements](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cliconcepts.htm#Requirements__SupportedPythonVersionsandOperatingSystems).

[Windows](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#)

Install a[supported version of Python](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cliconcepts.htm#Requirements__SupportedPythonVersionsandOperatingSystems)from the[Python Windows downloads](https://www.python.org/downloads/windows/)page. During installation, choose to add Python to the PATH and/or environment variables (depending on the prompt).

[Oracle Linux](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#)

Some versions of Oracle Linux come with incompatible versions of Python, and might require additional components to install the CLI. Before installing the CLI, run the following commands on a new Oracle Linux image.
Tip  
  
The CLI is installed by default on Oracle Linux 9, Oracle Autonomous Linux versions 7 and 8 and Oracle Linux Cloud Developer 8.

##### Oracle Linux 8
```

```

Python is available as version-specific[Application Stream modules](https://docs.oracle.com/en/operating-systems/oracle-linux/8/software-management/dnf.html#appstream)in Oracle Linux 8 and CentOS 8.
Use`dnf module list`to see the currently available Python modules. For example:
```

```

Then, enable and install a Python module. The following example will enable and install Python 3.9:
```

```

Replace`python39`and`python3.9`with either`python36`and`python3.6`or`python38`and`python3.8`to install and use those versions.

##### Oracle Linux 7
```

```

Note  
  
For Oracle Linux 7, note that`python3-devel`is in the`ol7_optional_latest`repository which may not be enabled by default. To install`python3-devel`, run the following from a shell prompt:
```

```

Details on how to install and use newer versions of Python that are available for Oracle Linux 7 can be found in the[Oracle Linux Software Collections Library documentation](https://docs.oracle.com/en/operating-systems/oracle-linux/scl-user/).

##### Oracle Linux 6
Important  
  
Oracle Linux 6 has reached end of support. Consider using Oracle Linux 9 instead.
```

```

[CentOS](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#)

Before you install the CLI, run the following commands on a new CentOS image.

##### CentOS Linux 8
```

```

Python is available as version-specific[Application Stream modules](https://docs.oracle.com/en/operating-systems/oracle-linux/8/software-management/dnf.html#appstream)in CentOS 8.

Use`dnf module list`to see the currently available Python modules.
For example:
```

```

This will produce output similar to the following:
```

```

Then, enable and install a Python module. The following example will enable and install Python 3.9:
```

```

Replace`python39`and`python3.9`with either`python36`and`python3.6`or`python38`and`python3.8`to install and use those versions.

##### CentOS Linux 7
```

```

Details on how to install and use newer versions of Python that are available for CentOS 7 can be found in the[Software Collections documentation](https://www.softwarecollections.org/en/docs/).

[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#)

Before you install the CLI, run the following commands on a new Ubuntu image.

##### Ubuntu 16, Ubuntu 18, and Ubuntu 20
```

```

[Mac OS X](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#)

Mac OS X comes with Python pre-installed.

To install the latest version of Python on Mac OS X, see[the official Python documentation](https://docs.python.org/3/using/mac.html).

### Step 2: Creating and Configuring a Virtual Environment

The[`venv`Python module](https://docs.python.org/3/library/venv.html)is a virtual environment builder that lets you create isolated Python environments. We recommend installing the CLI in a virtual environment.

#### Installing and Activating your Virtual Environment

After Python is installed, set up a virtual environment for your operating system using the following steps.

[Windows](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#)

- Navigate to the directory in which you would like to create the virtual environment.
- Create the virtual environment by running the following command:

```

```

- Activate the virtual environment by running the following command:

```

```

[Linux and Mac](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#)

- Navigate to the directory in which you would like to create the virtual environment.
- Create the virtual environment by running one of the following commands, depending on the version of Python installed:

```

```

```

```

- Activate the virtual environment by running the following command:

```

```

### Step 3: Installing the Command Line Interface

You can download the CLI from[GitHub](https://github.com/oracle/oci-cli/releases)or install the package from[Python Package Index (PyPI)](https://pypi.python.org/pypi/oci-cli).

To install using the GitHub download:
- Download and unzip oci-cli.zip .
- Optionally[validate the downloaded file](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#cliinstall_topic_verifying_checksum).
- 

Run the following command.

```

```

To install using PyPI, run the following command:

```

```

For information on how to start a CLI session, see[Using the CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliusing.htm).

## Offline Installation

If you have a[supported version of Python](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cliconcepts.htm#Requirements__SupportedPythonVersionsandOperatingSystems)installed, you can perform an offline installation of the OCI CLI.
To perform an offline installation:
- Go to the[OCI CLI release page on GitHub](https://github.com/oracle/oci-cli/releases)and select the version of the CLI that you want to install.
- Scroll down to the Assets section of the release page and click on the zip file to download it.
- Optionally[validate the downloaded file](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#cliinstall_topic_verifying_checksum).
- Copy the zip file to the target system.
- Unzip the zip file.
- Run the appropriate installer for the platform:
- On Unix and Linux, run`bash install.sh --offline-install`
- On Windows, run`install.ps1 -OfflineInstall`
- Follow the installation prompts.

For troubleshooting offline installs, see[Common Issues](https://github.com/oracle/oci-cli/blob/master/COMMON_ISSUES.rst)or[create an issue](https://github.com/oracle/oci-cli/issues)on GitHub.

## Installing Without a Virtual Environment

We do not recommend installing the CLI in your system-wide Python and suggest that instead you install the CLI using the installer or virtual environment.

In cases where you are trying to install the CLI in your system-wide Python using the latest pip version, you might encounter conflicts with some`distutils`installed packages. Following is an example error message when this occurs:
```

```

Another option is to install the CLI for the user using the following command, although this approach is not supported:
```

```

## Validating the Release Checksum

After the CLI package is downloaded, you can validate the SHA-256 checksum. Depending on your operating system, use the following instructions to compare the SHA-256 value provided in Github release with the value you get when completing this procedure for your operating system.
Windows
- Open a command shell.
- Change to the directory where the download file is located.
- Run the following command to generate the checksum value, where`filename`is the name of the downloaded file on your computer:
```

```

- Verify that the returned checksum value matches the SHA-256 value provided in the Github release. If the values do not match, please download the file again and repeat this procedure.
Mac OS
- Open a terminal window.
- Run the following command, where`fileLocation`is the full path of the file on your computer:
```

```
This command should return a checksum value.
- Verify that the returned checksum value matches the SHA-256 value provided in the Github release. If the values do not match, please download the file again and repeat this procedure.
Linux
- Open a terminal session.
- Run the following command, where`fileLocation`is the full path of the file on your computer:
```

```

This command should return a checksum value.
-
