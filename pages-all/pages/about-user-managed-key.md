# About Master Encryption Key Management on Autonomous AI Database
- Source: https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-user-managed-key.html
- Fetched: 2026-09-05 18:58 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-user-managed-key.html#dcoc-content-body)

# About Master Encryption Key Management on Autonomous AI Database

Autonomous AI Database provides two options for Transparent Data Encryption (TDE) to encrypt your database: Oracle-managed encryption keys and Customer-managed encryption keys.

Autonomous AI Database uses Transparent Data Encryption, including a TDE master key and TDE tablespace keys to encrypt data in the database. As shown in the following figure, the TDE master key generates and encrypts/decrypts the TDE tablespace keys, and the TDE tablespace keys encrypt the data files.

[Description of the illustration adb_kms_keys.png](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/img_text/adb_kms_keys.html)

## Oracle-Managed Master Encryption Keys on Autonomous AI Database

By default, Autonomous AI Database uses Oracle-managed encryption keys.

Using Oracle-managed keys, Autonomous AI Database creates and manages the encryption keys that protect your data and Oracle handles rotation of the TDE master key.

## Customer-Managed Master Encryption Keys on Autonomous AI Database

With customer-managed master encryption keys, Autonomous AI Database uses the master encryption key in a customer-managed key vault to generate the TDE master key. If your organization’s security policies require customer-managed encryption keys, you can configure Autonomous AI Database to use a master encryption key in the following key management systems:
- 

Oracle Cloud Infrastructure (OCI) Vault

See[Manage Master Encryption Keys in OCI Vault](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/sec-manage-master-encryption-keys-oci-vault.html#GUID-D6862EFF-5FF4-4684-A562-603B0CC59B9B)for more information.
- 

Microsoft Azure Key Vault

See[Manage Master Encryption Keys in Azure Key Vault](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/encryption-keys-azure-key-vault.html#GUID-CB9BC7E3-6BAC-4792-A5F7-E152817E6BCF)for more information.
- 

Amazon Web Services (AWS) Key Management Service (KMS)

See[Manage Master Encryption Keys in AWS Key Management Service](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/encryption-keys-aws-key-service.html#GUID-ABD9D3F1-B24B-414A-A7FD-A0B87FC5C130)for more information.
- 

Oracle Key Vault (OKV)

See[Manage Master Encryption Keys in Oracle Key Vault](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/encryption-keys-oracle-key-vault.html#GUID-94948E1B-56F4-4775-BBB0-844311855FEE)for more information.

- [About Master Encryption Key Management on Autonomous AI Database](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-user-managed-key.html#GUID-F7FE0CAD-FE11-46DF-A14C-4A1E56DC5777)
- [Oracle-Managed Master Encryption Keys on Autonomous AI Database](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-user-managed-key.html#GUID-779A6140-5932-4271-8937-B0E8B47740E5)
- [Customer-Managed Master Encryption Keys on Autonomous AI Database](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-user-managed-key.html#GUID-2C0DE953-C04B-4F37-B1AA-203129C33634)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
