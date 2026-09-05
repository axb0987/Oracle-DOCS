# Getting a User Challenge
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_get_challenge.htm
- Fetched: 2026-09-05 02:33 CDT

# Getting a User Challenge

Learn how to get a user challenge with the Dedicated KMS user management utility.

The`getChallenge`command gets the random challenge and the signature from a partition. This challenge requires you to unlock CO user.

Note  
  
Before running the`getChallenge`command, you must create the`<ChallengeDirPath>`and`<SignatureDirPath>`directories.

In the User Management utility, open a command prompt and run`getChallenge`command to get random challenge and the signature from a partition. The challenge is required to unlock CO user.

Syntax

```

```

Parameter Description
`CO name`Name of the CO user to be unlocked.
`ChallengeDirPath`Directory to store the challenge returned by partition(s).
`SignatureDirPath`Directory to store the partition certificate signed challenge returned by partition(s).

Example
```

```
