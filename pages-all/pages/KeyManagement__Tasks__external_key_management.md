# External Key Management Service
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/external_key_management.htm
- Fetched: 2026-09-05 02:35 CDT

# External Key Management Service

With Oracle Cloud Infrastructure External Key Management Service (EKMS) you can create and manage encryption keys that are hosted outside of OCI. EKMS integrates with supported third-party key management systems to perform cryptographic operations without importing key material into OCI.

OCI's native Key Management Service (KMS) uses a hardware security module (HSM) hosted within the Oracle data center for storing and managing master keys for encrypting data at rest. For enhanced data security, and for customers who have regulatory compliance rules that require storing keys in an key management platform located outside of OCI, KMS offers the External Key Management Service (External KMS), a service that integrates your OCI tenancy with a third-party key management platform hosted outside of OCI.

In External KMS, you can store and control master encryption keys (as external keys) in the third-party key management system. You can then use these keys for encrypting your data in Oracle. You can disable your keys anytime. With the actual keys residing in the third-party key management system, you create and store only key references (metadata associated with the key material) in OCI.

## Benefits

EKMS offers the following benefits:
- Key provenance: You create and manage the usage of externally created keys in your external key management platform. The external keys are never cached or stored anywhere in OCI, and OCI KMS doesn't have any control over your keys. Instead, OCI KMS interacts directly with the third-party key management system for cryptographic (encrypt and decrypt) operations.
- Enhanced security: EKMS protects data at rest with maximum security using a third-party key management system
- Centralized key management: Managing your keys in a third-party key management system let you management in a single location encryption keys that you use OCI and elsewhere.

## Use Cases

EKMS can be a part of overall data security in the following use cases:
- Banks and public sector organizations who have compliance regulations might need to store encryption keys on-premises, physically separated from data stored in OCI.
- Banking customers that have security regulations requiring that they perform cryptographic operations in their on-premises HSM can use EKMS to satisfy this requirement.
- Customers who use more than one cloud provider (for example, Oracle's[multicloud](https://docs.oracle.com/iaas/Content/multicloud/Oraclemulticloud.htm)customers) might require databases in OCI to connect with encryption services located in a different cloud. EKMS makes these types of integrations possible.

## Terminology

Familiarize the following terminologies to understand External Key Management (EKMS) functionality:

Terminology Description
External Key Manager An HSM owned and hosted by the customer, or a key management platform that resides outside of OCI. This is also referred to as a third-party key management system.
External Vault A vault created in the third-party key management system that's used for storing keys externally.
External key Keys created in the third-party key management system that contain one or more external key versions.
External key versions Each external key is automatically assigned a key version. When you rotate an external key, the external key manager generates a new key version.
FastConnect FastConnect is a way to create a private connection between the customer premises and Oracle Cloud Infrastructure (OCI).
Private endpoint (PE) A private endpoint is a private IP address within the customer's VCN that can be used to access a service within OCI.
Data encryption key (DEK) An encryption key whose function is to encrypt and decrypt data.

## Supported Services

External Key Management can be used with the following OCI services:

Service Notes
[Block Volume](https://docs.oracle.com/iaas/Content/Block/home.htm)
Compute Supports[boot volume](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm)encryption, and encryption of other storage types listed in this table.
[File Storage](https://docs.oracle.com/iaas/Content/File/home.htm)
[Kubernetes Engine (OKE)](https://docs.oracle.com/iaas/Content/ContEng/home.htm)
[Object Storage](https://docs.oracle.com/iaas/Content/Object/home.htm)
[Oracle Autonomous AI Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/index.html)
[Oracle Autonomous AI Database Serverless](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-intro-adb.html)
[Oracle Base Database](https://docs.oracle.com/en/cloud/paas/base-database/index.html)
[Oracle Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/index.html)
[Streaming](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm)
