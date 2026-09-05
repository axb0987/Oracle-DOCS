# Configuring IMDS for Kubernetes Clusters
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringimds.htm
- Fetched: 2026-09-05 01:54 CDT

# Configuring IMDS for Kubernetes Clusters

Find out how to configure IMDS for Kubernetes clusters you've created using Kubernetes Engine (OKE).

The instance metadata service (IMDS) can provide information about compute instances hosting managed nodes in clusters you've created using Kubernetes Engine. The instance metadata service is available in two versions, version 1 and version 2. IMDSv2 offers increased security for metadata requests when compared with IMDSv1. For more information about IMDS, see[Getting Instance Metadata](https://docs.oracle.com/iaas/Content/Compute/Tasks/gettingmetadata.htm).

The image you specify for a managed node pool determines whether the compute instances hosting managed nodes in the node pool have IMDSv1 and/or IMDSv2 endpoints. If the image supports both IMDSv1 and IMDSv2, requests are allowed to both IMDSv1 and IMDSv2 endpoints by default. Where IMDSv2 is supported, we strongly recommend that you increase security by disabling requests to the IMDSv1 endpoint and only allow requests to the IMDSv2 endpoint.

To disable the IMDSv1 endpoint on compute instances hosting managed nodes when you create or update node pools that use images that support IMDSv1, see:
- [Using the CLI to disable the IMDSv1 endpoint on compute instances hosting Kubernetes worker nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringimds.htm#contengconfiguringimds_using-the-cli)
- [Confirming the IMDSv1 endpoint is disabled on compute instances hosting Kubernetes worker nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringimds.htm#contengconfiguringimds_confirming-imdsv1-disabled)

## Using the CLI to disable the IMDSv1 endpoint on compute instances hosting Kubernetes worker nodes

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

To use the CLI to disable the IMDSv1 endpoint on compute instances hosting Kubernetes worker nodes when creating a new node pool, specify`"areLegacyImdsEndpointsDisabled" : "true"`as a value of the`--node-metadata`parameter when using the`oci ce node-pool create`command. For example:
```

```

To use the CLI to disable the IMDSv1 endpoint on compute instances hosting new managed nodes when updating an existing node pool, specify`"areLegacyImdsEndpointsDisabled" : "true"`as a value of the`--node-metadata`parameter when using the`oci ce node-pool update`command. For example:
```

```

Having updated an existing node pool, the IMDSv1 endpoint is disabled on compute instances hosting new managed nodes from now on. However, note that compute instances already hosting existing managed nodes are not updated, and their IMDSv1 endpoints remain enabled.
Important  
  
Any changes you make to worker node properties will only apply to new worker nodes. You cannot change the properties of existing worker nodes. If you want the changes to take effect immediately, consider creating a new node pool with the necessary settings and shift work from the original node pool to the new node pool (see[Creating Worker Nodes with Updated Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode.htm))

## Confirming the IMDSv1 endpoint is disabled on compute instances hosting Kubernetes worker nodes

To confirm that the IMDSv1 endpoint is disabled on a compute instance hosting a Kubernetes worker node:
- Connect to the compute instance hosting the worker node using SSH. For example, by entering:`ssh opc@192.0.2.254`

For more information, see[Connecting to Managed Nodes Using SSH](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconnectingworkernodesusingssh.htm).
- Enter the following command:
```

```
