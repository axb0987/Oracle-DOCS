# Log Group Commands
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/log_group_commands.htm
- Fetched: 2026-09-05 02:38 CDT

# Log Group Commands

The following are log group-related commands.

Create a new log group with a unique display name

```

```

This call fails if the log group is already created with same`displayName`in the compartment.

Get a specified log group's information

```

```

List all log groups for the specified compartment or tenancy

```

```

Updates an existing log group with the associated configuration

```

```

This call fails if the log group does not exist.

Move a log group into a different compartment within the same tenancy

```

```

When provided, the If-Match is checked against the ETag values of the resource. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

To delete a specified log group

```

```
