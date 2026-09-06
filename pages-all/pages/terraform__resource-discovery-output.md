# Output File Contents
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/resource-discovery-output.htm
- Fetched: 2026-09-05 19:20 CDT

# Output File Contents

Understand output of the OCI Terraform provider's resource discovery feature.

The Oracle Cloud Infrastructure (OCI) Teraform provider's resource discovery`export`command discovers resources that are in an active or usable state. Resources that have been terminated or otherwise made inactive are generally excluded from the generated configuration.

By default, the Terraform names of the discovered resources share the same name as the display name for that resource, if one exists.

The attributes of the resources are populated with the values that are returned by the OCI services.

In some cases, a required or optional attribute may not be discoverable from the OCI services and may be omitted from the generated Terraform configuration. This omission may be expected behavior from the service, which may prevent discovery of certain sensitive attributes or secrets. In such cases, a placeholder value is set along with a comment like this:
```

```

The missing required attributes are also added to lifecycle`ignore_changes`. This addition is done to avoid Terraform plan failure when moving manually-managed infrastructure to Terraform-managed infrastructure. Any changes made to such fields are not reflected in the Terraform plan. If you want to update these fields, remove them from`ignore_changes`.

Resources that are dependent on availability domains will be generated under`availability_domain.tf`file. These include:
- `oci_core_boot_volume`
- `oci_file_storage_file_system`
- `oci_file_storage_mount_target`
- `oci_file_storage_snapshot`
