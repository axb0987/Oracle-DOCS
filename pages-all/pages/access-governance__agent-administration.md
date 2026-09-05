# Manage Oracle Access Governance Agent for Indirect Integrations
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm
- Fetched: 2026-09-05 03:13 CDT

# Manage Oracle Access Governance Agent for Indirect Integrations

In some cases, an orchestrated system does not have a direct connection to Oracle Access Governance and requires an agent to enable data transfer between Oracle Access Governance and the orchestrated system.

## Register and Download the Oracle Access Governance Agent

To enable an orchestrated system to connect to Oracle Access Governance, you need to enter integration details and credentials for the system and build an agent specific to your environment.

- In a browser, navigate to the Oracle Access Governance service home page and log in as a user with the Administrator application role.
- On the Oracle Access Governance service home page, click on the icon and select Service Administration and then Orchestrated Systems .
- Select the Add a connected system button, to navigate to the Add n orchestrated system page to begin the configuration.
- On the Select system step, select the system you want to integrate with Oracle Access Governance, and then click Next .
- On the Enter Details step, enter the basic details, such as name and description, for your orchestrated system, and then click Next .
- On the Configure step, enter connection details for the orchestrated system:

Note  
  
The integration details will differ depending on the type of orchestrated system. For specific details related to each orchestrated system, refer to the[Supported Integrations with Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/supported-integrations-in-oracle-access-governance.htm)article.
- Click Next . A message is displayed to download the agent. Select the Download link and download the agent zip file to the environment in which the agent will run.
- Verify the package contents of your downloaded zip file.

The contents of the agent package will look similar to the following:

```

```

The agent package does not contain the orchestrated system integration configuration. It connects to the Oracle Access Governance service instance and retrieves the information as required. This means that there is no need to download or reinstall the agent for subsequent integration configuration changes.

## Prerequisites

Prerequisites for installation and running of an agent.

The following prerequisites should be met in order to install and run an agent.

- The agent management script supports docker and podman as the container runtime. The agent management script auto-detects the container run time. If both are present, podman is selected.
- The container runtime (docker/podman) should be configured to be run as a non-root user, the same as that which is used to install the agent.
- Utilities:
The agent requires the following operation system utilities:
- unzip
- sed
- awk
- crontab
Note  
  
The agent installation user should have permission to use each of these utilities.
- JDK: Agent requires JDK 11.0.x .
- Enable processes for the OS user that starts the agent to 'linger' after the user's session is terminated. If this option is not enabled, when you terminate the user's session the agent process will stop and you will see errors when trying to communicate between Oracle Access Governance, the agent, and your orchestrated system.
- To check if linger is enabled for your OS user check for a file with the same name as the user in the`/var/lib/systemd/linger`directory. If the file exists then this option is enabled:
```

```

- To enable linger for your OS user enable the systemd linger behavior:
```

```

- Minimum disk space required for the agent should be:
- 4GB freespace for the directory configured as the volume for the agent.
- 5GB freespace for the docker/podman home.

The minimum values above include disk space consumed during upgrade, in the process of which, a backup is created and a new agent image is downloaded and loaded.
- If SELinux is enabled on the host system, set the security context of the Persistent Volume used by the Agent by running the following command:
```

```

## Sizing Virtual Machine/Host

The table below suggests values for sizing your orchestrated system agent VM or host for small, medium, and large scale implementations.

Parameter Description Small Scale Medium Scale Large Scale

CPU Cores

Number of CPU Cores.

2

4

8

Memory

Amount of memory (GB)

16

32

64

## Install Oracle Access Governance Agent

A step-by-step process to install the Oracle Access Governance Agent with sample commands to run:
To install the downloaded agent into the local system, perform the following steps:

- Unzip the downloaded agent to the local location.

Contents of the unzipped agent should be:

```

```

- Run the management script with the following parameters:

```

```

An example with default configuration would look such as the following:

```

```

An example with custom configuration would look such as the following:

```

```

Tip  
  
