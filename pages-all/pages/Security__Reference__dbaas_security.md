# Securing Database
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/dbaas_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Database

## Security Recommendations

This section lists security recommendations for managing Oracle Cloud Infrastructure Database instances. Recommendations for securely configuring Oracle databases are available in the Oracle Database Security Guide. In this documentation, "database system" refers to Oracle Database deployments using[Base Database](https://docs.oracle.com/en/cloud/paas/base-database/index.html)service,[Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/index.html), and[Autonomous AI Database on dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/index.html). (Note that some topics may not be applicable to Autonomous AI Database in situations where Oracle manages the functionality described.)

## Database Access Control
- Users authenticate to the database using their password. We recommend that these passwords be strong. For guidelines on choosing Oracle database passwords, see[Guidelines for Securing Passwords](https://docs.oracle.com/cd/E11882_01/network.112/e36292/guidelines.htm#DBSEG10005). In addition, Oracle database provides a PL/SQL script to verify database password complexity. This script is located at`$ORACLE_HOME/rdbms/admin/UTLPWDMG.SQL`. For instructions on running UTLPWDMG.SQL script to verify password complexity, see[Enforcing Password Complexity Verification](https://docs.oracle.com/cd/B28359_01/network.111/b28531/authentication.htm#i1007341).
- In addition to the database password, you can use VCN network security groups or security lists to enforce network access control to database instances. We recommend that you configure VCN network security groups or security lists to allow least privilege access to customer databases in Oracle Cloud Infrastructure Database.
- 

Database systems created within a public subnet can send outbound traffic directly to the Internet. Database systems created within a private subnet don't have internet connectivity, and internet traffic (both egress and ingress) can't reach the instance directly. If you try to define a route to a Database system within a private subnet using an internet gateway, the route is ignored.

To perform OS patching and backup for a database system on private subnet, you can use a service gateway or a NAT gateway to connect to your patching or backup endpoints.

In an virtual cloud network (VCN), you can use security rules along with a private subnet to restrict access to a database system. In multi-tier deployments, a private subnet and VCN security rules can be used to restrict access to the database system from the application tiers.

## Data Durability
- We recommend that you give database delete permissions (`DATABASE_DELETE`,`DB_SYSTEM_DELETE`) to a minimum possible set of IAM users and groups. This minimizes loss of data because of inadvertent deletes by an authorized user or because of malicious deletes. Only give`DELETE`permissions to tenancy and compartment administrators.
- You can use RMAN to do periodic backups of Database databases, where encrypted backup copies are stored in local storage (block volumes, for example) or Oracle Cloud Infrastructure Object Storage. RMAN encrypts each backup of a database with a unique encryption key. In transparent mode, the encryption key is stored in the Oracle Wallet. RMAN backups to Object Storage require internet gateway (IGW), and VCN network security groups or security lists need to be configured to allow secure access to Object Storage. For information about setting up the VCN for backing up bare metal databases, see[Back Up a Database to Object Storage Using RMAN](https://docs.oracle.com/en/cloud/paas/bm-and-vm-dbs-cloud/dbbackuprman/index.html#articletitle). For information about backing up and Exadata databases, see[Managing Exadata Database Backups by Using bkup_api](https://docs.oracle.com/iaas/exadatacloud/exacs/ecs-managing-db-backup-and-recovery.html#GUID-C3242075-DDC9-4741-BB41-B22E78466A7B).

## Database Encryption and Key Management
- 

All databases created in Oracle Cloud Infrastructure are encrypted using transparent data encryption (TDE). Note that if you migrate an unencrypted database from on-premise to Oracle Cloud Infrastructure using RMAN, the migrated database will not be encrypted. Oracle requires encrypting such databases after migrating them to the cloud.

To learn how to encrypt your database with minimum downtime during migration, see the Oracle Maximum Availability Architecture white paper[Converting to Transparent Data Encryption with Oracle Data Guard using Fast Offline Conversion](https://www.oracle.com/technetwork/database/availability/tde-conversion-dg-3045460.pdf).

Note that virtual machine DB systems use Oracle Cloud Infrastructure block storage instead of local storage. Block storage is encrypted by default.
- User-created tablespaces are encrypted by default in Oracle Cloud Infrastructure Database. In these databases,`ENCRYPT_NEW_TABLESPACES`parameter is set to`CLOUD_ONLY`where tablespaces created in a Database Cloud Service (DBCS) database are transparently encrypted with the AES128 algorithm unless a different algorithm is specified.
- The Database administrator creates a local Oracle Wallet on a newly created database instance, and initializes the Transparent Data Encryption (TDE) master key. Then the Oracle Wallet is configured to be "auto-open". However, a customer can choose to set a password for the Oracle Wallet, and We recommend that you set a strong password (eight characters or more, with at least one capital letter, one small letter, one number, and one special symbol).
- We recommend that you periodically rotate the TDE master key. The recommended rotation period is 90 days or less. You can rotate the TDE master key by using native database commands ("administer key management" in 12c, for example) or dbaascli. All previous versions of TDE master key are maintained in the Oracle Wallet.
- Oracle Key Vault (OKV) is a key management appliance used for managing Oracle TDE master keys. OKV can store, rotate, and audit accesses to TDE master keys. For instructions about installing and configuring OKV in Oracle Cloud Infrastructure, see[Managing Oracle Database Encryption Keys in Oracle Cloud Infrastructure with Oracle Key Vault.](https://cloud.oracle.com/iaas/whitepapers/manage-encryption-keys-oci-okv.pdf)

## Database Patching

Applying Oracle database security patches (Oracle Critical Patch Updates) is imperative to mitigate known security issues, and We recommend that you keep patches up-to-date. Patchsets and Patch Set Updates (PSUs) are released on a quarterly basis. These patch releases contain security fixes and additional high-impact/low-risk critical bug fixes.

For information about the latest known security issues and available fixes, see[Critical Patch Updates, Security Alerts and Bulletins](https://www.oracle.com/technetwork/topics/security/alerts-086861.html#CriticalPatchUpdates). If your application doesn't support the latest patches and needs to use a database system with older patches, you can provision a database system with an older version of the Oracle Database edition you're using. In addition to reviewing the critical patch updates and security alerts for your Oracle Database, We recommend that you analyze and patch the OS provisioned with the database system.

For information about applying patches to Oracle Cloud Infrastructure Database instances, see[Update a DB System](https://docs.oracle.com/iaas/Content/Security/Reference/dbaas_security.htm)and[Patching Oracle Grid Infrastructure and Oracle Databases Using dbaascli](https://docs.oracle.com/iaas/exadatacloud/exacs/ecs-using-dbaascli.html#GUID-D92CAF95-43E0-4CFC-8C16-198D5A643CFC).

## Database Security Configuration Checking
- The[Oracle Database Security Assessment Tool](http://www.oracle.com/technetwork/database/security/dbsat/overview/index.html)(DBSAT) provides automated security configuration checks of Oracle databases in Oracle Cloud Infrastructure. DBSAT performs security checks for user privilege analysis, database authorization controls, auditing polices, database listener configuration, OS file permissions, and sensitive data stored. Oracle database images in Oracle Cloud Infrastructure Database are scanned with DBSAT before provisioning. After provisioning, We recommend that you periodically scan databases with DBSAT, and remediate any issues found. DBSAT is available free of charge to Oracle customers.

## Database Security Auditing

Oracle Audit Vault and Database Firewall (AVDF) monitors database audit logs and creates alerts. For instructions about installing and configuring AVDF in Oracle Cloud Infrastructure, see[Deploying Oracle Audit Vault and Database Firewall in Oracle Cloud Infrastructure](https://cloud.oracle.com/iaas/whitepapers/deploy-avdf-in-oci.pdf).

## Data Safe

We recommend using the Data Safe service to enhance the security of your database deployments. Oracle Data Safe is a unified control center for your Oracle databases which helps you understand the sensitivity of your data, evaluate risks to data, mask sensitive data, implement and monitor security controls, assess user security, monitor user activity, and address data security compliance requirements. See[Get Started](https://docs.oracle.com/en/cloud/paas/data-safe/index.html)for complete information.

## Database Backups

We recommend using Managed backups (backups created using the Oracle Cloud Infrastructure Console or the API) whenever possible. When you use managed backups, Oracle manages the object store user and credentials, and rotates these credentials every 3 days. Oracle Cloud Infrastructure encrypts all managed backups in the object store. Oracle uses the Database Transparent Encryption feature by default for encrypting the backups.

If you are not using managed backups, Oracle recommends that you change the object store passwords at regular intervals.

## Security Policy Examples

### Prevent Delete of Database Instances

The following example policy allows the group`DBUsers`to perform all management actions except delete databases and any artifacts.

```

```
