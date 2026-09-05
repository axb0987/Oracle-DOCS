# Securing Autonomous Recovery Service
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/autonomous_recovery_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Autonomous Recovery Service

This topic provides security information and recommendations for Oracle Database Autonomous Recovery Service.

Recovery Service simplifies database backup management and provides enhanced data protection to Oracle Cloud Databases.

## Security Responsibilities

To use Recovery Service securely, learn about your security and compliance requirements.You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.
Oracle is responsible for the following security requirements:
- 

Physical Security :

Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- 

Network Security :

Recovery Service requires that you use a private endpoint inside a virtual cloud network where the database resides. In an virtual cloud network (VCN), you can use security rules to control Recovery Service access to a database. This also keeps all traffic to and from the database off of the public internet.
- Access Control : Use Recovery Service policies to limit access to recovery service resources. Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

IAM Policies :
Recovery Service policy recommendations:
- The Database Service must have networking permissions and service permissions to access Recovery Service resources.
- Assign least privilege access for IAM users and groups in recovery-service-family.
- We recommend that you allow a single set of compliance admins to manage protection policies in all the compartments.

For more information, see[Recovery Service Policies and Permissions](https://docs.oracle.com/iaas/recovery-service/doc/recovery-service-policies-resources.html).

Database Backup Security :

Recovery Service provides you with options to preserve backups before terminating a database, and supports data recovery from accidental or malicious damages.
While enabling automatic backups for a database, specify one of these options to preserve protected database backups:
- Retain backups according to the protection policy retention period - After you terminate a database, Recovery Service will continue to retain backups for period defined in the assigned protection policy.
-
