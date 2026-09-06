# Network Load Balancer Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#dcoc-content-body)

## Network Load Balancer Common Types

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_T Type

The configuration of a backend server that is a member of a network load balancer backend set. For more information, see[Managing Backend Servers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendservers.htm).

Syntax
```

```

Fields

Field Description

`name`

(optional) A read-only field showing the IP address/IP OCID and port that uniquely identify this backend server in the backend set. Example: `10.0.0.3:8080`, or `ocid1.privateip..oc1.&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;:443` or `10.0.0.3:0`

`ip_address`

(optional) The IP address of the backend server. Example: `10.0.0.3`

`target_id`

(optional) The IP OCID/Instance OCID associated with the backend server. Example: `ocid1.privateip..oc1.&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;`

`port`

(required) The communication port for the backend server. Example: `8080`

`weight`

(optional) The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see[How Network Load Balancing Policies Work](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm). Example: `3`

`is_drain`

(optional) Whether the network load balancer should drain this server. Servers marked \"isDrain\" receive no incoming traffic. Example: `false`

`is_backup`

(optional) Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"isBackup\" fail the health check policy. Example: `false`

`is_offline`

(optional) Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic. Example: `false`

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SUMMARY_T Type

The configuration of a backend server that is a member of a network load balancer backend set. For more information, see[Managing Backend Servers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendservers.htm).

Syntax
```

```

Fields

Field Description

`name`

(optional) A read-only field showing the IP address/IP OCID and port that uniquely identify this backend server in the backend set. Example: `10.0.0.3:8080`, or `ocid1.privateip..oc1.&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;:443` or `10.0.0.3:0`

`ip_address`

(optional) The IP address of the backend server. Example: `10.0.0.3`

`target_id`

(optional) The IP OCID/Instance OCID associated with the backend server. Example: `ocid1.privateip..oc1.&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;`

`port`

(required) The communication port for the backend server. Example: `8080`

`weight`

(optional) The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see[How Network Load Balancing Policies Work](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm). Example: `3`

`is_drain`

(optional) Whether the network load balancer should drain this server. Servers marked \"isDrain\" receive no incoming traffic. Example: `false`

`is_backup`

(optional) Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"isBackup\" fail the health check policy. Example: `false`

`is_offline`

(optional) Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic. Example: `false`

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_backend_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_COLLECTION_T Type

Wrapper object for an array of BackendSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(optional) An array of BackendSummary objects.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_DETAILS_T Type

The network network load balancing configuration details of a backend server.

Syntax
```

```

Fields

Field Description

`name`

(optional) A read-only field showing the IP address/OCID and port that uniquely identify this backend server in the backend set. Example: `10.0.0.3:8080`, or `ocid1.privateip..oc1.&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;:443` or `10.0.0.3:0`

`ip_address`

(optional) The IP address of the backend server. Example: `10.0.0.3`

`target_id`

(optional) The IP OCID/Instance OCID associated with the backend server. Example: `ocid1.privateip..oc1.&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;`

`port`

(required) The communication port for the backend server. Example: `8080`

`weight`

(optional) The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see[How Network Load Balancing Policies Work](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm). Example: `3`

`is_backup`

(optional) Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"isBackup\" fail the health check policy. Example: `false`

`is_drain`

(optional) Whether the network load balancer should drain this server. Servers marked \"isDrain\" receive no incoming traffic. Example: `false`

`is_offline`

(optional) Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic. Example: `false`

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_HEALTH_CHECK_RESULT_T Type

Information about a single backend server health check result reported by a network load balancer.

Syntax
```

```

Fields

Field Description

`l_timestamp`

(required) The date and time the data was retrieved, in the format defined by RFC3339. Example: `2020-05-01T18:28:11+00:00`

`health_check_status`

(required) The result of the most recent health check.

Allowed values are: 'OK', 'INVALID_STATUS_CODE', 'TIMED_OUT', 'HEALTH_PAYLOAD_MISMATCH', 'CONNECT_FAILED', 'UNKNOWN'

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_HEALTH_CHECK_RESULT_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_health_check_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_HEALTH_T Type

The health status of the specified backend server.

Syntax
```

```

Fields

Field Description

`status`

(required) The general health status of the specified backend server. * **OK:** All health check probes return `OK` * **WARNING:** At least one of the health check probes does not return `OK` * **CRITICAL:** None of the health check probes return `OK`. * * **UNKNOWN:** One of the health checks probes return `UNKNOWN`, * or the system is unable to retrieve metrics at this time.

Allowed values are: 'OK', 'WARNING', 'CRITICAL', 'UNKNOWN'

`health_check_results`

(required) A list of the most recent health check results returned for the specified backend server.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_HEALTH_CHECKER_T Type

