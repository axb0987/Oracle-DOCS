# Testing Authentication into Linux Using IAM
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/test-authn-linux.htm
- Fetched: 2026-09-05 02:23 CDT

# Testing Authentication into Linux Using IAM

Test authentication on Linux using a user in IAM.
Before you begin: Ensure that configured your Confidential Application and that it only contains the following roles:
- Me
- POSIX Viewer
- Signin Identity Domain Administrator or User Administrator should not be listed. See[Configuring a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/configure-confidential-application.htm)for additional information.

- SSH into your Linux environment where the Linux Pluggable Authentication Module (PAM) is installed.
- When prompted enter the password for the IAM user:

For example:

```

```
