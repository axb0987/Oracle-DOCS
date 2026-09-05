# Copying a Stack
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/copy-stacks.htm
- Fetched: 2026-09-05 02:54 CDT

# Copying a Stack

Duplicate a stack in Resource Manager.

You can copy a stack using the CLI only.

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/copy.html)oci resource-manager stack copy`command and required parameters to copy a stack.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

[Example Requests](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/copy-stacks.htm#)

[Create a copy of a stack in the current compartment and region](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/copy-stacks.htm#)

```

```

[Copy a stack to a different compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/copy-stacks.htm#)

```

```

[Copy a stack that uses CI/CD to a different region](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/copy-stacks.htm#)

In this example, the stack uses a[configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm)specifying GitHub, which helps achieve continuous integration and continuous delivery (CI/CD). The GitHub access token is required when copying a stack to another region.

```

```
