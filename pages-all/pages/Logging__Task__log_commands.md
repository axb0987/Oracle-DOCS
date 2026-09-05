# Log Commands
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/log_commands.htm
- Fetched: 2026-09-05 02:38 CDT

# Log Commands

The following are log commands.

Create a log within a specified log group

```

```

This call fails if the log group has already been created with the same displayName or (service, resource, category) triplet.

Get the log object configuration for the log object OCID

```

```

List the specified log group's log objects

```

```

Move a log into a different log group within the same tenancy

```

```

When provided, the If-Match is checked against the ETag values of the resource.

To delete a log object in a log group

If you have an issue with deleting a log object, open a command prompt and run the following command to delete it:

```

```

To ingest logs associated with a logId

```

```

List all services supporting logging

```

```

Update an existing log object with the associated configuration

```

```
