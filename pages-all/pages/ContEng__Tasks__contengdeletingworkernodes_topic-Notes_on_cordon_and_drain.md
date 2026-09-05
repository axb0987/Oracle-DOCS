# Cordoning and Draining Managed Nodes Before Shut Down or Termination
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm
- Fetched: 2026-09-05 01:55 CDT

# Cordoning and Draining Managed Nodes Before Shut Down or Termination

Find out about setting cordon and drain options with Kubernetes Engine (OKE).

## Cordoning

Cordoning is the name given to marking a worker node in a Kubernetes cluster as unschedulable. Cordoning a worker node prevents the kube-scheduler from placing new pods onto that node, but doesn't affect existing pods on the node. Cordoning a worker node is a useful preparatory step before performing administrative and maintenance tasks. For example:
- Before terminating a node to perform tasks such as deleting a node, scaling down a node pool, changing placement configuration, and terminating and replacing a node.
- Before shutting down a node to perform tasks such as rebooting a node and replacing a node's boot volume.

For more information about cordoning, see[Manual Node Administration](https://kubernetes.io/docs/concepts/architecture/nodes/#manual-node-administration)in the Kubernetes documentation.

## Draining

Draining is the name given to safely evicting pods from a worker node in a Kubernetes cluster. Safely evicting pods ensures the pod's containers terminate gracefully and perform any necessary cleanup. For more information, see[Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node)and[Termination of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination)in the Kubernetes documentation.

## Pod disruption budgets

Pod disruption budgets are a Kubernetes feature to limit the number of concurrent disruptions that an application experiences. Using pod disruption budgets ensures high application availability whilst at the same time enabling you to perform administrative and maintenance tasks on worker nodes. Pod disruption budgets can prevent pods being evicted when draining worker nodes. For more information, see[Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb)in the Kubernetes documentation.

## Cordon and drain options

When you perform administrative and maintenance tasks (such as deleting a node, scaling down a node pool, changing placement configuration, rebooting a node, replacing a node's boot volume, and terminating and replacing a node), you can use the following Cordon and drain options to specify when and how worker nodes are shut down or terminated:
- Eviction grace period (mins): The length of time to allow to cordon and drain worker nodes before shutting down or terminating them. Either accept the default (60 minutes, which is the maximum), or specify an alternative. For example, when scaling down a node pool or changing its placement configuration, you might want to allow 30 minutes to cordon worker nodes and drain them of their workloads. To shut down or terminate worker nodes immediately, without cordoning and draining them, specify 0 minutes.
- Force terminate after grace period: Whether to shut down or terminate worker nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. By default, this option is not selected.

Node pools containing worker nodes that couldn't be shut down or terminated within the eviction grace period have the Needs attention status. See[Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm).
- Force action after grace period: When performing maintenance tasks on worker nodes (such as rebooting a node, and replacing a node's boot volume), whether to perform the action at the end of the eviction grace period, even if the worker node hasn't been successfully cordoned and drained. By default, this option isn't selected.

### Node pools with a "Needs attention" status

A node pool with the Needs attention status indicates that one or more of the worker nodes in the node pool failed to evict all the pods running on it within the eviction grace period. The status of the work request that initiated the termination operation is set to Failed . You can view the reason for the failure, including the specific pods that cannot be evicted, in the work request logs (see[Viewing Work Requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm)). There are a number of possible reasons why a pod cannot be evicted, including restrictive pod disruption budgets. For more information, see[Scheduling, Preemption and Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/)in the Kubernetes documentation.

To resolve a node pool's Needs attention status and terminate affected worker nodes, do either of the following actions:
- Re-issue the original command and select the Force terminate after grace period option. Nodes are terminated at the end of the eviction grace period, even if they have not been successfully cordoned and drained.
- Examine the work request log to determine the reason for the eviction failure, address the reason (for example, by creating a less restrictive pod disruption budget), and re-issue the original command.

#### Using the CLI to resolve a node pool's "Needs attention" status

To use the CLI to resolve a node pool's Needs attention status and terminate affected worker nodes, enter:

```

```

where`--node-pool-id <nodepool-ocid>`is the OCID of the node pool with the Needs attention status.

For example:
```

```

The response to the command lists worker nodes currently in a node-error state, along with an explanation. For example:
```

```

In this example, you can see that a pod could not be evicted from the worker node within the eviction grace period. As a result, the worker node could not be terminated. It is your responsibility to identify why the pod could not be evicted, and then to fix the underlying problem. For example, by creating a less restrictive pod disruption budget.

Having fixed the problem, you can go ahead and retry the operation.

You can force the termination of a worker node without cordoning and draining the worker node, and without rectifying the underlying problem, by including the`--override-eviction-grace-duration PT0M`parameter in the command to set the eviction grace period to 0 minutes.

For example, when deleting a node, you can force the termination of the node without cordoning and draining it by entering:
```

```

## Node pools with quantityPerSubnet set to 1 or more

When creating and updating node pools in earlier Kubernetes Engine releases, you specified how many worker nodes you wanted in a node pool by entering a value for the Quantity per subnet property (`quantityPerSubnet`in the API).

In more recent Kubernetes Engine releases, you specify how many worker nodes you want in a node pool by entering a value for the Number of Nodes property (`size`in the API).

Note that you can only shut down or terminate specific worker nodes (and select Cordon and drain options) in node pools that have Quantity per subnet (`quantityPerSubnet`) set to zero or null. To shut down or terminate specific worker nodes (and select Cordon and drain options) from an older node pool that has Quantity per subnet (`quantityPerSubnet`) set to 1 or more, you must first set Quantity per subnet (`quantityPerSubnet`) to zero or null. Having set Quantity per subnet (`quantityPerSubnet`) to zero or null, you can then specify the number of worker nodes by entering a value for Number of Nodes (`size`) instead. From that point onwards, you can shut down or terminate specific worker nodes (and select Cordon and drain options).

To find out the value of Quantity per subnet (`quantityPerSubnet`) for a node pool, enter the following command:

```

```
