# Troubleshooting Compute
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/References/troubleshooting-compute-instances.htm
- Fetched: 2026-09-05 01:49 CDT

# Troubleshooting Compute

Use troubleshooting information to identify and address common issues that can occur while working with Compute.

## Diagnosing Issues Using the Console

Use the troubleshooting and diagnostic tool in the Console to identify and resolve issues with an instance. The tool observes the instance for some common potential issues and provides suggested troubleshooting steps.
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Click the instance that you're interested in.
- 

Click More Actions , and then click Troubleshoot instance .

The Troubleshoot instance panel displays the status of the indicators that are being observed. If an issue is detected, then the panel displays recommended troubleshooting steps that you can follow to resolve the issue.
- (Optional) To download a PDF of the troubleshooting suggestions, click Download results .

## Resources for Troubleshooting

For detailed information about how to troubleshoot issues with compute instances, see the following topics:
- [Troubleshooting the SSH Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/troubleshooting-ssh-connection.htm). If you're unable to connect to a Linux instance using a Secure Shell (SSH) connection, follow the troubleshooting steps to identify common problems.
- [Compute Instance Health Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/compute-health-metrics.htm). To determine whether an instance is responsive, use the instance accessibility status metric. Compute sends an Address Resolution Protocol (ARP) request to the instance's virtual network interface card (VNIC). If the ARP ping fails, the metric shows that the instance is unresponsive.
- [Troubleshooting Instances Using Instance Console Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm). To interactively debug issues that happen during instance launch or during the OS boot sequence, use a serial console connection or a VNC console connection.
- [Troubleshooting Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/manage-plugins-troubleshooting.htm). If the status for all Oracle Cloud Agent plugins on the Instance Details page is Invalid or you can't see any metrics in the Metrics section of the Console, confirm that Oracle Cloud Agent is installed, running, and able to communicate with Oracle services.
- [Performing a Diagnostic Reboot](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/diagnostic-reboot.htm). To troubleshoot an unreachable virtual machine (VM) instance when other troubleshooting steps aren't successful, you can rebuild the instance by performing a diagnostic reboot.
- [Sending a Diagnostic Interrupt](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/sendingdiagnosticinterrupt.htm). To debug a running VM instance that becomes unresponsive, you can generate a copy of the system memory (also called a crash dump) by sending a diagnostic interrupt to the instance.
- [Displaying the Instance Console History](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/displayingconsole.htm)
