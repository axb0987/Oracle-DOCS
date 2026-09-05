# Installing the Agent
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/installing_the_agent.htm
- Fetched: 2026-09-05 02:37 CDT

# Installing the Agent

Learn about how to install the Unified Monitoring Agent, whether for new instances, existing instances, or instances created from custom images, and non-Oracle Cloud Infrastructure instances.

On new Oracle Cloud Infrastructure instances with supported operating systems, you can enable the agent directly during creation time. For both new and existing instances with supported operating systems, the Custom Logs Monitoring plugin must be enabled, and all plugins must be running. See[Available Plugins](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#available-plugins)for more information.

## Manual Installation

If you already have the Custom Logs Monitoring plugin enabled, then your instance will be automatically patched to install the agent. Otherwise, you can use the following manual installation instructions.

Run the following command to get more details on the latest agent download versions for each OS:

```

```

The command downloads the`versionInfoV2.yml`file with the following contents:
```

```

The`stableVersion`field in`versionInfoV2.yml`shows the latest version number to use for each OS.

After you have found the proper version number, perform the following setup steps, whether for Linux or Windows.

Linux:
- [Connect to the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm).
- [Set up token-based authentication for the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/clitoken.htm).
- 

Use the following command to download the non-FIPS or FIPS-enabled agent for your Linux OS, while replacing &lt;bucket&gt; , &lt;name&gt; , and &lt;file&gt; for the particular OS version:

```

```

OS Version &lt;Bucket&gt; &lt;Name&gt; and &lt;File&gt;
non-FIPS agent: x86
Oracle Linux 7`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-7- <version> .rpm`
Oracle Linux 8`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-8- <version> .rpm`
Oracle Linux 9`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-9- <version> .rpm`
Oracle Linux 10`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-10- <version> .rpm`
CentOS 7`unified-monitoring-agent-cl-bucket``unified-monitoring-agent-cl-7- <version> .rpm`
Red Hat Enterprise Linux 8`unified-monitoring-agent-rl-bucket``unified-monitoring-agent-rl-8- <version> .rpm`
Red Hat Enterprise Linux 9`unified-monitoring-agent-rl-bucket``unified-monitoring-agent-rl-9- <version> .rpm`
Red Hat Enterprise Linux 10`unified-monitoring-agent-rl-bucket``unified-monitoring-agent-rl-10- <version> .rpm`
Ubuntu 18.04`unified-monitoring-agent-ub-bucket``unified-monitoring-agent-ub-18- <version> .deb`
Ubuntu 20.04`unified-monitoring-agent-ub-bucket``unified-monitoring-agent-ub-20- <version> .deb`
Ubuntu 22.04`unified-monitoring-agent-ub-bucket``unified-monitoring-agent-ub-22- <version> .deb`
Ubuntu 24.04`unified-monitoring-agent-ub-bucket``unified-monitoring-agent-ub-24- <version> .deb`
non-FIPS agent: ARM
Oracle Linux 7`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-7- <version> .aarch64.rpm`
Oracle Linux 8`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-8- <version> .aarch64.rpm`
Oracle Linux 9`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-9- <version> .aarch64.rpm`
Oracle Linux 10`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-10- <version> .aarch64.rpm`
Red Hat Enterprise Linux 8`unified-monitoring-agent-rl-bucket``unified-monitoring-agent-rl-8- <version> .aarch64.rpm`
Red Hat Enterprise Linux 9`unified-monitoring-agent-rl-bucket``unified-monitoring-agent-rl-9- <version> .aarch64.rpm`
Red Hat Enterprise Linux 10`unified-monitoring-agent-rl-bucket``unified-monitoring-agent-rl-10- <version> .aarch64.rpm`
Ubuntu 22.04`unified-monitoring-agent-ub-bucket``unified-monitoring-agent-ub-22- <version> .aarch64.deb`
Ubuntu 24.04`unified-monitoring-agent-ub-bucket``unified-monitoring-agent-ub-24- <version> .aarch.64.deb`
FIPS-enabled agent: x86
Oracle Linux 7`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-7-fips- <version> .rpm`
Oracle Linux 8`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-8-fips- <version> .rpm`
Oracle Linux 9`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-9-fips- <version> .rpm`
CentOS 7`unified-monitoring-agent-cl-bucket``unified-monitoring-agent-cl-7-fips- <version> .rpm`
Red Hat Enterprise Linux 8`unified-monitoring-agent-rl-bucket``unified-monitoring-agent-rl-8-fips- <version> .rpm`
Red Hat Enterprise Linux 9`unified-monitoring-agent-rl-bucket``unified-monitoring-agent-rl-9-fips- <version> .rpm`
FIPS-enabled agent: ARM
Oracle Linux 7`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-7-fips- <version> .aarch64.rpm`
Oracle Linux 8`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-8-fips- <version> .aarch64.rpm`
Oracle Linux 9`unified-monitoring-agent-ol-bucket``unified-monitoring-agent-ol-9-fips- <version> .aarch64.rpm`
Red Hat Enterprise Linux 8`unified-monitoring-agent-rl-bucket``unified-monitoring-agent-rl-8-fips- <version> .aarch64.rpm`
Red Hat Enterprise Linux 9`unified-monitoring-agent-rl-bucket``unified-monitoring-agent-rl-9-fips- <version> .aarch64.rpm`
- Run the following command to install the RPM:

```

```

For Ubuntu:

```

```

Windows:
- [Connect to the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm).
- [Set up token-based authentication for the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/clitoken.htm).
- Use the following command to download the non-FIPS or FIPS-enabled agent for Windows Server 2016, 2019, 2022, and 2025 while replacing &lt;name&gt; , and &lt;file&gt; for the particular Windows OS version:

```

```

OS Version &lt;Name&gt; and &lt;File&gt;
non-FIPS agent
Windows 2016`unified-monitoring-agent-win-2016- <version> .msi`
Windows 2019`unified-monitoring-agent-win-2019- <version> .msi`
Windows 2022`unified-monitoring-agent-win-2022- <version> .msi`
Windows 2025`unified-monitoring-agent-win-2025- <version> .msi`
FIPS-enabled agent
Windows 2016`unified-monitoring-agent-win-2016-fips- <version> .msi`
Windows 2019`unified-monitoring-agent-win-2019-fips- <version> .msi`
Windows 2022`unified-monitoring-agent-win-2022-fips- <version> .msi`
Windows 2025`unified-monitoring-agent-win-2025-fips- <version> .msi`
- Open an elevated command prompt (as an Administrator), and run the MSI command. Installation can take up to five minutes to complete:

```

```

For a more advanced version of the preceding command to debug MSI installation issues, run:

```

```

## Instances Created from Custom Images and Non-Oracle Cloud Infrastructure Instances
- Install the agent according to the same steps in[Manual Installation](https://docs.oracle.com/iaas/Content/Logging/Task/installing_the_agent.htm#installing_the_agent__manual-install).
- Configure user API keys for the instance you're running on. To generate the user API key, follow the instructions described in[How to Generate an API Signing Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#two).
- (Linux) . Place the ".oci" directory and its contents under`/etc/unified-monitoring-agent`.
- (Windows) . For Windows, some steps differ, so ensure to follow the appropriate steps. Create the ".oci" folder and its contents in the directory`C:\oracle_unified_agent`.
- Follow the instructions described in[Creating a Profile in the Oracle Cloud Infrastructure CLI Configuration File](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsconfigureocicli.htm), to create the configuration file with the modifications in the next step.
- After following the steps in[Creating a Profile in the Oracle Cloud Infrastructure CLI Configuration File](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsconfigureocicli.htm), ensure to name the profile ( &lt;profile-name&gt; ) for this section as "UNIFIED_MONITORING_AGENT".
The following is an example configuration for the Unified Monitoring Agent to use for authentication with the service:
```

```

## Managed System Resources (Non-Instance)
- Install the agent according to the same steps in[Manual Installation](https://docs.oracle.com/iaas/Content/Logging/Task/installing_the_agent.htm#installing_the_agent__manual-install).
- Create a Dynamic Group with a matching rule targeting database resources, and apply it to your[agent configuration](https://docs.oracle.com/iaas/Content/Logging/Task/create-logging-agent-configuration.htm). For more information, see[About Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#About). Select a dynamic group from the Group list matching the rule for a resource of any resource type (`database`,`dbsystem`,`cloudvmcluster).`
```

```

For example:`ALL {resource.type = 'database', resource.id = 'ocid1.database.oc1.phx. <unique_ID> '}`.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). To learn more about writing policies for dynamic groups or other IAM components, see[Details for IAM without Identity Domains](https://docs.oracle.com/iaas/Content/Identity/Reference/iampolicyreference.htm).
- Create a policy granting the dynamic group you created access to the Logging service.
```

```

For example:`Allow dynamic-group linuxdbvm to use log-content in compartment <compartment-name>`.
- Create a file in the`/etc/resource_principal_env`directory on the host using the following format.
```

```

The following is an example for the Oracle Exadata Database service in the`us-phoenix-1`region:
```

```

For more information, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
- Restart the agent using the following command:
```

```
