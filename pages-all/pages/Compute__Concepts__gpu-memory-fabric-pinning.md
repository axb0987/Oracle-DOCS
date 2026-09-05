# GPU Memory Fabric Firmware Pinning
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/gpu-memory-fabric-pinning.htm
- Fetched: 2026-09-05 01:49 CDT

# GPU Memory Fabric Firmware Pinning

Your AI cloud infrastructure consists of multiple device types: hosts, GPUs, and NVLink switches—all of which must run compatible firmware versions to ensure stable operation. To help maintain this critical compatibility, OCI enforces firmware version consistency across all components. You also have the ability to set the desired firmware bundle on your GPU memory fabric (called pinning ) using the Memory Fabric API.

To set the desired firmware bundle, you use`memoryFabricPreferences`in[UpdateComputeGpuMemoryFabric](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryFabric/UpdateComputeGpuMemoryFabric). Your selection takes precedence over any OCI process for determining the target firmware bundle in an automated upgrade, thus giving you greater control over the pace of migration to newer firmware.

(Note that you can also use`memoryFabricPreferences`in[UpdateComputeGpuMemoryFabric](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryFabric/UpdateComputeGpuMemoryFabric)to set the fabric recycle level . See[GPU Memory Fabric Recycle Level](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/GMF-fabric-recycle-level.htm#GMF-fabric-recycle-level).)

## Setting GPU Memory Fabric Preferences

To set GPU memory fabric preferences, you can also use the OCI[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html):

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-gpu-memory-fabric/update.html)compute-gpu-memory-fabric update`command and required parameters:

```

```

## Firmware Bundle-Related APIs

Use these APIs to view and pin firmware bundles:

Firmware Bundle-related APIs
Task Related API
Obtain the available firmware bundles.[ListFirmwareBundles](https://docs.oracle.com/iaas/api/#/en/iaas/latest/FirmwareBundlesCollection/ListFirmwareBundles)
Specify the desired firmware bundle to be pinned to your GPU memory fabric.[UpdateComputeGpuMemoryFabric](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryFabric/UpdateComputeGpuMemoryFabric)
View the fabric's current firmware bundle.[GetComputeGpuMemoryFabric](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryFabric/GetComputeGpuMemoryFabric)
View the host's current firmware bundle.[GetComputeHost](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeHost/GetComputeHost)
View the target firmware bundle that represents what the memory fabric will upgrade to, when the memory fabric's`lifecycleState`is next unoccupied by a GPU memory cluster.[GetComputeGpuMemoryFabric](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryFabric/GetComputeGpuMemoryFabric)
View the GPU memory fabric's`lifecycleState`.[GetComputeGpuMemoryFabric](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryFabric/GetComputeGpuMemoryFabric)

See also[GPU Memory Fabric States](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/GMF-lifecycle-states.htm#gpu-memory-fabric-states).
List all GPU memory clusters.[ListComputeGpuMemoryClusters](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryCluster/ListComputeGpuMemoryClusters)

See also[ComputeGpuMemoryFabric](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryFabric/).

## Firmware Details

You can obtain firmware details from[GetComputeGpuMemoryFabric](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryFabric/GetComputeGpuMemoryFabric).

This table describes the firmware-related fields in more detail.

Firmware Fields
Field Description
`targetFirmwareBundleId`

The firmware bundle that the current firmware bundle will be set to, when the GPU memory fabric's`lifecycleState`is next unoccupied by a GPU memory cluster.

When the[UpdateComputeGpuMemoryFabric](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryFabric/UpdateComputeGpuMemoryFabric)API is called to set`memoryFabricPreferences`, the`customerDesiredFirmwareBundle`is reflected in the`targetFirmwareBundleId`field in the response, if the API call is successful.

Note: OCI can't upgrade or downgrade GPU memory fabric to the specified`customerDesiredFirmwareBundleId`([UpdateComputeGpuMemoryFabric](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryFabric/UpdateComputeGpuMemoryFabric)) when its state is OCCUPIED (occupied by Compute GPU memory clusters).

Instead, once`memoryFabricPreferences`are updated, you must then terminate all Compute GPU memory clusters on the fabric. After termination is complete, OCI reprovisions the fabric with the specified firmware.
`currentFirmwareBundleId`

The currently installed firmware bundle on the fabric.

Possible values are:
- null - when the fabric is undergoing a firmware upgrade
- different from`targetFirmwareBundleId`- when the fabric is occupied (you must terminate Compute GPU memory clusters before the firmware upgrade can start). Note that OCI might be running its own memory clusters as part of its validation process, and they will be preempted if there's a firmware upgrade.
- equal to`targetFirmwareBundleId`- when the firmware upgrade is complete.
`firmwareUpdateState`

Indicates whether a pending firmware upgrade on the fabric exists. Possible values are:
- WILL_UPDATE: pending or ongoing firmware upgrade
- NO_UPDATE: no pending firmware upgrade
- SKIP_RECYCLE_ENABLED:`fabricRecycleLevel`has been set to SKIP_RECYCLE
`firmwareUpdateReason`Optional message describing the reason behind firmware update decisions.

## FAQs

[Can an ongoing firmware update be interrupted?](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/gpu-memory-fabric-pinning.htm#)

An ongoing firmware update can't be interrupted or canceled while the GPU memory fabric is in the PROVISIONING state.

To apply a new`customerDesiredFirmwareBundleId`, you must wait until the fabric transitions to the AVAILABLE state, at which point a new update can be initiated.

[What does a 409 Conflict mean when updating a memory fabric?](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/gpu-memory-fabric-pinning.htm#)

A`409 Conflict`indicates that the GPU memory fabric is currently in the PROVISIONING state and isn't eligible for updates. Updates are allowed only when the fabric is in the AVAILABLE or OCCUPIED state.

[What happens if I terminate my GPU memory cluster before setting customerDesiredFirmwareBundleId?](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/gpu-memory-fabric-pinning.htm#)

All the hosts in the terminated GPU memory cluster will be provisioned with the existing firmware bundle, at first. The remaining behavior depends on whether the GPU memory fabric is associated with a single GPU memory cluster or multiple GPU memory clusters:

Single GPU memory cluster

When the only GPU memory cluster on the fabric is terminated:
- The fabric may transition back to the AVAILABLE state after termination completes. In this case, you can immediately set a new`customerDesiredFirmwareBundleId`. The remaining available hosts will then be provisioned with the new bundle. Hosts returning from the terminated GPU memory cluster will be reprovisioned to align with the new desired bundle.
- The fabric may also transition to the PROVISIONING state, if provisioning is needed. In this case, the ongoing provisioning can't be canceled, and you must wait for it to complete before applying a new update.

Multiple GPU memory clusters

When one of multiple GPU memory clusters is terminated:
- The fabric remains in the OCCUPIED state. You can still set a new`customerDesiredFirmwareBundleId`. However, available hosts will not be immediately provisioned with the new bundle.
- Provisioning to the new bundle will occur only after all GPU memory clusters are terminated and the fabric becomes eligible for provisioning. Hosts that return with the old bundle will be reprovisioned again to align with the new desired bundle.

[Is a GPU memory cluster launch and terminate required to update firmware?](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/gpu-memory-fabric-pinning.htm#)

If the GPU memory fabric is already occupied by a GPU memory cluster, we recommend updating the fabric to a new firmware bundle, and then terminating the GPU memory cluster to start the firmware update.

If the fabric's`lifecycleState`
