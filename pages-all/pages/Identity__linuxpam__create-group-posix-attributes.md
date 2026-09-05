# Creating a Group with POSIX Attributes
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/create-group-posix-attributes.htm
- Fetched: 2026-09-05 02:23 CDT

# Creating a Group with POSIX Attributes

Create a group with POSIX attributes.

- Create a`group.json`file with the following request body:

`group.json`
```

```

where:
- `displayName`is set to the name of the group that you wish to create
- `gidNumber`must be set to a unique group id (gid) number. Use the`getent group`command on Linux to see the existing group gid's.
- Run the following curl command to create the group:

```

```

where:
- `token-string`is the OAuth access token that you obtained
- `identity-cloud-service-instance-url`is your IAM Instance URL

Note
