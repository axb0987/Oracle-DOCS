# Dedicated Virtual Machine Hosts
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm
- Fetched: 2026-09-05 01:48 CDT

# Dedicated Virtual Machine Hosts

Dedicated virtual machine hosts let you run Oracle Cloud Infrastructure Compute virtual machine (VM) instances on dedicated servers that are a single tenant and not shared with other customers. Use dedicated virtual machine hosts to meet compliance and regulatory requirements for isolation that prevent you from using shared infrastructure. You can also use dedicated virtual machine hosts to meet node-based or host-based licensing requirements that require you to license an entire server.

## Managing Dedicated Virtual Machine Hosts

For steps to manage dedicated virtual machine hosts, see the following topics.
- [Listing Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Listing_a_Dedicated_Virtual_Machine_Host.htm)
- [Creating a Dedicated Virtual Machine Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Creating_a_Dedicated_Virtual_Machine_Host.htm)
- [Getting a Dedicated Virtual Machine Host Details](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh-get_tabs.htm)
- [Placing Instances on a Dedicated Virtual Machine Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Placing_an_Instance_on_a_Dedicated_Virtual_Machine_Host.htm)
- [Changing the Shape of an Instance on a Dedicated Virtual Machine Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh_changing_shape_dedicated_virtual_machine_host.htm)
- [Managing On-Demand Reboot Migration for Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_migrating-on-demand.htm)
- [Managing Maintenance Reboot Migration for Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-infrastructure-maintenance.htm)
- [Migrating Dedicated Virtual Machine Host Instances with Manual Migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_manual-migration.htm)
- [Moving a Dedicated Virtual Machine Host to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh-move_tabs.htm)
- [Deleting Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Deleting_a_Dedicated_Virtual_Machine_Host.htm)

## Support and Limitations