If you see issues during copy-paste or an error while executing a script, such as an invalid format error, you might try to manually insert double hyphen ("-", ASCII value for hyphen is 45).
- Start the agent with the following command:

```

```

For example:

```

```

## Verify Agent

Details how to verify the installation and operation of the orchestrated system agent.
To verify the installation of the orchestrated system agent, complete the following steps:

- In the Oracle Access Governance Console, select the icon to display the navigation menu.
- In the Oracle Access Governance Console, select Service Administration → Orchestrated Systems from the navigation menu.
- On the Orchestrated Systems screen, the orchestrated system shows a status of Waiting for initial integration . Click on Manage → Troubleshooting Checklist .
- The Activity Log at the bottom of the page will show the status of the Validate operation, Pending while the agent comes up. If the agent does not come up, check the agent install and operation logs for any issues.
- Once the agent has come up, the status of the Validate operation will show as Success .

## Agent Example Usage

Displays examples of usage of the agent management script.

Once you have successfully installed and verified your agent, you can start to manage the lifecycle. The`agentManagement.sh`script provides support for the start, stop, restart, uninstall, and upgrade operations.

### Start the Agent

You start the agent with the following command:

```

```

For example:

```

```

### Stop the Agent

You stop the agent with the following command:

```

```

For example:

```

```

### Restart the Agent

You restart the agent with the following command:

```

```

For example:

```

```

### Uninstall the Agent

You uninstall the agent with the following command:

```

```

For example:

```

```

### Upgrade the Agent

You upgrade the agent with the following command:

```

```

For example:

```

```

### Enable Auto Upgrade

Enable auto upgrade with the following command:

```

```

For example:

```

```

### Disable Auto Upgrade

