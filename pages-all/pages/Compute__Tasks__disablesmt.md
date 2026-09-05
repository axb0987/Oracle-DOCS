# Disabling Simultaneous Multithreading
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/disablesmt.htm
- Fetched: 2026-09-05 01:51 CDT

# Disabling Simultaneous Multithreading

You can disable simultaneous multithreading (SMT) on your instances through the console or by using CLI commands.

- For bare metal instances, optionally[configure advanced BIOS settings](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/bios-settings.htm), such as disabling simultaneous multithreading, disabling cores, or optimizing the NUMA settings. Click Show advanced BIOS settings , and then select the options that you want to configure. The settings that are available depend on the shape.
- For virtual machine instances, if you want to disable simultaneous multithreading, click Show advanced OCPU options , and then uncheck Enable simultaneous multithreading (SMT) . Simultaneous multithreading is enabled by default.

See[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)for more information.

Confirming SMT Status

To confirm the status of SMT on your instance, follow the steps outlined below. The threads per core indicate whether SMT is on or off. If there is one thread per core, SMT is off. If there are two threads per core, SMT is on.

To confirm the SMT status for Linux:
- SSH into the instance.
- Input the following to get the IP of the instance:
```

```

- In the shell of the instance, the return should look something like the example below. In this example, SMT is off.
```

```

To confirm the SMT status for Windows:
- Remote desktop (RDP) into the instance.
- In PowerShell, input the following query:
```

```

- The return should look something like the example below. In this example, SMT is off.
```

```
