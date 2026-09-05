# Non-Terminating Repair
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/non-terminating-repair.htm
- Fetched: 2026-09-05 01:52 CDT

# Non-Terminating Repair

Non-Terminating Repair (NTR) in OCI enables the maintenance and repair of underlying hardware or software components without the need to terminate or evacuate running instances.
Important  
  
NTR is only supported on bare metal shapes.

This approach contrasts with traditional Terminating Repair (TR) methods, which require instance termination before maintenance proceeds. NTR minimizes service disruptions and enhances application availability on OCI. NTR encompasses the following maintenance types:
- Downtime repairs: Instances are stopped prior to maintenance. The process requires the host to be shut down or rebooted during maintenance.
- Instance Action :`STOP`
- Live repairs: Maintenance occurs while instances remain operational. Instances remain in a running state, with no termination or power-off needed during maintenance.
- Instance Action :`NONE`
- Live background repair: A use case where no user action is needed and OCI creates a maintenance event and executes the repair in the background.
- Instance Action :`NONE`
Important  
  
Maintenance Initiation : NTR maintenance begins when the scheduled start time window is reached. Schedule maintenance at the desired time for maintenance initiation.

## Maintenance Events

OCI provides maintenance events to manage infrastructure maintenance processes.

Maintenance events are created when your instance/host needs maintenance. The events notify users of upcoming maintenance activities affecting their instances. Maintenance events appear in the Instance Maintenance resource in OCI Console. In addition, maintenance events can be managed using the CLI or SDKs. All interfaces allow users to reschedule maintenance windows, monitor maintenance progress, and perform necessary pre-maintenance or post-maintenance actions.

For example, the following link provides an example of a maintenance event class defined in Python. InstanceMaintenanceEvent:[https://docs.oracle.com/iaas/tools/python/latest/api/core/models/oci.core.models.InstanceMaintenanceEvent.html](https://docs.oracle.com/iaas/tools/python/latest/api/core/models/oci.core.models.InstanceMaintenanceEvent.html).

## Terminating Repair

Historically, Terminating Repair (TR) is the sole method for OCI to perform repairs on the underlying hardware or software of an instance.

This process requires evacuation and termination of the affected instance before repairs can begin. TR maintenance begins when the customer terminates the instance. Then, the maintenance takes place without having to reschedule the maintenance.

## Managing NTR Events using the CLI

The following steps provide an example of managing maintenance events through an entire maintenance process using the CLI.

### Discover Phase

Identify upcoming Instance Maintenance Events.

#### List Maintenance Events

```

```

Replace`<compartment-id>`with your compartment's OCID.

Example:

```

```

Sample output:

```

```

#### Get Instance Maintenance Event Details

View a specific maintenance event.

```

```

Replace`<instance-maintenance-event-id>`with the specific event's OCID.

Example:

```

```

Sample output:

```

```

### Pre-Maintenance Phase

Reschedule the start time window of an Instance Maintenance Event and perform any necessary pre-maintenance actions.

#### Reschedule Instance Maintenance Event

```

```

Replace`<instance-maintenance-event-id>`with the event's OCID and`<time-window-start>`with the desired start time in ISO 8601 format.

Example:

```

```

Sample output:

```

```

Important  
  
Ensure all pre-maintenance actions are completed before the scheduled start time window.

### Monitor Phase

Maintenance starts at the scheduled start time. Please wait until maintenance is completed.

#### Monitor Instance Maintenance Event Status

Monitor the status of a maintenance event during execution.

```

```

Replace`<instance-maintenance-event-id>`with the event's OCID.

Example:

```

```

Sample output:

```

```

### Post-maintenance phase

You can do your own post-maintenance action, if there is any, after the Instance Maintenance Events completed.

### More Information

For more information see:[Managing Maintenance Events](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managing-maintenance-events.htm)
