# Troubleshooting Logging
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/troubleshooting.htm
- Fetched: 2026-09-05 02:38 CDT

# Troubleshooting Logging

Use troubleshooting information to identify and address common issues that can occur while working with Logging.
- [General Unified Monitoring Agent Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Logging/troubleshooting.htm#troubleshooting_agent_general)
- [Linux Unified Monitoring Agent](https://docs.oracle.com/en-us/iaas/Content/Logging/troubleshooting.htm#troubleshooting_agent_linux)
- [Windows Unified Monitoring Agent](https://docs.oracle.com/en-us/iaas/Content/Logging/troubleshooting.htm#troubleshooting_agent_windows)

## General Unified Monitoring Agent Troubleshooting

### Hardware Requirements

Depending on your logging requirements and configuration (number of logs, type of buffering, and so on), the hardware requirements and performance of the Unified Monitoring Agent can vary widely. When no operational pressure is present (less than 1.000 log events per minute), the agent should not consume more than 200 MB of RAM, and 20% of a CPU core. The Unified Monitoring Agent service hard-coded limits are 5 GB RAM, and 40% of a core. 1 GB of RAM is also recommended.

### Enabling Monitoring

Monitoring can aid with troubleshooting. See[Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm)for more information on how you can enable monitoring (metrics and logging) in your Oracle Cloud Infrastructure Compute instances.

## Linux Unified Monitoring Agent

### `systemd`Units

The Unified Monitoring Agent is based on`systemd`units, and is composed of the following components:
- unified-monitoring-agent.service: The main Unified Monitoring Agent service.
- unified-monitoring-agent_config_downloader.service: The configuration automatic updater service.
- unified-monitoring-agent_config_downloader.timer: The timer unit, which triggers the automatic downloader service on specified, randomized, intervals.
- unified-monitoring-agent_restarter.path: The path unit, which triggers the reload of the configuration by the Unified Monitoring Agent, if a change is detected (because of a new configuration being downloaded by the automatic updater service).
Note  
  
Most of the systemctl or journalctl commands must be run with super user privileges (either as`root`, or through`sudo`).

To verify the correct operation of these`systemd`units, you can use the`systemctl`command like the following:
```

```

Where`<unit_name>`must be replaced with one of the following values:
- `unified-monitoring-agent.service`
- `unified-monitoring-agent_config_downloader.service`
- `unified-monitoring-agent_config_downloader.timer`
- `unified-monitoring-agent_restarter.path`

Typically these`systemctl`commands show output similar to the following:
```

```

```

```

```

```

```

```

The most important parts of the systemctl command output are the`Loaded`and`Active`fields. The`Loaded`field has the value`loaded`for all system units. The`Active`field has the following values:
- `active (running)`for the unified-monitoring-agent.service unit.
- `active (waiting)`or`active (running)`for the unified-monitoring-agent_restarter.path and the unified-monitoring-agent_config_downloader.timer units.
- `active (running)`or`inactive (dead)`for the unified-monitoring-agent_config_downloader.service unit. For the latter value, the field`Main PID`includes the value`code=exited, status=0/SUCCESS)`.

### Check Running Processes

Another way to further verify the correct operation of the Unified Monitoring Agent, is to check the system’s running processes. When operating correctly, the Unified Monitoring Agent runs two processes: one supervisor process, and one worker process. You can verify their existence by running the following command in a terminal (sample output included):
```

```

As shown in the preceding sample, there are two processes running, with the same arguments, except for the extra`–under-supervisor`added to the second one. This denotes the worker process, thus making the process without this parameter the supervisor.

### Unified Monitoring Agent Log Location
Note  
  
Most of the systemctl or journalctl commands must be run with super user privileges (either as`root`, or through`sudo`).

The Unified Monitoring Agent logs are available at`/var/log/unified-monitoring-agent/unified-monitoring-agent.log`. This file includes logs from the Unified Monitoring Agent itself.

Besides the agent's logs, which do not contain system-related events (for example, service start, service stop, and so on), you can also view the logs from`journald`,`systemd`'s system logging service. To view the system logs specific to a unit, you can use the`journalctl`command like the following:
```

```

Where`<unit_name>`must be replaced with one of the following values:
- `unified-monitoring-agent.service`
- `unified-monitoring-agent_config_downloader.service`
- `unified-monitoring-agent_config_downloader.timer`
- `unified-monitoring-agent_restarter.path`
When querying`journald`logs through`journalctl`, you can also define specific time ranges:
```

```
The date format used is YYYY-MM-DD HH:MM:SS.
You can also tail the journal logs, by adding the`-f`parameter:
```

```

### The Unified Monitoring Agent isn't Installed

For newly created instances, it can take up to 25 minutes for the automatic installation of the agent. If it is not installed after this time period, check the following:
- The network connectivity of the instance.
- Whether monitoring is enabled in the Console.

You can also check the log file`/var/log/oracle-cloud-agent/plugins/unifiedmonitoring/unifiedmonitoring.log`for information regarding the installation of the Unified Monitoring Agent by the Oracle Cloud Agent.

### The Unified Monitoring Agent isn't Running

If the status is not loaded or active, nor are both supervisor and worker processes running, restart the Unified Monitoring Agent and check the logs for any problems:
```

```

### Configuration Not Automatically Downloaded

Ensure you have followed the steps in[Installing the Agent](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/installing_the_agent.htm)and[Verify Agent Installation](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/verify_agent_installation.htm). Consult the journal of the automatic configuration updater service by running:
```

```

### Configuration Not Automatically Reloaded

Ensure you have followed the steps in[Installing the Agent](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/installing_the_agent.htm)and[Verify Agent Installation](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/verify_agent_installation.htm). Consult the journal of all the units:
- The timer unit must have run at least one time.
- The automatic configuration download service must have run after the relevant time unit has triggered it. You can verify from its logs that the configuration has been downloaded and extracted to the Unified Monitoring Agent's configuration directory. You can also verify this by listing the files in that directory: ls -lhatR /etc/unified-monitoring-agent .
- Verify that the path unit is active by checking its status: systemctl status unified-monitoring-agent_restarter.path .
- Verify that a reload signal has been received by the Unified Monitoring Agent, by inspecting its journal: journalctl -u unified-monitoring-agent_config_downloader.service . "Reloading unified-monitoring-agent" appears in the output of this command.

### Test Parsing Pattern and Force Agent to Immediately Download the Configuration

Run the following command:
```

```

Note  
  
Automatic update of the configuration on the agent side can take up to 30 minutes.

### Data Collection

If you want to open a ticket so an engineer can help you with your problem regarding the Unified Monitoring Agent, include the output of the following commands. Super user privileges might be required for some of them.
```

```

For Ubuntu use a command like the following:
```

```

Also include an archive of the files under`/var/log/unified-monitoring-agent/`and`/var/log/oracle-cloud-agent/`. You can create a gzipped tar archive of these directories with the command:
```

```

If the Unified Monitoring Agent is running but has erratic behavior, you can also include backtrace and memory profile information, by running the following command and including the files`/tmp/sigdump- <integer> .log`in your report (where`<integer>`is an integer with 1–6 digits, even though in rare cases it might have more than that).
```

```

What this command does is to find the Unified Monitoring Agent process PIDs, and send them the SIGCONT signal, which causes a dump to be generated in`/tmp/sigdump- <integer> .log`.

### Uninstall and Reinstall

You can remove the Unified Monitoring Agent, without removing the agent's configuration, by running the following command:
```

```

For Ubuntu:
```

```

The agent's configuration remains under the`/etc/unified-monitoring-agent/`directory. If you do not want to keep the configuration for a future (re)installation of the Unified Monitoring Agent package, you need to remove it manually:
```

```

The agent is automatically reinstalled by the Oracle Cloud Agent, at most 25 minutes. You need to have monitoring enabled for your instance in the Console for this to occur. See[Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm)for more information.

## Windows Unified Monitoring Agent

### To Check Service Status

- The agent runs as part of a Windows service, to see its status, open the start menu and type Services.msc and open it. Go to the service Oracle Cloud Unified Monitoring Service to see the status.
- Right-click the service and select Properties for more information. Start/stop/restart are available here.
- From the Start menu type cmd , right-click on Command Prompt and select Run as Administrator . Run the following commands:
- To view Unified Monitoring Agent service status:
```

```

- Restart the Unified Monitoring Agent service:
```

```

Note  
  
The preceding commands do not work in PowerShell, so you must instead use the Windows Command Prompt.

### To Find Windows Service Errors

- From the Start menu, type Event Viewer and select it.
- Open Windows Logs , then System . Every time a service starts or stops, fails to do either, or crashes suddenly, it is recorded here.
Note  
  
On most Windows machines, there is a cap on how many events can be in the event viewer. As a result, if an event happened a long time ago, the logs might not be available.

### To View Fluentd Logs

- Open explorer.exe (file icon on the task bar)
- Go to C:\oracle_unified_agent.
- If there is only one file, it means that there isn’t a valid configuration file on the machine.
- If there are two files, then there is a supervisor log that will have all the setup/start-up logs, and a worker log with all the parsing/output logs. unified-monitoring-agent.conf is the name of the configuration file if it has been downloaded properly.
- Run Fluentd manually. Try the preceding steps to identify the issue, but if needed, you can debug an issue by manually running Fluentd.
Note  
  
Running Fluentd manually runs it in the Windows service, which stops the service from running as normally, which is different behavior than on Linux.
- Use the following command to run Fluentd manually. This can be run in PowerShell or Command Prompt, but it needs to be run as Administrator:
```

```

### Automatic Configuration Updater Steps

- Verify Task Scheduler is running as expected.
- From the Start menu, and type Task Scheduler .
- Go to Task Scheduler (Local) , then Task Scheduler Library . Find the task named UnifiedAgentConfigUpdater .
- Verify the Last Run Time . If it was at an invalid date, or it says not run , then the Next Run time will be when it should run for the first time. For debugging, select the task and select Run if you need it to run immediately.
- Last Run Result specifies the outcome of downloading the configuration from the control plane. If there is an error result, you need to run it manually to determine what happened. Task Scheduler does not keep output logs.
- Run the configuration updater manually.
Note  
  
Run the updater in PowerShell as an Administrator for the best experience.
```

```

### Check Oracle Cloud Agent Logs

For Windows Server 2012r2 or 2016, the log file locations are:
- `C:\Users\OCA\AppData\Local\Local\OracleCloudAgent\agent.log`
- `C:\Users\OCAUM\AppData\Local\OracleCloudAgent\plugins\unifiedmonitoring\unifiedmonitoring.log`(runtime logs)
- `C:\Users\OCAUM\AppData\Local\OracleCloudAgent\plugins\unifiedmonitoring\unifiedmonitoring_msi.log`(install logs)
- `C:\oracle_unified_agent\unified-monitoring-agent-0.log`(agent worker log, which might not exist depending on state)
- `C:\oracle_unified_agent\unified-monitoring-agent-supervisor-0.log`(agent supervisor log, which might not exist depending on state)

Windows Server 2019/2022 log file locations:
- `C:\Windows\ServiceProfiles\OCA\AppData\Local\OracleCloudAgent\agent.log`
- `C:\Windows\ServiceProfiles\OCAUM\AppData\Local\OracleCloudAgent\plugins\unifiedmonitoring\unifiedmonitoring.log`(runtime logs)
- `C:\Windows\ServiceProfiles\OCAUM\AppData\Local\OracleCloudAgent\plugins\unifiedmonitoring\unifiedmonitoring_msi.log`(install logs)
- `C:\oracle_unified_agent\unified-monitoring-agent-0.log`(agent worker log, which might not exist depending on state)
- `C:\oracle_unified_agent\unified-monitoring-agent-supervisor-0.log`(agent supervisor log, which may not exist depending on state)

### Intermittent Failed MSI Install

An intermittent failed MSI install can occur for one of two reasons:
- An MSI installation was interrupted (system reboot, process stop, and so on), and on the second run, the msiexec.exe process is still holding a file handle to a folder that it created.
- During an upgrade where the MSI fails to get access to the main agent folder, because Ruby.exe doesn’t end like it should (a Fluentd issue). This causes the MSI to fail and to clean up the system, removing much of the agent (not the position or buffer files though).

In both instances, a second install or letting Oracle Cloud Agent run through the install a second time resolves this issue. If it still is stuck in this state do the following:
- Stop all msiexec and ruby processes in Task Manager, Details.
- Rename C:\oracle_unified_agent to C:\oracle_unified_agent_old.
- Install the agent again, or wait for Oracle Cloud Agent to install it.

### Generic Paths not Working with Agent Configuration

Use a forward slash (/) while configuring paths for the Windows agent configuration. A backslash (\) with an asterisk (*) does not work on Windows due to internal limitations. To avoid this, do not use a path like`C:\\path\\to\\*\\foo.log`. Use the following forward slash method instead:
```

```

The following paths are the supported generic working path examples for Windows:
- `C:/logs/*`
- `C:/logs/t2*.txt`
- `C:/logs/a*b.txt`
- `C:/logs/abc*`
- `C:/logs/*.txt`
- `C:/logs/*/abc*`
- `C:/logs/*/a.txt`
- `C:/logs/*/a*b.txt`
- `C:/logs*/*.txt`

The`C:/logs/*log.txt`
