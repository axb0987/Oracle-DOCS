# Permissions Granted to Containers Running Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsrunningasunprivileged.htm
- Fetched: 2026-09-05 02:09 CDT

# Permissions Granted to Containers Running Functions

Find out about the permissions granted to containers running functions with OCI Functions.

When a function you've deployed to OCI Functions is invoked, it runs inside a container. The operations that a container can perform are determined by the user ID (UID) and group ID (GID) specified when the container is started. If a UID or GID is not specified, the container runs processes as the root user, with all the default capabilities enabled.

When starting a container to run a function, OCI Functions always specifies a user named 'fn' with a UID of 1000, and a group name 'fn' with a GID of 1000. No privileges are granted to UID 1000 and GID 1000, so the container (and the function running inside it) does not acquire the default capabilities listed in the[Docker documentation](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities). In addition, the container is prevented from gaining privileges.

As a result, do not create and deploy functions that:
- depend on capabilities that are unavailable
- depend on privilege elevation (for example,`su`,`sudo`or`setuid`)

If you are using your own Dockerfile, include the following lines:

```

```

For example:
```

```

Note that if you do not include the`groupadd`and`adduser`lines in the above example Dockerfile, you will see the following error message:
```

```
