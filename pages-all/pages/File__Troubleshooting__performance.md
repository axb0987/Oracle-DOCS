# Application Performance is Not as Expected
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/performance.htm
- Fetched: 2026-09-05 02:06 CDT

# Application Performance is Not as Expected

Learn how to troubleshoot application performance on File Storage file systems.

Several factors can impact application performance:
- 

Available bandwidth

We recommend that you use bare metal compute instances because instance bandwidth scales with the number of oCPU's. Bare metal compute instances provide the greatest bandwidth. Virtual machines (VMs) are bandwidth limited based on the number of CPUs consumed. Single oCPU VM compute instances provide the least bandwidth.
- 

Latency

Subnets can be either AD-specific or regional. The type of subnet you choose to create your File Storage resources in can affect latency. You can create File Storage resources in either type of subnet.

Regional subnets allow compute instances to connect to any mount target in the subnet regardless of AD, with no additional routing configuration. However, to minimize latency, place mount targets in the same AD as compute instances just as you would in an AD-specific subnet.

For more information, see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).
Tip  
  

If you want to verify that your instance and mount target are in the same availability domain, you can view the availability domain for any mount target on its[Details](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/managingmounttargets.htm#Details_About_Your_Mount_Target)page, in the Mount Target Information tab.

A file system is always in the same subnet as its associated mount target.

You can also view the availability domain for any[instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/instances.htm)on its Details page, in the Instance Information tab.
- 

Mount options

By not providing explicit values for mount options such as`rsize`and`wsize`
