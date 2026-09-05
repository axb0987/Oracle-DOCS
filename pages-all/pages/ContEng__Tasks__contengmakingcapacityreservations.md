# Using Capacity Reservations to Provision Managed Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmakingcapacityreservations.htm
- Fetched: 2026-09-05 01:55 CDT

# Using Capacity Reservations to Provision Managed Nodes

Find out how to reserve compute capacity for clusters you've created using Kubernetes Engine (OKE).

The Compute service enables you to create capacity reservations to ensure that compute capacity is available for workloads when required during critical events, such as disaster recovery or unexpected workload spikes. For more information about how the Compute service allocates capacity, how much capacity is reserved, and how limits and quotas are applied, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm).

Having created a capacity reservation in the Compute service, you can specify that capacity reservation when using Kubernetes Engine to define a managed node pool's placement configuration. Specifying the capacity reservation ensures that the node pool's managed nodes are created using compute instances from the reserved capacity.

Note the following:
- Before you can specify a capacity reservation in a node pool's placement configuration, the capacity reservation must already exist. For steps to create a capacity reservation, see[Managing Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#reservecapacity_managing_capacity_reservations).
- Make sure that the node shape, availability domain, and fault domain in the node pool's placement configuration match the capacity reservation's instance type, availability domain, and fault domain respectively.
- If you specify multiple availability domains in a node pool's placement configuration, you can specify a different capacity reservation for each availability domain.
- Any changes you make to worker node properties only apply to new worker nodes. Updating the capacity reservation associated with a node pool does not impact the properties of existing worker nodes.

## Required IAM Policies for Using Capacity Reservations

To use a capacity reservation when defining a node pool's placement configuration, you must belong to a group that has been granted permission to use capacity reservations. To grant this permission, create the following policy:

```

```

Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format`group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format`group id <group-ocid>`.

To provision managed nodes from a capacity reservation, you must give Kubernetes Engine permission to launch instances using capacity reservations. To grant this permission, create a policy with the following policy statements:
```

```

For more information, see[Required IAM Policy](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#reservecapacity_topic-required_iam_policy).

## Default Capacity Reservations

Kubernetes Engine supports the use of default capacity reservations when launching managed nodes. With default capacity reservations, you can ensure the same capacity reservation is used every time an instance is launched in the availability domain and tenancy associated with the reservation. Having created a default capacity reservation, all instances (including managed nodes) launched in that availability domain and tenancy use capacity from the default capacity reservation where possible. For more information, see[Default Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).

There might be occasions when you do not want to provision worker nodes from a default capacity reservation. You can select an alternative capacity reservation, or choose not to use any capacity reservation at all.

## Using the Console

### Creating A Cluster and Specifying Capacity Reservations
- Follow the instructions to create a cluster using the 'Custom Create' workflow. See[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm).
- When specifying the Node placement configuration for a managed node pool in the cluster:
- Specify the first availability domain and subnet:
- Availability domain: Select the availability domain associated with the capacity reservation you intend to use.
- Worker node subnet compartment: Select the compartment in which the worker node subnet resides.
- Worker node subnet: Select the subnet associated with the capacity reservation you intend to use.
- Fault domains: (Optional) One or more fault domains in the availability domain in which to place worker nodes.
- 

Select Advanced options and specify the capacity reservation to use:
- Capacity type: Select Capacity reservation .
- 

Capacity reservation: Select the capacity reservation to use from the list. If you don't explicitly select a capacity reservation and a default capacity reservation has been created for the availability domain, the default capacity reservation is used. If you don't want to use the default capacity reservation or any other capacity reservation, select Opt out of default reservation .
- Optionally select Add row to add additional availability domains, subnets, and capacity reservations to the placement configuration. If you specify multiple availability domains in a node pool's placement configuration, you can specify a different capacity reservation for each availability domain.

### Creating A Managed Node Pool and Specifying Capacity Reservations
- On the Clusters list page, select the name of the cluster where you want to create a new node pool. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- On the Node pools tab of the cluster details page, select Add node pool to create a new managed node pool and specify the required properties for its worker nodes.
- When specifying the Node placement configuration for a managed node pool in the cluster:
- Specify the first availability domain and subnet:
- Availability domain: Select the availability domain associated with the capacity reservation you intend to use.
- Worker node subnet compartment: Select the compartment in which the worker node subnet resides.
- Worker node subnet: Select the subnet associated with the capacity reservation you intend to use.
- Fault domains: (Optional) One or more fault domains in the availability domain in which to place worker nodes.
- 

Select Advanced options and specify the capacity reservation to use:
- Capacity type: Select Capacity reservation .
- 

Capacity reservation: Select the capacity reservation to use from the list. If you don't explicitly select a capacity reservation and a default capacity reservation has been created for the availability domain, the default capacity reservation is used. If you don't want to use the default capacity reservation or any other capacity reservation, select Opt out of default reservation .
- Optionally select Add row to add additional availability domains, subnets, and capacity reservations to the placement configuration. If you specify multiple availability domains in a node pool's placement configuration, you can specify a different capacity reservation for each availability domain.

### Updating A Managed Node Pool and Specifying Capacity Reservations
- On the Clusters list page, select the name of the cluster you want to modify. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- On the Node pools tab of the cluster details page, select the name of the managed node pool you want to modify.
- Select Edit from the Actions menu.
- When specifying the Node placement configuration for a managed node pool in the cluster:
- Specify the first availability domain and subnet:
- Availability domain: Select the availability domain associated with the capacity reservation you intend to use.
- Worker node subnet compartment: Select the compartment in which the worker node subnet resides.
- Worker node subnet: Select the subnet associated with the capacity reservation you intend to use.
- Fault domains: (Optional) One or more fault domains in the availability domain in which to place worker nodes.
- 

Select Advanced options and specify the capacity reservation to use:
- Capacity type: Select Capacity reservation .
- 

Capacity reservation: Select the capacity reservation to use from the list. If you don't explicitly select a capacity reservation and a default capacity reservation has been created for the availability domain, the default capacity reservation is used. If you don't want to use the default capacity reservation or any other capacity reservation, select Opt out of default reservation .
- Optionally select Add row to add additional availability domains, subnets, and capacity reservations to the placement configuration. If you specify multiple availability domains in a node pool's placement configuration, you can specify a different capacity reservation for each availability domain.
- Save the changes.

## Using the CLI

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### Creating A Managed Node Pool and Specifying Capacity Reservations

To use the CLI to create a managed node pool that uses a capacity reservation to provision managed nodes, include the`capacityReservationId`key/value pair in the`--placement-configs`parameter.

For example:

```

```

If a default capacity reservation has been created for the availability domain in which you are creating the node pool, that capacity reservation is used by default. If you don't want to use the default capacity reservation or any other capacity reservation, set the value of the`capacityReservationId`key to be an empty string enclosed within double quotes, namely`\"capacityReservationId\":\""`.

If you specify multiple availability domains in a node pool's placement configuration, you can specify a different capacity reservation for each availability domain.

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the`placementConfigs`attribute of the`nodeConfigDetails`object to specify capacity reservations when creating or updating managed node pools.

If a default capacity reservation has been created for the availability domain in which you are creating the managed node pool, that capacity reservation is used by default. If you don't want to use the default capacity reservation or any other capacity reservation, set the value of the`capacityReservationId`field to be an empty string enclosed within double quotes, namely`"capacityReservationId":""`.
