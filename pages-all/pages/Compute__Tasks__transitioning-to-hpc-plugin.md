# Enabling GPU metrics with the OCA HPC plugin
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/transitioning-to-hpc-plugin.htm
- Fetched: 2026-09-05 01:52 CDT

# Enabling GPU metrics with the OCA HPC plugin

You can enable GPU metrics with the Oracle Cloud Agent High Performance Computing plugin on your instances.

Current OCI HPC package New OCA plugin Description
oci-cn-auth Compute HPC RDMA Authentication

oci-rdma-authentication Configures RDMA/RoCE network interfaces with QoS, MTU, etc. settings and maintains authentication.
oci-hpc-mlx-configure Compute HPC RDMA Auto-Configuration

oci-hpc-configure Configures Mellanox ConnectX-5 firmware and PCIE settings.
oci-hpc-rdma-configure Compute HPC RDMA Auto-Configuration

oci-hpc-configure Configures RDMA interface ip addresses.
oci-hpc-dapl-configure Compute HPC RDMA Auto-Configuration

oci-hpc-configure Configure legacy MPI DAPL oci-dat.conf.
Note  
  
You can transition from python-based solutions to use the Oracle Cloud Agent High Performance Computing plugin.

## Enabling Compute HPC RDMA Authentication and Auto-Configuration on an Existing Instance
To enable HPC RDMA authentication and auto-configuration on a host that is running the current OCI HPC packages, follow these steps.
Note  
  
Do not perform this workflow on a running workload. These actions can be disruptive and result in data loss.
- 

Determine which version of Oracle Cloud Agent is installed. Version 1.35.0 or above is required. If the version is not 1.35.0 or above, contact support to obtain the installation package.

OL7/8
```

```

Ubuntu
```

```

- 

Stop the existing oci-cn-auth services.
```

```

- 

Verify that oci-cn-auth is stopped.
```

```

- 

Stop the wpa_supplicant services.
```

```

- 

Verify that wpa_supplicant service are stopped.
```

```

- 

Remove the oci-cn-auth, oci-hpc-rdma-configure, oci-hpc-mlx-configure, and oci-hpc-dapl-configure package, if installed.

OL7/8
```

```

Ubuntu20
```

```

- 

Verify that the agent is enabled and running.

OL7/8
```

```

Ubuntu20
```

```

- 

Download the current agent configuration on the instance. See[Managing Plugins](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)for information on how to enable the plugin.
```

```

- 

Modify the agent-config.json to enable one or more plugins.
```

```

- 

Use the OCI ZCLI or OCI SDK to update the agentConfig for the instance.
```

```

- 

Verify that OCA plugin is enabled for the instance via the command line of the SDK.
```

```

- 

Verify that the plugin is running. It takes several minutes for the agentConfig changes to populate to the Oracle Cloud Agent.
```

```

- 

Confirm that all RDMA network interfaces have a wpa_supplicant
```

```

## Launching instance with HPC RDMA Authentication plug-in enabled

Provided the custom image has Oracle Cloud Agent 1.35.0 or above and the OCI HPC packages are not present, the LaunchInstanceDetails is used to apply the agentConfig with the plug-in enabled. OS must have the NVIDIA GPU drivers and Mellanox OFED drivers installed.

For more information, see[Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm).

## Enabling RDMA GPU monitoring

With Oracle Cloud Agent 1.35.0 new functionality to monitor RDMA and GPU is available. To enable this functionality on an existing instance do the following:
- 

Download the current agent configuration on the instance. The sections below are only one way of enabling the plug-in. For more information, see[Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm).
```

```

- 

Modify the json by adding the "Compute RDMA GPU Monitoring".
```

```

- 

Use the OCI CLI or OCI SDK to update the agentConfig for the instance.
```

```

## Required policies for RDMA GPU monitoring

If you use a private VPN, you need Service Gateway. If you use a public internet gateway, Service Gateway is not required.

For information on how to use the Monitoring service, see[Securing Monitoring](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm).

Create a dynamic group

This example creates a group that contains all instances in a specific compartment.
```

```

Create a policy

Create a policy using the dynamic group to allow to instances to publish metrics. The HPC monitoring plug-in creates 2 custom namespaces that are billed:
- `gpu_infrastructure_health`
- `rdma_infrastructure_health`
```

```

For information on how to publish custom metrics to the Monitoring service, see[Publishing Custom Metrics](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm)
