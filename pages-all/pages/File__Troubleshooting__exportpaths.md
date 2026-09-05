# Mount Command Fails
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/exportpaths.htm
- Fetched: 2026-09-05 02:05 CDT

# Mount Command Fails

Learn how to troubleshoot issues with file system mount commands.

Some common causes for mount command failures include:
- [Missing network security rules](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/exportpaths.htm#security-rules-connectivity)
- [Network peering configuration incorrect](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/exportpaths.htm#network-peering)
- [Missing export option](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/exportpaths.htm#missing-export)
- [Export option disallows instance](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/exportpaths.htm#mount-command-fails-due-to-export-CIDR)
- [Mount command is incorrect or includes a typo](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/exportpaths.htm#incorrect-command)
- [Mount command using an FQDN fails, but succeeds with an IP address](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/exportpaths.htm#fqdn-issue)
- [A third-party security module on the instance restricts NFS mounting](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/exportpaths.htm#mount-command-fails-due-to-third-party-agent)

## Missing network security rules

Symptom: Mount commands fail and return errors such as:
```

```

```

```

```

```

Cause: Network security rules are incorrectly set up or missing.

Solution: Test the connection to the File Storage mount target using the`telnet`,`nc`, or`ssh`utility.
Important  
  

If any of these connection tests fail, verify that the ingress and egress network security rules are set up according to the instructions found in[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm).

[Testing NFS connectivity using telnet and nc](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/exportpaths.htm#)

Testing with Telnet

Run the following`telnet`commands. Replace the variables in this command with a mount target's IP address and test NFS ports 2048, 2049, 2050, and 111 in succession:

```

```

A successful connection returns something such as:
```

```

A failure returns something such as:
```

```

Testing with nc

Run the following`nc`commands. Replace the variables in this command with a mount target's IP address and test NFS ports 2048, 2049, 2050, and 111 in succession:

```

```

A successful connection returns something such as:
```

```

A failure returns something such as:
```

```

Installing telnet and nc

By default, many Oracle Cloud Infrastructure Compute images don't come with`telnet`and`nc`utilities installed. To install these utilities on an instance, use the following yum command:

```

```

[Testing connectivity using SSH](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/exportpaths.htm#)

If policies don't allow the telnet and nc utilities to be installed, you can use the ssh utility to test connectivity. Replace the variables in this command with a mount target's IP address and test NFS ports 2048, 2049, 2050, and 111 in succession:

```

```

The response to the ssh command can help identify the possible cause of the mount failure:
- `ssh_exchange_identification: Connection closed by remote host`- this is the expected response. It indicates that instance can connect to the mount target without issue.
- `ssh: connect to host 10.0.0.5 port 2048: Connection timed out`- this response indicates an inability to connect to the mount target. Verify that the ingress and egress network security rules are set up according to the instructions found in[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm).
- `ssh: connect to host 10.0.0.6 port 2048: No route to host`- this response indicates that the mount target doesn't exist, or the provided IP address is incorrect.

[Testing NFS connectivity from a Windows instance](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/exportpaths.htm#)

Use Windows PowerShell to test connectivity from the Windows instance where you're mounting the file system.
- From the Start menu, select Windows PowerShell .
- 

Run the following command:

```

```

If the output of the preceding commands returns`TcpTestSucceeded`as`True`, the connection was successfully established. If the return is`False`, verify firewall and network security settings.
Tip  
  

You can also[use RPCINFO to check network connectivity with your mount target](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/check-mt-network-rpcinfo.htm).

UDP testing note

Ports 2048 and 111 of the mount target use the UDP protocol. Testing connectivity of UDP ports is challenging because, unlike TCP, UDP is a connectionless protocol. No clear acknowledgement is provided for sent packets.

To test connectivity to UDP ports, use a Microsoft diagnostics utility such as[PortQry](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/portqry-command-line-port-scanner-v2)or a third-party tool such as[ncat](https://nmap.org/download#windows).

For example:

```

```

Output that includes "LISTENING" or "FILTERED" indicates that the port is most likely open.

## Network peering configuration incorrect

Symptom: Mount command fails.

Cause: An issue with the peering configuration of the network between the instance and the file system is affecting connectivity. Examples of network peering include:
- Remote Peering: Same tenancy, different region
- Local Peering: Same-region, cross-tenancy
- On-premises network to Oracle Cloud Infrastructure

Solution: Verify that your network peering elements are correctly configured to allow traffic. Some examples of elements that restrict traffic are:
- Route table source and destination
- Firewall rules

If you can mount the file system from an instance within the same VCN or subnet, your connection issue is caused by your peering network configuration. For more information, see[Networking Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm).

## Missing export option

Symptom: Mount command fails with an error such as:
```

```

Cause: No export option is specified for the export you're using in the mount command.

Solution: Ensure that at least one export option exists in the export you use to mount the file system. To find out if the NFS exports are available to mount, test with the following command from your compute instance:
```

```

For more information, see[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/exportoptions.htm)and[Editing an Export and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/edit-export.htm).

## Export option disallows instance

Cause: The export option does not allow the instance where file system will be mounted.

Solution: Update the export option's source CIDR to include the intended instance. See[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/exportoptions.htm)and refer to the[Editing an Export and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/edit-export.htm)for more information.

## Mount command is incorrect or includes a typo

Symptom: Mount command fails with an error such as:
```

```
or
```

```

Cause: The information in the mount command is incorrect or there's a typo in it.

Solution: Verify that the information in your mount command is correct:
- Verify that the mount point directory exists. If not, create it.
- Verify that there's no typo in the mount point in the mount command.
- Verify that the export path in the mount command doesn't contain a typo, and the spelling and case is the same as in the export.
Tip  
  

If there's a typo in the mount point, the system reports that the mount point doesn't exist.

If there's a typo or a case mismatch in the export path, the system reports that the path doesn't exist.

The export path is specified when you create an export for the file system in a mount target. It uniquely identifies the file system within the mount target, letting you associate multiple file systems to a single mount target. The export path is appended to the mount target IP address, and used to mount the file system. For example:
```

```

In this example,`10.0.0.5:`is the mount target IP address, and`/example/path`is the export path.`/mnt/mountpointA`is the path to the directory on the client instance on which the external file system is mounted.
Tip  
  
You can find all the export paths for a file system in the Exports list shown in its[Details page](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/get-file-system-details.htm), together with associated mount target information.
- You can obtain the correct export path by copying mount commands directly from the file system export. These commands minimize the chance of a typing error. See[Getting Mount Command Samples](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingfilesystems.htm#get-mount-command-samples)for more information.
- If one file system associated with a mount target uses an export path of '/', it prevents you from associating more file systems with that mount target. No two file systems associated with the same mount target can have an export path that contains a complete path of the other.

See[Paths in File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Concepts/filesystempaths.htm)for more information.

## Mount command using an FQDN fails, but succeeds with an IP address

Symptom: Mounting a file system using an FQDN in the mount command fails, but mounting with an IP address succeeds.

Cause: If the mount target has a hostname specified, the File Storage service creates an FQDN for it and includes it in the mount command sample for the file system. Be sure that the FQDN correctly resolves to the mount target's IP address. For more information about DNS resolution, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm).

## A third-party security module on the instance restricts NFS mounting

Symptom: Mount command fails. The`[](https://man7.org/linux/man-pages/man1/dmesg.1.html)dmesg`operation displays a message like the following, which can vary depending on the module:
```

```

Cause: The security module, such as[TrendMicro Deep Security Agent](https://www.trendmicro.com/en_us/business/products/hybrid-cloud/deep-security.html), has mount hooks that can interfere with NFS.

Solution: Stop the`ds_agent`by running the following command:

```

```
