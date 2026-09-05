# Managing Instance Pools Lifecycle
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle.htm
- Fetched: 2026-09-05 01:51 CDT

# Managing Instance Pools Lifecycle

Pre-termination lifecycle actions let an instance pool pause instance termination so applications and automation can finish cleanup before the instance is terminated.

## Overview

Use a pre-termination lifecycle action when you want an instance in an instance pool to complete shutdown work before a scale-in operation or pool termination removes the instance.

Use this feature to:
- Drain traffic from the instance before it leaves service.
- Archive logs or application data before termination.
- Release application-level resources.
- Notify external systems that the instance is being removed.

## How Pre-termination Lifecycle Actions Work

When an instance pool operation selects an instance for removal, such as scale-in or pool termination, the following steps are performed.
- The pool places the instance in`TerminationAwait`state.
- While the instance is in this state, the application or automation completes its pre-termination work.
- Termination resumes when you send the termination proceed action for the instance or when the configured timeout expires.
Note  
  
If the timeout expires before termination proceeds, OCI handles the instance's boot volumes and block volumes according to the on-timeout preservation settings for the pool.
Note  
  
A pre-termination lifecycle action applies to future scale-in and pool termination events for the instance pool.

## Configure Options

You can configure the following instance pools lifecycle options.
- Enable or disable a pre-termination lifecycle action for an instance pool.
- Set the amount of time that the pool waits before termination resumes automatically.
Tip  
  
In the console, enter the completion timeout duration in minutes. In CLI and API payloads, set`timeout`in seconds.
- Select how OCI handles boot volumes if the timeout expires.
- Select how OCI handles block volumes if the timeout expires.

## Limitations and Considerations

Consider the following when creating life cycle actions.
- Pre-termination lifecycle actions apply to instances managed by instance pools. They do not apply to standalone instances.
- The timeout value must be nonnegative and can't exceed the maximum value allowed by the service.

You can configure boot volume and block volume handling independently. For each volume type, select one of these options:
- `PRESERVE_ALWAYS`: Preserve that volume type whenever termination continues.
- `PRESERVE_ON_TIMEOUT`: Preserve that volume type only when the configured timeout expires before you send the termination proceed action.
- `DELETE_ALWAYS`: Delete that volume type whenever termination continues.

## Lifecycle Actions

The following links provide more details on instance pools lifecycle actions.
- [Creating an Instance Pools Pre-termination Lifecycle Action](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-create.htm)
- [Editing Instance Pools Pre-termination Lifecycle Actions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-edit.htm)
- [Disabling Instance Pools Pre-termination Lifecycle Actions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-disable.htm)
- [Using Instance Pools Pre-termination Lifecycle Actions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-use.htm)
