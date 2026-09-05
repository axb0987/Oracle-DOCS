# Using Instance Pools Pre-termination Lifecycle Actions
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-use.htm
- Fetched: 2026-09-05 01:51 CDT

# Using Instance Pools Pre-termination Lifecycle Actions

Use this task when an instance pool has already paused termination for an instance and the automation is ready to let termination continue.

When pre-termination is enabled, instance pool instances selected during scale-in or pool termination enter`TerminationAwait`. Continue termination by identifying the waiting instance and sending the termination proceed request for that instance.

## Before You Begin

Before enabling termination, consider the following.
- Ensure that you have permission to read the instance pool and update the lifecycle action for the target instance.
- Identify the instance pool waiting on pre-termination work.
- If the automation already tracks the instance directly, keep the instance OCID available for the proceed request.

## 1. Identify the Instance Waiting in TerminationAwait

Use the instance-pool instance APIs to find the instance whose`state`is`TerminationAwait`.

To list instances in the pool:

```

```

If you already know the instance OCID, get that specific pool instance:

```

```

Look for an instance whose`state`is`TerminationAwait`.

## 2. Send the Termination Proceed Request

When the cleanup work is complete, send the termination proceed request for the instance.

Use the`terminationProceed`action:

```

```

Request body example:

```

```

The service returns`202 Accepted`after it accepts the request.

## Configuration Considerations

Consider the following when sending requests regarding pre-termination actions.
- Send the proceed request only for an instance in`TerminationAwait`.
- If the automation doesn't send the proceed request before the timeout expires, the service resumes termination automatically and applies the pool's on-timeout volume preservation settings.
-
