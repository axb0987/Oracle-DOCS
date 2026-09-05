# Installing the Linux PAM
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/install-linux-pam.htm
- Fetched: 2026-09-05 02:23 CDT

# Installing the Linux PAM

To install the Linux Pluggable Authentication Module (PAM) on your Linux environment, you install the PAM rpm's along with some dependencies:

- Extract the downloaded zip file to a directory of your choice. This will extract the following files:

- `pam_oracle-cloud- <version> .x86_64.rpm`
- `authn_oracle_cloud- <version> .x86_64.rpm`
- Check the curl and json-c Linux dependencies are installed:
- As the root user, run the following commands:
- `yum list installed | grep curl.x86_64`
- `yum list installed | grep json-c.x86_64`
- If they aren't installed, run the following commands:
- `yum install json-c`
- `yum install curl`
- Change to the directory where you saved the OS version you want to install:

- `cd <folder where pam_oracle-cloud- version .rpm resides>`
- Install the PAM rpm's as the root user.
- If using yum:
- `yum install pam_oracle-cloud- version .rpm authn-oracle-cloud.rpm`
- If using rpm:
- `rpm -Uvh pam_oracle-cloud.rpm authn-oracle-cloud.rpm`
