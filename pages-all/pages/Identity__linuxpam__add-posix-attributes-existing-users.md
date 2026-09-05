# Adding POSIX Attributes to Existing Users
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/add-posix-attributes-existing-users.htm
- Fetched: 2026-09-05 02:23 CDT

# Adding POSIX Attributes to Existing Users

Add POSIX attributes to existing users.

Note  
  
In order to add POSIX attributes to an existing user, that user must first be part of a group, and that group must have POSIX attributes.

- Create a`user_update.json`file with the following request body:

`user_update.json`
```

```

where:
- `homeDirectory`is set to the location of the user's home directory
- `gecos`is set to general information about the user, for example the user's username and phone number
- `uidNumber`must be set to a unique user id (uid) number in Linux. Use the`getent passwd`command on Linux to see existing users and their uid's
- `gidNumber`must be set to the group id (gid) number updated previously
- `loginShell`is set to the default shell
- Run the following curl command to retrieve the user id's:

```

```

where:
- `token-string`is the OAuth access token that you obtained
- `identity-cloud-service-instance-url`is your IAM Instance URL

In the response, note the`id`of the user you want to update with POSIX attributes. For example, in the response below, the msmith user`id`is`e5438fce80374d539b8638c289036ecd`:
```

```

- Run the following curl command to update the user:

```

```

where:
- `token-string`is the OAuth access token that you obtained
- `identity-cloud-service-instance-url`is your IAM Instance URL
- `id`is the id for the user that you want to update with POSIX attributes

Note