Shapes and capacity: When you create a dedicated virtual machine host, you select a[shape for the dedicated virtual machine host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../References/computeshapes.htm#dedicatedvmhost). The shape determines how much capacity is available and what types of instances can be launched on the host. Note that there is a difference between the number listed for billed OCPUs compared to available OCPUs. This is because some OCPUs are reserved for virtual machine management.

When you launch an instance on a dedicated virtual machine host, you can choose any of the[VM shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../References/computeshapes.htm#vmshapes)that are supported for that host.

You can mix VM instances with different supported shapes on the same dedicated virtual machine host. The size of each instance might impact the maximum number of instances that you can place on the dedicated virtual machine host. For more information, see[Optimizing Capacity on a Dedicated Virtual Machine Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm#optimize-capacity).

Billing: You are billed for the dedicated virtual machine host as soon as you create it, but you are not billed for any of the individual VM instances you place on it. You will still be billed for image licensing costs if they apply to the image you are using for the VM instances.

Unsupported features: Most of the Compute features for VM instances are supported for instances running on dedicated virtual machine hosts. However, the following features are not supported:
- Autoscaling
- Burstable instances
- Capacity reservations
- Instance pools
- Live migration (You can use[reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_migrating-on-demand.htm)or[manual migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_manual-migration.htm)instead.)

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The simplest policy to enable users to work with dedicated virtual machine hosts is listed in[Let users manage Compute dedicated virtual machine hosts](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#dvhLaunch). It gives the specified group access to launch instances on dedicated virtual machine hosts and manage dedicated virtual machine hosts.

See[Let users launch Compute instances on dedicated virtual machine hosts](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#dvhLaunch)for an example of a policy that allows users to launch instances on dedicated virtual machine hosts without giving them full administrator access to dedicated virtual machine hosts.

## Auditing your Dedicated Virtual Machine Host

To fully meet requirements for some compliance scenarios, you might be required to validate that your instances are running on a dedicated virtual machine host and not using shared infrastructure. The Oracle Cloud Infrastructure Audit service provides you with the functionality to do this. Use the steps described in[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm)to access the log events for the dedicated virtual machine host.

The section on searching log events walks you through how to retrieve the log events with the data you need to verify that your instances are running on a dedicated virtual machine host. For this procedure:
- Ensure that you select the dedicated virtual machine host's compartment and not the compartment for the instances that are hosted on it.
- Use the dedicated virtual machine host's OCID as the search keyword.

After you have retrieved the log events for the dedicated virtual machine host, view the log event lower-level details, and check the contents of the`responsePayload`property. This property should contain the OCIDs for the instances that are running on the dedicated virtual machine host.

## Monitoring a Dedicated Virtual Machine Host Metrics from the Console

You can monitor the health and performance metrics of a dedicated virtual machine host from the Console.

### View Dedicated Virtual Machine Host Metrics

To see the available metric graphs for a host, navigate to the host and select the metric namespace.
- Open the navigation menu.
- Click Compute .
- Under Compute , click Dedicated Virtual Machine Hosts .
- If no compartment is selected, select a compartment.
- Select the name of the host to be monitored.
- Under Resources , click Metrics .
- Under Metric Namespace , select from one of the two Dedicated Virtual Machine Hosts metric namespaces:
- oci_computeagent: Metrics related to the activity level and throughput of compute instances, as emitted by the Compute Instance Monitoring plugin. See[Compute Instance Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../References/computemetrics.htm#Compute_Instance_Metrics). To enable monitoring for compute instance metrics, see[Enabling Monitoring for Compute Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/enablingmonitoring.htm#Enabling_Monitoring_for_Compute_Instances).
- oci_compute_infrastructure_health: Metrics related to the up/down status, health, and maintenance status of instances. This namespace focuses on the underlying infrastructure for instances. See[Infrastructure Health Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../References/infrastructurehealthmetrics.htm#Infrastructure_Health_Metrics).

### View the Status and Health of Instances on the Host

To view the health and performance metrics reports for individual virtual machine instances on the host, navigate to the Hosted Instances view.
- Open the navigation menu.
- Click Compute .
- Under Compute , click Dedicated Virtual Machine Hosts .
- If no compartment is selected, select a compartment.
- Select the name of the host to be monitored.
- Under Resources , click Hosted Instances .

All the instances running on this host are listed. There are two key columns.
- The State column displays the running state for each instance.
- The Metric column displays the health of the instance. If an instance has an issue, an alert icon is placed in the column. Click the down arrow icon to the left of the instance name to expand the inline view of the metrics reports for that instance.

## Optimizing Capacity on a Dedicated Virtual Machine Host

When designing your cloud footprint, we recommend that you plan to always launch the largest instance first. Here's why:

When you place instances on a dedicated virtual machine host, Oracle Cloud Infrastructure launches the instances in a manner to optimize performance. For example, a dedicated virtual machine host created based on the DVH.Standard2.52 shape has two sockets with 24 cores configured per socket. Instances are placed so that each instance will only use resources that are local to a single physical socket. In scenarios where you are creating and terminating instances with a mix of shapes, this can result in an inefficient distribution of resources, meaning that not all OCPUs on a dedicated virtual machine host are available to be used. It might appear that a dedicated virtual machine host has enough OCPUs to launch an additional instance, but the new instance will fail to launch because of the distribution of existing instances.

Continuing this example, say that you want to launch instances using a shape with 16 OCPUs. On a DVH.Standard2.52 dedicated virtual machine host, you can only launch a maximum of two instances with 16 OCPUs. You cannot launch a third instance with 16 OCPUs, even though the dedicated virtual machine host has 16 remaining OCPUs. You can, however, launch additional instances using shapes with a smaller number of OCPUs.

What this means is, when you're placing an instance on a dedicated virtual machine host, you can only create the instance if the host has sufficient capacity based on the shape of the instance. In the Console, you can only choose from the hosts with sufficient capacity. Similarly, when you place an instance on a dedicated virtual machine host using the API, CLI, or SDKs, the operation will succeed only if the dedicated virtual machine host has sufficient capacity.

If you have a dedicated virtual machine host that doesn't have enough capacity to launch instances, you can do any of the following things:
- Delete (terminate) instances you no longer need on the dedicated virtual machine host to make capacity available.
- Choose a different, smaller shape for the instance you are trying to place on the dedicated virtual machine host.
-
