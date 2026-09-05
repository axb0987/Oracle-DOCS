# Unlock a CO User
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_unlock_user.htm
- Fetched: 2026-09-05 02:33 CDT

# Unlock a CO User

Command to unlock CO user.

The`unlockCO`command lets you to unlock a user account that has exceeded the maximum number of login attempts. The command lets you can reset the login attempt count to zero. Note that if you try to unlock a user account that's not locked, the system displays an error.
Complete the following steps to unlock an CO user account:
- Get challenges of the locked user by using`getChallenge`command.
- Sign the challenge with Partition Owner key.
```

```

- Create a template file like below with the signature files paths.
```

```

Syntax
```

```

Parameter Description
`CO name`Name of the CO user to be unlocked
`TemplateFilePath`Path to template file which contains the signature file paths. Sample template file can be obtained running the command with non-existent file path.

Example
```

```
