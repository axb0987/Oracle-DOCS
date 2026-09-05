# Using the Fn Project CLI with OCI Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingwithfncli.htm
- Fetched: 2026-09-05 02:09 CDT

# Using the Fn Project CLI with OCI Functions

Find out how to use the Fn Project CLI with OCI Functions.

OCI Functions is powered by the Fn Project open source engine. As a result, you can use the Fn Project CLI to perform create, read, update, and delete operations on OCI Functions.

To enable you to use the Fn Project CLI with OCI Functions, you perform a number of preparatory tasks. See[Functions QuickStart Guides](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartguidestop.htm)and[Client Environment Configuration Notes for OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfiguringclient.htm).

Most Fn Project CLI commands have a similar syntax:
```

```

For example, to:
- list all the available applications, use the command:

```

```

- create an application, use a command like:

```

```

- invoke a function, use a command like:

```

```

- change the profile that the Fn Project CLI uses for its context, use a command like:

```

```

To see a complete list of Fn Project CLI commands, you can:
- Log in to your development environment as a functions developer and enter`fn --help`or`fn -h`in a terminal window.
- In a web browser, go to the[Fn Project CLI documentation](https://github.com/fnproject/docs/tree/master/cli).

To see detailed information about individual Fn Project CLI commands, you can:
- Log in to your development environment as a functions developer and enter`fn <command> [subcommand] --help`or`fn <command> [subcommand] -h`in a terminal window. For example:

```

```

```

```

- In a web browser, go to the[Fn Project CLI documentation](https://github.com/fnproject/docs/tree/master/cli)and select the command from the list.

From time to time, new versions of the Fn Project CLI are released. See[Upgrading the Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm)
