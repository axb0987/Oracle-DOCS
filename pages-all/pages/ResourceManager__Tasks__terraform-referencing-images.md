# Referencing Images
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/terraform-referencing-images.htm
- Fetched: 2026-09-05 02:56 CDT

# Referencing Images

Reference images in Terraform configurations used by Resource Manager.

When launching compute instances, your Terraform configuration should use the same image every time you run a Terraform`apply`job.
Note  
  
To avoid referencing a different image in subsequent Terraform`apply`jobs, specify the region-specific image OCID in the Terraform configuration. Do not locate the image OCID using the`oci_core_image`data source. This data source calls into the`ListImages`API, whose return values can change over time because over time images are added and older ones deleted. For a list of Oracle-provided images and their OCIDs, see[Oracle-Provided Images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm). For more information, see[Results of oci_core_images will change over time for Oracle-provided images](https://github.com/oracle/terraform-provider-oci/issues/352).

To find the latest region-specific OCIDs for an image:
- 

Go to[Image Release Notes](https://docs.oracle.com/iaas/images/).
- 

For the image that you want, select Latest Image .

An image OCID is listed for each region.
- 

Copy the region-specific image OCID that you want.

For example, copy the image OCID for the`us-phoenix-1`region.

We recommend the following pattern for specifying an image for regions:

```

```

Compute instance example of this pattern:

```

```
