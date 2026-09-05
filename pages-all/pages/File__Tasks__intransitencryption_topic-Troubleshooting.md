# General Troubleshooting for In-transit Encryption-enabled Mount Targets
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption_topic-Troubleshooting.htm
- Fetched: 2026-09-05 02:03 CDT

# General Troubleshooting for In-transit Encryption-enabled Mount Targets

Try the following troubleshooting techniques if you experience issues with in-transit encryption.

## Verify that you have all the security list rules set up correctly for the mount target subnet

Test the connection to the File Storage mount target using`telnet`or`nc`.
Important  
  

If these connection tests fail, verify that the network security rules are set up according to the instructions found in[Scenario C: Mount target and instance use TLS in-transit encryption](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#scenario-c).

[Testing with Telnet](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption_topic-Troubleshooting.htm#)

Run the following`telnet`commands. Replace the variables in this command with a mount target's IP address and test NFS port 2051:

```

```

A successful connection returns something such as:
```

```

A failure returns something such as:
```

```

[Testing with nc](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption_topic-Troubleshooting.htm#)

Run the following`nc`commands. Replace the variables in this command with a mount target's IP address and test NFS port 2051:

```

```

A successful connection returns something such as:
```

```

A failure returns something such as:
```

```

[Installing telnet and nc](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption_topic-Troubleshooting.htm#)

By default, many Oracle Cloud Infrastructure Compute images don't come with`telnet`and`nc`utilities installed. To install these utilities on an instance, use the following yum command:

```

```

## Verify that the oci-fss service is running for the mounted file system

If it's not, restart the service.

[To verify the service is running](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption_topic-Troubleshooting.htm#)

When you install the oci-fss-utils package, it creates three`systemd`-managed services called`oci-fss-gc.timer`,`oci-fss-init.service`and`oci-fss-monitor.service`.
- Open a terminal window on the instance.
- 

Verify that the services are running using the following commands:
```

```

The status should be active and waiting.
```

```

The status should be active and exited.
```

```

The status should be active and running.
- 

After you mount a file system using the`mount.oci-fss`command, it creates a`systemd`-managed service called`oci-fss-0 <number> .service`which is the oci-fss-forwarder process. Verify it's running by using the following command:
```

```

The status should be active and running.

[To start the service](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption_topic-Troubleshooting.htm#)

- Open a terminal window on the instance.
- 

Use the following commands to start the service:

```

```

```

```

## Verify that the namespace ns1 has been created and contains a network interface

[To verify the network namespace](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption_topic-Troubleshooting.htm#)

- Open a terminal window on the instance.
- 

Use the following command to verify the namespace and see the network interface:

```

```

You should see output displaying all the ethernet devices within namespace`ns1`. For example:
```

```

## Use the tcpdump utility to analyze traffic between the oci-fss service and the NFS client

[To obtain information using TCPDUMP](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption_topic-Troubleshooting.htm#)

- Open a terminal window on the instance.
- 

Type the following command:

```

```

## Use the journalctl command to view any messages that may have been logged by systemd regarding the service

[To obtain information from the SYSTEMD journal](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption_topic-Troubleshooting.htm#)

- Open a terminal window on the instance.
- 

Enter the following command:

```

```

`-f`displays the most recent journal entries, and prints new entries as they are appended to the journal.

`-u`specifies a specific`systemd`service unit. In this case,`oci-fss-0 <sequence_number>`is the specified unit. If no unit is specified,`journalctl`returns all`systemd`
