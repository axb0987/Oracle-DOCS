# Managing Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys.htm
- Fetched: 2026-09-05 02:35 CDT

# Managing Keys

Create and manage vault keys and key versions.

For information about creating vault keys with your own key material, see[Importing Vault Keys and Key Versions](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys.htm). For information about assigning keys to protect supported resources, see[Assigning Master Encryption Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys.htm). For information about how you can use keys in cryptographic operations, see[Using Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys.htm). For information about backing up and restoring keys, see[Backing Up and Restoring Vaults and Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys.htm). For information about what you can do with vaults where you store keys, see[Managing Vaults](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults.htm). For more information, see[Vault and Key Management Concepts](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/keyoverview.htm#concepts).

Managing vault keys include the following configurations:
- [Create a key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm)
- [View key details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_key_details.htm)
- [View a list of keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm)
- [View a list of key versions for a specific key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_key_versions.htm)
- [Enable keys for use in vault cryptographic operations](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_enable_a_key.htm)
- [Rotate keys to generate vault cryptographic material](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_rotate_a_master_encryption_key.htm)
- [Disable keys to prevent their usage in vault cryptographic operations](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_disable_a_key.htm)
- [Delete keys to permanently prevent their usage in vault cryptographic operations or assignment to resources](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_delete_a_key.htm)
- [Move a key to a new compartment](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_move_a_key_to_a_different_compartment.htm)

Note  
  
For enhanced control and visibility over your vault encryption keys, the External Key Management (EKM) feature in Vault enables you to manage your keys in a third-party key management system outside of Oracle cloud. To enable EKM in your tenancy, contact Oracle sales.

## Required IAM Policy

Open the navigation menu, select Identity &amp; Security , and then select Vault ."

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Tagging Keys

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Monitoring Resources

This section describes how to monitor your Vault resources.

You can monitor your vault resources.

## Moving Resources to a Different Compartment

Learn how to move Vault resources such as keys to different compartment.

You can move keys from one compartment to another. After you move a key to a new compartment, inherent policies apply immediately and affect access to the key and key versions. Moving a key doesn't affect access to the vault that a key is associated with. Similarly, you can move a vault from one compartment to another independently of moving any of its keys. For more information, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm)
