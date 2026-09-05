# Miscellaneous issues when using OCI Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Miscellaneous-issues-when-using-Oracle-Functions.htm
- Fetched: 2026-09-05 02:09 CDT

# Miscellaneous issues when using OCI Functions

Find out how to troubleshoot miscellaneous issues when using OCI Functions.

You might encounter these miscellaneous issues when using OCI Functions.

## When running OCI Functions on Ubuntu, Docker login returns an "error getting credentials - err: exit status 1..." message

When you configure your development environment for OCI Functions, you have to install Docker (see[Installing Docker for Use with OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstalldocker.htm)). If your development environment is running Ubuntu, when you follow the subsequent instructions to log in to Oracle Cloud Infrastructure Registry using Docker (see[Logging in to Oracle Cloud Infrastructure Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionslogintoocir.htm)), you might see a message similar to the following:
```

```

For more information about this Docker issue, including likely causes and possible resolutions, see[https://github.com/docker/docker-credential-helpers/issues/60](https://github.com/docker/docker-credential-helpers/issues/60)
