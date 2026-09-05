# Referencing Availability Domains
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/terraform-referencing-availability-domains.htm
- Fetched: 2026-09-05 02:56 CDT

# Referencing Availability Domains

Use Resource Manager and Terraform configurations to mange availability domains.

Note  
  
The examples on this page use the compartment variable`var.compartment_ocid`. To specify the tenancy or root compartment, use the tenancy variable,`var.tenancy_ocid`.

Regarding availability domains, avoid the following pattern:

```

```

Instead, we recommend explicitly listing the[availability domain names](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#ad-names)for the regions in your configuration. To do so, use a variable that you have defined as follows:
```

```

You can then use the variable as shown here:

```

```

You can then set the`ad_list`variable directly by using the availability domain names for your tenant and region, as shown here:
```

```

The advantage of using this method is that it gives you control over your availability domain usage and prevents unexpected changes over time. However, this approach is problematic when configurations are shared between tenancies and regions, because availability domain names are tenancy- and region-specific.

A convenient alternative is to instead set the`ad_list`value by using the`oci_identity_availability_domains`data source. Do this in the configuration, then pass them into the modules. This effectively centralizes the list of ADs, making it easy to switch to an explicit list later if needed. (In the modules themselves, don't use the`oci_identity_availability_domains`data source.)

```

```

## Regions with a Single Availability Domain

Some Oracle Cloud Infrastructure regions have a[single availability domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About). When writing configurations that use plural data sources, such as`oci_identity_availability_domains`, ensure that you account for a single domain if required by your region.

The following example uses the`oci_identity_availability_domains`data source when listing fault domains in a single-availability domain region. The`availability_domains`index must be`0`. Any other index value is invalid in this region:

```

```

The full reference of the OCI Terraform provider's supported resources and data sources contains usage, argument, and attribute details. The full reference is available at[docs.oracle.com](https://docs.oracle.com/iaas/tools/terraform-provider-oci/latest/)and[Terraform Registry](https://registry.terraform.io/providers/oracle/oci/latest/docs). For releases of the OCI Terraform Provider, see[oracle/terraform-provider-oci](https://github.com/oracle/terraform-provider-oci/releases)
