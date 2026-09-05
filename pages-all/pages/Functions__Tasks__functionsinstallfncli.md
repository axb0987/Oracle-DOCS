# Installing the Fn Project CLI
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstallfncli.htm
- Fetched: 2026-09-05 02:08 CDT

# Installing the Fn Project CLI

Find out how to install the Fn Project CLI for use with OCI Functions.

Before using OCI Functions, the Fn Project CLI must be installed in your development environment.

If you are using Cloud Shell as your development environment, the Fn Project CLI has already been installed for you.

You can install the Fn Project CLI in a number of different ways according to your environment.

The instructions in this topic assume:
- you are not using Cloud Shell as your development environment
- you are using Linux
- you have already completed the steps in[Installing Docker for Use with OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstalldocker.htm)

To install the Fn Project CLI:
- 

Log in to your development environment as a functions developer.
- 

Open the[README.md](https://github.com/fnproject/cli/blob/master/README.md)file in the fnproject/cli repository on GitHub and follow the appropriate instructions for installing the Fn Project CLI in your development environment. As a convenient overview, the instructions are summarized below:
- 

In a MacOS environment using Homebrew, install the Fn Project CLI by entering:

```

```

- 

In a Linux or MacOS environment, install the Fn Project CLI by entering:

```

```

If prompted for a password, enter the superuser's password.
- In a Windows environment, install the Fn Project CLI by following the[Install Fn Client](https://github.com/fnproject/docs/blob/master/fn/develop/running-fn-client-windows.md#install-fn-client)instructions in the[How-to: Run Fn client on Windows and connect to a remote Fn server](https://github.com/fnproject/docs/blob/master/fn/develop/running-fn-client-windows.md)topic on GitHub.
- 

In a Linux, MacOS, or Windows environment, install the Fn Project CLI by downloading the binary from the[Releases](https://github.com/fnproject/cli/releases)page and running it.
- 

In a terminal window, confirm that the CLI has been installed by entering:

```

```

Assuming the Fn Project CLI has been installed correctly, you'll see a message indicating the version of the CLI that has been installed.

When you have completed the steps in this topic, go on to[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)
