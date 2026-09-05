# Assigning Master Encryption Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys.htm
- Fetched: 2026-09-05 02:31 CDT

# Assigning Master Encryption Keys

Assign master encryption keys to supported resources and remove them when they are not needed anymore.

Instead of using an encryption key that Oracle manages, you can assign master encryption keys that you manage to block or boot volumes, databases, file systems, buckets, and stream pools. Block Volume, Database, File Storage, Object Storage, and Streaming use the keys to decrypt the data encryption keys that protect the data that is stored by each respective service. By default, these services rely on Oracle-managed master encryption keys for cryptographic operations. When you remove a Vault master encryption key assignment from a resource, the service returns to using an Oracle-managed key for cryptography.

You can also assign master encryption keys to clusters that you create using Kubernetes Engine to encrypt Kubernetes secrets at rest in the etcd key-value store.

Assigning keys include the following configurations:
- [Creating a Compute Instance with an Encrypted Boot Volume](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_Compute_instance_with_an_encrypted_boot_volume.htm)
- [Creating a Boot Volume Encrypted with a Vault key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_boot_volume_thats_encrypted_with_a_Vault_key.htm)
- [Creating a Kubernetes Cluster with Encrypted Secrets](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_Kubernetes_cluster_with_encrypted_secrets_in_the_etcd_keyvalue_store.htm)
- [Assigning a Key to an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_Object_Storage_bucket.htm#cli)
- [Assigning a key to a stream pool](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_stream_pool.htm)
- [Assigning a Key to a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_boot_volume.htm)
- [Assigning a key to a file system](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_file_system.htm)
- [Assigning a Key to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_Block_Volume.htm)
- [Editing a Key to a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_boot_volume.htm#assignkeyexistingbootvolume_cli)
- [Editing a Key to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Block_Volume.htm#assignkeyexistingblockvolume_cli)
- [Removing a Key Assignment from a Block Volume](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_remove_a_key_assignment_from_a_Block_Volume.htm)
- [Removing a Key Assignment from a Object Storage](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_remove_a_key_assignment_from_a_bucket.htm#unassignkeybucket_cli)

For information about managing the creation and usage of master encryption keys and key versions, see[Managing Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys.htm). For information specifically about creating keys with your own key material, see[Importing Vault Keys and Key Versions](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys.htm). For information about how you can use keys in cryptographic operations, see[Using Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys.htm). For information about what you can do with vaults where you store keys, see[Managing Vaults](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults.htm).

## Required IAM Policy

Caution  
  
Keys associated with volumes, buckets, file systems, clusters, and stream pools will not work unless you authorize Block Volume, Object Storage, File Storage, Kubernetes Engine, and Streaming to use keys on your behalf. Additionally, you must also authorize users to delegate key usage to these services in the first place. For more information, see[Let a user group delegate key usage in a compartment](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#os-bv-admins-use-key-id)and[Create a policy to enable encryption keys](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#services-use-key)in[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). Keys associated with databases will not work unless you authorize a dynamic group that includes all nodes in the DB system to manage keys in the tenancy. For more information, see[Required IAM Policy in Exadata Cloud Service](https://docs.oracle.com/iaas/exadatacloud/exacs/preparing-for-ecc-deployment.html#GUID-EA03F7BC-7D8E-4177-AFF4-615F71C390CD)

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: for typical policies that give access to vaults, keys, and secrets, see[Let security admins manage vaults, keys, and secrets](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#sec-admins-manage-vaults-keys). For more information about permissions or if you need to write more restrictive policies, see[Details for the Vault Service](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)
