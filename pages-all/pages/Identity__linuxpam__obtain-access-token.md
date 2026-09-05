# Obtaining an Access Token
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/obtain-access-token.htm
- Fetched: 2026-09-05 02:23 CDT

# Obtaining an Access Token

Obtain an access token with Identity Domain Administrator or User Administrator privileges. This allows you to create groups and users with POSIX attributes, or add POSIX attributes to existing groups and users.

In the Linux environment, run the following command:

```

```

where:
- `client-id`is the client ID of a confidential application with Identity Domain Administrator or User Administrator privileges
- `client-secret`is the client secret of a confidential application with administrative privileges
- `identity-cloud-service-instance-url`is your IAM Instance URL
Note  
  

The PAM confidential application`client-id`and`client-secret`are used by the PAM client library to create both groups or POSIX groups.
To create a POSIX group, use the following endpoint with an admin access token.
```

```
