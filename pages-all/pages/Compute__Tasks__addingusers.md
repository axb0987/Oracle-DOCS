# Adding Users to an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/addingusers.htm
- Fetched: 2026-09-05 01:50 CDT

# Adding Users to an Instance

You can add additional users to a compute instance.

If you created your instance using a Linux or CentOS platform image, you can use SSH to access your instance from a remote host as the`opc`user. If you created your instance using an Ubuntu platform image, you can use SSH to access your instance from a remote host as the`ubuntu`user. After signing in, you can add users to the instance.

If you created your instance using a Windows platform image, you can create new users after you sign in to the instance through a Remote Desktop client.

## Creating Additional Users on a Linux Instance

If you do not want to share your SSH key, you can create additional SSH-enabled users for a Linux instance. At a high level, you do the following things:
- Generate SSH key pairs for the users offline.
- Add the new users.
- Append a public key to the`~/.ssh/authorized_keys`file for each new user.

The new users then can SSH to the instance using the appropriate private keys.
Tip  
  

If you re-create an instance from a platform image, users and SSH public keys that you added or edited manually (that is, users that weren't defined in the machine image) must be added again.

If you need to edit the`~/.ssh/authorized_keys`file of a user on your instance, start a second SSH session before you make any changes to the file and ensure that it remains connected while you edit the file. If the`~/.ssh/authorized_keys`file becomes corrupted or you inadvertently make changes that lock you out of the instance, you can use the backup SSH session to fix or revert the changes. Before closing the backup SSH session, test all changes you made by logging in with the new or updated SSH key.

To create an additional SSH-enabled user:
- [Generate an SSH key pair](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm)for the new user.
- Copy the public key value to a text file for use later in this procedure.
- [Sign in to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm).
- 

Become the root user:

```

```

- 

Create the new user:

```

```

- 

Create a`.ssh`directory in the new user's home directory:

```

```

- 

Copy the SSH public key from the text file into the`/home/new_user/.ssh/authorized_keys`file:
Note  
  
&lt;public_key&gt; should be the SSH public key itself, not the name of the file containing the key.

```

```

- 

Change the owner and group of the`/home/username/.ssh`directory to the new user:

```

```

- 

To enable`sudo`privileges for the new user, run the`visudo`command and edit the`/etc/sudoers`file as follows:
- 

In`/etc/sudoers`, look for:
```

```

- 

Add the following line immediately after the preceding line:

```

```

The new user can now sign in to the instance.

## Creating Additional Users on a Windows Instance

For the most current steps, see[Manage User Accounts](https://docs.microsoft.com/en-us/windows-server-essentials/manage/manage-user-accounts-in-windows-server-essentials)in the Microsoft documentation.
- 

[Sign in to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm)using a Remote Desktop client.
- 

On the Start menu, click Control Panel .
- 

Click User Accounts , and then click User Accounts again.
- 

Click Manage another account .
- 

Click Add a user account .
- 

Enter a User name and Password .
- 

Confirm the password, and then create a Password hint .
- 

Click Next .
- 

Verify the account, and then click Finish .
