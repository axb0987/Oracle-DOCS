# Verifying Endpoints
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/verify-endpoints.htm
- Fetched: 2026-09-05 02:23 CDT

# Verifying Endpoints

Verify that you can view users and groups and their POSIX attributes.

- Obtain a POSIX access token by running the following curl command:

```

```

where:
- `client-id`is the client ID for the POSIX confidential application
- `client-secret`is the client secret for the POSIX confidential application
- `identity-cloud-service-instance-url`is your IAM Instance URL
- Run the following curl command to view users with POSIX attributes:

```

```

where:
- `token-string`is the OAuth POSIX access token that you obtained
- `identity-cloud-service-instance-url`is your IAM Instance URL

An example response is as follows:

`GET HOST/admin/v1/Users`
```

```

- Run the following curl command to view groups with POSIX attributes:

```

```

where:
- `token-string`is the OAuth POSIX access token that you obtained
- `identity-cloud-service-instance-url`is your IAM URL

An example response is as follows:

`GET HOST/admin/v1/Groups`
```

```
