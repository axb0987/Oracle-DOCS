# Dedicated KMS
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms.htm
- Fetched: 2026-09-05 02:32 CDT

# Dedicated KMS

This topic provides an overview of the OCI's Dedicated Key Management service.

The Dedicated Key Management service (DKMS) is a managed, highly available service that offers a single-tenant Hardware Security Module (HSM) partition. This gives you exclusive access to dedicated partitions within a physical, tamper-resistant HSM device to ensure that encryption keys are fully protected and isolated.

In Dedicated KMS, you cryptographically own your HSM partitions with full control over its key generation, storage, and usage. The HSM partitions are FIPS 140-2 Level 3 certified, offering the highest level of security for key management. To perform cryptographic operations, the service supports PKCS#11 standard to perform cryptographic operations without the need for any OCI APIs or modules. Dedicated KMS provides HSM clusters in all OCI regions that are are automatically synchronized and are highly available, with a 99.9% availability SLA.
Dedicated KMS offers the following:
- Provides greater access control by managing not only keys, but HSM partitions and administrative users directly.
- Heightened control gives you deeper visibility into cryptographic operations and lets you customize the HSM environment to your needs.
- The use of the PKCS#11 standard for direct interactions with the HSM lets you bypass OCI APIs for more streamlined and efficient cryptographic operations.

## Partition Responsibility

While Oracle ensures high availability for HSM partitions and keys within a region, customers are responsible for synchronizing users and keys across all replicas in an HSM cluster. Unavailability of users and keys in one or more replicas can impact the availability of customer applications, especially if the only partitions containing those users or keys become unavailable. See[Creating a User](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_create_users.htm)and[Generating Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicate_kms_key_mgmt_gen_keys.htm)in the Dedicated Key Management documentation for information on these operations.

## Supported Client SDKs
Use the following client SDKs to interact with keys in Dedicated KMS:
- PKCS#11: This standard specifies an API for managing keys and performing cryptographic operations in the hardware security module (HSM). See[PKCS #11 Library](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_pkcs_library.htm)for more information.
- Java Cryptography Extension (JCE): Dedicated KMS offers a JCE provider to perform cryptographic operations using the Java Development Kit (JDK). See[JCE Provider](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/dkms_jce_provider.htm)for more information.
- Windows CNG and KSP: OCI Dedicated Key Management supports[Cryptography API: Next Generation](https://learn.microsoft.com/windows/win32/seccng/cng-portal)(CNG) and Key Storage Providers (KSP) for Microsoft Windows applications. See[Windows Next Generation (CNG) and Key Storage Providers (KSP)](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_windows_cng_ksp.htm)for more information.

## Dedicated KMS Terms and Concepts

Term Description
HSM Cluster A cluster is a collection of individual HSM partitions that OCI KMS keeps in sync.
HSM Partition (Dedicated) A single-tenant secure cryptographic enclave within the HSM cluster which is fully isolated for your keys.
HSM Users An HMS user is distinct from IAM users. Unlike an IAM user, an HSM user will use the HSM credentials to access the user management utility to authenticate operations on the HSM because credentials takes place directly on the HSM.
CO Crypto Officer user who can perform user management operations on the HSM partition.
CU Crypto User who can perform key management and cryptographic operations on the key in an HSM partition.
