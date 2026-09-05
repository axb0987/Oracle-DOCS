# Preserving Hosts File Edits for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/preserving_hosts_edits.htm
- Fetched: 2026-09-05 02:58 CDT

# Preserving Hosts File Edits for Roving Edge Infrastructure

Preserve your edits to the`/etc/hosts`file on a compute instance on your Roving Edge Infrastructure device.

To preserve your edits to the`/etc/hosts`file on a compute instance in Roving Edge Infrastructure, open the following file:
```

```

Update the`PRESERVE_HOSTINFO`value at the bottom of the configuration from the default`0`to`2`or`3`. For example:
```

```

Updating the`PRESERVE_HOSTINFO`value prevents the metadata service from overwriting the changes to the`/etc/hosts`
