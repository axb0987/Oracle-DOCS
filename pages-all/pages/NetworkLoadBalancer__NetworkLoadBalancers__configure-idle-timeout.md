# Changing a Listener's Idle Timeout
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/configure-idle-timeout.htm
- Fetched: 2026-09-05 02:48 CDT

# Changing a Listener's Idle Timeout

Change the idle timeout for a listener in a network load balancer.

The default idle timeout duration for the supported listener protocols are:
- 

TCP: 360 seconds (6 minutes).
- 

UDP: 120 seconds (2 minutes).
- 

L3IP: 120 seconds (2 minutes).

You can adjust this time when initially configuring the listener when creating a network load balancer, and also when editing the configuration of an existing listener.

The TCP and UDP timeout configurations and the default values remains valid for the TCP and UDP protocols in the L3IP listener. And the L3IP timeout covers for the rest of the protocols in the L3IP listeners.
Note  
  

You can only change the idle timeout using the CLI or API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/configure-idle-timeout.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/configure-idle-timeout.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/configure-idle-timeout.htm#)
- 

This task can't be performed using the Console.
- 

Use the`tcp-idle-timeout`,`udp-idle-timeout`, and`l3-ip-idle-timeout`parameters to configure the idle timeout for TCP, UDP, and L3IP listeners when creating or editing a listener. Specify the timeout value in seconds. For example:
```

```

or
```

```

or
```

```

In these examples, "600" equals 600 seconds or 10 minutes. "360" equals 6 minutes. "200" equals 2 minutes and 40 seconds.
You can include several types of listener idle timeouts in the same command:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the`tcpIdleTimeout`and`udpIdleTimeout`options when running the[CreateListener](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/Listener/CreateListener)or[UpdateListener](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/Listener/UpdateListener)
