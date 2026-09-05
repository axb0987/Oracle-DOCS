# Enforcing SELinux
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/enforcing_selinux.htm
- Fetched: 2026-09-05 02:23 CDT

# Enforcing SELinux

Set SELinux to enforcing.
Before you begin:

Check that the following packages are installed on Oracle Linux:

`rpm -q selinux-policy-targeted policycoreutils libselinux-utils libselinux-python libselinux`
Note  
  
When you change the SELinux mode from Permissive or Disabled to Enforcing, then you must reboot.
Create a policy and ensure that PAM works when SELinux is set to enforcing:

- If necessary, install these packages on Oracle Linux:

```

```

- Allow outbound communication on 443:

```

```

- Create a local policy so that`sssd_t`can create`opc`dir to create, and read and write to the`pam_nss.log`file (which is mentioned in`/etc/opc.conf`). It doesn't need to be located in a specific location because it's compiled by the SELinux utilities.
- Create the policy file and save it with the filename`idcs-pam.te`. This is the content:

```

```

- Build the SELinux policy module. Run:

```

```

- Install the SELinux module. Run:
`$ semodule -i idcs-pam.pp`
- Reload SELinux. Run:
`$ semodule -R`
- Finally, authenticate the PAM user again.
The`/opc`dir and`/opc/pam_nss.log`
