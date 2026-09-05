# Virtual Hostnames for Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/hostname_management.htm
- Fetched: 2026-09-05 01:41 CDT

# Virtual Hostnames for Load Balancers

Use virtual hostnames to assign a hostname to a load balancer listener.

When used in concert with records you create in your DNS system, you can assign virtual hostnames to any listener you create for your load balancer. Hostnames associated with a listener correspond to the backend sets of that listener. These backend sets route traffic to specific backends which host different applications. Some advantages of virtual hostnames include:
- A single associated IP address. Multiple hostnames, backed by DNS entries that you create in your nameservers, can point to the same load balancer IP address.
- A single load balancer. You don't need a separate load balancer for each application.
- A single load balancer shape. Running several applications behind a single load balancer helps you manage aggregate bandwidth demands and optimize usage.
- Simpler backend set management. Managing a set of backend servers under a single resource simplifies network configuration and administration.

You can perform the following virtual hostname management tasks:

[List the virtual hostnames for a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-hostname.htm)

[Create a new virtual hostname for a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_hostname.htm)

[Get a virtual hostname's details.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_hostname.htm)

[Edit a virtual hostname's settings.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_hostname.htm)

[Delete a virtual hostname from a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_hostname.htm)

## Defining Hostnaming

You can define exact virtual hostnames, such as "app.example.com," or you can use wildcard names. Wildcard names include an asterisk (*) in place of the first or last part of the name. When searching for a virtual hostname, the service chooses the first matching variant in the following priority order:
- Exact name match (no asterisk), such as`app.example.com`.
- Longest wildcard name that begins with an asterisk, such as`*.example.com`.
Note  
  
Prefix wildcard names might require a wildcard certificate for HTTPS sites.
- Longest wildcard name that ends with an asterisk, such as`app.example.*`.
Note  
  
Suffix wildcard names might require a multi-domain Subject Alternative Name (SAN) certificate for HTTPS sites.

You don't need to specify the matching pattern to apply. The pattern is inherent in the asterisk position, that is, starting, ending, or none.

The following considerations apply to virtual hostnames:
- You can't use regular expressions.
- To apply virtual hostnames to a listener, you first create one or more virtual hostnames associated with a load balancer.
- Virtual hostname selection priority is not related to the listener's configuration order.
- You can apply a maximum of 16 virtual hostnames to a listener.
- You can associate a maximum of 16 virtual hostnames with a load balancer.
Note  
  
The virtual hostnames feature supports HTTP and HTTPS listeners only, but does not support TCP listeners.
Note  
  

Default Listener

If a listener has no virtual hostname specified, that listener is the default for the assigned port.
