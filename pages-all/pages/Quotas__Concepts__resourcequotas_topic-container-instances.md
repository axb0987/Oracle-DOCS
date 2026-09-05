# Container Instances Quotas
- Source: https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-container-instances.htm
- Fetched: 2026-09-05 02:53 CDT

# Container Instances Quotas

Container Instances quota details.

Quotas for container instances are available per core (OCPU), amount of memory (GB), and shape.
Important  
  
Quotas are shared between Compute resources and Container Instances resources.

## Core-Based Quotas

Family name:`compute-core`

Name

Scope

Description
standard-a1-core-count Availability domain

Total number of OCPUs for shapes in the VM.Standard.A1, BM.Standard.A1, and container instances that use the CI.Standard.A1.Flex shape series.

Note: This quota applies to both Compute and Container Instances resources. See[Compute Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Compute_Quotas.htm).
standard-e4-core-count Availability domain

Total number of OCPUs for Compute instances created using shapes in the VM.Standard.E4 and BM.Standard.E4 series and container instances created using the CI.Standard.E4.Flex shape.

Note: This quota applies to both Compute and Container Instances resources. See[Compute Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Compute_Quotas.htm).
standard-e5-core-ad-count Availability domain

Total number of OCPUs for Compute instances created using shapes in the VM.Standard.E5, BM.Standard.E5 series, and container instances created using the CI.Standard.E5.Flex shape.

Note: CI.Standard.E5.Flex is only available in selected regions. Quota availability doesn't guarantee regional shape availability. See the shapes table in[Container Instances](https://docs.oracle.com/iaas/Content/container-instances/home.htm)for a list of supported regions.

## Example

```

```

## Memory-Based Quotas

Family name:`compute-memory`

Name

Scope

Description
standard-a1-memory-count Availability domain

Total amount of memory for shapes in the VM.Standard.A1 and BM.Standard.A1 series, and container instances that use the CI.Standard.A1.Flex shape in GB.

Note: This quota applies to both Compute and Container Instances resources. See[Compute Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Compute_Quotas.htm).
standard-e4-memory-count Availability domain

Total amount of memory for Compute instances created using shapes in the VM.Standard.E4 and BM.Standard.E4 series and container instances created using the CI.Standard.E4.Flex shape in GB

Note: This quota applies to both Compute and Container Instances resources. See[Compute Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Compute_Quotas.htm).
standard-e5-memory-count Availability domain

Total amount of memory for Compute instances created using shapes in the VM.Standard.E5 and BM.Standard.E5 series and container instances created using the CI.Standard.E5.Flex shape in GB

Note: CI.Standard.E5.Flex is only available in selected regions. Quota availability doesn't guarantee regional shape availability. See the shapes table in[Container Instances](https://docs.oracle.com/iaas/Content/container-instances/home.htm)for a list of supported regions.

## Example

```

```