The health check policy configuration. For more information, see[Editing Health Check Policies](https://docs.oracle.com/iaas/Content/Balance/Tasks/editinghealthcheck.htm).

Syntax
```

```

Fields

Field Description

`protocol`

(required) The protocol the health check must use; either HTTP or HTTPS, or UDP or TCP. Example: `HTTP`

Allowed values are: 'HTTP', 'HTTPS', 'TCP', 'UDP'

`port`

(optional) The backend server port against which to run the health check. If the port is not specified, then the network load balancer uses the port information from the `Backend` object. The port must be specified if the backend port is 0. Example: `8080`

`retries`

(optional) The number of retries to attempt before a backend server is considered \"unhealthy\". This number also applies when recovering a server to the \"healthy\" state. The default value is 3. Example: `3`

`timeout_in_millis`

(optional) The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. The default value is 3000 (3 seconds). Example: `3000`

`interval_in_millis`

(optional) The interval between health checks, in milliseconds. The default value is 10000 (10 seconds). Example: `10000`

`url_path`

(optional) The path against which to run the health check. Example: `/healthcheck`

`response_body_regex`

(optional) A regular expression for parsing the response body from the backend server. Example: `^((?!false).|\\s)*$`

`return_code`

(optional) The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol, then you can use common HTTP status codes such as \"200\". Example: `200`

`request_data`

(optional) Base64 encoded pattern to be sent as UDP or TCP health check probe.

`response_data`

(optional) Base64 encoded pattern to be validated as UDP or TCP health check probe response.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_backend_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SET_T Type

The configuration of a network load balancer backend set. For more information about backend set configuration, see[Managing Backend Sets](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendsets.htm). **Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) A user-friendly name for the backend set that must be unique and cannot be changed. Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information. Example: `example_backend_set`

`policy`

(optional) The network load balancer policy for the backend set. Example: `FIVE_TUPLE`

Allowed values are: 'TWO_TUPLE', 'THREE_TUPLE', 'FIVE_TUPLE'

`is_preserve_source`

(optional) If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.

`ip_version`

(optional) IP version associated with the backend set.

Allowed values are: 'IPV4', 'IPV6'

`backends`

(optional) Array of backends.

`health_checker`

(required)

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SET_SUMMARY_T Type

The configuration of a network load balancer backend set. For more information about backend set configuration, see[Managing Backend Sets](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendsets.htm). **Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) A user-friendly name for the backend set that must be unique and cannot be changed. Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information. Example: `example_backend_set`

`policy`

(required) The network load balancer policy for the backend set. Example: `FIVE_TUPLE`

Allowed values are: 'TWO_TUPLE', 'THREE_TUPLE', 'FIVE_TUPLE'

`is_preserve_source`

(optional) If this parameter is enabled, the network load balancer preserves the source IP of the packet forwarded to the backend servers. Backend servers see the original source IP. If the `isPreserveSourceDestination` parameter is enabled for the network load balancer resource, this parameter cannot be disabled. The value is true by default.

`ip_version`

(optional) IP version associated with the backend set.

Allowed values are: 'IPV4', 'IPV6'

`backends`

(required) An array of backends.

`health_checker`

(required)

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_backend_set_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SET_COLLECTION_T Type

Wrapper object for an array of `BackendSetSummary` objects.

Syntax
```

```

Fields

Field Description

`items`

(optional) An array of `BackendSetSummary` objects.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SET_DETAILS_T Type

The configuration of a network load balancer backend set. For more information about backend set configuration, see[Managing Backend Sets](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendsets.htm). **Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`policy`

(optional) The network load balancer policy for the backend set. Example: `FIVE_TUPLE`

Allowed values are: 'TWO_TUPLE', 'THREE_TUPLE', 'FIVE_TUPLE'

`ip_version`

(optional) IP version associated with the backend set.

Allowed values are: 'IPV4', 'IPV6'

`is_preserve_source`

(optional) If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.

`backends`

(optional) An array of backends.

`health_checker`

(required)

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SET_HEALTH_T Type

The health status details for a backend set. This object does not explicitly enumerate backend servers with a status of `OK`. However, the backend sets are included in the `totalBackendCount` sum.

Syntax
```

```

Fields

Field Description

`status`

(required) Overall health status of the backend set. * **OK:** All backend servers in the backend set return a status of `OK`. * **WARNING:** Half or more of the backend servers in a backend set return a status of `OK` and at least one backend server returns a status of `WARNING`, `CRITICAL`, or `UNKNOWN`. * **CRITICAL:** Fewer than half of the backend servers in a backend set return a status of `OK`. * **UNKNOWN:** If no probes have yet been sent to the backends, or the system is unable to retrieve metrics from the backends.

Allowed values are: 'OK', 'WARNING', 'CRITICAL', 'UNKNOWN'

`warning_state_backend_names`

(required) A list of backend servers that are currently in the `WARNING` health state. The list identifies each backend server by IP address or OCID and port. Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;:8080`

`critical_state_backend_names`

(required) A list of backend servers that are currently in the `CRITICAL` health state. The list identifies each backend server by IP address and port. Example: `10.0.0.4:8080`

`unknown_state_backend_names`

(required) A list of backend servers that are currently in the `UNKNOWN` health state. The list identifies each backend server by IP address and port. Example: `10.0.0.5:8080`

`total_backend_count`

(required) The total number of backend servers in this backend set. Example: `7`

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_CHANGE_NETWORK_LOAD_BALANCER_COMPARTMENT_DETAILS_T Type

The configuration details for moving a network load balancer to a different compartment. **Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to which to move the network load balancer.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_CREATE_BACKEND_DETAILS_T Type

The configuration of a backend server that is a member of a network load balancer backend set. For more information, see[Managing Backend Servers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendservers.htm).

Syntax
```

