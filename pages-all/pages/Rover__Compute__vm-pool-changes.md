# Updating a Roving Edge Infrastructure Device Instance when the IP Pool Range Changes
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/vm-pool-changes.htm
- Fetched: 2026-09-05 02:58 CDT

# Updating a Roving Edge Infrastructure Device Instance when the IP Pool Range Changes

Describes how to update your instance's public IP when you change your instance's public IP address pool range without having to recreate the instances.

You can change your instance's public IP range without having to recreate your instances. Updating your instances when the IP address pool changes requires you to perform the following tasks:
- 

Configuring the attached VNIC for no public IP. You can do this through the Device Console.
- 

Use the serial console to specify the updated pool range of public IP addresses available for use.
- 

Use the Device Console to reconfigure the attached VNIC back to using an ephemeral or reserved public IP.

- Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- Select a State from the list to limit the instances displayed to that state.
- Select the instance whose public IP address you want to change. The instance's Details page appears.
- Select Attached VNICs under Resources . The Attached VNICs page appears.
- Select the attached VNIC whose IP address you want to update. The attached VNIC's Details page appears.
- Select IP Addresses under Resources . The IP Addresses page appears. The IP addresses are displayed in tabular form.
- Select the Actions menu ( ) next to the IP address you need to make private and select Edit . The Edit Private IP Address dialog box appears.
- Select No public IP and select Update .
- Open the Roving Edge Infrastructure device's serial console. See[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/../Getting_Started/setting_up_devices.htm#OperatingSerialConsole).
- Select Configure Networking . The Network Configuration menu appears.
- Select Display Public IP Pool Status . The serial console displays the public IP address pool ranges. Press`ENTER`to exit.
- Select Set IP Pool Range for Compute Instances . Enter a list of IP address ranges separated by`ENTER`. Use the following format:`x.x.x.x - y.y.y.y`to specify the beginning and end of the range. If the range is a single address, just enter that address by itself. Press`ENTER`to exit.
- Reopen the Edit Private IP Address dialog box and select the Ephemeral public IP or Reserved public IP option.
-
