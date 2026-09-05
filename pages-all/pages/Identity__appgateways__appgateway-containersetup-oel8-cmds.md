# App Gateway Commands for Container Setup on OEL8
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/appgateway-containersetup-oel8-cmds.htm
- Fetched: 2026-09-05 02:18 CDT

# App Gateway Commands for Container Setup on OEL8

On Oracle Linux 8 (OEL8), Docker is replaced by Podman. The commands for creating containers remain unchanged. You may optionally install the 'podman-docker' package, which aliases the 'docker' command to Podman.

## To install the 'podman-docker' package:

`sudo dnf install podman-docker`

## To install Podman and related tools, enable the container-tools module:

`sudo dnf module install container-tools:ol8`

## To list running containers in Podman, use:

`docker ps --external`

Or

`podman ps --external`
Note  
  
Don’t use '`podman ps -a`'

## To allow a non-root user to run Docker commands, add the user to the 'docker' group:

`sudo usermod -a -G docker opc`

Or

`sudo usermod -aG docker $USER`

## To forcefully remove a container:

`docker rm -f appgateway`

Or

`podman rm -f appgateway`
