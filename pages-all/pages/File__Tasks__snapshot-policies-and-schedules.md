# Policy-Based Snapshots and Scheduling
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm
- Fetched: 2026-09-05 02:04 CDT

# Policy-Based Snapshots and Scheduling

File Storage snapshot policies and schedules control the frequency of automatic snapshot creation and set the retention period of snapshots created by the policy.

A snapshot policy can contain up to 10 unique schedules . When you create a schedule, you can specify when snapshots are created, the frequency of the scheduled snapshots, and the retention period of the snapshots. Snapshot expiration time is computed using the snapshot creation time and the retention period. When a snapshot expires, the File Storage service deletes the snapshot.

After you[create a snapshot policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-create.htm), you can[associate the policy with one or more file systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-file-system.htm). Up to 100 file systems can be attached to a single snapshot policy. The File Storage service automatically generates snapshots of the file system according to[schedules within the policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-schedule.htm). Snapshots created by the system on these schedules are called policy-based snapshots to differentiate them from snapshots created by users, or by replication. See[Snapshot Types](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm#Managing_Snapshots__section_snapshot-types)for more information.

File Storage deletes policy-based snapshots according to a retention period set in the schedule. To keep a policy-based snapshot beyond its retention period, you can search for the snapshot and[change its expiration time](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-expiration.htm). Changes to the expiration time on a policy-based snapshot only apply to that snapshot, not the corresponding schedule or policy.

To monitor policy-based snapshots, we recommend using events. For more information, see[Monitoring Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm#monitoring).

## Schedule Types and Timing

When you configure schedules within a policy, you can choose the schedule type, the date and time that the schedule becomes effective, and more schedule details, including what time zone the schedule runs according to. Create a policy that includes schedules that best address your compliance and security requirements.

You can configure policy-based snapshot creation using the following schedule types:
- Hourly: Snapshots are created hourly, but not necessarily at the top of each hour.

Note  
  
A snapshot policy can only contain one schedule set to create snapshots hourly.
- Daily: Snapshots are created once every 24 hours.
- Weekly: Snapshots are created on the selected day of the week.
- Monthly: Snapshots are created on a selected day of month.
- Yearly: Snapshots are created on a selected month and day of the year.

A schedule doesn't start until its Effective From date and time. If you don't specify when the schedule becomes effective, the schedule goes into effect when it's created.

After selecting the schedule type and when it goes into effect, you can optionally provide more schedule details. If you don't provide schedule details, the system automatically chooses them for you:

- Hour of the day (Optional): For daily, weekly, monthly, and yearly schedules, you can optionally choose the hour of the day that the schedule creates a snapshot.
- Day of the week (Optional): For weekly, monthly, and yearly schedules, you can optionally choose the day of the week that the schedule creates a snapshot.
- Day of the month (Optional): For monthly and yearly schedules, you can optionally choose the day of the month that the schedule creates a snapshot.
- Month of the year (Optional): For yearly schedules, you can optionally choose the month of the year that the schedule creates a snapshot.
Note  
  
A policy-based snapshot isn't guaranteed to start at the exact time specified by the schedule in a policy.

## Snapshot Retention Duration

Each policy-based snapshot is created with a retention duration. At the end of the retention duration, the snapshot expires and the system deletes it. If you don't explicitly set the snapshot retention duration when creating policies and schedules, the File Storage service assigns a default value. The default and maximum retention duration depends on the schedule type of the scheduled snapshot.

Maximum and Default Retention Duration
Schedule Type Maximum Retention Default Retention
Hourly 168 hours 24 hours
Daily 120 days 7 days
Weekly 52 weeks 4 weeks
Monthly 144 months 12 months
Yearly 50 years 5 years

The minimum retention duration for a snapshot is one hour.

If you need to keep a snapshot beyond its retention duration, you can[modify or remove its expiration time](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-expiration.htm).

## Limitations and Considerations

The following limitations and considerations exist for File Storage snapshot policies and schedules:
- A policy-based snapshot isn't guaranteed to start at the exact time specified by the schedule in a policy. It can start within a window that extends before and after the scheduled time.
- A snapshot policy can only contain one schedule set to create snapshots hourly.
- Each schedule within a snapshot policy must be a combination of type, effective from, and snapshot retention duration that's unique to the policy.
- If a snapshot policy has more than one schedule, and the schedules would create a snapshot at the same time, only the snapshot with the longer retention period is created. For example, a policy containing an hourly schedule and a daily schedule might both be configured to take a snapshot at 1 p.m., but because the daily schedule has a longer retention duration, the hourly scheduled snapshot is skipped.
- In rare cases, the File Storage service might be busy when a snapshot is scheduled, so the snapshot remains queued. If the policy queues another snapshot with the same schedule type, the system may skip the first queued snapshot and proceed with the second.
- A maximum of 100 file systems can be associated with a specific snapshot policy.
Tip  
  
To monitor policy-based snapshots, we recommend using events. For more information, see[Monitoring Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm#monitoring).

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users create, manage, and delete file systems](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#general-file-system-management)allows users to create and manage snapshot policies.

Use the`filesystem-snapshot-policies`resource-type when using policies to control access to policy-based snapshots. For more information, see[Policy Details for the File Storage service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Next Steps

- [Creating a Snapshot Policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-create.htm)
- [Adding a Schedule to a Snapshot Policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-schedule.htm)
- [Attaching a File System to a Snapshot Policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-file-system.htm)
- [Attaching a Snapshot Policy to a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-to-file-system.htm)
