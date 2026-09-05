# Using Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys.htm
- Fetched: 2026-09-05 02:36 CDT

# Using Keys

Use the vault master encryption keys for cryptographic operations.

For information about managing keys, see[Managing Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys.htm). For information about exporting keys, see[Exporting Vault Keys and Key Versions](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/exportingkeys.htm). For information about managing the vaults in which you store keys, see[Managing Vaults](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults.htm).

See the following topics for information on using keys and performing cryptographic operations:
- [Retrieving the Public Key for an Asymmetric Master Encryption Key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_view_the_public_key_of_an_asymmetric_key.htm)
- [Generating a Data Encryption Key from a Master Encryption Key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_generate_a_data_encryption_key_from_your_Vault_master_encryption_key.htm)
- [Encrypting Data](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_encrypt_data_by_using_your_Vault_master_encryption_key.htm)
- [Decrypting Data](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_decrypt_data_by_using_your_Vault_master_encryption_key.htm)
- [Signing Data Using an Encryption Key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_sign_data_by_using_your_Vault_master_encryption_key.htm)
- [Verifying Signed Data Using an Encryption Key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_verify_signed_data_by_using_your_Vault_master_encryption_key.htm)

You can use either the CLI or API to perform cryptographic operations.

## Required IAM Policy

Caution  
  
Keys associated with volumes, buckets, file systems, clusters, and stream pools will not work unless you authorize Block Volume, Object Storage, File Storage, Kubernetes Engine, and Streaming to use keys on your behalf. Additionally, you must also authorize users to delegate key usage to these services in the first place. For more information, see[Let a user group delegate key usage in a compartment](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#os-bv-admins-use-key-id)and[Create a policy to enable encryption keys](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#services-use-key)in[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). Keys associated with databases will not work unless you authorize a dynamic group that includes all nodes in the DB system to manage keys in the tenancy. For more information, see[Required IAM Policy in Exadata Cloud Service](https://docs.oracle.com/iaas/exadatacloud/exacs/preparing-for-ecc-deployment.html#GUID-EA03F7BC-7D8E-4177-AFF4-615F71C390CD)

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: for typical policies that give access to vaults, keys, and secrets, see[Let security admins manage vaults, keys, and secrets](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#sec-admins-manage-vaults-keys). For more information about permissions or if you need to write more restrictive policies, see[Details for the Vault Service](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Monitoring Resources

You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)and[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm)
