# Block Volume Encryption
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeencryption.htm
- Fetched: 2026-09-05 01:44 CDT

# Block Volume Encryption

The Block Volume service always encrypts all block volumes, boot volumes, and volume backups at rest by using the Advanced Encryption Standard (AES) algorithm with 256-bit encryption. By default all volumes and their backups are encrypted using the Oracle-provided encryption keys. Each time a volume is cloned or restored from a backup the volume is assigned a new unique encryption key.
Important  
  
The Block Volume service doesn't support encrypting volumes with keys encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When using your own keys, you must use keys encrypted using the Advanced Encryption Standard (AES) algorithm. This applies to block volumes and boot volumes.

Block Volume uses envelope encryption to encrypt the data. With envelope encryption, data is encrypted using a unique generated data encryption key (DEK) and then the data encryption key is encrypted using the customer-managed key. The data encryption key is unique for each volume.

By default,[Oracle-provided encryption keys](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeencryption.htm#top__oraclekeys)are used for encryption. You have the option to override or specify[customer-managed keys](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeencryption.htm#top__customerkeys)stored in the[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)service. Block Volume uses the encryption key configured for the volume for both at-rest and in-transit encryption.

If you don't specify a customer-managed key, or you later unassign a key from the volume, then the Block Volume service uses the Oracle-provided encryption key instead. This situation applies to both encryption at-rest and paravirtualized in-transit encryption.

To use your own key for new volumes, see[Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/creatingavolume.htm). To change keys, see[Changing the Assigned Master Encryption Key](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/assign-encryption-key.htm)and[Editing a Key to a Block Volume](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Block_Volume.htm).

No option exists for unencrypted volumes at-rest. Encryption at-rest doesn't impact the performance of the volume and doesn't incur extra cost. Block Volume also provides[in-transit encryption](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeencryption.htm#top__intransit). In-transit encryption for block volumes attached to VMs is optional, and you can enable or disable it as needed for these volumes. In-transit encryption for bare metal instances is supported and enabled and you can't disable it for the following shapes:
- 

BM.Standard.E3.128
- 

BM.Standard.E4.128
- 

BM.DenseIO.E4.128

To confirm support for other Linux-based custom images and for more information, contact[Oracle support](https://support.oracle.com/).

## Oracle-Provided Keys

An Oracle-provided key is the default encryption scheme, using keys managed internally by Oracle. No action is needed to use these keys. If you don't specify a customer-managed key, your Block Volume resources are encrypted using Oracle-managed keys. The service rotates the keys periodically.

## Customer-Managed Keys

You can use customer-managed keys, which are your own keys stored with the[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)service. You can import external keys to the Vault service or use the service to generate new keys. Using customer-managed keys to encrypt data incurs no extra cost or performance impact. For more information, see[Managing Vault Encryption Keys for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm).

## Custom Encryption

You can opt to perform your own custom encryption at the operating system level using third-party software such as devicemapper crypt (`dm-crypt`), BitLocker Drive Encryption, and so on. This encryption is in addition to the standard encryption provided by Oracle for volumes. This means that volumes are double encrypted, first by the software at the operating system level, and then by Oracle using Oracle managed keys.

When you use a custom encryption mode, you incur no extra cost, but you could see a degradation in overall performance of the volume. This encryption uses host CPU cycles, and the volume performance depends on the actual shape of the Compute instance.

## In-transit Encryption
Important  
  

- In-transit encryption for boot and block volumes is only available for virtual machine (VM) instances launched from platform images, along with bare metal instances that use the following shapes: BM.Standard.E3.128, BM.Standard.E4.128, BM.DenseIO.E4.128. It is not supported on other bare metal instances. To confirm support for certain Linux-based custom images and for more information,[contact Oracle support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
- 

For bare metal instances that support in-transit encryption, including instances launched from custom images, it is always enabled by default. This applies to both boot volumes and block volumes. The following bare metal shapes support in-transit encryption for the instance's boot volume and iSCSI-attached block volumes:
- BM.Standard.E3.128
- BM.Standard.E4.128
- BM.DenseIO.E4.128

All the data moving between the instance and the block volume is transferred over an internal and highly secure network. If you have specific compliance requirements related to the encryption of the data while it is moving between the instance and the block volume, the Block Volume service provides the option to enable in-transit encryption for paravirtualized volume attachments on virtual machine (VM) instances.

In-transit encryption for bare metal instances isn't supported for US Government Cloud regions.

In-transit encryption isn't enabled for these shapes in the following scenarios:
- Boot volumes for instances launched June 8, 2021 or earlier.
- Volumes attached to the instance June 8, 2021 or earlier

To enable in-transit encryption for the volumes in these scenarios, you need to detach the volume from the instance and then reattach it.

## Cross Security Compartment Key Access

As a best practice, CIS Oracle Cloud Infrastructure Foundations Benchmark recommends that you create a vault for your customer-managed keys in a separate compartment and restrict access to this compartment. The following diagram shows how to organize this.

The following policies are required to use the keys in a separate security compartment with restricted access to encrypt boot volumes, block volumes, and related resources.
```

```
