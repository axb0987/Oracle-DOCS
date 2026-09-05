# VCN Flow Logs Example
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/vcn_flowlogs_eg.htm
- Fetched: 2026-09-05 02:38 CDT

# VCN Flow Logs Example

The following are sample logging commands related to VCN Flow Logs.

To create a log group

As a required prerequisite, run the oci session authenticate command first:
```

```

Next, execute the oci logging command using the --profile &lt;profile_name&gt; and --auth security_token options:

```

```

To create a`flowlogs`log object (enable Flow Logs)

Run the oci session authenticate command:
```

```
Next, execute the oci logging command using the --profile &lt;profile_name&gt; and --auth security_token options:

```

```

Sample configuration file:
```

```

To disable a`flowlogs`log object (disable Flow Logs)

Run the oci session authenticate command:
```

```
Next, execute the oci logging command using the --profile &lt;profile_name&gt; and --auth security_token options:

```

```

To delete the log object

Run the oci session authenticate command:
```

```
Next, execute the oci logging command using the --profile &lt;profile_name&gt; and --auth security_token options:

```

```