```

Fields

Field Description

`name`

(optional) Optional unique name identifying the backend within the backend set. If not specified, then one will be generated. Example: `webServer1`

`ip_address`

(optional) The IP address of the backend server. Example: `10.0.0.3`

`target_id`

(optional) The IP OCID/Instance OCID associated with the backend server. Example: `ocid1.privateip..oc1.&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;`

`port`

(required) The communication port for the backend server. Example: `8080`

`weight`

(optional) The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see[How Network Load Balancing Policies Work](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm). Example: `3`

`is_drain`

(optional) Whether the network load balancer should drain this server. Servers marked \"isDrain\" receive no incoming traffic. Example: `false`

`is_backup`

(optional) Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"isBackup\" fail the health check policy. Example: `false`

`is_offline`

(optional) Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic. Example: `false`

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_HEALTH_CHECKER_DETAILS_T Type

The health check policy configuration. For more information, see[Editing Health Check Policies](https://docs.oracle.com/iaas/Content/Balance/Tasks/editinghealthcheck.htm).

Syntax
```

```

Fields

Field Description

`protocol`

(required) The protocol the health check must use; either HTTP or HTTPS, or UDP or TCP. Example: `HTTP`

Allowed values are: 'HTTP', 'HTTPS', 'TCP', 'UDP'

`port`

(optional) The backend server port against which to run the health check. If the port is not specified, then the network load balancer uses the port information from the `Backend` object. The port must be specified if the backend port is 0. Example: `8080`

`retries`

(optional) The number of retries to attempt before a backend server is considered \"unhealthy\". This number also applies when recovering a server to the \"healthy\" state. The default value is 3. Example: `3`

`timeout_in_millis`

(optional) The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. The default value is 3000 (3 seconds). Example: `3000`

`interval_in_millis`

(optional) The interval between health checks, in milliseconds. The default value is 10000 (10 seconds). Example: `10000`

`url_path`

(optional) The path against which to run the health check. Example: `/healthcheck`

`response_body_regex`

(optional) A regular expression for parsing the response body from the backend server. Example: `^((?!false).|\\s)*$`

`return_code`

(optional) The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol, then you can use common HTTP status codes such as \"200\". Example: `200`

`request_data`

(optional) Base64 encoded pattern to be sent as UDP or TCP health check probe.

`response_data`

(optional) Base64 encoded pattern to be validated as UDP or TCP health check probe response.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_backend_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_CREATE_BACKEND_SET_DETAILS_T Type

The configuration details for creating a backend set in a network load balancer. For more information about backend set configuration, see[Managing Backend Sets](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendsets.htm). **Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`name`

(required) A user-friendly name for the backend set that must be unique and cannot be changed. Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information. Example: `example_backend_set`

`policy`

(required) The network load balancer policy for the backend set. Example: `FIVE_TUPLE``

Allowed values are: 'TWO_TUPLE', 'THREE_TUPLE', 'FIVE_TUPLE'

`is_preserve_source`

(optional) If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.

`ip_version`

(optional) IP version associated with the backend set.

Allowed values are: 'IPV4', 'IPV6'

`backends`

(optional) An array of backends to be associated with the backend set.

`health_checker`

(required)

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_CREATE_LISTENER_DETAILS_T Type

The configuration of the listener. For more information about backend set configuration, see[Managing Load Balancer Listeners](https://docs.oracle.com/iaas/Content/Balance/Tasks/managinglisteners.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) A friendly name for the listener. It must be unique and it cannot be changed. Example: `example_listener`

`default_backend_set_name`

(required) The name of the associated backend set. Example: `example_backend_set`

`port`

(required) The communication port for the listener. Example: `80`

`protocol`

(required) The protocol on which the listener accepts connection requests. For public network load balancers, ANY protocol refers to TCP/UDP. For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true). To get a list of valid protocols, use the`LIST_NETWORK_LOAD_BALANCERS_PROTOCOLS`Function operation. Example: `TCP`

Allowed values are: 'ANY', 'TCP', 'UDP', 'TCP_AND_UDP'

`ip_version`

(optional) IP version associated with the listener.

Allowed values are: 'IPV4', 'IPV6'

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_RESERVED_IP_T Type

An object representing a reserved IP address to be attached or that is already attached to a network load balancer.

Syntax
```

```

Fields

Field Description

`id`

(optional) OCID of the reserved public IP address created with the virtual cloud network. Reserved public IP addresses are IP addresses that are registered using the virtual cloud network API. Create a reserved public IP address. When you create the network load balancer, enter the OCID of the reserved public IP address in the reservedIp field to attach the IP address to the network load balancer. This task configures the network load balancer to listen to traffic on this IP address. Reserved public IP addresses are not deleted when the network load balancer is deleted. The IP addresses become unattached from the network load balancer. Example: \"ocid1.publicip.oc1.phx.unique_ID\"

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_LISTENER_DETAILS_T Type

The listener's configuration. For more information about backend set configuration, see[Managing Load Balancer Listeners](https://docs.oracle.com/iaas/Content/Balance/Tasks/managinglisteners.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) A friendly name for the listener. It must be unique and it cannot be changed. Example: `example_listener`

`default_backend_set_name`

(required) The name of the associated backend set. Example: `example_backend_set`

`ip_version`

(optional) IP version associated with the listener.

Allowed values are: 'IPV4', 'IPV6'

`port`

(required) The communication port for the listener. Example: `80`

`protocol`

(required) The protocol on which the listener accepts connection requests. For public network load balancers, ANY protocol refers to TCP/UDP. For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true). To get a list of valid protocols, use the`LIST_NETWORK_LOAD_BALANCERS_PROTOCOLS`Function operation. Example: `TCP`

