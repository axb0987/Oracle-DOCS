# Displaying the Instance Console History
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm
- Fetched: 2026-09-05 01:51 CDT

# Displaying the Instance Console History

You can capture and display recent serial console data for an instance. The data includes configuration messages that occur when the instance boots, such as kernel and BIOS messages, and is useful for checking the status of the instance or diagnosing and troubleshooting problems.

The console history captures up to a megabyte of the most recent serial console data for the specified instance. Note that the raw console data, including multi-byte characters, is captured.

The console history is a point-in-time record. To troubleshoot a malfunctioning instance using an interactive console connection, use a[serial console connection or a VNC console connection](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/serialconsole.htm).

On the instance details page in the Console, perform the following tasks to look at the console history.
- [Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/list-instances-displayingconsole.htm)
- [Capturing the Instance Console History](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-capturing.htm)
- [Downloading the Instance Console History](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-downloading.htm)
- [Viewing the Instance Console History](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-viewing.htm)
- [Editing an Instance Console History Log](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-editing.htm)
- [Deleting an Instance Console History Log](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-deleting.htm)

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances)includes the ability to manage console history data. If the specified group doesn't need to launch instances or attach volumes, you could simplify that policy to include only`manage instance-family`, and remove the statements involving`volume-family`and`virtual-network-family`.

## Tagging Resources

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
