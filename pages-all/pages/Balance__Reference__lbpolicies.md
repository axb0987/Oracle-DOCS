# Load Balancer Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/lbpolicies.htm
- Fetched: 2026-09-05 01:40 CDT

# Load Balancer Policies

Apply load balancer policies to control traffic distribution to your backend servers.

After you create a load balancer, you can apply policies to control traffic distribution to your backend servers. The Load Balancer service supports three primary policy types:
- [Round Robin](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/lbpolicies.htm#round-robin)
- [Least Connections](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/lbpolicies.htm#least-connections)
- [IP Hash](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/lbpolicies.htm#ip-hash)

When processing load or capacity varies among backend servers, you can refine each of these policy types with backend server weighting . Weighting affects the proportion of requests directed to each server. For example, a server weighted '3' receives three times the number of connections as a server weighted '1.' You assign weights based on criteria of your choosing, such as each server's traffic-handling capacity. Weight values must be from 1 to 100.

Load balancer policy decisions apply differently to TCP load balancers, cookie-based session persistent HTTP requests (sticky requests), and non-sticky HTTP requests.
- A TCP load balancer considers policy and weight criteria to direct an initial incoming request to a backend server. All subsequent packets on this connection go to the same endpoint.
- An HTTP load balancer configured to handle cookie-based session persistence forwards requests to the backend server specified by the cookie's session information.
- For non-sticky HTTP requests, the load balancer applies policy and weight criteria to every incoming request and specifies an appropriate backend server. Multiple requests from the same client could be directed to different servers.
Note  
  
To create a load balancer with a reserve IP, add this policy:
```

```

See[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)for general information on policies.

## Round Robin

Round Robin is the default load balancer policy. This policy distributes incoming traffic sequentially to each server in a backend set list. After each server has received a connection, the load balancer repeats the list in the same order.

Round Robin is a simple load balancing algorithm. It works best when all the backend servers have similar capacity and the processing load required by each request doesn't vary.

## Least Connections

The Least Connections policy routes incoming non-sticky request traffic to the backend server with the fewest active connections. This policy helps you maintain an equal distribution of active connections with backend servers. As with the round robin policy, you can assign a weight to each backend server and further control traffic distribution.
Note  
  
In TCP use cases, a connection can be active but have no current traffic. Such connections do not serve as a good load metric.

## IP Hash

The IP Hash policy uses an incoming request's source IP address as a hashing key to route non-sticky traffic to the same backend server. The load balancer routes requests from the same client to the same backend server as long as that server is available. This policy honors server weight settings when establishing the initial connection.

IP Hash ensures that requests from a particular client are always directed to the same backend server, as long as the backend server is available.

You can't add a backend server marked as Backup to a backend set that uses the IP Hash policy.
Important
