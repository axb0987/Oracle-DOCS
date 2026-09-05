# Creating a User with POSIX Attributes and Add to Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/create-user-posix-attributes-and-add-group.htm
- Fetched: 2026-09-05 02:23 CDT

# Creating a User with POSIX Attributes and Add to Group

Create a user with POSIX attributes and add the user to the group previously created.

- Create a`user.json`file with the following request body:

`user.json`
```

```

where:
- `userName`is set to the username of the user that you want to create
- `homeDirectory`is set to the location of the user's home directory
- `loginShell`is set to the default shell
- `gecos`is set to general information about the user, for example the user's username and phone number
- `uidNumber`must be set to a unique user id (uid) number in Linux. Use the`getent passwd`command on Linux to see existing users and their uid's
- `gidNumber`must be set to the group id (gid) number created previously
- Run the following curl command to create the user and add it to the group:

`user.json`
```

```

where:
- `token-string`is the OAuth access token that you obtained
- `identity-cloud-service-instance-url`is your IAM Instance URL

Note  
  
You can't create a user with POSIX attributes using the Console.
