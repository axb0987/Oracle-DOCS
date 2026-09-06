# About Oracle Database Autonomous Recovery Service
- Source: https://docs.oracle.com/iaas/recovery-service/doc/about-recovery-service.html
- Fetched: 2026-09-05 18:57 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/recovery-service/doc/about-recovery-service.html#dcoc-content-body)

# About Oracle Database Autonomous Recovery Service

Understand the core concepts and key features of Recovery Service.

Oracle Database Zero Data Loss Autonomous Recovery Service is a fully managed service based on the on-premises[Oracle Zero Data Loss Recovery Appliance (ZDLRA)](https://www.oracle.com/engineered-systems/zero-data-loss-recovery-appliance/)technology. It provides modern cybersecurity protection for Oracle Databases of any size running on Exadata Database Service on Dedicated Infrastructure, Exadata Database Service on Exascale Infrastructure, Oracle Base Database Service, Oracle Database@AWS, Oracle Database@Azure, Oracle Database@Google Cloud, or on-premises environments.

Recovery Service is the recommended solution for protecting Oracle Databases and provides the following unique advantages over Object Storage backups:

- Zero Data Loss for All Database Backups - Zero Data Loss Autonomous Recovery Service provides real-time protection of the database, enabling recovery to within less than a second of when an outage or ransomware attack occurs. If a ransomware attack happens, you know you are protected up to the moment before the attack instead of having to go back to the last scheduled backup, which could have been hours ago.
- Achieve Faster Backups with Less Database Overhead - Recovery Service eliminates the need for weekly full backups using an offloaded incremental-forever backup paradigm, reducing database CPU, memory, and I/O overhead along with the backup window. Your valuable database resources can now be more focused on business needs rather than backup tasks.
- Be Confident in Reliable Recovery - All backups are validated for data anomalies that can impact recovery operations. Combined with immutability and enforced encryption, your data is safe, unalterable by anyone in the tenancy, and always ready for recovery in case of a ransomware attack.
- Get Deeper Insights into your Database Protection - A centralized data protection dashboard addresses key questions about the state of your database backups. Are my backups healthy? How long has it been since my last backup? How far back can I recover? How much space is my backup using? Are all my databases using the same retention policy?

For Recovery Service backups without Zero Data Loss protection, costs remain the same as Object Storage backups. Zero Data Loss is a premium option enabled by selecting Real-Time Protection.

Select Autonomous Recovery Service as the backup destination for Oracle managed automatic backups, which is the method that Oracle recommends for backing up Oracle Cloud and Oracle Multicloud Databases. See[Backing Up Oracle Cloud Databases to Recovery Service](https://docs.oracle.com/iaas/recovery-service/doc/automatic-backup-recovery-service.html#GUID-45B445F1-8E73-46D9-BFA2-A66BFB0BF6F8)for details.

To protect on-premises databases using Recovery Service, you must use[Oracle Database Zero Data Loss Cloud Protect](https://docs.oracle.com/iaas/recovery-service/doc/protecting-premises-databases-using-recovery-service.html#GUID-4175418A-1D30-487C-880F-60D391D98F45).

Parent topic:[Overview of Oracle Database Autonomous Recovery Service](https://docs.oracle.com/iaas/recovery-service/doc/overview-recovery-service.html#GUID-C7549465-E00C-4AE1-9BEF-70E735972AB4)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
