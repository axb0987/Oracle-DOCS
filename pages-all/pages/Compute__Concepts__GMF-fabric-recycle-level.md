# GPU Memory Fabric Recycle Level
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/GMF-fabric-recycle-level.htm
- Fetched: 2026-09-05 01:48 CDT

# GPU Memory Fabric Recycle Level

Use the fabric recycle level to control how the system handles the memory fabric when an instance is terminated.
The`fabricRecycleLevel`parameter is part of`memoryFabricPreferences`in[UpdateComputeGpuMemoryFabric](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryFabric/UpdateComputeGpuMemoryFabric), and allows these values:
- SKIP_RECYCLE: OCI "Quick recycles" the Compute host and skips reprovisioning the fabric before returning the host for reuse.

Use Quick Recycle to skip the standard OCI host provisioning process to minimize the time a host is unavailable for use after an instance is terminated. However, note that the host provisioning process ensures hosts are cleaned, healthy, compliant, and secure, so hosts being shared or in production environments should always go through a Full Recycle.
Note  
  
You can't change`customerDesiredFirmwareBundleId`when setting`fabricRecycleLevel`to SKIP_RECYCLE.
- FULL_RECYCLE: When a Compute host is recycled, OCI does a bare metal wipe and reprovisions the fabric.
- OPPORTUNISTIC_FULL_RECYCLE: Updates firmware through a FULL_RECYCLE if the target firmware bundle is different from the current firmware bundle. Otherwise, a SKIP_RECYCLE is performed.
-
