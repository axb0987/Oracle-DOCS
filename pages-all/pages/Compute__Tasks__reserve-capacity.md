# Capacity Reservations
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm
- Fetched: 2026-09-05 01:52 CDT

# Capacity Reservations

Capacity reservations allow you to reserve instances in advance so that the capacity is available for your workloads when you need it.

Capacity reservations provide the following benefits:
- Assurance that you have the capacity necessary to manage your workload. Reserved capacity is available for your tenancy to consume at any time.
- No size or time commitments. Create a reservation with as little or as much capacity as you need, and delete the reservation at any time to stop paying for it.

Capacity reservations are helpful in the following scenarios:
- 

Disaster recovery: Ensure that capacity is available when you need to failover to your secondary location.
- 

Unplanned growth : Reserve capacity as a buffer for unexpected workload spikes.
- 

Planned migrations and new launches: When you have large capacity requirements for migrations or new project launches, capacity reservations ensure that you'll have the capacity that you need.
- 

Committed capacity for long-running projects: When maintenance or seasonal adjustments cause your usage to vary, capacity reservations provide the needed capacity.

You can perform the following tasks with capacity reservations.
- [Listing Capacity Reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/listing-capacity-reservations.htm)
- [Creating a Capacity Reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-create_tabs.htm)
- [Creating a Capacity Reservation Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-create-instance_tabs.htm)
- [Getting a Capacity Reservation Details](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-get_tabs.htm)
- [Editing a Capacity Reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-editing_tabs.htm)
- [Moving a Capacity Reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-move.htm)
- [Deleting Capacity Reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-delete.htm)
- [Moving an Instance into a Capacity Reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-moving-in_tabs.htm#top)
- [Moving an Instance out of a Capacity Reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-moving-out_tabs.htm#top)
- [Adding a Capacity Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-configuration-add_tabs.htm)
- [Editing a Capacity Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-configuration-edit_tabs.htm)
- [Deleting a Capacity Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-configuration-delete_tabs.htm)
- [Viewing Capacity Configuration Resources](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-view-resources_tabs.htm)

## How Reserved Capacity Works

Capacity reservations allow you to reserve compute capacity in advance and use this capacity when you create instances against the reservation. There is no minimum time or size commitment. You can create, modify, and terminate your capacity reservation at any time. When instances that use the reserved capacity are terminated, the capacity is returned to the reservation, and the unused capacity in the reservation increases. Unused reserved capacity is metered differently than used reserved capacity. For more information, see the Oracle Compute Cloud Services section of[Oracle PaaS and IaaS Universal Credits Service Descriptions](https://www.oracle.com/assets/paas-iaas-universal-credits-3940775.pdf).

### Using Reservations

When you create your capacity reservation, you specify the availability domain in the tenancy where you want to reserve capacity. You can then add a capacity configuration, which defines the amount of space that you want to reserve and the shape to use when creating instances against that capacity configuration. Optionally, you can specify the fault domain to reserve capacity in. Each capacity reservation can have multiple capacity configurations.

To use reserved capacity, specify the reservation ID when creating an instance. The instance being created must have the same availability domain, shape, and fault domain as one of the capacity configurations in the reservation.

As an advanced option, you can create[default reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#default-capacity-reservations), which allow you to configure your capacity reservation once for the availability domain within the root tenancy and use this reservation every time you create an instance in that availability domain and tenancy.

When instances that use reserved capacity are terminated, the capacity is returned to the reservation. When instances that use reserved capacity are stopped, the capacity is held by that instance for use when that instance is restarted.

Use instance pools to create multiple instances that use reserved capacity at the same time. In the Console, the reservation is automatically applied to the instance pool based on the instance configuration. In the API, specify the capacity reservation ID in the instance configuration for the pool. As long as sufficient capacity is available, the pool creates instances using capacity from the associated reservation. You can also use the pool to simultaneously stop, start, or terminate multiple instances that use capacity from the associated reservation.

### Support and Limitations

Capacity reservations have the following limitations and restrictions:
- When you create your capacity reservation, you specify the availability domain in the tenancy where you want to reserve capacity. Reservations are specific to that availability domain and tenancy. They cannot be shared between availability domains and tenancies, and they do not span entire regions and realms.
- Capacity reservations cannot be moved from one availability domain to another, nor can they be moved from one tenancy to another.
- Capacity reservations are not available with Free Tier accounts.
- Capacity reservations are not available with confidential computing.
- Capacity reservations cannot be used with preemptible instances or with the dedicated virtual machine host feature.
- Capacity reservations do not support burstable instances.
- 

Capacity is allocated when the reservation is created. If sufficient capacity isn't available to complete the request, the capacity reservation is created with as many instances as possible.

For example, if you request 50 instances and only 40 are available, a capacity reservation with 40 instances is created. If no capacity is available, a reservation with capacity for zero instances is made. If the requested shape does not exist in the region, the reservation is not made, and an error occurs. To see how much capacity is reserved, use the[GetComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/GetComputeCapacityReservation)operation.
- Capacity reservations can have up to 50 capacity configurations. See the following known issue:[Creating more than 50 capacity configurations results in an internal error](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../known-issues.htm#capacity_reservation_error).
- After you create a capacity configuration for a flexible shape, you cannot change the number of OCPUs or amount of memory assigned to the instances in that configuration. To include instances with a different number of OCPUs or amount of memory, create new capacity configurations in the reservation.
- In order to move an instance that uses on-demand capacity into a capacity reservation, the reservation must contain a capacity configuration for that shape, and the capacity configuration must contain enough unused capacity to accommodate the instance. If the capacity configuration doesn't have sufficient capacity for the instance,[add capacity](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-configuration-edit_tabs.htm)before moving the instance into the reservation.
- Service limits and compartment quotas apply to reserved capacity. If your request for reserved capacity will exceed your[service limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm), request a service limit increase before you reserve the capacity. When viewing limits, quotas, and usage in the Console, Reservable Cores and Reservable Memory indicate the service limit. Reserved Cores and Reserved Memory indicate current usage. Capacity reservations have the following known issues with service limits:[No service category for capacity reservations when requesting service limit increases](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../known-issues.htm#servicecategor_capacityreservations)and[Capacity reservation service limits are inaccurate](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../known-issues.htm#capacityreservationlimits).
- For[shielded instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/shielded-instances.htm)and instances with[Windows Defender Credential Guard](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/shielded-instances.htm#shielded-instances-credential-guard): When creating the instance, if there is no available host in the[availability domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About)that is compatible with shielded instances or Credential Guard, the create operation will not be successful. You can try a different availability domain, wait and try the operation later, or try again without enabling the shielded instance or Credential Guard feature.
- Capacity reservations are not available with[extended memory VM instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/extended-memory-vm-instances.htm).

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The following examples shows typical policies that gives access to capacity reservations. Create the policy in the tenancy so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the autoscaling configurations in a particular compartment, specify that compartment instead of the tenancy.

Type of access: Ability to create an instance in a reservation.

```

```

Type of access: Ability to manage capacity reservations.

```

```

## Tagging Resources

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Advanced Options

In addition to the standard capacity reservation features, advanced configuration options are available, such as default capacity reservations.

### Default Capacity Reservations

With default reservations, you can configure your capacity reservation once and use this reservation every time you create an instance in the availability domain and tenancy associated with the default reservation. To create a default reservation, when you create the capacity reservation, select the option to use this reservation as the default reservation. After you create the default reservation, all instances created in that availability domain and tenancy use capacity from this reservation if possible.

Sometimes the instance cannot be created using capacity from the default reservation. For example, the reservation might not have sufficient capacity, or the user might not have permission to use the reservation. In those situations, the instance is created using[on-demand capacity](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/computeoverview.htm#capacity_types).

#### Requirements

To use default reservations:
- The default capacity reservation must be in the root compartment.
- You can only have one default reservation in each availability domain.
- You must grant users who create instances permission to use this reservation. For more information, see[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#iam_policy).

## Billing and Cost Management

When you create a reservation, you are immediately charged for the reserved resources. When you no longer need a reservation, delete the reservation to stop incurring charges. Because reservations consume resources, reserved capacity incurs charges even when the capacity is unused. Unused reserved capacity is metered differently than used reserved capacity.
- For more information about billing, see the Oracle Compute Cloud Services section of[Oracle PaaS and IaaS Universal Credits Service Descriptions](https://www.oracle.com/assets/paas-iaas-universal-credits-3940775.pdf).
- For more information, see[Compute Pricing](https://www.oracle.com/cloud/compute/pricing.html).

## Monitoring Capacity Reservations Costs and Usage

In the Console, you can access[cost and usage reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm)to see the breakdown of costs for your capacity reservation, and you can use the[cost analysis](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm)feature to track and optimize your spending.
- To view cost and usage reports: Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost and Usage Reports . For more information, see[Accessing Cost and Usage Reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/usagereportsoverview.htm#Accessing_Cost_and_Usage_Reports).
- To view cost analysis: Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost Analysis . For details instructions explaining how to work with the cost analysis tool, see[Cost Analysis Overview](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm).

In the cost and usage report, for capacity reservations, the product/Description column includes the words Capacity Reservation . If no capacity remains in the reservation because instances have been created against all of the reserved capacity, the cost for the capacity reservation is zero. Instances are billed at the standard rate for the given shape.

The report shows the bill rate per hour for each resource. Resources are aggregated by the number of cores.
- Unused reserved capacity is billed at 85%. Instances created against a capacity reservation are billed at 100%.
- If you create an instance against a capacity reservation thirty minutes into the hour, you're billed at the reserved capacity rate for the first half of the hour and at the standard rate for the second half of the hour. These rates appear as separate line items.
- When an instance is created from reserved capacity at the beginning of an hour for the whole hour, the instance is billed at the standard rate for the full hour.

For example, you have a capacity reservation with capacity for a single instance that uses one core. Fifteen minutes into the hour, you create an instance against that reservation. The cost and usage report has two lines for this reservation:
- The first line shows reserved capacity billed at 85% for 15 minutes. The number in the usage/billedQuantity column is calculated by multiplying 85% by ¼ of an hour and the number of cores.
- The second line shows a standard instance billed at 100% for 45 minutes. The number in the usage/billedQuantity column is calculated by multiplying 100% by ¾ of an hour and the number of cores.

In the cost analysis report, the bar chart shows costs associated with capacity reservations. The legend indicates which bars represent capacity reservations. If no capacity remains in the reservation because instances have been created against all of the reserved capacity, the cost for the capacity reservation is zero. Instances are billed at the standard rate for the given shape and are grouped with standard instances in the chart.

## Known Issues

- [Creating more than 50 capacity configurations results in an internal error](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../known-issues.htm#capacity_reservation_error)
- [No service category for capacity reservations when requesting service limit increases](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../known-issues.htm#servicecategor_capacityreservations)
- [Capacity reservation service limits are inaccurate](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../known-issues.htm#capacityreservationlimits)