Perform this step only if absolutely necessary, as this can cause failures in the communication between the agent and the Oracle Access Governance service. If you perform this step and you see failures, immediately upgrade the agent by following the steps mentioned in the Upgrade the Agent example in[Agent Example Usage](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm#agent-example-usage).

Disable auto upgrade with the following command:

```

```

For example:

```

```

## Custom Jar Support

When integrating with Oracle Access Governance some orchestrated systems may need custom jar(s).For instance to communicate with DB2 and MYSQL database the respective driver jar is needed. Use the following steps to upload the custom jar.
- Download the driver jar and place it in the`customJarsDirectory`path as specified in the`config.json`. For example,`config.json`may contain an entry,`customJarsDirectory : /app/data/customJars`, where`/app`is the agent volume.
- Calculate the checksum of the downloaded driver jar using`SHA-512`.
- On the Oracle Access Governance Console, go to Service Administration and then Orchestrated Systems .
- On the Connected Systems page, select Manage integration for your orchestrated system.
- Under Configurations , select the Manage button on the Integration Settings tile.
- Update the orchestrated system configuration in the Custom Jar Details field. Provide the driver jar name and the checksum in the format`<jarName>::<checksum>`.
For DB2 connected system, sample value in Custom Jar Details
```

```

- Click Save .

## Agent Management Operations

Lists details of the operations that the agent can perform and related parameter descriptions.

The orchestrated system agent can be managed using the`agentManagement.sh`script. This script can be downloaded from GitHub. The script supports`docker`and`podman`, it autodetects the container runtime available. If both are available, the script uses`podman`.

### Operations

Operation Description Additional Information

`--install`

- Installs the downloaded agent package to the specified volume.
- Loads the container image.

Use`--config`to use a custom configuration.

`--start`

- Starts the agent container.
- Starts the agent daemon.

Use`--newcontainer`to start a new container.

Use`--config`to use a custom configuration.

`--stop`

- Stops the agent daemon.
- Stops the agent container.

`--restart`

- Stops the agent daemon.
- Stops the agent container.
- Remove the agent container if`newcontainer`flag is set to true .
- Starts the agent container.
- Starts the agent daemon.

`--uninstall`

- Stops the agent daemon.
- Remove the agent container.
- Clean up the volume.

`--upgrade`

- Unzips new`agent-package.zip`in a temporary location.
- Validates the package contents.
- Loads the image from the new zip file.
- Starts a temporary container using the new image and configuration.
- If the temporary container has no issues then stop the container.
- Stop the existing container.
- Copy new configuration from the temporary location to the current location. This retains any customizations.
- Starts the agent with the new image and configuration.
- Starts the agent daemon.

The following changes require an upgrade.

- Change in configuration`config.json`
- Connector bundle change
- Change in Wallet
- Change of agent image

The following changes will trigger a reconfigure operation which is handled by the agent framework.

- Connector (same template version)
- Connector (different template version)

For more information, refer[Upgrade an Agent](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm#agent-example-usage).

`--status`
Lists the following details of the agent:
- Agent ID
- Container runtime and version
- Agent package
- Agent version
- Install location
- Agent state

`--enableautoupgrade`

Enables automatic upgrade by performing the following tasks:

- Sets up a`cron`job to detect upgrades for any changes in target connectivity parameters, or in connector bundle code.
- `cron`job runs every 30 minutes and upgrades the agent automatically if required.

`--disableautoupgrade`

Disables automatic upgrades by removing the auto-upgrade`cron`job.

## Agent Parameters

### Parameters

Parameter Name Description Mandatory Default Value Argument Argument shorthand

__AGENT_ID__

Agent ID with which the agent container would run.

No

`agent-<hostname>-<timestamp>`

`--agentid`

`-ai`
Agent Package Location Local Agent package location with the package name.

Yes`--agentpackage`

`-ap`

Volume

Directory to persist agent data such as configuration, wallet, and logs.

Yes

`--volume`

`-pv`

New Container with start and restart

Create a new container. This parameter doesn't need a value.

No

`--newcontainer`

`-nc`

Custom configuration

Provide custom configurations through a property file.

No

`--config`

`-c`

Auto Upgrade

Use this parameter with install operation to setup auto upgrade of the agent.

No

`true`

`--autoupgrade`

`-au`

Custom configuration is provided to the script through the`config.properties`file that has the following format:

```

```

## Tuning Runtime Configuration

The following table lists the parameters for fine tuning the runtime configuration of the orchestrated system agent, and suggests specific values for small, medium, and large scale implementations.

Details of how to configure these parameters can be found in[Agent Parameters](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm#agent-parameters).

Note  
  
soft limits for sizing are:
- Small : 10-20k identities/accounts and associated data
- Medium : 40-50k identities/accounts and associated data
- Large : Beyond 50k identities/accounts and associated data

Parameter Description Small Scale Medium Scale Large Scale

idoConfig.sparkMaxResultSizeInGB

Limit of total size of serialized results of all partitions for each action (e.g. collect) in bytes. Should be at least 1M, or 0 for unlimited. Jobs are canceled if the total size is beyond this limit. Having a high limit might cause out-of-memory errors in driver (depends on spark.driver.memory and memory overhead of objects in JVM). Setting a proper limit can protect the driver from out-of-memory errors.

2

5

7

idoConfig.sparkExecutorMemoryInGB

Amount of additional memory to be allocated per executor process, in MiB unless otherwise specified. This is memory that accounts for things such as VM overheads, interned strings, other native overheads, etc.

2

5

7

idoConfig.numberOfPartition Number of partitions.

3

5

7

## Troubleshooting Oracle Access Governance Agent

Learn how to address error messages and other problems you may see when configuring or using the Oracle Access Governance Agent.

### Topics:
- [Unexpected Agent Shutdown Due To Resource Constraints](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm#troubleshootingagagent)

### Unexpected Agent Shutdown Due To Resource Constraints

If you start to hit resource limits on memory, CPU, or disk, the agent might unexpectedly shutdown. To bring the agent back up again cleanly you must restart the agent after rectifying the underlying issue.
Solution: Restart the agent using the`restart`command rectifying the underlying issue.
```

```
