# Confidential Computing
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/References/confidential_compute.htm
- Fetched: 2026-09-05 01:49 CDT

# Confidential Computing

Confidential computing encrypts and isolates data in use (data actively processed in memory) and the applications processing that data. Confidential instances are Compute virtual machines (VMs) or bare metal instances where data and application execution are protected while the workload runs, helping prevent unauthorized access to or modification of in-memory data.

On OCI, confidential VMs use AMD Secure Encrypted Virtualization (SEV-family). Encryption keys are generated at VM creation and held in the AMD Secure Processor; these keys aren’t accessible to applications, the guest, the hypervisor, or OCI.

## Core Concepts

When working with confidential Compute instances, consider the following core concepts.

### Trusted Execution Environment (TEE)

A Trusted Execution Environment (TEE) is an isolated execution boundary that helps protect code and data while they are being processed.In OCI confidential computing, TEEs are achieved using hardware-backed memory encryption and isolation mechanisms.

### Confidential VMs vs Confidential Bare Metal (clarification)

Confidential VMs provide VM-scoped isolation and encryption for each VM, while Confidential Bare Metal provides host memory encryption as a foundation. Bare metal confidentiality alone does not automatically provide a VM-scoped TEE or a tenant-facing remote attestation flow for guest VMs.

### VM-scoped confidential computing (Confidential VMs)

VM-scoped confidential computing provides per-VM isolation and memory encryption using AMD SEV technology.

Newer AMD shapes support SEV-SNP, which adds stronger memory integrity protections and enables hardware-backed attestation.

### Bare metal confidential computing (Confidential Bare Metal)

When a customer enables confidential computing on bare metal, OCI uses AMD Transparent Secure Memory Encryption (TSME) to encrypt host memory.

With the platform booted in confidential mode (confidential-enabled BIOS/firmware), customers can build a VM-scoped TEE on top of confidential-capable bare metal using the supported firmware capabilities:
- E3/E4: VM-scoped SEV (no SEV-SNP)
- E5/E6: VM-scoped SEV-SNP (BIOS/firmware support for SEV-SNP enablement is applicable to E5 and E6 bare metal shapes)

## Bring Your Own Attestation Service (BYAS)

Attestation provides cryptographic proof that a workload is running in the expected confidential environment before releasing secrets (for example, keys, tokens, or datasets).

OCI supports Bring Your Own Attestation Service (BYAS) for E5/E6 SEV-SNP shapes, where customers deploy and operate their own attestation service using OCI guidance. BYAS attests the confidential VM environment (VM-scoped TEE state), not merely the bare metal host, and is typically used to gate secret release based on verification results. BYAS is not supported for legacy E3/E4 shapes. See[Remote Attestation for Confidential Computing](https://docs.oracle.com/iaas/oracle-linux/oci/security-attestation.htm).

## Support Matrix (Shapes, SEV/SEV-SNP, OS, Regions)

The following table provides details on supported shapes and related technologies.
Note  
  
"VM technology" indicates the VM-scoped confidential capability (SEV vs SEV-SNP).

SHAPE(S) DEPLOYMENT VM TECHNOLOGY BYAS SUPPORTED OS REGIONS
VM.Standard.E3.Flex, VM.Standard.E4.Flex VM SEV (no SNP) No Oracle Linux 7+, Ubuntu 20+ Australia East (Sydney), Canada Southeast (Toronto), Germany Central (Frankfurt), India South (Hyderabad), India West (Mumbai), UK South (London), UK West (Newport), US East (Ashburn), US West (Phoenix)
BM.Standard.E3.128, BM.Standard.E4.128, BM.DenseIO.E4.128 BM Supports customer-built VM-scoped SEV No Oracle Linux 7+, Ubuntu 20+ All OC1 public regions
VM.Standard.E5.Flex VM SEV-SNP Yes Oracle Linux 9 (UEK8), Oracle Linux 10 (UEK8), Ubuntu 24.04 All OC1 public regions except ZRH/SIN/ORD
VM.Standard.E6.Flex VM SEV-SNP Yes Oracle Linux 9 (UEK8), Oracle Linux 10 (UEK8), Ubuntu 24.04 All OC1 public regions
BM.Standard.E5.192, BM.DenseIO.E5.128, BM.Standard.E6.256 BM Supports customer-built VM-scoped SEV-SNP Yes Oracle Linux 9 (UEK8), Oracle Linux 10 (UEK8), Ubuntu 24.04 All OC1 public regions

For enabling Confidential Computing on VM Shapes with Oracle Linux, refer to[Confidential Computing For Oracle Linux](https://docs.oracle.com/iaas/oracle-linux/oci/confidential-computing.htm).

## Pricing and availability

- There is no additional cost to enable Confidential Computing.
- Availability varies by shape (see table).

## Performance

Confidential Computing is designed to provide strong in-use protections with minimal performance impact for many workloads. For more details see:[Performance Impact of Enabling Confidential Computing on Oracle Cloud Infrastructure VMs](https://blogs.oracle.com/cloud-infrastructure/perf-impact-of-confidential-computing-on-oci-vms).

## Support and limitations

The following is a list of support details and limitations for confidential computing.
- Confidential Computing must be enabled at launch and can't be turned on/off after instance’s creation.
- Confidential Computing E5 and E6 VMs can be launched on[Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Concepts/dedicatedvmhosts.htm).
- After you enable confidential computing on an instance, you can only edit the name of the instance. You can't change the shape of the instance.
- Shielded Instances and Confidential Computing are mutually exclusive (you can't enable both).
- The following features aren't available with confidential computing:
- Preemptible capacity
- Capacity reservations
- Shielded instances

## Enabling Confidential Computing

To enable confidential computing for an instance, follow these steps.
- Select a supported Bare Metal or VM shape in OCI which can be enabled for confidential computing.
- During the instance creation workflow, ensure the Enable Confidential Computing option is selected in the shape configuration.
- Complete all other instance configuration as needed, including networking, platform image, and boot volume settings. Then start the instance. See[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/launchinginstance.htm)
