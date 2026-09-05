# Write to File System Fails
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/cannotwrite.htm
- Fetched: 2026-09-05 02:05 CDT

# Write to File System Fails

Learn how to troubleshoot problems writing to your File Storage file systems.
Important  
  

Before proceeding with troubleshooting, be sure to implement the following prerequisites for connecting to file systems from Linux-style instances:
- Mount the file system. Follow the procedure found in[Mounting File Systems From UNIX-Style Instances](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingunixstyleos.htm).
- Set up security rules to work with File Storage. Follow the procedure found in[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm)

Symptom 1: Writing to a file system from a mounted instance fails.

For example, open a terminal window on the instance and use the`touch`command to write a '`helloworld`' file:

```

```

The write operation fails with the error:

```

```

Cause: When a file system is created, the root user owns the root directory. If you're connecting from an instance that uses a Linux or CentOS platform image, the default user is opc . The default user is ubuntu when you connect from an instance that uses an Ubuntu platform image. These default users are not root users, so you can't initially write a file or directory to a new file system with these users.

Solution : You can implement one of the following solutions:
- Connect as the root user. Then, create files or directories in the new file system.
- 

Connect as the root user. Then, change the ownership or permissions of the file system root directory to allow other users (such as opc or ubuntu ) to write to the file system.
- 

Connect as the root user. Then, create subdirectories with ownership or permissions that allow other users to write to the subdirectory.

[Learn more about updating file and directory ownership and permissions.](https://linux.die.net/man/3/chmod)
- 

Connect as the default user. Then, use the`sudo`command to write or to change permissions or ownership of files or directories. The`sudo`command temporarily provides a regular user with root user permissions. Here's an example of using the`sudo`command to write to the file system:

```

```

[Learn more about the`sudo`command.](https://linux.die.net/man/8/sudo)

For more information about accessing instances, see[Connecting to an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm)
