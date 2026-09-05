# RADIUS Proxy
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/radius-proxy.htm
- Fetched: 2026-09-05 02:29 CDT

# RADIUS Proxy

Learn how to troubleshoot common RADIUS Proxy issues.

## /sbin/service idcs_radius is Stopped

When you see that the status of`/sbin/service idcs_radiusd`is stopped, use the following steps.

- Check that the radius agent is running by using the following Python command:`<radius_proxy_installer_location>/oracle_radius_proxy/radius_agent/scripts/src/radius_agent.py status`
- If the status is running, check the agent logs at:`<radius_proxy_installer_location>/oracle_radius_proxy/radius_agent/logs/agent.log`
- If you see the following exception in the RADIUS Proxy logs (`<radius_proxy_installer_location>/oracle_radius_proxy/radius_proxy/log/radius_proxy.log`), ensure that the host entry is correct in the RADIUS Proxy listener:`Exception in thread "main" java.net.BindException: Cannot assign requested address at sun.nio.ch.Net.bind0(Native Method)`
