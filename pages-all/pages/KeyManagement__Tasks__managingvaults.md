# Managing Vaults
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults.htm
- Fetched: 2026-09-05 02:36 CDT

# Managing Vaults

Create and manage vaults as logical containers for encrypting keys and secrets.

For information specifically about backing up and restoring vaults, see[Backing Up and Restoring Vaults and Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys.htm). For information about configuring cross-region replication for vaults and keys, see[Replicating Vaults and Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/replicatingvaults.htm). For information about what you can do with keys, see[Managing Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys.htm). For information about what you can do with secrets in the Secret Management Service, see[Managing Secrets](https://docs.oracle.com/iaas/Content/secret-management/Concepts/manage-secrets.htm).

The Vault service lets you create vaults in your tenancy as containers for encryption keys and secrets. If needed, a virtual private vault provides you with a dedicated partition in a hardware security module (HSM), offering a level of storage isolation for encryption keys that's effectively equivalent to a virtual independent HSM.

Vault key management includes the following configurations:
- [Creating a vault](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm)
- [Viewing vault configuration details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_view_vault_configuration_details.htm)
- [Deleting a vault](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_delete_a_vault.htm)
- [Cancelling the deletion of a vault](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_cancel_the_deletion_of_a_vault.htm)
- [Moving a vault to a new compartment](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_move_a_vault_to_a_different_compartment.htm)

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.
Open the navigation menu, select Identity &amp; Security , and then select Vault ."

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Tagging Vaults

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Moving a Vault to a Different Compartment
