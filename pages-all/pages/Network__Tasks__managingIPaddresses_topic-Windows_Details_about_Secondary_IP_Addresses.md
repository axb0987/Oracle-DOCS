# Configuring Windows to Use a Secondary IP Addresses
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Windows_Details_about_Secondary_IP_Addresses.htm
- Fetched: 2026-09-05 02:45 CDT

# Configuring Windows to Use a Secondary IP Addresses

Configure the Windows OS to use a secondary private IP.
[After assigning a secondary private IP to a VNIC, you must configure the OS to use it](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm). Here are instructions for using a PowerShell script or the Network and Sharing Center UI.

[Using a PowerShell Script](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Windows_Details_about_Secondary_IP_Addresses.htm#)

You must run PowerShell as an administrator. The script configures two things: static IP addressing on the instance and the secondary private IP. The configuration persists through a reboot of the instance.
- In a browser, go to the Console, and note the secondary private IP address that you want to configure on the instance.
- 

Connect to the instance, and run the following command at a command prompt:

```

```

- 

Note the values for the following items so you can enter them into the script in the next step:
- Default Gateway
- DNS Servers
- 

Replace the variables in the following PowerShell script with appropriate values:

```

```

For example:

```

```

- 

Save the script with a name you select and a`.ps1`extension, and run it on the instance.
[

If you run`ipconfig /all`again, see that DHCP has been disabled and the secondary private IP address is included in the list of IP addresses.

Later, to delete the address, you can use this command:

```

```

Also, ensure that you[delete the secondary IP from the VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-delete.htm). You can do that before or after executing the preceding command to delete the address from the OS configuration.

[Using the Network and Sharing Center UI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Windows_Details_about_Secondary_IP_Addresses.htm#)

The following instructions configure two things: static IP addressing on the instance and the secondary private IP. The configuration persists through a reboot of the instance.
- In a browser, go to the Console, and note the secondary private IP address that you want to configure on the instance.
- 

Connect to the instance, and run the following command at a command prompt:

```

```

[
- 

Note the values for the following items so you can enter them elsewhere in a later step:
- IPv4 Address
- Subnet Mask
- Default Gateway
- DNS Servers
- In the instance's Control Panel , open the Network and Sharing Center (see the image that follows for the set of dialog boxes in these steps).
- For the active networks, select the connection ( Ethernet ).
- Select Properties .
- Select Internet Protocol Version 4 (TCP/IPv4) , and then select Properties .
- 

Select the radio button for Use the following IP address , and then enter the values you noted earlier for the IP address, subnet mask, default gateway, and DNS servers.
[
- Select Advanced... .
- Under IP addresses , select Add... .
- 

Enter the secondary private IP address and the subnet mask you used earlier and select Add .
[
- Select OK until the Network and Sharing Center is closed.
- 

Verify the changes by returning to the command prompt and running`ipconfig /all`.

You should now see that DHCP is disabled (static IP addressing is enabled), and the secondary private IP address is in the list of addresses displayed. The address is now configured on the instance and available to use.
[
Note  
  

You might not see the primary private IP address when you again view the properties for Internet Protocol Version 4 (TCP/IPv4) in the Network and Sharing Center UI. The best way to confirm changes is to use`ipconfig /all`
