# GPU Memory Fabric States
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/GMF-lifecycle-states.htm
- Fetched: 2026-09-05 01:48 CDT

# GPU Memory Fabric States

This topic describes the states available in the GPU memory fabric.

Use the[GetComputeGpuMemoryFabric](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryFabric/GetComputeGpuMemoryFabric)API to view the`lifecycleState`.

GPU memory fabric states
Memory Fabric State Description
AVAILABLE The fabric is ready for use. There is no GPU memory cluster on the fabric and at least one host is available to use.
OCCUPIED The fabric is in use . There is at least one active GPU memory cluster running on it.
PROVISIONING The fabric is getting set up . Some hosts are still starting up, and none are ready to run yet. This can happen when the fabric is in the recycling or provisioning state.
UNAVAILABLE The fabric is currently unavailable . This could be due to internal repair operations or because it's not open for use.
DEGRADED The fabric is running, but a hardware problem exists . GPU memory cluster creation isn't allowed in this state, and the fabric will be scheduled for repair.

Note  
  
There can be a scenario where your GPU memory fabric reads as`AVAILABLE`when it's`OCCUPIED`by a validation run. If your GPU memory fabric is in the`AVAILABLE`state but not responding as expected, check the`additionalData`
