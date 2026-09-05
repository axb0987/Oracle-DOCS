# Starting the Windows Client Service
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_start_windows_client_installer.htm
- Fetched: 2026-09-05 02:34 CDT

# Starting the Windows Client Service

Learn how to start Windows client service.
- Open the Windows start menus and search for "Services" to find the Services system application.
- Right-click Services and select Run as Administrator .
- In the Services window, select Oracle Cloud Dedicated Key Management Service from the list of services.
- Right-click and select Start .
- In the Services window, ensure that the Oracle Cloud infrastructure Dedicated key management service has the "running" status.

After you start the service, you can see client daemon log files added to`logfiles_location`. defined in`client.cfg`. A successful start of the service has the`HSM Return: SUCCESS`
