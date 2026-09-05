# Details for Load Balancing
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/lbpolicyreference.htm
- Fetched: 2026-09-05 02:26 CDT

# Details for Load Balancing

This topic covers details for writing policies to control access to the Load Balancer service.

## Resource-Types

`load-balancers`

## Supported Variables

Only the general variables are supported (see[General Variables](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm)).

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

For example, the`read`verb for load-balancers includes the same permissions and API operations as the`inspect`verb, plus the LOAD_BALANCER_READ permission and a number of API operations (e.g.,`GetLoadBalancer`,`ListWorkRequests`, etc.). The`use`verb covers still another permission and set of API operations compared to`read`. And`manage`covers two more permissions and operations compared to`use`.

### load-balancers

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

LOAD_BALANCER_INSPECT

`ListLoadBalancers`

`ListShapes`

`ListPolicies`

`ListProtocols`

none
read

INSPECT +

LOAD_BALANCER_READ

INSPECT +

`GetLoadBalancer`

`ListWorkRequests`

`GetWorkRequest`

`ListBackendSets`

`GetBackendSet`

`ListBackends`

`GetBackend`

`GetHealthChecker`

`ListCertificates`

none
use

READ +

LOAD_BALANCER_UPDATE

LOAD_BALANCER_MOVE

READ +

`UpdateLoadBalancer`

`ChangeLoadBalancerCompartment`

`UpdateBackendSet`

`CreateBackendSet`

`DeleteBackendSet`

`UpdateBackend`

`CreateBackend`

`DeleteBackend`

`UpdateHealthChecker`

`CreateCertificate`

`DeleteCertificate`

`UpdateListener`

`CreateListener`

`DeleteListener`

none
manage

USE +

LOAD_BALANCER_CREATE

LOAD_BALANCER_DELETE

USE +

`CreateLoadBalancer`

`DeleteLoadBalancer`

none

## Permissions Required for Each API Operation

The following table lists the API operations in a logical order, grouped by resource type.
Tip  
  
If a group uses the Console to manage load balancers, permissions to use the associated networking resources are required. See the[load balancing policy examples](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/../policiescommon/commonpolicies.htm#network-admins-manage-load-balancers)for further guidance.

For information about permissions, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/../policies/permissions.htm).

API Operation Permissions Required to Use the Operation
`ListLoadBalancers`LOAD_BALANCER_INSPECT and
`GetLoadBalancer`LOAD_BALANCER_READ
`ChangeLoadBalancerCompartment`LOAD_BALANCER_MOVE
`UpdateLoadBalancer`LOAD_BALANCER_UPDATE
`CreateLoadBalancer`LOAD_BALANCER_CREATE
`DeleteLoadBalancer`LOAD_BALANCER_DELETE
`ListShapes`LOAD_BALANCER_INSPECT
`ListWorkRequests`LOAD_BALANCER_READ
`GetWorkRequest`LOAD_BALANCER_READ
`ListBackendSets`LOAD_BALANCER_READ
`GetBackendSet`LOAD_BALANCER_READ
`UpdateBackendSet`LOAD_BALANCER_UPDATE
`CreateBackendSet`LOAD_BALANCER_UPDATE
`DeleteBackendSet`LOAD_BALANCER_UPDATE
`ListBackends`LOAD_BALANCER_READ
`GetBackend`LOAD_BALANCER_READ
`UpdateBackend`LOAD_BALANCER_UPDATE
`CreateBackend`LOAD_BALANCER_UPDATE
`DeleteBackend`LOAD_BALANCER_UPDATE
`GetHealthChecker`LOAD_BALANCER_READ
`UpdateHealthChecker`LOAD_BALANCER_UPDATE
`ListCertificates`LOAD_BALANCER_READ
`CreateCertificate`LOAD_BALANCER_UPDATE
`DeleteCertificate`LOAD_BALANCER_UPDATE
`UpdateListener`LOAD_BALANCER_UPDATE
`CreateListener`LOAD_BALANCER_UPDATE
`DeleteListener`LOAD_BALANCER_UPDATE
`ListPolicies`LOAD_BALANCER_INSPECT
`ListProtocols`
