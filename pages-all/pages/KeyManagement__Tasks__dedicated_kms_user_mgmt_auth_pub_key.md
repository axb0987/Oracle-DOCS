# Registering Authentication Public Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_auth_pub_key.htm
- Fetched: 2026-09-05 02:33 CDT

# Registering Authentication Public Key

Command to register public key.

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

The`registerUserAuthPubKeys`command registers a public key with the HSM. A key can be registered without assigning it to a specific user.

In the User Management utility, open a command prompt and run`registerUserAuthPubKey`command to register a public key with the HSM. A key can be registered without assigning it to a specific user.

Syntax
```

```

Parameter Description
`PubKeyFilePath`Path to the file containing PEM encoded publick key.
`UserName`Username

Example
```

```
