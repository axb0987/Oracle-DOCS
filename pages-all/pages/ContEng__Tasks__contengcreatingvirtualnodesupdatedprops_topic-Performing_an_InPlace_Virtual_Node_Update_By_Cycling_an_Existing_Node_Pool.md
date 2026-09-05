# Performing an In-Place Virtual Node Update by Cycling Virtual Nodes in an Existing Virtual Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodesupdatedprops_topic-Performing_an_InPlace_Virtual_Node_Update_By_Cycling_an_Existing_Node_Pool.htm
- Fetched: 2026-09-05 01:55 CDT

# Performing an In-Place Virtual Node Update by Cycling Virtual Nodes in an Existing Virtual Node Pool

Find out how to update the properties of virtual nodes in a virtual node pool by changing properties of the existing node pool, and then cycling the virtual nodes to terminate and replace them, using Kubernetes Engine (OKE).

You can update the properties of virtual nodes in a virtual node pool by changing properties of the existing virtual node pool, and then cycling the nodes to terminate and replace them.

If a cycling operation fails, it is safe to retry the operation. Kubernetes Engine detects which virtual nodes are already running the new configuration and only cycles the virtual nodes that are still running the older configuration.

## Balancing service availability and cost when cycling virtual nodes in virtual node pools

When you cycle virtual nodes to terminate and replace them, Kubernetes Engine cordons and drains the virtual nodes using two strategies:
- Create new (additional) nodes, and then remove existing nodes: Kubernetes Engine adds an additional node (or nodes) to the node pool with updated properties. When the additional node is active, Kubernetes Engine cordons an existing node, drains the node, and removes the node from the node pool. This strategy maintains service availability, but costs more.
- Remove existing nodes, and then create new nodes: Kubernetes Engine cordons an existing node (or nodes) to make it unavailable, drains the node, and removes the node from the node pool. When the node has been removed, Kubernetes Engine adds a new node to the node pool to replace the node that has been removed. This strategy costs less, but might compromise service availability.

To tailor Kubernetes Engine behavior to meet your own requirements for service availability and cost, control and balance the two strategies by specifying values for maxSurge and maxUnavailable . For more information, see[Balancing Service Availability and Cost When Cycling Virtual Nodes in Virtual Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/balance-service-availability-cost-virtual-nodes.htm).

## Using the CLI

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### To perform an 'in-place' virtual node update by cycling nodes

Use the[oci ce virtual-node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/update.html)command to specify the virtual node property that you want to change. Include the`--virtual-node-pool-cycling-details`parameter in the command to specify that you want to cycle virtual nodes to terminate and replace them, optionally specifying a maximum allowed number of new nodes that can be created during the update operation, and a maximum allowed number of nodes that can be unavailable:
```

```

where`--<property-to-update> <new-value>`is a new value for a virtual node pool property. Note that you must change at least one virtual node pool property for the update command to run. The specific property can be any valid property that you want to update.

Monitor the progress of the operation by viewing the status of the associated work request:
```

```

```

```

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[UpdateVirtualNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/UpdateVirtualNodePool)
