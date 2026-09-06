# Using Retention Lock to Protect Backups
- Source: https://docs.oracle.com/iaas/recovery-service/doc/about-policy-locking.html
- Fetched: 2026-09-05 18:57 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/recovery-service/doc/about-policy-locking.html#dcoc-content-body)

# Using Retention Lock to Protect Backups

Retention lock applies to the backup retention period defined in a protection policy.

Locking the backup retention period enables Recovery Service to prevent the modification of backups for the duration defined in the policy. Use the retention lock feature to protect backups from accidental modifications or malicious damages, such as ransomware.

When you enable the retention lock, you must also set a date for the lock to take effect. Recovery Service mandates a minimum delay of 14 days to permanently lock the retention period defined in a policy.

For example, assuming that you enable the retention lock on August 1, you can set the lock date as August 15 or later.

During the specified delay period, you can either increase or decrease the backup retention period or disable the retention lock, if necessary.

When the specified delay ends, the retention period is permanently locked. Recovery Service strictly prohibits the modification or deletion of backups until the retention period expires.
Be aware of these restrictions that apply (to all users including tenancy administrators) if the retention period is permanently locked for a protection policy.
- You cannot disable the retention lock
- You are only allowed to increase the backup retention period for the policy (maximum 95 days)
- You cannot assign a different protection policy to a protected database if the retention period is permanently locked for the existing policy
Note  
  
If you assign a database to a policy where the retention period is permanently locked, then Recovery Service does not immediately enforce the retention lock for the newly added database. You can leverage the 14 day (minimum) grace period before the retention lock can take permanent effect for the newly added database. For example, assume that the retention period is permanently locked for a policy on August 15. If you assign the same policy to another database on August 16, then the retention lock would take effect only August 30 for the newly added database.

Parent topic:[Managing Protection Policies](https://docs.oracle.com/iaas/recovery-service/doc/manage-protection-policy.html#GUID-3823E813-1236-4755-B791-ABE1963C4EB8)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
