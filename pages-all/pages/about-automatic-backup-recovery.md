# About Using Recovery Service to Backup and Recover Oracle Cloud Databases
- Source: https://docs.oracle.com/iaas/recovery-service/doc/about-automatic-backup-recovery.html
- Fetched: 2026-09-05 18:57 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/recovery-service/doc/about-automatic-backup-recovery.html#dcoc-content-body)

# About Using Recovery Service to Backup and Recover Oracle Cloud Databases

Learn how to automate backups using Recovery Service .

The OCI Console managed automatic backups feature is the preferred method for backing up Oracle Cloud databases because you can easily configure backup settings using the console.

The automatic backups feature supports Recovery Service as the backup destination to provide you with a fully automated cloud backup solution. You do not need to perform any manual backups or backup storage administration tasks.

Use the Console to configure automatic backups and set Autonomous Recovery Service as the backup destination. By default, the Oracle-defined Silver (35-day retention period) protection policy is applied for backup retention. Alternatively, you can assign a different Oracle-defined policy or a custom policy to suit your internal storage demands.

When you enable automatic backups, OCI automatically sends an initial full (RMAN level 0) backup and successive incremental (RMAN level 1) backups to Recovery Service . Backups are retained for the period defined in the assigned protection policy.

After you enable automatic backups, Recovery Service creates an associated protected database resource. The Protected databases page provides you an unified interface to view a list of all the protected databases in your tenancy. You can select a protected database to view the list of backups, monitor database protection and backup status, and analyze storage utilization.

You can use the console to restore a database using a backup created by Recovery Service . You can also create a new database by using a protected database backup.
Note  
  
For more information, refer your Oracle Cloud Database Service documentation.

Parent topic:[Using Recovery Service to Backup and Recover Oracle Cloud Databases](https://docs.oracle.com/iaas/recovery-service/doc/configuring-recovery-service.html#GUID-50813B91-5A86-461E-B2F0-FF75C7EAB3FD)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
