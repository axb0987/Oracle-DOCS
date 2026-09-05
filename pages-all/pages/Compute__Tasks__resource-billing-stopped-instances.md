# Resource Billing for Stopped Instances
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resource-billing-stopped-instances.htm
- Fetched: 2026-09-05 01:52 CDT

# Resource Billing for Stopped Instances

When you stop an Oracle Cloud Infrastructure Compute instance, billing for the stopped instance depends on the shape that you used to create the instance.
- Standard shapes: Stopping an instance pauses billing. However, stopped instances continue to count toward your service limits.
- Dense I/O shapes: Billing continues for stopped instances because the NVMe storage resources are preserved. Related resources continue to count toward your service limits. To halt billing and remove related resources from your service limits, you must[terminate the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm).
- 

GPU shapes: For VM instances that use shapes in the VM.GPU.A10 series, stopping an instance pauses billing. However, stopped instances continue to count toward your service limits.

For all other GPU shapes, billing continues for stopped instances because GPU resources are preserved. Related resources continue to count toward your service limits. To halt billing and remove related resources from your service limits, you must[terminate the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm).
- HPC shapes: Billing continues for stopped instances because the NVMe storage resources are preserved. Related resources continue to count toward your service limits. To halt billing and remove related resources from your service limits, you must[terminate the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm).
- 

Optimized shapes: For VM instances, stopping an instance pauses billing. However, stopped instances continue to count toward your service limits.

For bare metal instances, billing continues for stopped instances because the NVMe storage resources are preserved. Related resources continue to count toward your service limits. To halt billing and remove related resources from your service limits, you must[terminate the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm).

Shutting down an instance[using the instance's OS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-stop-instance.htm#operatingsystem)does not stop billing for that instance. If you shut down an instance this way, be sure to also stop it from the Console or API.

For steps to stop an instance, see[Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm). For more information about shapes, see[Compute Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm).

For more information about Compute pricing, see[Compute Pricing](https://www.oracle.com/cloud/compute/pricing.html). For more information about how instances running Microsoft Windows Server are billed when they are stopped, see[How am I charged for Windows Server on Oracle Cloud Infrastructure?](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/microsoftlicensing.htm#generalquestions__pricing-for-win-server)
