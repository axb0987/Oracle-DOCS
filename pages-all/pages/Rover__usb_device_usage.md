# Connecting USB Devices to Instances
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/usb_device_usage.htm
- Fetched: 2026-09-05 03:03 CDT

# Connecting USB Devices to Instances

Use USB devices with Roving Edge devices.

You can connect a USB device to your Roving Edge device and make it available to a compute instance (see[Identify Front and Rear Panel Items](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/rear_panel_identification.htm#rear_panel_identification)). For example, you can attach a camera to the OpenCV analytics workload, or attach a Mobius VPU to an inferencing workload.

Using a USB device with your Ultra device requires you create your compute instance using the Specialty shape type (see[Instance Shapes](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/instance-shapes.htm#instance-shapes)).

The USB devices that you plug into the Ultra device become available to the instance using the PCI passthrough. See[Creating an Instance on a Roving Edge Infrastructure Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create_instance.htm#LaunchInstance)for more information.

## Installing the Driver

Ensure that the image that you use to create the instance is a USB shape and has the driver needed to run the USB device. Unplug and then plug in the USB device to verify that the instance reports new network interfaces after plugging in the device. In Linux, the command to list the set of network interfaces is usually`ifconfig`.

If the instance cannot recognize the USB device, install the necessary driver. Consult with the device manufacturers for the drivers and installation instructions. You might need to enable some services and reboot the instance for the installed driver to run.
Tip  
  

After you confirm that the instance recognizes the USB device, We recommend you create an instance image from the instance for creating future USB-enabled instances.

## IP and Route Setup

For Wi-Fi dongles, refer to its documentation on how to connect to wireless networks.

For USB Ethernet adapters, you might want to set up the respective network interfaces. Here are some Linux commands to help you set up the interfaces.
- 

Confirm the name of the USB Ethernet network interface:`ip addr sh | grep "inet"`
- 

Add an IP on the network interface:`sudo ip addr add IP / subnet_mask dev interface_name`
- 

Show all routes:`ip route sh`
- 

Show the route to a specific destination:`ip route get destination_IP / FQDN`
- 

Add a route:`sudo ip route add destination_IP / subnet_mask via gateway_IP dev interface_name`

You can adjust the`iptables`rules on the instance as well.

To check whether traffic goes through and arrives at specific destinations using the specific interface (and IP) as wanted, use the`ping`and`tcpdump`commands. For example:
- 

Ping a specific destination:`ping destination`
- 

Check if ping packets arrive at an interface:`sudo tcpdump -i interface_name icmp -n`
