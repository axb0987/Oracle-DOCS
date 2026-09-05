# User Operations
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Reference/reference_dedicated_kms_user_mgmt_user_operations.htm
- Fetched: 2026-09-05 02:31 CDT

# User Operations

Configure user operations to perform user management operations.

The User Management utility lets you to perform user management operations.
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
