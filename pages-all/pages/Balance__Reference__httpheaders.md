# Load Balancer Headers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/httpheaders.htm
- Fetched: 2026-09-05 01:40 CDT

# Load Balancer Headers

Learn about using HTTP "X" and host headers in a load balancer.

HTTP requests and responses often include header fields that provide contextual information about the message.[RFC 2616](https://tools.ietf.org/html/rfc2616#section-4.2)defines a standard set of HTTP header fields. Some nonstandard header fields, which begin with`X-`, are common. The Load Balancer service adds or changes the Host header and the following`X-`headers when it passes requests to your servers. Because these headers are always added and can't be disabled, you can't remove or change headers using a rule set.

## X-Forwarded-For

Provides a list of connection IP addresses.

The load balancer appends the last remote peer address to the`X-Forwarded-For`field from the incoming request. A comma and space precede the appended address. If the client request header does not include an`X-Forwarded-For`field, this value is equal to the`X-Real-IP`value. The original requesting client is the first (left-most) IP address in the list, assuming that the incoming field content is trustworthy. The last address is the last (most recent) peer, that is, the machine from which the load balancer received the request. The format is:
```

```

Example incoming field:

```

```

Example field with appended proxy IP address:

```

```

## X-Forwarded-Host

Identifies the original host and port requested by the client in the`Host`HTTP request header. This header helps you find the original host, because the hostname or port of the reverse proxy (load balancer) might differ from the original server handling the request.

```

```

## X-Forwarded-Port

Identifies the listener port number that the client used to connect to the load balancer. For example:

```

```

## X-Forwarded-Proto

Identifies the protocol that the client used to connect to the load balancer, either`http`or`https`. For example:

```

```

## X-Real-IP

Identifies the client's IP address. For the Load Balancer service, the "client" is the last remote peer.

Your load balancer intercepts traffic between the client and your server. Your server's access logs, therefore, include only the load balancer's IP address. The`X-Real-IP`header provides the client's IP address. For example:
```

```

## X-Request-Id

The Request ID can help you with tracking and managing a request by providing a unique request identifier exposed in HTTP request and response headers.

When the request ID is enabled, the default header name X-Request-Id is included in the HTTP request header from the load balancer to the backend and HTTP header responses. If not enabled, the load balancer doesn't add this unique request ID header to the request passed through to the load balancer backend or to the response returned.

You can enter a different header name instead of using the default. Any custom header name must start with "X-".

## Host

Identifies the original host and optionally the port requested by the client in the Host HTTP request header. For example:
```

```
