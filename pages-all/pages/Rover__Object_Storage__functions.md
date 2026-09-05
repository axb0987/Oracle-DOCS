# Running Functions on Object Storage for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/functions.htm
- Fetched: 2026-09-05 03:02 CDT

# Running Functions on Object Storage for Roving Edge Infrastructure

Describes how to assign a function to an object storage event for Roving Edge Infrastructure.

You can assign a function to an object storage event. For example, you can configure the function to update any bucket object, including the object that triggered the event. When triggered, the Events service attempts to call the function indefinitely until it succeeds. You can see pending events and the calls statistics in the Device Console. You can cancel any pending event.

- Launch the`orei-function-server-image-vi.oci`functions platform image as a virtual machine compute instance. See[Managing Instances](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/../Compute/Instance/instance_management.htm#ComputeInstanceManagement)for more information.
- Set up your functions within this instance.
- Follow the steps to begin creating an event. See[Creating an Events Rule](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/../Events/create_rule.htm#top)for more information.
- Provide a name and description for the function-based event.
- Configure the following in the Rule Conditions section of the Create Rule dialog box:

Condition : Select Event Type from the list.

Service Name : Select Object Storage from the list.

Event Type : Select Object - Create from the list.

Rule Logic : Enter the function.
- Select + Another Condition to add another function-based condition entry, or any other type of condition.
-
