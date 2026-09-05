# Configuring the CLI
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliconfigure.htm
- Fetched: 2026-09-05 01:36 CDT

# Configuring the CLI

You can use these optional configurations to extend CLI functionality. The CLI supports using a file for CLI-specific configurations. You can:
- Specify a default profile.
- Set default values for command options so you don't have to type them into the command line.
- Define aliases for commands. For example, using "ls" as an alias for`list`.
- Define aliases for options. For example, using "--ad" as an alias for`--availability-domain`.
- Define named queries that are passed to the`--query`option instead of typing a JMESPath expression on the command line.

The CLI also supports the use of environment variables to specify defaults for some options. See[CLI Environment Variables](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clienvironmentvariables.htm)for more information.

## CLI Configuration File

The default location and file name for the CLI-specific configuration file is`~/.oci/oci_cli_rc`, but you can use the`OCI_CLI_RC_FILE`environment variable to modify where the CLI looks for a configuration file and its default values upon startup.

You can also explicitly specify a CLI configuration file with the`--cli-rc-file`option or with the legacy`--defaults-file`option. For example:

```

```

To set up an oci_cli_rc file, run the following command.

```

```

This command creates the file you specify that includes examples of default command aliases, parameter aliases, and named queries.
Note  
  
If you're using Windows, use backslash as the directory separator in pathnames instead of the forward slash.

## Specifying a Default Profile

Specify a default profile in the`OCI_CLI_SETTINGS`section of the CLI configuration file. The next example shows how to specify a default profile named IAD. The CLI looks for a profile named IAD in your`~/.oci/config`file, or any other file that you specify using the`--config-file`option or the`OCI_CLI_CONFIG_FILE`environment variable.

```

```

You can also specify a default profile by using the`--profile`option or by setting the`OCI_CLI_PROFILE`environment variable.

If a default profile value has been specified in multiple locations, the order of precedence is:
- The value specified in the`--profile`option.
- The value specified in the`OCI_CLI_PROFILE`environment variable.
- The value specified in the`default_profile`field in the`OCI_CLI_SETTINGS`section of the CLI configuration file.

## Specifying Default Values

The CLI supports using default values so that you don't have to keep typing every value into the command line. For example, instead of typing in a`--compartment-id`on each launch instance command or having to keep specifying the`--namespace`when using Object Storage commands. You can specify this information in a default values file.

Default values can be applied at different levels, from general to specific:
- Globally, across all the CLI commands.
- To a particular service, such as Compute or Object Storage.
- To a specific group, such as commands related to exporting images.
- To a specific command.

Default values are treated hierarchically, with specific values having a higher order of precedence than general values. For example, if there is a globally defined value for`compartment-id`and a specific`compartment-id`defined for the`compute instance launch`command, the CLI uses the value for the`compute instance launch`instead of the global default.

### Command Value Priority

If a value is provided on the command line also exists in`--cli-rc-file`, the value from the command line has priority. For a command with options that take multiple values, the values are taken entirely from the command line or from`--cli-rc-file`. The 2 sources aren't merged.

### Defaults Value File Syntax

The`--cli-rc-file`file can be divided into different sections with one or more keys per section.

### Sections

In the next example, the file has two sections, with a key in each section. To specify which section to use, you use the`--profile`option in the CLI.

```

```

### Keys

Keys are named after command line options, but do not use a leading double hyphen (--). For example, the key for`--image-id`is`image-id`. You can specify keys for single values, multiple values, and flags.
- 

Keys for Single Values. The next example shows how to specify key values at different levels, and with different scope.

```

```

- 

Keys for Multiple Values. Some options, such as`--include`and`--exclude`on the`oci os object bulk-upload`command can be specified more than once. For example:

```

```

The next example shows how you would enter the`--include`values in the`--cli-rc-file`file

```

```

In the previous example, one value is given for each line and each line must be indented underneath its key. You can use tabs or spaces and the amount of indentation doesn't matter. You can also put a value on the same line as the key, add more values on the following lines, and use a path statement for a value. For example:

```

```

- 

Keys for Flags. Some command options are flags, like`--force`, which uses a Boolean value. To set a flag for the`--force`option, use the following command.

```

```

## Specifying Command Aliases

Specify named queries in the OCI_CLI_COMMAND_ALIASES section of the CLI configuration file. There are two types of aliases, global aliases and command sequence aliases. The following example shows each type of alias.

```

```

If you want to define default values for options in your CLI configuration file, you can use the alias names you have defined. For example, if you have`-ls`as an alias for`--list`, you can define a default for an availability domain when listing instances by using the following command.

```

```

## Specifying Option Aliases

Specify option aliases in the OCI_CLI_PARAM_ALIASES section of the CLI configuration file. Option aliases are applied globally. The following example shows some aliases for command options.

```

```

If you want to define default values for options in your CLI configuration file, you can use the alias names you have defined. For example, if you have`-ad`as an alias for`--availability-domain`, you can define a default for an availability domain when listing instances by using the following command.

```

```

## Specifying Named Queries

If you use the`--query`parameter to filter or manipulate output, you can define named queries instead of using a JMESPath expression on the command line.

Specify named queries in the OCI_CLI_CANNED_QUERIES section of the CLI configuration file.

[Examples of Named Queries](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliconfigure.htm#)

```

```

You can reference any of these queries using this syntax:`query://<query name>`.

For example, to get id and display name from a list, run the following command.

```

```

## Enabling Auto-complete

If you used the CLI installer, you don't have to configure auto-complete because it's enabled automatically.

To enable auto-complete (tab completion) for a manual CLI installation, run the following command.

```

```

To enable auto-complete on a session by session basis, run the following command.

```

```

Note  
  

Support for Auto-complete on Windows

Auto-complete on Windows is only supported if you're using PowerShell. A script runs to enable this feature. However, you must change the PowerShell execution policy to RemoteSigned. To configure this policy, run the following command at the PowerShell command line.

```

```

## Specifying a Proxy Server

If your environment requires you to use a proxy server for outgoing HTTP requests, you can specify the proxy setting using an environment variable.

To configure a proxy server, set the environment variables`http_proxy`,`https_proxy`,`HTTP_PROXY`, and`HTTPS_PROXY`to the correct proxy server in your environment.

For example, in a Linux or Unix shell environment:

```

```

In PowerShell:
```

```

## Using FIPS-validated Libraries

The CLI can be configured to use FIPS-validated libraries on Linux. The CLI is built on the Oracle Cloud Infrastructure SDK for Python and leverages operating system level cryptographic libraries.

### Configuring the Environment
- Verify the installed version of OpenSSL is FIPS-compliant. Run the following command:

```

```

If "fips" is not part of the version name, you should upgrade OpenSSL to a FIPS-compliant version. You can download the latest versions of OpenSSL at:[https://www.openssl.org/source/](https://www.openssl.org/source/)
- Determine the location of the FIPS-compliant version of libcrypto:

```

```

- Set the environment variable OCI_CLI_FIPS_LIBCRYPTO_FILE to the location of libcrypto:

```

```

If you do not want to run this command at the start of every session, you can add it to your.bashrc or .bash_profile file.

You can confirm that the environment variable is set properly with this command:

```

```

You can now proceed to the standard installation process outlined in[Quickstart](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm)

### Verifying the Configuration

To verify that the CLI is using the library that you specified during[Configuring the CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliconfigure.htm), execute the following commands in Python. Be sure to do so in the same environment that the CLI uses.

```

```
