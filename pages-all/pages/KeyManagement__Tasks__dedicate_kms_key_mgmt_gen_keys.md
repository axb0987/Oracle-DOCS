# Generating Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicate_kms_key_mgmt_gen_keys.htm
- Fetched: 2026-09-05 02:32 CDT

# Generating Keys

Learn how to generate keys with the Dedicated KMS user management utility.

As a Crypto User, you can use the commands in this topic to generate symmetric and asymmetric keys.
Important  
  
Ensure users are synchronized across all replicas before creating keys. Use the[listUsers](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/dedicated_kms_user_mgmt_listing_user.htm)command to verify user presence on all replicas. If users aren't synchronized, use the[syncUser](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/dedicated_kms_user_mgmt_sync_user.htm)command.
Symmetric keys:
- `genSymKey`
Asymmetric keys
- `genECCKeyPair`
- 

`genRSAKeyPair`
Note
