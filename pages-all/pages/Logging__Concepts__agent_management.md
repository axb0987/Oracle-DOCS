# Agent Management Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/agent_management.htm
- Fetched: 2026-09-05 02:36 CDT

# Agent Management Overview

To ingest events from your applications into your custom log, you can install the Oracle fluentd-based agent. This agent allows you to control exactly which logs you want to collect, how to parse them, and more.
Note  
  
The Unified Monitoring Agent is a fully managed agent, and custom client configuration isn't officially supported. For example, gathering logs from remote sources isn't recommended, because doing so can have serious security implications (because the log source can't be verified).

Oracle Cloud Infrastructure Logging includes Agent Configurations to enable and manage the agent for a set of supported operating systems. Agent Configurations give you a central experience to easily configure what custom logs you want to ingest across your fleet of hosts. The following are the supported operating systems for agent configurations:

OS non-FIPS FIPS ARM
Oracle Linux 7 Yes Yes Yes
Oracle Linux 8 Yes Yes Yes
Oracle Linux 9 Yes Yes Yes
Oracle Linux 10 Yes No Yes
CentOS 7 Yes Yes No
Red Hat Enterprise Linux 8 Yes Yes Yes
Red Hat Enterprise Linux 9 Yes Yes Yes
Red Hat Enterprise Linux 10 Yes No Yes
Windows Server 2016 Yes Yes No
Windows Server 2019 Yes Yes No
Windows Server 2022 Yes Yes No
Windows Server 2025 Yes Yes No
Ubuntu 18.04 Yes No No
Ubuntu 20.04 Yes No No
Ubuntu 22.04 Yes No Yes
Ubuntu 24.04 Yes No Yes
Note  
  

The Oracle Unified Monitoring Agent is designed to function on standard Linux distributions, including Rocky Linux. If you use a Linux distribution that's not listed in the support matrix, contact your distribution provider for details on Unified Monitoring Agent installation and support.

See[Installing the Agent](https://docs.oracle.com/iaas/Content/Logging/Task/installing_the_agent.htm)for instructions on obtaining the installation files for each OS.

## Unified Monitoring Agent and Agent Configuration Security

Unified Monitoring Agent configurations are secured using the Dynamic Group feature from IAM. For more information, see[Selecting Target Hosts with Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/custom_logs_multihost.htm).

In addition, agent configuration updates are securely processed only by authorized users. After any update is made, the logging backend propagates the update to the agent itself.
