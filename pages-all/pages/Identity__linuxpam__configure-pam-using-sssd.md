# Configuring the PAM using SSSD
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/configure-pam-using-sssd.htm
- Fetched: 2026-09-05 02:23 CDT

# Configuring the PAM using SSSD

Configure the PAM on Linux using the SSSD service.

- The SSSD service must be installed. If it's not installed, install using`sudo yum install sssd`.
- The service must be configured to start when the system reboots. You can perform this configuration using`sudo chkconfig sssd on`.
- Execute the steps[Enforcing SELinux](https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/enforcing_selinux.htm)when the property SELINUX is set as enforced in file`/etc/selinux/config`.

You can also set`SELINUX=permissive`or`SELINUX=disabled`, which case enforcing SELinux is not required

Note  
  
Restart Linux if you update`/etc/selinux/config`.

- Verify that the`/etc/sssd/sssd.conf`file exists, has 600 permission, and is owned by the root user. If the file doesn't exist create it as follows and run`chmod 600``/etc/sssd/sssd.conf`.

`/etc/sssd/sssd.conf`
```

```

Optionally, you can configure email addresses as the SSO usernames. To do this, add the line in bold to the`/etc/sssd/sssd.conf`file to specify the regular expression.
```

```

- Verify the`/etc/pam.d/sssd_proxy_oracle_cloud`file exists and is owned by the root user. If the file doesn't exist, then create it as the root user and add the following:

`/etc/pam.d/sssd_proxy_oracle_cloud file`
```

```

- Edit the`/etc/pam.d/sshd`and add the`pam_oracle_cloud`module:

`/etc/pam.d/sshd`
```

```

Note  
  
Add this either before the line`auth include password-auth`, or`auth substack password-auth*`.
- Edit the`/etc/ssh/sshd_config`to configure`sshd`to allow the use of multifactor authentication (MFA):

`/etc/ssh/sshd_config`

Search for the`ChallengeResponseAuthentication`property and set it to`yes`. If the property isn't in the configuration file, add it.
- Edit the`/etc/opc.conf`to let the plugin to interact with IAM:

`/etc/opc.conf`
```

```

- Restart sssd and sshd:
- For OEL6 &amp; OEL7:`authconfig --enablemkhomedir --enablepamaccess --update`.
- For OEL8:`authselect select sssd with-mkhomedir with-pamaccess`.
- Run:`service sshd restart`.
- Run:`service sssd restart`
