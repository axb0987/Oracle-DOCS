# Adding POSIX Attributes to Existing Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/add-posix-attributes-existing-groups.htm
- Fetched: 2026-09-05 02:23 CDT

# Adding POSIX Attributes to Existing Groups

Add POSIX attributes to existing groups.

- Create a`group_update.json`file with the following request body:

`group_update.json`
```

```

where:
- `gidNumber`must be set to a unique group id (gid) number. Use the`getent group`command on Linux to see the existing group gid's.
- Run the following curl command to retrieve the group id's:

```

```

where:
- `token-string`is the OAuth access token that you obtained
- `identity-cloud-service-instance-url`is your IAM Instance URL

In the response, note the`id`of the group you want to update with POSIX attributes. For example, in the response below, the Marketing group`id`is`8c1f45fee6354e20aa9e57079082d6a2`:
```

```

- Run the following curl command to update the group:

```

```

where:
- `token-string`is the OAuth access token that you obtained
- `identity-cloud-service-instance-url`is your IAM Instance URL
- `id`is the id for the group that you want to update with POSIX attributes

Note
