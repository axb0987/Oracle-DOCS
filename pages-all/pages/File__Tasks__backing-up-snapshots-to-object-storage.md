# Backing Up Snapshots to Object Storage Using rclone
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/backing-up-snapshots-to-object-storage.htm
- Fetched: 2026-09-05 02:02 CDT

# Backing Up Snapshots to Object Storage Using rclone

You might want to back up your File Storage snapshots in another location, such as Object Storage.

You can follow this process to use the[rclone](https://rclone.org/)utility to back up snapshots.
- Install rclone using the instructions for your operating system at[https://rclone.org/downloads/](https://rclone.org/downloads/).
- 

Create a`~/.rclone.conf`configuration file containing this information:

```

```

Note  
  
Refer to[Working with Customer Secret Keys](https://docs.oracle.com/iaas/Content/Identity/access/managing-user-credentials.htm#Working2)for details on obtaining a Customer Secret key.
- 

Verify that rclone can access Object Storage:

```

```

- 

Create a snapshot, if necessary:

```

```

- 

Use the`copy`,`copyto`, or`sync`option to copy the snapshot to Object Storage:

```

```

Tip  
  
Any File Storage directory path can be used as the source for the`rclone`command.

Refer to the[rclone documentation](https://rclone.org/docs/)
