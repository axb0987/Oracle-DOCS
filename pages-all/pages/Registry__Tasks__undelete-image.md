# Undeleting (Restoring) an Image
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/undelete-image.htm
- Fetched: 2026-09-05 02:54 CDT

# Undeleting (Restoring) an Image

Find out how to undelete (restore) an image from Container Registry.

You can undelete an image you've previously deleted, for up to 48 hours after you deleted it. After that time, the image is permanently removed from Container Registry. You use the Oracle Cloud Infrastructure REST API and CLI to undelete images.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/undelete-image.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/undelete-image.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/undelete-image.htm#)
- 

This task can't be performed using the Console.
- 

Use the[oci artifacts container image restore](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/image/restore.html)command and required parameters to undelete an image you've previously deleted:

```

```

For example:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[RestoreContainerImage](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImage/RestoreContainerImage)
