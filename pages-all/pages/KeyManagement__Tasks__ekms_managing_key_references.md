# Managing Key References
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_managing_key_references.htm
- Fetched: 2026-09-05 02:34 CDT

# Managing Key References

Learn how to manage key references in OCI External Key Management to external encryption keys created in a third-party key management system.

When you create a key in the external key manager, the system generates a key ID (GUID). You can use key ID and key details (key type and shape) to create a key reference in the OCI KMS. When you create a key reference, KMS stores the key mapping details and not the actual key material.

When you temporarily restrict access to the external key manager either by disconnecting or disabling access to specific keys, it leads to a complete loss of key access on the OCI KMS side. The key state is retained until the access is restored. During this period, you can't decrypt the ciphertext that's encrypted using the KMS key. Also, the ciphertext that are encrypted using a KMS key in the external key store becomes unrecoverable. OCI KMS can't create, delete, or manage any keys in external key manager.

Creation of an Key reference in OCI doesn't create a key in the external key manager. Similarly, deletion of a key reference in OCI doesn't delete the external key. The key reference stores only the external key metadata located in the external key manager and OCI KMS uses the key reference for handling cryptographic operation requests.
Note  
  
Ensure the key is in "Active" state to perform AES encryption or decryption. Also, the External KMS functionality allows you to create only AES 256 bit key reference.
Following are the topics related to managing key references in External KMS:
- [Creating Key References](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_create_key_references.htm)
- [Renaming Key References](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_rename_key_references.htm)
- [Moving Key References](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_moving_key_references.htm)
- [Rotating Key References](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_rotating_key_references.htm)
- [Disabling Key References](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_disabling_key_references.htm)
- [Deleting Key References](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deleting_key_references.htm)
- [Cancelling Deletion of Key References](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_cancelling_key_reference_deletion.htm)
- [Creating Key Reference Version](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_creating_key_reference_version.htm)
