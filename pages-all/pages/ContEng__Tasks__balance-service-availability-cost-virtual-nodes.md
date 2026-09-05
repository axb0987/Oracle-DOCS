# Balancing Service Availability and Cost When Cycling Virtual Nodes in Virtual Node Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/balance-service-availability-cost-virtual-nodes.htm
- Fetched: 2026-09-05 01:53 CDT

# Balancing Service Availability and Cost When Cycling Virtual Nodes in Virtual Node Pools

Find out how to balance service availability and cost when cycling virtual nodes in virtual node pools that you've created using Kubernetes Engine (OKE).

When cycling virtual nodes in virtual node pools, Kubernetes Engine automatically cordons existing nodes to make them unavailable, and drains the nodes.

You can tailor Kubernetes Engine behavior to meet your own requirements for service availability and cost as follows:
- You can specify the number of virtual nodes to allow to be unavailable during the operation (referred to as Maximum unavailable , or maxUnavailable for short). The greater the number of virtual nodes that you allow to be unavailable, the more virtual nodes Kubernetes Engine can update in parallel without increasing costs. However, the greater the number of virtual nodes that you allow to be unavailable, the more service availability might be compromised.
- You can specify the number of additional virtual nodes to temporarily allow during the operation (referred to as Maximum surge , or maxSurge for short). The greater the number of additional virtual nodes that you allow, the more virtual nodes Kubernetes Engine can update in parallel without compromising service availability. However, the greater the number of additional virtual nodes that you allow, the greater the cost.

For both maxUnavailable and maxSurge , you can specify the allowed number of virtual nodes as an integer, or as a percentage of the number of nodes shown in the virtual node pool's Node count property in the Console (the virtual node pool's Size property in the API).

When cycling virtual nodes, if you don't explicitly specify allowed numbers for additional nodes ( maxSurge ) and unavailable nodes ( maxUnavailable ), then the following apply:
- If you don't specify a value for either maxSurge or maxUnavailable , then maxSurge defaults to 1, and maxUnavailable defaults to 0.
- If you only specify a value for maxSurge , then maxUnavailable defaults to 0.
- If you only specify a value for maxUnavailable , then maxSurge defaults to 1.
- You cannot specify 0 as the allowed number for both additional virtual nodes ( maxSurge ) and unavailable virtual nodes ( maxUnavailable ).

Note the following:
- At the end of the operation, the number of virtual nodes in the virtual node pool returns to the number specified by the virtual node pool's Node count property shown in the Console (the virtual node pool's Size property in the API).
- When cycling virtual nodes, if you specify a value for maxSurge during the operation, your tenancy must have sufficient quota for the number of additional nodes you specify.
- When you specify a value for maxUnavailable , if the virtual node pool cannot make that number of virtual nodes unavailable (for example, due to a pod disruption budget), the operation fails.
- If you enter a percentage as the value of maxUnavailable , Kubernetes Engine rounds up the percentage to the closest integer when calculating the allowed number of virtual nodes.
- When updating large virtual node pools, be aware that the values you specify for maxUnavailable might result in unacceptably long cycle times. For example, if you specify 1 as the value for maxUnavailable when cycling the virtual nodes of a virtual node pool with 1000 nodes, Kubernetes Engine might take several days to cycle all the nodes in the node pool. If the node cycling operation does not complete within 30 days, the status of the associated work request is set to Failed . Submit another node cycling request to resume the operation.
-
