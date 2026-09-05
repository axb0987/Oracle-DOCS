# Managing Vault Encryption Keys for Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm
- Fetched: 2026-09-05 01:44 CDT

# Managing Vault Encryption Keys for Block Volume

Customer-managed keys are keys that are managed and made available using the Oracle Cloud Infrastructure Vault.

By default block volumes are encrypted using Oracle-managed keys. You have the option to use your own keys, managed by Vault. You can specify a customer-managed key when you create a volume. The volume's backups automatically use the specified key. You can specify a different key when you create a new volume by cloning a volume or restoring a volume from a volume backup.

## Tasks

- [Assigning a New Master Encryption Key](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/assign-encryption-key-new.htm)
- [Changing the Assigned Master Encryption Key](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/assign-encryption-key.htm)

For general instructions to assign master encryption keys, see[Assigning Master Encryption Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/assigningkeys.htm).

## Rotating the Encryption Key

Rotating the same key isn't supported today and the behavior isn't defined when you have multiple versions of a key. Block Volume supports keys with a single version only. To rotate an encryption key, change the volume's encryption key to a new key. You can also change the encryption key for a volume backup.

When you rotate the key for a volume by specifying a new encryption key, any child resources created before you updated the key continue to use the old encryption key. Such child resources include backups and clones.

## Volume Backup Encryption Keys

The Oracle Cloud Infrastructure Vault service enables you to bring and manage your own keys to use for encrypting volumes and their backups. When you create a volume backup, the encryption key used for the volume is also used for the volume backup.

For instructions and requirements related to changing the assigned key, see[Changing the Assigned Master Encryption Key](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/assign-encryption-key.htm).

See also[Block Volume Encryption](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeencryption.htm)and[Volume Group Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups_topic-Volume_Group_Backups.htm)
