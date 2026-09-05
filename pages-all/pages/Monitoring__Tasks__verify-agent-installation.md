# Verifying Agent Installation
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/verify-agent-installation.htm
- Fetched: 2026-09-05 02:40 CDT

# Verifying Agent Installation

Verify Unified Monitoring Agent installation for all supported OS.
Note  
  
The agent, or Unified Monitoring Agent, is also known as the Oracle Cloud Agent plugin that is called "Custom Logs Monitoring".

## Windows

- [Connect to the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm).
- Open Services.msc (Start menu and type services.msc ). Scroll until you see the "Oracle Unified Monitoring Agent" and that the agent is in a "Running" state.
- In the Task Scheduler under Task Scheduler Library , verify that the UnifiedAgentConfigUpdater exists, and has (or will) run successfully. After the initial install, it can take up to 20 minutes for the first run. If preferred, this can be run manually.
- After the`UnifiedAgentConfigUpdater`task has run, verify that a`unified-monitoring-agent.conf`file in exists in`C:\oracle_unified_agent`.

After a few minutes, supervisor (`unified-monitoring-agent-supervisor-0.log`) logs and worker (`unified-monitoring-agent-0.log`) logs appear in the`C:\oracle_unified_agent`directory.

The preceding logs contain the Fluentd parser and plugin output.

## Linux

These instructions apply to Oracle Linux 7, 8, and 9, CentOS 7 and 8, CentOS Stream 8, Ubuntu 16, 18, and 20.

- [Connect to the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm).
- Check that the agent is running by running the following command:

```

```

The status looks like the following:
```

```
