# Creating a Network Load Balancer Listener
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/create-listener.htm
- Fetched: 2026-09-05 02:48 CDT

# Creating a Network Load Balancer Listener

Create a listener that checks for incoming traffic on the IP address of a network load balancer.
For prerequisite information, see[Listeners for Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/listener-management.htm).
Note  
  
If you selected L3 IP as the listener traffic type, the backend set you select must have the preserve source ID feature enabled. Only those backend sets with that feature enabled are available to select from the Backend set list.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/create-listener.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/create-listener.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/create-listener.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Listeners .
- Select Create listener .
- Enter the following information:

- Name : Specify a friendly name for the listener. The name must be unique, and can't be changed. Avoid entering confidential information.
- Protocol : Select one of the following options:
- Public network load balancers:
- UDP
- TCP
- UDP/TCP
- L3 IP
- Private network load balancers:
- UDP
- TCP
- UDP/TCP
- TCP/UDP/ICMP
- L3 IP
- IP protocol version : Required if you previously enabled IPv6 Address Assignment. The load balancer listener and backend set must use the same IP protocol version.
- Ingress traffic port : Select one of the following options to specify the port your listener monitors for ingress traffic depending on the traffic type:
- Public network load balancers:
- Use any port : This option uses a 0 or wildcard as the port.
- Select the port : Enter the port you want to use.
- Private network load balancers:
- Use any port : This option uses a 0 or wildcard as the port.
- Select the port : (UDP, TCP, and UDP/TCP only) Enter the port you want to use.
- UDP and TCP: Select one of the following options:
- Use any port: This option uses a 0 or wildcard as the port.
- Select the Port: Enter the port you want to use.
- UDP/TCP : Uses any port.
- Backend set : Specify the default backend set to which the listener routes traffic from the list.
Note  
  
If you selected L3 IP as the listener traffic type, the backend set you select must have the preserve source ID feature enabled. Only those backend sets with that feature enabled are available to select from the Backend set list.
- Timeout :
Enter the timeout for each traffic type in seconds. If you don't enter a timeout value, the default values are used. The number of timeout values you must enter varies depending on the listener traffic type you selected earlier:
- UDP : One timeout. Default is 120 seconds.
- TCP : One timeout. Default is 360 seconds.
- UDP/TCP : Two timeouts, one for each protocol (UDP and TCP). Default is 120 and 360 seconds.
- L3IP : Three timeouts, for one for each protocol (L3IP, UDP, and TCP). Default is 120, 120, and 360 seconds.
- Select Create listener .
The listener you create appears in the Listener list of the network load balancer.
- 

Use the[oci nlb listener create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/listener/create.html)command to create a listener for a network load balancer:

```

```

For the`protocol`on which the listener accepts connection requests, use one of the following values:

- `TCP`: Allows only TCP traffic on a specific or all ports.
- `UDP`: Allows only UDP traffic on a specific or all ports.
- `TCP_AND_UDP`: Allows both TCP and UDP traffic on a specific or all ports.
- `ANY`: Allows both TCP and UDP traffic on any port and also allows ICMP traffic. This option is only for SRC/DST header preserved mode (transparent mode).
- `L3IP`: Allows Layer 3 IP traffic.

To change the default idle timeout settings for listeners, see[Changing a Listener's Idle Timeout](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/../NetworkLoadBalancers/configure-idle-timeout.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateListener](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/Listener/CreateListener)
