# Installing and Configuring the Linux PAM
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/overview.htm
- Fetched: 2026-09-05 02:23 CDT

# Installing and Configuring the Linux PAM

The Pluggable Authentication Module (PAM) lets you to integrate your Linux environment with IAM to perform end-user authentication with first and second factor authentication.

The topics in this section include:
- [What is the Linux PAM](https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/overview.htm#what-is-linux-plug-authn-module)
- [Installing the Linux PAM](https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/install-linux-pam.htm)
- [Why use the Linux PAM](https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/overview.htm#why-use-oracle-identity-cloud-service-linux-pluggable-authentication-module)
- [Certified Components for the Linux PAM](https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/overview.htm#certified-components)

## What is the Linux PAM

The PAM is an authentication module for Linux that performs end-user authentication with IAM.

The PAM also lets Linux administrators, or end users, to query information about users and groups stored in IAM using standard Linux commands that use NSS such as`id`,`group`, and`getent`.

## Why use the Linux PAM

Use the PAM when you want to authenticate users in Linux using IAM.

An organization might have large numbers of Linux servers, making management of users, for example creating, modifying, or deleting users, a time intensive and costly activity. With the Linux PAM you can manage Linux users centrally in IAM, providing cost and time savings.

Linux administrators can utilize IAM to authenticate end users. End users can sign in to a Linux server, for example with SSH, and authenticate with their IAM user credentials. In addition, the multifactor authentication offerings of IAM can be utilized so end users are prompted to authenticate with a second factor such as a One Time Password code sent using Email, SMS, a Mobile Authenticator application, or authenticate using security questions. As well as authenticating with single or multiple factors, administrators, and end users can use NSS and standard Linux commands to query user and group information.

## Certified Components for the Linux PAM

The following table lists the certified releases for IAM and your OS (which is required for the Linux PAM to run).

Note  
  
Every PAM download includes all certified components.

64-Bit OS

Yes. (x86_64)

Oracle Linux 7

Oracle Linux 8

Oracle Linux 9

Yes. (ARM)

Oracle Linux 7

Oracle Linux 8
