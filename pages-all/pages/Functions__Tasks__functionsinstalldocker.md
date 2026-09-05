# Installing Docker for Use with OCI Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstalldocker.htm
- Fetched: 2026-09-05 02:08 CDT

# Installing Docker for Use with OCI Functions

Find out how to install Docker for use with OCI Functions.

Before using OCI Functions, a version of Docker supported by Fn Project must be installed in your development environment.

If you are using Cloud Shell as your development environment, a suitable version of Docker has already been installed for you.

If Docker is not already installed, or the installed version of Docker is not supported, you'll have to install or upgrade Docker.

The instructions in this topic assume:
- you are not using Cloud Shell as your development environment
- you are using Linux
- you have already completed the steps in[Creating a Profile in the Oracle Cloud Infrastructure CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfigureocicli.htm)
Note  
  

By default, Fn Project (and by extension, OCI Functions) assumes the use of Docker to build and deploy function images. However, Fn Project also supports Podman as an alternative to Docker. See[Note on the use of Podman instead of Docker](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstalldocker.htm#Install_Docker_for_Use_with_Oracle_Functions__section_podman_instead_of_docker).

To confirm that a supported version of Docker is installed in your development environment:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, confirm that Docker is installed by entering:

```

```

- 

Do one of the following, depending on the message you see:
- If you see an error message indicating that Docker is not installed, you have to install Docker before proceeding to the next step. See the[Docker documentation](https://docs.docker.com/)for information about installing Docker on your platform. If your platform is Oracle Linux, see[Oracle Container Runtime for Docker User's Guide](https://docs.oracle.com/cd/E52668_01/E87205/html/docker_install_upgrade.html).
- If you see a message indicating the version of Docker that's installed, go to the next step.
- 

Assuming Docker is installed, go to the[Fn Project home page on GitHub](https://github.com/fnproject/fn/)to confirm that the installed version of Docker is at least the minimum version specified in the[Pre-requisites section](https://github.com/fnproject/fn#pre-requisites).

If the installed version of Docker is not supported by Fn Project, you have to upgrade the version of Docker before proceeding. See the[Docker documentation](https://docs.docker.com/)for information about upgrading Docker on your platform. If your platform is Oracle Linux, see[Oracle Container Runtime for Docker User's Guide](https://docs.oracle.com/cd/E52668_01/E87205/html/docker_install_upgrade.html).

When you have completed the steps in this topic, go on to[Installing the Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstallfncli.htm).

## Note on the use of Podman instead of Docker

By default, Fn Project (and by extension, OCI Functions) assumes the use of Docker to build and deploy function images. However, Fn Project also supports Podman as an alternative to Docker. When using Fn Project CLI version 0.6.12 and above, you can set a configuration setting to specify that you want to use Podman instead of Docker.

Having installed the Fn Project CLI (see[Installing the Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstallfncli.htm)), specify that you want to use Podman as follows:

1. Install Podman (version 3.4 or later), and add Podman to the system path. See[Podman Installation Instructions](https://podman.io/getting-started/installation)

2. Add the`container-enginetype`configuration setting to the`~/.fn/config.yaml`file as follows:
```

```

If you subsequently want to use Docker rather than Podman, do either of the following:
- Remove the`container-enginetype`configuration setting from the`~/.fn/config.yaml`file.
- Update the`container-enginetype`configuration setting in the`~/.fn/config.yaml`file to specify`docker`rather than`podman`, as follows:
```

```
