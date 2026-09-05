# Virtual Hostname and Path Route Rules Combinations for Load Balancer Backend Sets
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/hostname_pathrouterules_combo.htm
- Fetched: 2026-09-05 01:40 CDT

# Virtual Hostname and Path Route Rules Combinations for Load Balancer Backend Sets

Learn about virtual hostnames and path route rules route requests to backend sets.

Virtual hostnames and path route rules route requests to backend sets. Listeners with a virtual hostname receive priority over the default (no hostname) listener. The following example shows the results of a simple routing interaction.

The example system includes three listeners and one path route set:

Listener 1
- Virtual hostname: none
- Default backend set:`A`
- Path route set:`PathRouteSet1`

Listener 2
- Virtual hostname:`captive.com`
- Default backend set:`B`
- Path route set:`PathRouteSet1`

Listener 3
- Virtual hostname:`wild.com`
- Default backend set:`C`
- Path route set:`PathRouteSet1`

Path Route Set
- Path route set name:`PathRouteSet1`
- Exact match on path string`/tame/`routes to backend set`B`.
- Exact match on path string`/feral/`routes to backend set`C`.

The following configuration examples show how incoming routes URLs are routed:
- `http://animals.com/`is routed to backend set`A`
- Virtual hostname`animals.com`matches Listener 1 .
- Path`/`is not an EXACT_MATCH for any path route string in`PathRouteSet1`.
- `http://animals.com/tame/`is routed to backend set`B`
- Virtual hostname`animals.com`matches Listener 1 .
- Path`/tame/`is an EXACT_MATCH for path route string`/tame/`in`PathRouteSet1`.
- `http://animals.com/feral/`is routed to backend set`C`
- Virtual hostname`animals.com`matches Listener 1 .
- Path`/feral/`is an EXACT_MATCH for path route string`/feral/`in`PathRouteSet1`.
- `http://captive.com/`is routed to backend set`B`
- Virtual hostname`captive.com`matches Listener 2 .
- Path`/`is not an EXACT_MATCH for any path route string in`PathRouteSet1`.
- `http://captive.com/tame/`is routed to backend set`B`
- Virtual hostname`captive.com`matches Listener 2 .
- Path`/tame/`is an EXACT_MATCH for path route string`/tame/`in`PathRouteSet1`.
- `http://captive.com/feral/`is routed to backend set`C`
- Virtual hostname`captive.com`matches Listener 2 .
- Path`/feral/`is an EXACT_MATCH for path route string`/feral/`in`PathRouteSet1`.
- `http://wild.com/`is routed to backend set`C`
- Virtual hostname`wild.com`matches Listener 3 .
- Path`/`is not an EXACT_MATCH for any path route string in`PathRouteSet1`.
- `http://wild.com/tame/`is routed to backend set`B`
- Virtual hostname`wild.com`matches Listener 3 .
- Path`/tame/`is an EXACT_MATCH for path route string`/tame/`in`PathRouteSet1`.
- `http://wild.com/feral/`is routed to backend set`C`
- Virtual hostname`wild.com`matches Listener 3 .
- Path`/feral/`is an EXACT_MATCH for path route string`/feral/`in`PathRouteSet1`
