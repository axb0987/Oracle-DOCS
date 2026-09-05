# Load Balancer Health Check Best Practices
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/health_check_best_practices.htm
- Fetched: 2026-09-05 01:41 CDT

# Load Balancer Health Check Best Practices

Follow the best practices to follow when running health checks on a load balancer.

Configure your health check protocol to match your application or service. If you run an HTTP service, then configure an HTTP-level health check. If you run a TCP-level health check against an HTTP service, then you might not get an accurate response. The TCP handshake can succeed and indicate that the service is up even when the HTTP service is incorrectly configured or having other issues. Although the health check appears good, you might experience transaction failures.

For example:
- 

The backend HTTP service has issues when communicating with the health check URL and the health check URL returns 5 nn messages. An HTTP health check catches the message from the health check URL and marks the service as down. In this case, a TCP health check handshake succeeds and marks the service as healthy, even though the HTTP service might not be usable.
-
