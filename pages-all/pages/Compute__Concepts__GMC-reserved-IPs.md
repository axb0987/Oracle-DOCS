# Reserving Private IPs for GPU Memory Clusters
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/GMC-reserved-IPs.htm
- Fetched: 2026-09-05 01:48 CDT

# Reserving Private IPs for GPU Memory Clusters

You can optionally supply a fixed list of private IP OCIDs (IPv4 or IPv6) so that a GPU memory cluster uses only this declared pool of addresses for primary VNIC assignment. This is useful when you want GPU memory cluster-local addressing to stay within a predefined set of IPs across the lifecycle of the cluster: through create, repair, replacement, and growth operations.

## How It Works
- A GPU memory cluster assigns primary VNIC IPs from a predefined list of private IP OCIDs (IPv4 or IPv6) provided in the GPU memory cluster's`privateIpIds`list.

See[ComputeGpuMemoryCluster Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryCluster/).
- If an IP address becomes unavailable after IP address validation but before instance launch, the service might retry using another available IP address from the same pool.
- If no usable IP address remains, the GPU memory cluster operation can fail.
- If a customer deletes, releases, or reassigns one of the reserved private IPs in the Virtual Cloud Network (VCN) outside of a GPU memory cluster operation, future GPU memory cluster operations can fail until the configuration issue is corrected.
- Deleting a GPU memory cluster releases the cluster's reserved IP address tracking within OCI, but doesn't delete the VCN private IP objects themselves.

GPU memory cluster behavior
Scenario Behavior
Create a GPU memory cluster with valid values in`privateIpIds`. The GPU memory cluster uses only the declared IP pool for primary VNIC assignment.
Replace or repair a GPU memory cluster instance. The replacement uses an available IP address from the same declared pool.
Update a GPU memory cluster and append more IPs. Allowed if validation passes.
Update a GPU memory cluster and remove an existing IP address, such as an unused reserved IP address. Not supported.
Change or delete a reserved IP address outside of a GPU memory cluster operation. A later GPU memory cluster operation can fail if that IP address is no longer usable.

## Prerequisites

Before creating or updating a GPU memory cluster with reserved IPs:
- The private IPs (IPv4 private IP or IPv6 objects) must already exist in a VCN.
Note  
  
OCI validates the supplied IPs during API processing, but OCI doesn't create or manage those VCN private IP objects on your behalf. Instead, you create or manage these IP objects through the Cloud Console, API, CLI, SDKs, or other VCN workflows.
- All supplied private IPs must belong to the same subnet used by the GPU memory cluster instance configuration.
- The supplied list must have enough IPs to satisfy the requested cluster size.
Warning  
  
If auto-upsizing is enabled, the`privateIpIds`list must be large enough for the target size, not just the current size. For example, if`size`is 14 and`targetSize`is 18, you must provide at least 18 reserved IPs.

## Reserved IP Examples

### Create a GPU memory cluster with reserved IPs

You can create a new GPU memory cluster with reserved IPs by populating`privateIpIds`in the create payload.

Example create payload:

```

```

The create request will succeed only if the supplied list passes validation and has enough currently usable IPs for the requested operation.

The request is rejected immediately if any of the following is true:
- A private IP OCID is malformed.
- A private IP address belongs to a different subnet than the GPU memory cluster launch configuration.
- The`privateIpIds`list doesn't contain enough IPs for the requested operation.
- One or more supplied IPs don't exist or aren't valid at validation time.
- The update request attempts to remove or replace a previously declared IP address.

### Update an existing GPU memory cluster with new reserved IPs

You can update an existing reserved-IP GPU memory cluster by supplying`privateIpIds`again.
Note  
  
Only additive updates are currently supported. The update request must preserve the existing stored set of IPs and can only append new IPs. You can't remove or replace previously declared IPs, such as unused reserved IPs.

Example update payload:

```

```

## Additional Sample Commands

The following create and lookup commands are useful for creating the VCN IP object, confirming the IP object OCID, and checking that the IP address is in an expected state, such as AVAILABLE with lifetime RESERVED, before using it in a GPU memory cluster.

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).

Create an IPv4 reserved private IP address:

```

```

Create an IPv6 reserved address:

```

```

Look up an IPv4 private IP address by subnet and IP address:

```

```

Look up an IPv6 object by subnet and IP address:

```

```
