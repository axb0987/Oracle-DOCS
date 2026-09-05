# Troubleshooting Oracle Cloud Agent
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm
- Fetched: 2026-09-05 01:51 CDT

# Troubleshooting Oracle Cloud Agent

When using[Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm), you might encounter the following problems:
- On the Oracle Cloud Agent tab of the Instance Details page, the status for all plugins is Invalid .
- In the Metrics section of the Console dashboard, you can't see any CPU, memory, network, or disk metrics for the instance.

If you encounter any of these problems, Oracle Cloud Agent might not be installed or running, or it might not be able to communicate with Oracle services. To diagnose the specific issue, follow these troubleshooting steps.
Tip  
  
In this topic, the instructions for Oracle Linux also apply to CentOS images.
Tip  
  
If you can't connect to your instance, see:
- [Troubleshooting the SSH Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm)
- [Troubleshooting Instances Using Instance Console Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/serialconsole.htm)

## Step 1: Verify that Oracle Cloud Agent is Installed

Follow these steps to confirm that Oracle Cloud Agent is installed on your instance.
- [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm)and run one of the following commands, depending on your operating system.

[Oracle Linux](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

```

```

If Oracle Cloud Agent is installed, a message similar to the following displays:
```

```

[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

```

```

If Oracle Cloud Agent is installed, the following message displays:
```

```

[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

Run the command in[Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows)as an administrator.

```

```

If Oracle Cloud Agent is installed, a message similar to the following displays:
```

```

- If the message indicating that Oracle Cloud Agent is installed does not display after you run the command,[install Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent). If Oracle Cloud Agent is installed, proceed to the next step to verify that it is running.

## Step 2: Verify that Oracle Cloud Agent is Running

After you confirm that Oracle Cloud Agent is installed, follow these steps to confirm that it is running.
- [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm)and run one of the following commands to restart Oracle Cloud Agent.

[Oracle Linux 7.x and later versions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

```

```

Expected response if Oracle Cloud Agent is running:
```

```

[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

```

```

Expected response if Oracle Cloud Agent is running:
```

```

[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

Run the command in[Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows)as an administrator.

```

```

Expected response if Oracle Cloud Agent is running:
```

```

- If the message indicating that Oracle Cloud Agent is running does not display after you run the command,[run the diagnostic tool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#diagnostic)and then file a[support ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)with the file that contains debugging information and logs for the plugins. If Oracle Cloud Agent is running, proceed to the next step to verify that it can connect to Oracle services.

## Step 3: Verify that Oracle Cloud Agent Can Connect to Oracle Services

If you confirm that Oracle Cloud Agent is installed and running but the status for all plugins on the Instance Details page is Invalid or you cannot see any metrics in the Metrics section of the Console dashboard, Oracle Cloud Agent might not be able to connect to Oracle services. The following sections explore possible reasons that Oracle Cloud Agent is unable to connect to Oracle services. To diagnose the issue, follow these steps in order.
- [Verify that the instance can access the Instance Metadata Service endpoint.](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__instancemetadataserviceendpoint)
- [Check for clock skew errors.](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__clockskew)
- [Verify that gateways are configured correctly.](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__gateways)
- [Change your proxy server settings.](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__proxyservers)

### Verify that the Instance Can Access the Instance Metadata Service Endpoint

These steps verify whether the instance can access the Instance Metadata Service endpoint.
- [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm)and run one of the following commands, depending on you operating system.

[Oracle Linux and Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

```

```

If Oracle Cloud Agent is running, a message similar to the following displays:
```

```

[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

Run the command in[Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows)as an administrator.

```

```

If Oracle Cloud Agent is running, a message similar to the following displays:
```

```

- If you get a successful response without proxy errors, check for clock skew errors. If proxy server errors occur,[check your proxy server settings](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__proxyservers).

### Check for Clock Skew Errors

Sometimes, the clock on an instance is not synchronized with the NTP service. Clock skew can cause TLS negotiations to fail, preventing the instance from connecting to Oracle services. Follow these steps to check for clock skew errors.
- 

[Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm)and run one of the following commands to generate the`monitoring.log`file.

[Linux](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

```

```

[Windows Server 2019, Windows Server 2022, Windows Server 2025](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

Run the command in[Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows)as an administrator.

```

```

[Windows Server earlier than 2019](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

Run the command in[Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows)as an administrator.

```

```

If there is a clock skew error, a message similar to the following displays:
```

```

- If a clock skew error occurs,[configure the Oracle Cloud Infrastructure NTP service for your instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringntpservice.htm). If no clock skew error occurs,[verify that gateways are configured correctly](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__gateways).
- If you configured the NTP service in the previous step, after you complete the configuration, run one of the following commands to restart Oracle Cloud Agent:

[Oracle Linux 7.x and later versions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

```

```

[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

```

```

[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

Run the command in[Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows)as an administrator.

```

```

- 

Generate the`monitoring.log`file again.

If Oracle Cloud Agent is running correctly, a successful response is 200 OK . In the`monitoring.log`, look for a message similar to the following:
```

```

### Verify Permissions for Windows Domain Joined Instances

If you have a Windows instance that is joined to a domain, verify that the virtual account is granted the Log on as a service user right in the local Group Policy. To set permissions, follow the steps for enabling service log on through a local group policy in Microsoft's[Enable Service Logon](https://docs.microsoft.com/en-us/system-center/scsm/enable-service-log-on-sm?view=sc-sm-2019#enable-service-log-on-through-a-local-group-policy)guide. For Log on as a service , add the user NT SERVICE\ALL SERVICES or the specific user.

### Verify that Gateways are Configured Correctly

For Oracle Cloud Agent to communicate with Oracle services, gateways in subnets must be configured correctly. Follow these steps to verify and correct your configuration.
- [Configure the internet gateway, NAT gateway, or service gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm)for the subnet in your VCN.
- After you follow the configuration steps, restart the services using the commands in the[Verify that the Instance Can Access the Instance Metadata Service Endpoint](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__instancemetadataserviceendpoint)section. After you restart the services, check the`monitoring.log`file for successful requests to Oracle services.

### Change Proxy Server Settings

Sometimes, local proxy servers prevent Oracle Cloud Agent from communicating with any services. Each proxy server is different.

Often, setting the`http_proxy`,`https_proxy`, and`no_proxy`environment variables for the`oracle-cloud-agent`and`oracle-cloud-agent-updater`services on the proxy client instances resolves proxy issues. After you set these environment variables, in the proxy server`access.log`file (or equivalent, depending on your system), verify that you see requests from the proxy client to services that Oracle Cloud Agent accesses.

[Oracle Linux](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

- 

Run the following command.

```

```

- 

In the editor window, add the following entries, and then save the file.

```

```

- &lt;proxy_url&gt; is the proxy URL.
- &lt;proxy_port&gt; is the proxy port.
- Repeat the previous two steps for the`oracle-cloud-agent-updater`service.
- 

Run the following commands, and then restart the services.

```

```

[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

- 

Run the following command.

```

```

- 

In the editor window, add the following entries, and then save the file.

```

```

- &lt;proxy_url&gt; is the proxy URL.
- &lt;proxy_port&gt; is the proxy port.
- Repeat the previous two steps for the`snap.oracle-cloud-agent.oracle-cloud-agent-updater`service.
- 

Run the following commands, and then restart the services.

```

```

[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

- 

Run the following commands in[Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows)as an administrator. Do not change the casing of the environment variables.

```

```

- &lt;proxy_url&gt; is the proxy URL.
- &lt;proxy_port&gt; is the proxy port.
- 

Restart the`oracle-cloud-agent`and`oracle-cloud-agent-updater`services.

```

```

- 

To verify that the`Custom Logs Monitoring`plugin is able to send metrics, tail the`monitoring.log`file.

Windows Server 2019, Windows Server 2022

```

```

Windows Server versions earlier than 2019

```

```

## Step 4: Generate a Diagnostic File for Oracle Cloud Agent

To make it easier for[Oracle support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)to help you troubleshoot issues with the Oracle Cloud Agent software, you can run the Oracle Cloud Agent diagnostic tool on your compute instances. The diagnostic tool generates a file that contains debugging information and logs for the plugins that Oracle Cloud Agent manages.

The diagnostic tool is installed with Oracle Cloud Agent version 1.14.0 and later. To update Oracle Cloud Agent, see[Updating the Oracle Cloud Agent Software](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#update-agent).

After you complete the previous troubleshooting steps, run the diagnostic tool and then file a[support ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)with the file that contains debugging information and logs for the plugins.

[To generate a diagnostic file on a Linux instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

- [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm).
- 

Change directories to the folder where the diagnostic tool is saved:

```

```

- 

Run the diagnostic tool:

```

```

The tool generates a TAR file with a name in the format`oca-diag- <date> . <identifier> .tar.gz`. Provide the file when you open the support request.

[To generate a diagnostic file on a Windows instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#)

- [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm).
- Open PowerShell as an administrator.
- 

Change directories to the folder where the diagnostic tool is saved:

```

```

- 

Run the diagnostic tool:

```

```

The tool generates a ZIP file and saves it to`C:\Users\opc\Desktop\`
