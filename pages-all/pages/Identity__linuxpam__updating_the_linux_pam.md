# Updating the Linux PAM
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/updating_the_linux_pam.htm
- Fetched: 2026-09-05 02:23 CDT

# Updating the Linux PAM

Use the following steps to update to a new Linux Pluggable Authentication Module (PAM) version.

- Confirm that PAM is installed by running the following command:
`$ rpm -qa | grep oracle-cloud`
You should see:
```

```

- Update the RPM using the`rpm-U`command:

```

```

- Restart sssd:
`$ service sssd restart`
