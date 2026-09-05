# Sample FIO Commands for Block Volume Performance Tests on Linux-Based Instances
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm
- Fetched: 2026-09-05 01:45 CDT

# Sample FIO Commands for Block Volume Performance Tests on Linux-Based Instances

This topic describes sample FIO commands you can use to run performance tests for the Oracle Cloud Infrastructure Block Volume service on instances created from Linux-based images.

## Installing FIO

To install and configure FIO on your instances with Linux-based operating systems, run the commands applicable to the operating system version for your instance.

[Oracle Linux and CentOS](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm#)

Run the following command to install and configure FIO for your Oracle Linux or CentOS systems.
- Oracle Autonomous Linux 8.x, Oracle Linux 8.x, and Oracle Linux Cloud Developer 8:

```

```

- Oracle Autonomous Linux 7.x, Oracle Linux 7.x, CentOS 7, and CentOS Stream 8:

```

```

[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm#)

Run the following commands to install and configure FIO for your Ubuntu systems:

```

```

This applies to Ubuntu 20.04, Ubuntu 18.04, and Ubuntu Minimal 18.04.

## FIO Commands

This section includes FIO example commands.

### IOPS Performance Tests

Use the following FIO example commands to test IOPS performance. You can run the commands directly or create a job file with the command and then run the job file.

[Test random reads](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm#)

Run the following command directly to test random reads:

```

```

In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
- 

Create a job file, fiorandomread.fio, with the following:

```

```

- 
Run the job using the following command:

```

```

[Test file random read/writes](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm#)

Run the following command against the mount point to test file read/writes:

```

```

Add both the read IOPS and the write IOPS returned.

[Test random read/writes](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm#)

Caution  
  
Do not run FIO tests with a write workload (`readwrite`,`randrw`,`write`,`trimwrite`) directly against a device that is in use.

Run the following command to test random read/writes:

```

```

Add both the read IOPS and the write IOPS returned.

In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
- 

Create a job file, fiorandomreadwrite.fio, with the following:

```

```

- 
Run the job using the following command:

```

```

[Test sequential reads](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm#)

For workloads that enable you to take advantage of sequential access patterns, such as database workloads, you can confirm performance for this pattern by testing sequential reads.

Run the following command to test sequential reads:

```

```

In some cases you may see more consistent results if you use a job file instead of running the command directly. Use the following instructions for this approach:
- 

Create a job file, fioread.fio, with the following:

```

```

- 
Run the job using the following command:

```

```

### Throughput Performance Tests

Use the following FIO example commands to test throughput performance.

[Test random reads](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm#)

Run the following command to test random reads:

```

```

In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
- 

Create a job file, fiorandomread.fio, with the following:

```

```

- 
Run the job using the following command:

```

```

[Test file random read/writes](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm#)

Run the following command against the mount point to test file read/writes:

```

```

Add both the read MBPs and the write MBPs returned.

[Test random read/writes](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm#)

Caution  
  
Do not run FIO tests with a write workload (`readwrite`,`randrw`,`write`,`trimwrite`) directly against a device that is in use.

Run the following command to test random read/writes:

```

```

Add both the read MBPs and the write MBPs returned.

In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
- 

Create a job file, fiorandomread.fio, with the following:

```

```

- 
Run the job using the following command:

```

```

[Test sequential reads](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm#)

For workloads that enable you to take advantage of sequential access patterns, such as database workloads, you can confirm performance for this pattern by testing sequential reads.

Run the following command to test sequential reads:

```

```

In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
- 

Create a job file, fioread.fio, with the following:

```

```

- 
Run the job using the following command:

```

```

### Latency Performance Tests

Use the following FIO example commands to test latency performance. You can run the commands directly or create a job file with the command and then run the job file.

[Test random reads for latency](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm#)

Run the following command directly to test random reads for latency:

```

```

In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
- 

Create a job file, fiorandomreadlatency.fio, with the following:

```

```

- 
Run the job using the following command:

```

```

[Test random read/writes for latency](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm#)

Caution  
  
Do not run FIO tests with a write workload (`readwrite`,`randrw`,`write`,`trimwrite`) directly against a device that is in use.

Run the following command directly to test random read/writes for latency:

```

```

In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
- 

Create a job file, fiorandomrwlatency.fio, with the following:

```

```

- 
Run the job using the following command:

```

```
