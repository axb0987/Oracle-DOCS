# Using Time-Based Locks on a Snapshot
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot_immutable_lock_howTo.htm
- Fetched: 2026-09-05 02:05 CDT

# Using Time-Based Locks on a Snapshot

Use time-based locks (governance or compliance) to protect File Storage snapshots from deletion for a specified retention period and help meet retention requirements.

[Time-based](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot_lock_overview.htm#top)locks provide retention protection for snapshots. In governance mode, you can set a time-limited lock or use a legal hold for protection without an end date. In compliance mode, locks become strict after a cool-off period.
Note  
  
You can also[create a snapshot policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-create.htm#top)that automatically creates snapshots with time-based locks.

## IAM Permissions

To manage snapshot locks, you must have permissions to create, update, and remove locks. Required permissions vary by lock type and mode (resource-based, governance, or compliance).

For details on File Storage permissions, see[Policy Details for the File Storage service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm).

## Locking a Time-Based Snapshot

Before you begin, confirm the following:
- You have an existing snapshot.
- You have these IAM permissions:
- To create a snapshot lock in governance mode, you must have`FILE_SYSTEM_MANAGE_SNAPSHOT_LOCK_GOVERNANCE`.
- To create a snapshot lock in compliance mode, you must have`FILE_SYSTEM_MANAGE_SNAPSHOT_LOCK_COMPLIANCE`.
Tip  
  
You can also use or use the API or CLI to lock a time based snapshot:
- API: Use the[CreateSnapshot](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/CreateSnapshot)or[UpdateSnapshot](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/UpdateSnapshot)operations and pass`LockDurationDetails`parameter.
- CLI: Use the[`fs snapshot create`or](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/create.html)[`fs snapshot update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/update.html)command and pass the`lock_duration_details`parameter.

Follow these steps to add a time-based lock to a snapshot in the console:

- On the File Systems list page, select the file system that contains the snapshot that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Snapshots .
- Select the snapshot that you want to lock.
- On the snapshot's details page, from the Actions menu, select Update snapshot lock .
- In the Update snapshot lock panel, under Lock modes , select Governance mode or Compliance mode .
- Configure these lock settings:

- Legal hold (governance mode only): Locks the snapshot until the legal hold is removed.
- Lock duration : Sets the number of days that the snapshot is protected from deletion or changes.
- Cool-off duration (compliance mode only): Sets the number of days you must change or remove the lock before the snapshot becomes completely immutable.
Tip  
  
To make a compliance lock take effect immediately, set Cool-off duration to 0.
- Select Update .

If you need to change lock settings later, override the snapshot lock. If you need to remove a lock (when allowed), unlock the snapshot.

## Overriding a Time-Based Snapshot

Before you begin, confirm the following:
- To change or remove a snapshot lock while the snapshot is in governance mode, you must have`FILE_SYSTEM_MANAGE_SNAPSHOT_LOCK_GOVERNANCE`.
- To change or remove a snapshot lock while the snapshot is in compliance mode, you must have`FILE_SYSTEM_MANAGE_SNAPSHOT_LOCK_COMPLIANCE`.
Tip  
  
You can also use the API or CLI to override (edit) a time-based snapshot lock:
- API: Use the[UpdateSnapshot](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/UpdateSnapshot)operation and pass the`LockDurationDetails`parameter.
- CLI: Use the[`fs snapshot update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/update.html)command and pass the`lock_duration_details`parameter.

Use this procedure to edit an existing time-based lock on a snapshot.

- On the File Systems list page, select the file system that contains the snapshot that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Snapshots .
- Select the snapshot with the lock that you want to change.
- On the snapshot’s details page, from the Actions menu, select Update snapshot lock .
- Configure these lock settings:

- Lock modes : Select Governance mode or Compliance mode (if allowed in the snapshot’s current state).
- Legal hold (governance mode only): Select or clear this option to lock the snapshot until you remove the legal hold.
- Lock duration : Updates the number of days that the snapshot is protected from deletion or changes.
- Cool-off duration (compliance mode only): Updates the number of days you have to change or remove the lock before the snapshot becomes completely immutable.
Tip  
  
If you're switching to compliance mode and want the change to take effect immediately, set Cool-off duration to 0.
- Select Update .

If you no longer need retention protection, unlock the snapshot (if allowed by the lock mode and current state).

## Unlocking a Time-Based Snapshot

Before you begin, confirm the following:
- To remove a snapshot lock in governance mode, you must have`FILE_SYSTEM_MANAGE_SNAPSHOT_LOCK_GOVERNANCE`.
- To remove a snapshot lock in compliance mode (during the cool-off period), you must have`FILE_SYSTEM_MANAGE_SNAPSHOT_LOCK_COMPLIANCE`.
Tip  
  
You can also use the API or CLI to unlock (remove) a time-based snapshot lock (when allowed by the snapshot's current state):
- API: Use the[UpdateSnapshot](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/UpdateSnapshot)operation and update/clear the`LockDurationDetails`parameter.
- CLI: Use the[`fs snapshot update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/update.html)command and update/clear the`lock_duration_details`parameter.

Use this procedure to remove a time-based lock from a snapshot.

- On the File Systems list page, select the file system that contains the snapshot that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Snapshots .
- Select the snapshot that you want to unlock.
- On the snapshot's details page, from the Actions menu, select Update snapshot lock .
- In the Update snapshot lock panel, under Lock modes , select No lock .
- Select Update .

- If you can't select No lock , it means that the lock can't be removed in the snapshot's current state.

If you still need basic protection that you can change later, consider using a[resource-based lock](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-snapshot.htm#top)
