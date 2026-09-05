# Adding cloud-init Information for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/cloud-init.htm
- Fetched: 2026-09-05 02:58 CDT

# Adding cloud-init Information for Roving Edge Infrastructure

Describes how to add cloud-init information for Roving Edge Infrastructure.

Use cloud-init to run customization scripts. See[Using Custom Cloud-init Initialization Scripts](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm)for more information about using cloud-init in Oracle Cloud Infrastructure. Refer to the following[cloud-init documentation](https://cloudinit.readthedocs.io/en/latest/)for general information about cloud-init.

Scripts must have a shebang (`#!`) at the top.

You can run Roving Edge Infrastructure-provisioned customization scripts for easy provisioning of Compute instances.

Roving Edge Infrastructure users that are created using cloud-init-based customization scripts, and installed software packages are preserved.

To configure your Roving Edge Infrastructure Compute instance to use cloud-init:
- 

Open the following file on your Roving Edge Infrastructure devices:

`/etc/cloud/cloud.cfg`
- 

Add the following line under the`scripts-user`section:

`[ scripts-user, always ]`
- 

Save and close the`/etc/cloud/cloud.cfg`file.
- 

Place any cloud-init customization scripts in the following folder:

`/var/lib/cloud/scripts/per-boot`
