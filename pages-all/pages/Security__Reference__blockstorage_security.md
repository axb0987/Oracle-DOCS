# Securing Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/blockstorage_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Block Volume

This topic provides security information and recommendations for Block Volume.

The[Block Volume](https://docs.oracle.com/iaas/Content/Block/home.htm)service lets you dynamically provision and manage block storage volumes . You can create, attach, connect, and move volumes, as well as change volume performance, as needed, to meet your storage, performance, and application requirements. After you attach and connect a volume to an instance, you can use the volume like a regular hard drive. You can also disconnect a volume and attach it to another instance without the loss of data.

## Security Responsibilities

To use Block Volume securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Encryption and Confidentiality: Use encryption keys and secrets to protect your data and connect to secured resources. Rotate these keys regularly.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Block Volume in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/blockstorage_security.htm#iam-policies)
Encrypt resources using a custom key[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/blockstorage_security.htm#data-encryption)
Enable and configure Cloud Guard (optional)[Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/blockstorage_security.htm#cloud-guard)
Create a security zone (optional)[Security Zones](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/blockstorage_security.htm#security-zones)

## Routine Security Tasks

After getting started with Block Volume use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Rotate encryption keys[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/blockstorage_security.htm#data-encryption)
Respond to problems detected in Cloud Guard[Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/blockstorage_security.htm#cloud-guard)
Take regular backups[Data Durability](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/blockstorage_security.htm#durability)
Perform a security audit[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/blockstorage_security.htm#auditing)

## IAM Policies

Use policies to limit access to Block Volume.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to tenancy and compartment administrators.

Oracle Cloud Infrastructure supports two types of volumes: block volumes and boot volumes. Block volumes allow instance storage capacity to be expanded dynamically. A boot volume contains the image used to boot the compute instance. The IAM service groups the family of related volume resource types into a combined resource type called`volume-family`.

Assign least privilege access for IAM users and groups to resource types in`volume-family`. The resource types in`volume-family`are`volumes`,`volume-attachments`, and`volume-backups`.
- The`volumes`resources are detachable block volume devices that allow dynamic expansion of instance storage capacity or contain the image for booting the instance.
- The`volume-attachments`resources are attachments between volumes and instances.
- The`volume-backups`resources are point-in-time copies of volumes that can be used to create block volumes or recover block volumes.

[Prevent Deletion of Volumes](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/blockstorage_security.htm#)

The following example policy allows group`VolumeUsers`to perform all actions on volumes and backups, except deleting them.

```

```

If`VolumeUsers`can't detach volumes from instances, you can add the following policy to the previous example.

```

```

For more information about Block Volume policies and to view more examples, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

## Cloud Guard

Enable Cloud Guard and use it to detect and respond to security issues in Block Volume.

Upon detecting a problem, Cloud Guard suggests corrective actions. You can also configure Cloud Guard to automatically take certain actions. Cloud Guard includes the following detector rules for Block Volume.
- Block Volume is encrypted with Oracle-managed key
- Block Volume is not attached

For a list of all available detector rules in Cloud Guard, see[Detector Recipe Reference](https://docs.oracle.com/iaas/Content/cloud-guard/using/detect-recipes.htm).

If you haven't done so already, enable Cloud Guard and configure it to monitor the compartments that contain your resources. You can configure Cloud Guard targets to examine your entire tenancy (root compartment and all subcompartments), or to check only specific compartments. See[Getting Started with Cloud Guard](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-start.htm).

After enabling Cloud Guard, you can view and resolve detected security problems. See[Processing Reported Problems](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-problems.htm).

## Security Zones

Using Security Zones ensures your resources in Block Volume comply with security best practices.

A security zone is associated with one or more compartments and a security zone recipe. When you create and update resources in a security zone's compartment, Oracle Cloud Infrastructure validates these operations against the list of security zone policies in the recipe. If any policy in the recipe is violated, then the operation is denied. The following security zone policies are available for resources in Block Volume.
- `deny block_volume_not_in_security_​zone_attach_to_instance_​in_security_zone`
- `deny block_volume_in_security_​zone_attach_to_instance_​not_in_security_zone`
- `deny boot_volume_not_in_security_​zone_attach_to_instance_​in_security_zone`
- `deny boot_volume_in_security_​zone_attach_to_instance_​not_in_security_zone`
- `deny attached_block_volume_not_​in_security_zone_move_to_​compartment_in_security_zone`
- `deny attached_boot_volume_not_in_​security_zone_move_to_​compartment_in_security_zone`
- `deny block_volume_without_​vault_key`
- `deny boot_volume_without_​vault_key`

For a list of all security zone policies, see[Security Zone Policies](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm).

To move existing resources to a compartment that is in a security zone, the resources must comply with all security zone policies in the zone's recipe. Similarly, resources in a security zone can't be moved to a compartment outside of the security zone because it might be less secure. See[Managing Security Zones](https://docs.oracle.com/iaas/Content/security-zone/using/managing-security-zones.htm).

## Data Encryption

The Block Volume service always encrypts all block volumes, boot volumes, and volume backups at rest by using the Advanced Encryption Standard (AES) algorithm with 256-bit encryption. You can use an Oracle-provided encryption key or a custom key in the Vault service. You can also encrypt your data volumes using tools like`dm-crypt`,`veracrypt`, and Bit-Locker.

By default all volumes and their backups are encrypted using the Oracle-provided encryption keys. Each time a volume is cloned or restored from a backup the volume is assigned a new unique encryption key.

### Encrypting Volumes with the Vault Service

Although default encryption keys can be generated automatically when you create certain Oracle Cloud Infrastructure resources, we recommend that you create and manage your own custom encryption keys in the Vault service.

A vault is a logical entity that stores the encryption keys you use to protect your data. Depending on the protection mode, keys are either stored on the server, or they are stored on highly available and durable hardware security modules (HSMs). Our HSMs meet Federal Information Processing Standards (FIPS) 140-2 Security Level 3 security certification. See[Managing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm)and[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

Create and rotate encryption keys in the Vault service to protect your resources in Block Volume. See[Creating a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/creatingavolume.htm)and[Assigning a Key to a Block Volume](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_Block_Volume.htm).

Each master encryption key is automatically assigned a key version. When you rotate a key, the Vault service generates a new key version. Periodically rotating keys limits the amount of data encrypted or signed by one key version. If a key is ever comprised, key rotation reduces the risk to your data. See[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

We recommend that you use IAM policies to strictly limit the creation, rotation, and deletion of encryption keys. See[Details for the Vault Service](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

### Encrypting Non-root Volumes with dm-crypt

`dm-crypt`is a kernel-level encryption mechanism (part of Linux`devicemapper`framework) to provide encrypted volumes. It encrypts data passed from the filesystem (for example,`ext4`and NTFS), and stores it on a storage device in Linux Unified Key Setup (LUKS) format.

The encrypted volumes can be stored on a complete disk, disk partition, logical volume, or a file-backed storage created using loopback devices.`Cryptsetup`is the user-level utility used to manage`dm-crypt`, and used to encrypt partitions and files.`dm-crypt`uses the Linux`crypto`APIs for encryption routines.

- Attach block storage volume to an instance (for example,`/dev/sdb`)
- Format`/dev/sdb`for LUKS encryption. Enter LUKS passphrase when prompted. The passphrase is used to encrypt the LUKS master key used for encrypting the volume.

```

```

- Verify that the LUKS formatting is successful.

```

```

- Get encryption information about the device.

```

```

- Get LUKS UUID of the device. The UUID value is used to configure the`/etc/crypttab`.

```

```

- Create a LUKS container with device name,`dev_name`. This command also creates a device node,`/dev/mapper/<dev_name>`.

```

```

- Get information about the mapped device.

```

```

- Format the device node as`ext4`filesystem.

```

```

- Mount the device node.

```

```

- Add an entry to`/etc/crypttab`.

```

```

All the files copied to`/home/encrypt_fs`are LUKS encrypts them.
- Add a keyfile to an available keyslot of the encrypted volume. This keyfile can be used to access the encrypted volume.

```

```

- Verify the encryption status of files.

```

```

- Unmount after you're finished.

```

```

If you need to access the encrypted volume:
```

```

If you lose the keyfile, or if the keyfile or passphrase gets corrupted, you can't decrypt the encrypted volume. The result is a permanent loss of data. We recommend that you store durable copies of the keyfile on an on-premises host.

### Remotely Mounting Data Volumes Encrypted with dm-crypt

The following steps assume that the keyfile is on an on-premises host (`SRC_IP`) and that`<OCI_SSH_KEY>`is the SSH private key of the instance.

- Copy keyfile from the on-premises host to an instance.

```

```

- Open the encrypted volume.

```

```

- Mount the volume.

```

```

- Perform operations on data in the mounted volume.
- Unmount the encrypted volume.

```

```

- Delete the keyfile from the instance.

```

```

## Data Durability

Take regular backups of your data in Block Volume. We recommend that you give a minimum set of users and groups permission to delete backups.

To minimize loss of data caused by deletes or corruption, we recommend that you make periodic backups of volumes. Oracle Cloud Infrastructure allows automated scheduled backups. For more information about scheduled backups, see[Policy-Based Backups](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).

To minimize loss of data caused by inadvertent deletes by an authorized user or by malicious deletes, we recommend that you grant`VOLUME_DELETE`,`VOLUME_ATTACHMENT_DELETE`, and`VOLUME_BACKUP_DELETE`permissions to a minimum possible set of IAM users and groups. Grant`DELETE`permissions only to tenancy and compartment administrators.

## Auditing

Locate access logs and other security data for Block Volume.

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm).

[Example Audit Log](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/blockstorage_security.htm#)

```

```

If you enabled Cloud Guard in your tenancy, then it reports any user activities that are potential security concerns. Upon detecting a problem, Cloud Guard suggests corrective actions. You can also configure Cloud Guard to automatically take certain actions. See[Getting Started with Cloud Guard](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-start.htm)and[Processing Reported Problems](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-problems.htm)
