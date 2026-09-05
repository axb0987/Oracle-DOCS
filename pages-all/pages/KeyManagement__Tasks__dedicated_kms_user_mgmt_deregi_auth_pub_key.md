# Deregistering Authentication Public Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_deregi_auth_pub_key.htm
- Fetched: 2026-09-05 02:33 CDT

# Deregistering Authentication Public Key

Command to deregister public key.

Important  
  

Oracle Cloud Infrastructure (OCI) upgraded the firmware on our Dedicated Key Management Service (DKMS) Hardware Security Modules (HSMs), on September 15, 2025 . This upgrade introduced important security and platform improvements, but also included a change that might impact usage of specific DKMS API functions.

What's changing?

With the new firmware version, our HSM vendor has removed support for the following User Authentication Public Key (UserAuthPubKey) functions, which are deprecated in DKMS starting September 15, 2025.
- RegisterUserAuthPubKey
- DeregisterUserAuthPubKey
- SetUserAuthPubKey
- ListUserAuthPubKeys
- UpdateUserAuthPubKey
- ResetUserAuthPubKey

What's the impact?

This deprecation affects only the listed functions related to UserAuthPubKey. This update has no impact to existing customers using password-based authentication , which continue to be fully supported and operational.

What's the replacement?

With the new firmware, OCI DKMS offers mutual TLS (mTLS)-based authentication . This method offers enhanced security and scalability for customers managing user access through certificates.

What actions do you need to take?

If you're using any of the deprecated functions, we recommend switching to password-based authentication as a supported workaround. This method remains fully functional and requires no changes during the upgrade. If you need help applying this workaround or have concerns about compatibility, contact the OCI support team so we can factor your needs into the firmware migration schedule.

For customers not using these functions, no action is required .

The`deregisterUserAuthPubKeys`command deregisters a public key with the HSM and closes all existing E2E sessions authenticated with the deregistered key. After it's deregistered, a key can no longer be used to authorize a user to perform operations unless it's registered again.

In the User Management utility, open a command prompt and run`deregisterUserAuthPubKey`command to deregister a public key with the HSM and closes all existing sessions authenticated with the deregistered key. After it's deregistered, a key can no longer be used to authorize a user to perform operations unless it's registered again.

Syntax
```

```

Parameter Description
`keySlot Id`Key Index, you can get the key index using the command`listtUserAuthPubKeys.`
`Retain Session flag`

Maintain active E2E session(s) of current user (Optional)

1 - Retain active session(s) (Default).

2 - Terminate active session(s).

Example
```

```