Allowed values are: 'ANY', 'TCP', 'UDP', 'TCP_AND_UDP'

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_RESERVED_IP_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_reserved_ip_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_CREATE_NETWORK_LOAD_BALANCER_DETAILS_T Type

The properties that define a network load balancer. For more information, see[Managing a network load balancer](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer.htm). To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, then contact an administrator. If you are an administrator who writes policies to give users access, then see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about endpoints and signing API requests, see[About the API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm). For information about available SDKs and tools, see[SDKS and Other Tools](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the network load balancer.

`display_name`

(required) Network load balancer identifier, which can be renamed.

`is_preserve_source_destination`

(optional) This parameter can be enabled only if backends are compute OCIDs. When enabled, the skipSourceDestinationCheck parameter is automatically enabled on the load balancer VNIC, and packets are sent to the backend with the entire IP header intact.

`reserved_ips`

(optional) An array of reserved Ips.

`is_private`

(optional) Whether the network load balancer has a virtual cloud network-local (private) IP address. If \"true\", then the service assigns a private IP address to the network load balancer. If \"false\", then the service assigns a public IP address to the network load balancer. A public network load balancer is accessible from the internet, depending on the security list rules for your virtual cloud network. For more information about public and private network load balancers, see[How Network Load Balancing Works](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm#how-network-load-balancing-works). This value is true by default. Example: `true`

`subnet_id`

(required) The subnet in which the network load balancer is spawned[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`network_security_group_ids`

(optional) An array of network security groups[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with the network load balancer. During the creation of the network load balancer, the service adds the new load balancer to the specified network security groups. The benefits of associating the network load balancer with network security groups include: * Network security groups define network security rules to govern ingress and egress traffic for the network load balancer. * The network security rules of other resources can reference the network security groups associated with the network load balancer to ensure access. Example: [\"ocid1.nsg.oc1.phx.unique_ID\"]

`nlb_ip_version`

(optional) IP version associated with the NLB.

Allowed values are: 'IPV4', 'IPV4_AND_IPV6'

`listeners`

(optional) Listeners associated with the network load balancer.

`backend_sets`

(optional) Backend sets associated with the network load balancer.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_IP_ADDRESS_T Type

A load balancer IP address.

Syntax
```

```

Fields

Field Description

`ip_address`

(required) An IP address. Example: `192.168.0.3`

`is_public`

(optional) Whether the IP address is public or private. If \"true\", then the IP address is public and accessible from the internet. If \"false\", then the IP address is private and accessible only from within the associated virtual cloud network.

`ip_version`

(optional) IP version associated with this IP address.

Allowed values are: 'IPV4', 'IPV6'

`reserved_ip`

(optional)

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_LISTENER_T Type

The congfiguration of the listener. For more information about backend set configuration, see[Managing Load Balancer Listeners](https://docs.oracle.com/iaas/Content/Balance/Tasks/managinglisteners.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) A friendly name for the listener. It must be unique and it cannot be changed. Example: `example_listener`

`default_backend_set_name`

(required) The name of the associated backend set. Example: `example_backend_set`

`port`

(required) The communication port for the listener. Example: `80`

`protocol`

(required) The protocol on which the listener accepts connection requests. For public network load balancers, ANY protocol refers to TCP/UDP. For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true). To get a list of valid protocols, use the`LIST_NETWORK_LOAD_BALANCERS_PROTOCOLS`Function operation. Example: `TCP`

Allowed values are: 'ANY', 'TCP', 'UDP', 'TCP_AND_UDP'

`ip_version`

(optional) IP version associated with the listener.

Allowed values are: 'IPV4', 'IPV6'

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_LISTENER_SUMMARY_T Type

The configuration of the listener. For more information about backend set configuration, see[Managing Load Balancer Listeners](https://docs.oracle.com/iaas/Content/Balance/Tasks/managinglisteners.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) A friendly name for the listener. It must be unique and it cannot be changed. Example: `example_listener`

`default_backend_set_name`

(required) The name of the associated backend set. Example: `example_backend_set`

`port`

(required) The communication port for the listener. Example: `80`

`protocol`

(required) The protocol on which the listener accepts connection requests. For public network load balancers, ANY protocol refers to TCP/UDP. For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true). To get a list of valid protocols, use the`LIST_NETWORK_LOAD_BALANCERS_PROTOCOLS`Function operation. Example: `TCP`

Allowed values are: 'ANY', 'TCP', 'UDP', 'TCP_AND_UDP'

`ip_version`

(optional) IP version associated with the listener.

Allowed values are: 'IPV4', 'IPV6'

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_LISTENER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_listener_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_LISTENER_COLLECTION_T Type

Wrapper object for an array of ListenerSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(optional) Array of ListenerSummary objects.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_IP_ADDRESS_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_ip_address_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_T Type

The properties that define a network load balancer. For more information, see[Managing a network load balancer](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer.htm). To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, contact an administrator. If you are an administrator who writes policies to give users access, then see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about endpoints and signing API requests, see[About the API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm). For information about available SDKs and tools, see[SDKS and Other Tools](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the network load balancer.

`display_name`

(required) A user-friendly name, which does not have to be unique, and can be changed. Example: `example_load_balancer`

`lifecycle_state`

(required) The current state of the network load balancer.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`nlb_ip_version`

(optional) IP version associated with the NLB.

Allowed values are: 'IPV4', 'IPV4_AND_IPV6'

`time_created`

(required) The date and time the network load balancer was created, in the format defined by RFC3339. Example: `2020-05-01T21:10:29.600Z`

`time_updated`

(optional) The time the network load balancer was updated. An RFC3339 formatted date-time string. Example: `2020-05-01T22:10:29.600Z`

`ip_addresses`

(required) An array of IP addresses.

`is_private`

(optional) Whether the network load balancer has a virtual cloud network-local (private) IP address. If \"true\", then the service assigns a private IP address to the network load balancer. If \"false\", then the service assigns a public IP address to the network load balancer. A public network load balancer is accessible from the internet, depending on the security list rules for your virtual cloud network. For more information about public and private network load balancers, see[How Network Load Balancing Works](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm#how-network-load-balancing-works). This value is true by default. Example: `true`

`is_preserve_source_destination`

(optional) When enabled, the skipSourceDestinationCheck parameter is automatically enabled on the load balancer VNIC. Packets are sent to the backend set without any changes to the source and destination IP.

`subnet_id`

(required) The subnet in which the network load balancer is spawned[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).\"

`network_security_group_ids`

(optional) An array of network security groups[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with the network load balancer. During the creation of the network load balancer, the service adds the new load balancer to the specified network security groups. The benefits of associating the network load balancer with network security groups include: * Network security groups define network security rules to govern ingress and egress traffic for the network load balancer. * The network security rules of other resources can reference the network security groups associated with the network load balancer to ensure access. Example: [\"ocid1.nsg.oc1.phx.unique_ID\"]

`listeners`

(optional) Listeners associated with the network load balancer.

`backend_sets`

(optional) Backend sets associated with the network load balancer.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Key-value pair representing system tags' keys and values scoped to a namespace. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_SUMMARY_T Type

Network load balancer object to be used for list operations.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the network load balancer.

`display_name`

(required) A user-friendly name, which does not have to be unique, and can be changed. Example: `example_load_balancer`

`lifecycle_state`

(required) The current state of the network load balancer.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`nlb_ip_version`

(optional) IP version associated with the NLB.

Allowed values are: 'IPV4', 'IPV4_AND_IPV6'

`time_created`

(required) The date and time the network load balancer was created, in the format defined by RFC3339. Example: `2020-05-01T21:10:29.600Z`

`time_updated`

(optional) The time the network load balancer was updated. An RFC3339 formatted date-time string. Example: `2020-05-01T22:10:29.600Z`

`ip_addresses`

(required) An array of IP addresses.

`is_private`

(optional) Whether the network load balancer has a virtual cloud network-local (private) IP address. If \"true\", then the service assigns a private IP address to the network load balancer. If \"false\", then the service assigns a public IP address to the network load balancer. A public network load balancer is accessible from the internet, depending the security list rules for your virtual cloud network. For more information about public and private network load balancers, see[How Network Load Balancing Works](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm#how-network-load-balancing-works). This value is true by default. Example: `true`

`is_preserve_source_destination`

(optional) When enabled, the skipSourceDestinationCheck parameter is automatically enabled on the load balancer VNIC. Packets are sent to the backend set without any changes to the source and destination IP.

`subnet_id`

(required) The subnet in which the network load balancer is spawned[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).\"

`network_security_group_ids`

(optional) An array of network security groups[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with the network load balancer. During the creation of the network load balancer, the service adds the new load balancer to the specified network security groups. The benefits of associating the network load balancer with network security groups include: * Network security groups define network security rules to govern ingress and egress traffic for the network load balancer. * The network security rules of other resources can reference the network security groups associated with the network load balancer to ensure access. Example: [\"ocid1.nsg.oc1.phx.unique_ID\"]

`listeners`

(optional) Listeners associated with the network load balancer.

`backend_sets`

(optional) Backend sets associated with the network load balancer.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Key-value pair representing system tags' keys and values scoped to a namespace. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_network_load_balancer_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_COLLECTION_T Type

Wrapper object for an array of NetworkLoadBalancerSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(optional) Array of NetworkLoadBalancerSummary objects.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_HEALTH_T Type

The health status details for the specified network load balancer. This object does not explicitly enumerate backend sets with a status of `OK`. However, the backend sets are included in the `totalBackendSetCount` sum.

Syntax
```

```

Fields

Field Description

`status`

(required) The overall health status of the network load balancer. * **OK:** All backend sets associated with the network load balancer return a status of `OK`. * **WARNING:** At least one of the backend sets associated with the network load balancer returns a status of `WARNING`, no backend sets return a status of `CRITICAL`, and the network load balancer life cycle state is `ACTIVE`. * **CRITICAL:** One or more of the backend sets associated with the network load balancer return a status of `CRITICAL`. * **UNKNOWN:** If any one of the following conditions is true: * The network load balancer life cycle state is not `ACTIVE`. * No backend sets are defined for the network load balancer. * More than half of the backend sets associated with the network load balancer return a status of `UNKNOWN`, none of the backend sets return a status of `WARNING` or `CRITICAL`, and the network load balancer life cycle state is `ACTIVE`. * The system could not retrieve metrics for any reason.

Allowed values are: 'OK', 'WARNING', 'CRITICAL', 'UNKNOWN'

`warning_state_backend_set_names`

(required) A list of backend sets that are currently in the `WARNING` health state. The list identifies each backend set by the user-friendly name you assigned when you created the backend set. Example: `example_backend_set3`

`critical_state_backend_set_names`

(required) A list of backend sets that are currently in the `CRITICAL` health state. The list identifies each backend set by the user-friendly name you assigned when you created the backend set. Example: `example_backend_set`

`unknown_state_backend_set_names`

(required) A list of backend sets that are currently in the `UNKNOWN` health state. The list identifies each backend set by the user-friendly name you assigned when you created the backend set. Example: `example_backend_set2`

`total_backend_set_count`

(required) The total number of backend sets associated with this network load balancer. Example: `4`

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_HEALTH_SUMMARY_T Type

A health status summary for the specified network load balancer

Syntax
```

```

Fields

Field Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer with which the health status is associated.

`status`

(required) The overall health status of the network load balancer. * **OK:** All backend sets associated with the network load balancer return a status of `OK`. * **WARNING:** At least one of the backend sets associated with the network load balancer returns a status of `WARNING`, no backend sets return a status of `CRITICAL`, and the network load balancer life cycle state is `ACTIVE`. * **CRITICAL:** One or more of the backend sets associated with the network load balancer returns a status of `CRITICAL`. * **UNKNOWN:** If any one of the following conditions is true: * The network load balancer life cycle state is not `ACTIVE`. * No backend sets are defined for the network load balancer. * More than half of the backend sets associated with the network load balancer return a status of `UNKNOWN`, none of the backend sets returns a status of `WARNING` or `CRITICAL`, and the network load balancer life cycle state is `ACTIVE`. * The system could not retrieve metrics for any reason.

Allowed values are: 'OK', 'WARNING', 'CRITICAL', 'UNKNOWN'

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_HEALTH_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_network_load_balancer_health_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_HEALTH_COLLECTION_T Type

Wrapper object for an array of NetworkLoadBalancerHealthSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(optional) An array of BackendSetSummary objects.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCERS_POLICY_COLLECTION_T Type

Wrapper object for array of NetworkLoadBalancersPolicySummary objects.

Syntax
```

```

Fields

Field Description

`items`

(optional) Array of NetworkLoadBalancersPolicySummary objects.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCERS_PROTOCOL_COLLECTION_T Type

This object is deprecated. Wrapper object for array of ProtocolSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(optional) Array of NetworkLoadBalancersProtocolSummary objects.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_UPDATE_BACKEND_DETAILS_T Type

The configuration details for updating a backend server.

Syntax
```

```

Fields

Field Description

`weight`

(optional) The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see[How Load Balancing Policies Work](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm). Example: `3`

`is_backup`

(optional) Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"isBackup\" fail the health check policy. Example: `false`

`is_drain`

(optional) Whether the network load balancer should drain this server. Servers marked \"isDrain\" receive no incoming traffic. Example: `false`

`is_offline`

(optional) Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic. Example: `false`

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_UPDATE_BACKEND_SET_DETAILS_T Type

The configuration details for updating a load balancer backend set. For more information about backend set configuration, see[Managing Backend Sets](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingbackendsets.htm). **Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`policy`

(optional) The network load balancer policy for the backend set. To get a list of available policies, use the`LIST_NETWORK_LOAD_BALANCERS_POLICIES`Function operation. Example: `FIVE_TUPLE`

`is_preserve_source`

(optional) If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.

`ip_version`

(optional) The IP version associated with the backend set.

Allowed values are: 'IPV4', 'IPV6'

`backends`

(optional) An array of backends associated with the backend set.

`health_checker`

(optional)

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_UPDATE_HEALTH_CHECKER_DETAILS_T Type

The configuration details of the health checker.

Syntax
```

```

Fields

Field Description

`protocol`

(optional) The protocol that the health check must use; either HTTP, UDP, or TCP. Example: `HTTP`

Allowed values are: 'HTTP', 'HTTPS', 'TCP', 'UDP'

`port`

(optional) The backend server port against which to run the health check. Example: `8080`

`retries`

(optional) The number of retries to attempt before a backend server is considered \"unhealthy\". This number also applies when recovering a server to the \"healthy\" state. Example: `3`

`timeout_in_millis`

(optional) The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. Example: `3000`

`interval_in_millis`

(optional) The interval between health checks, in milliseconds. Example: `10000`

`url_path`

(optional) The path against which to run the health check. Example: `/healthcheck`

`response_body_regex`

(optional) A regular expression for parsing the response body from the backend server. Example: `^((?!false).|\\s)*$`

`return_code`

(optional) The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol, then you can use common HTTP status codes such as \"200\". Example: `200`

`request_data`

(optional) Base64 encoded pattern to be sent as UDP or TCP health check probe.

`response_data`

(optional) Base64 encoded pattern to be validated as UDP or TCP health check probe response.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_UPDATE_LISTENER_DETAILS_T Type

The configuration of the listener. For more information about backend set configuration, see[Managing Network Load Balancer Listeners](https://docs.oracle.com/iaas/Content/Balance/Tasks/managinglisteners.htm).

Syntax
```

```

Fields

Field Description

`default_backend_set_name`

(optional) The name of the associated backend set. Example: `example_backend_set`

`port`

(optional) The communication port for the listener. Example: `80`

`protocol`

(optional) The protocol on which the listener accepts connection requests. For public network load balancers, ANY protocol refers to TCP/UDP. For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true). To get a list of valid protocols, use the`LIST_NETWORK_LOAD_BALANCERS_PROTOCOLS`Function operation. Example: `TCP`

Allowed values are: 'ANY', 'TCP', 'UDP', 'TCP_AND_UDP'

`ip_version`

(optional) IP version associated with the listener.

Allowed values are: 'IPV4', 'IPV6'

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_UPDATE_NETWORK_LOAD_BALANCER_DETAILS_T Type

Configuration details to update a network load balancer. **Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly display name for the network load balancer, which does not have to be unique and can be changed. Avoid entering confidential information. Example: `example_network_load_balancer`

`is_preserve_source_destination`

(optional) This parameter can be enabled only if backends are compute OCIDs. When enabled, the skipSourceDestinationCheck parameter is automatically enabled on the load balancer VNIC, and packets are sent to the backend with the entire IP header intact.

`nlb_ip_version`

(optional) IP version associated with the NLB.

Allowed values are: 'IPV4', 'IPV4_AND_IPV6'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_UPDATE_NETWORK_SECURITY_GROUPS_DETAILS_T Type

An object representing an updated list of network security groups that overwrites the existing list of network security groups. * If the network load balancer has no configured network security groups, then the network load balancer uses the network security groups in this list. * If the network load balancer has a list of configured network security groups, then this list replaces the existing list. * If the network load balancer has a list of configured network security groups and this list is empty, then the operation removes all of the network security groups associated with the network load balancer.

Syntax
```

```

Fields

Field Description

`network_security_group_ids`

(optional) An array of network security group[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with the network load balancer. During the creation of the network load balancer, the service adds the new network load balancer to the specified network security groups. The benefits of associating the network load balancer with network security groups include: * Network security groups define network security rules to govern ingress and egress traffic for the network load balancer. * The network security rules of other resources can reference the network security groups associated with the network load balancer to ensure access.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_RESOURCE_T Type

A resource that a work request creates or on which the work request operates.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type that the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted remains in the IN_PROGRESS state until work is complete for that resource, at which point the resource transitions to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path on which the user can perform a GET request to access the resource metadata.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_T Type

A description of work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of work request.

Allowed values are: 'CREATE_NETWORK_LOAD_BALANCER', 'UPDATE_NETWORK_LOAD_BALANCER', 'DELETE_NETWORK_LOAD_BALANCER', 'CREATE_BACKEND', 'UPDATE_BACKEND', 'DELETE_BACKEND', 'CREATE_LISTENER', 'UPDATE_LISTENER', 'DELETE_LISTENER', 'CREATE_BACKENDSET', 'UPDATE_BACKENDSET', 'DELETE_BACKENDSET', 'UPDATE_NSGS', 'UPDATE_HEALTH_CHECKER', 'CHANGE_COMPARTMENT', 'ATTACH_NLB_TO_POD', 'DETACH_NLB_FROM_POD'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The identifier of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests are scoped to the same compartment as the resource that the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, then the service team must choose the primary resource whose compartment is to be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time that the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time that the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time that the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_SUMMARY_T Type

Summary of work request object.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of work request.

Allowed values are: 'CREATE_NETWORK_LOAD_BALANCER', 'UPDATE_NETWORK_LOAD_BALANCER', 'DELETE_NETWORK_LOAD_BALANCER', 'CREATE_BACKEND', 'UPDATE_BACKEND', 'DELETE_BACKEND', 'CREATE_LISTENER', 'UPDATE_LISTENER', 'DELETE_LISTENER', 'CREATE_BACKENDSET', 'UPDATE_BACKENDSET', 'DELETE_BACKENDSET', 'UPDATE_NSGS', 'UPDATE_HEALTH_CHECKER', 'CHANGE_COMPARTMENT', 'ATTACH_NLB_TO_POD', 'DETACH_NLB_FROM_POD'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The identifier of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests are scoped to the same compartment as the resource that the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, then the service team must choose the primary resource whose compartment is to be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time that the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time that the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time that the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_COLLECTION_T Type

Wrapper object for an array of WorkRequest objects.

Syntax
```

```

Fields

Field Description

`items`

(optional) An array of WorkRequest objects.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_ERROR_T Type

An error encountered while running a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed here: (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human-readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured in the form of an RFC3339 formatted date-time string.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_ERROR_COLLECTION_T Type

Wrapper object for an array of WorkRequestErrorSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(optional) An array of WorkRequestErrorSummary objects.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the running of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written displayed as an RFC3339 formatted date-time string.

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_network_load_balancer_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Wrapper object for an array of WorkRequestLogEntry objects.

Syntax
```

```

Fields

Field Description

`items`

(optional) An array of WorkRequestLogEntry objects.

- [Network Load Balancer Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-5B823025-606C-4188-A5AE-7B119CA782D5)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-A0F7FB6B-93A4-4065-9A2D-549BCBF5788D)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-4300B8CF-EB6C-40D3-96DF-E8CF6C87B9A9)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-B9687F60-286A-4D6D-BB6E-C0F6A3CB9B73)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-DB923849-544B-450F-91DD-EB0692CC48AA)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-7453AE9B-59DE-452B-BEBC-AE41D4540C2E)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-54980A31-18D6-409A-B55C-99C486F7F46D)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_HEALTH_CHECK_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-397BD986-769D-49B6-AF1E-5154C82C23B9)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_HEALTH_CHECK_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-08B2E4BF-59EF-4B8C-ADCE-B086DC2B35ED)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_HEALTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-46618BD7-787E-477E-88CD-1D98A45F7EAB)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_HEALTH_CHECKER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-5ABB8FC4-3F70-4D06-9746-572A40EF8DDA)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-A9E2B921-DA05-4679-9854-36F2CDB18FAC)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-7FA6C3FE-F4FF-412B-BA6B-DF7EB7A5B1BB)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-C12778F7-78BC-48CD-BFB7-03E20175829E)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-887D448D-95AD-4146-A7AE-B2E034E98A62)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-2A66CC2A-8F4E-4D7F-9B62-F152D6CC31E3)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-04AD111C-6462-4D16-82D8-EEE781F8C341)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_SET_HEALTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-385A33D9-9DD0-495D-A766-D644AD7039C4)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_CHANGE_NETWORK_LOAD_BALANCER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-35AFA6F4-3DC8-41FF-95F1-16C4F6058127)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_CREATE_BACKEND_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-180C6277-DC84-416A-B76A-FF266B16210B)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_HEALTH_CHECKER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-48F0746A-0DCA-4F5F-A351-001FC45D19E6)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_BACKEND_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-AA91913A-63BA-4CD5-A443-A27555E8E2BD)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_CREATE_BACKEND_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-E95D9865-6ECE-413A-934F-1BDEB855AD3A)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_CREATE_LISTENER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-C216A1EE-85ED-4EDC-B51F-C3AD0863C84A)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_RESERVED_IP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-379C8F7B-385C-418F-A4FB-E35E072FE404)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_LISTENER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-EAB07062-B38A-4859-AA9F-1668FF3B774B)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_RESERVED_IP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-4C2E7E3D-2808-4F96-A3B2-BF05D68E686C)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_CREATE_NETWORK_LOAD_BALANCER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-94E29E9A-8259-4DEE-9652-F77DDCC8D263)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-49812B2B-E072-4666-A431-D490B03711A8)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_IP_ADDRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-25A1E1AE-5BF2-4C56-8D8F-B533EA5EC0E2)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_LISTENER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-7B1F711A-B72B-4964-A55A-9743062B37C0)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_LISTENER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-230D92BD-821C-491B-AB69-461F37D4B23C)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_LISTENER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-329C019B-C2C0-4955-B99E-38C401263D65)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_LISTENER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-5C88C41D-D061-42F7-B670-0A246D0B8B0E)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_IP_ADDRESS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-5C311452-71F0-4917-906A-C783F8628586)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-C2CD9F23-27A5-441E-A397-13EBCAA2C10C)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-277A1E8E-4846-4A05-AA0A-FF075FB44079)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-32479223-E9A8-445A-AD0F-8EB1B37A9681)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-55370C3A-CCA1-4A71-B577-A02E61E3051F)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_HEALTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-0B11F9C7-253B-49D2-84C0-72DBE6A8BD38)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_HEALTH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-CAF48804-2ED2-4EE0-8D1F-845AEC0AEAE2)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_HEALTH_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-AD5E7D28-F615-4968-9E1E-DD25491CF51F)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCER_HEALTH_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-F3F58FE4-482E-477F-B644-75C22414BDEE)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCERS_POLICY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-7F5179C9-6893-4ED2-87B4-E435F50A2568)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_NETWORK_LOAD_BALANCERS_PROTOCOL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-4B697247-F3DD-43E3-85C0-CF6536D324F4)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_UPDATE_BACKEND_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-E1183C9E-9BD7-4727-BBE7-996A5F608C79)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_UPDATE_BACKEND_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-00949B70-B1E2-4B63-A84D-461C8863AAB7)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_UPDATE_HEALTH_CHECKER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-FDE0889A-23E6-4184-ADAB-093BCD8ADDAB)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_UPDATE_LISTENER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-F0148E28-0E1F-48B6-A948-96C24CA23001)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_UPDATE_NETWORK_LOAD_BALANCER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-C194D3AD-4063-4D5A-8B62-D413C6C10D87)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_UPDATE_NETWORK_SECURITY_GROUPS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-3311438E-1A07-4D5B-9BA6-875026B0D235)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-9240BAC2-483D-4EB1-94CE-659623C5345A)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-FD13AC66-43B8-4E17-AEE1-3DF25EBB9582)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-8837F969-9198-4FE6-913A-49A1FB86C9CA)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-23AC8854-A6D2-4320-BC40-72F852BDB7E3)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-B0D4BE72-975A-4F54-80D6-941E5911E358)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-D0723645-0147-4057-BA97-99AB83D6F72A)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-8EF207DE-B55B-47DF-8E33-309128CE30B0)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-3476380E-5747-4EE4-9CD2-51E34BAD17E6)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-73C2DD46-E489-45AF-8231-F0BEF135D0BB)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-E7DBED3D-CCE1-4106-85CE-30EDFC32CA0D)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-ABB76593-44A0-4C7E-AAD4-BB841E813586)
- [DBMS_CLOUD_OCI_NETWORK_LOAD_BALANCER_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/network_load_balancer_t.html#ADSDK-GUID-927D87F1-3167-448E-ABAA-26A89D68D881)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
