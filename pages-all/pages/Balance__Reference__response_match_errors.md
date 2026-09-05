# Load Balancer Response Match Failures
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/response_match_errors.htm
- Fetched: 2026-09-05 01:40 CDT

# Load Balancer Response Match Failures

Learn about response match failures associated with load balancers.

Any of the following load balancer behaviors are indicative of regular expression mismatch, incorrect value returned, or incorrect values provided to the health check:
- The backend server fails the health check.
- The client fails with a 502 Bad Gateway error.
- A "response match result: failed" appears in the error logs.

If these behaviors occur, determine why the backend server is sending the incorrect body. Adjust the path or regular expression pattern of the health check to match the backend server.

See[Health Check Policies for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Tasks/load_balancer_health_management.htm)
