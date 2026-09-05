# HTTP WAF Headers
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Reference/httpheaders.htm
- Fetched: 2026-09-05 03:11 CDT

# HTTP WAF Headers

HTTP requests and responses often include header fields that provide contextual information about the message.[RFC 2616](https://tools.ietf.org/html/rfc2616#section-4.2)defines a standard set of HTTP header fields. Some non-standard header fields, which begin with`X-`, are common. The WAF service adds or modifies the following headers when it passes the requests to your servers or the response to the end users.

## X-Client-IP

Contains the remote user IP address. If the webapp is using a CDN and has the feature "behind cdn" enabled, this IP is taken from one of the configured headers. While forwarding the request to the origin, WAF adds X-Client-IP.

## X-Country-Code

Contains the geo location country code where the user's IP belongs to. While forwarding the request to the origin, WAF adds X-Country-Code.

## Zen-Host: ZENEDGE

Identifies that the request was analyzed by a WAF node. While forwarding the request to the origin, WAF adds Zen-Host: ZENEDGE.

## Request-Id

Identifies the request in the logs. While forwarding the request to the origin, WAF adds Request-Id.

## Connection

If there is not a defined Connection value previously established (for example, "Upgrade" or "WebSocket"), WAF clears the Connection header by default. This header can be modified based on the available connection pool to "close" or "keep-alive". While forwarding the request to the origin, WAF modifies, adds, or removes Connection.

## Accept-Encoding

In this header, WAF clears Accept-Encoding with an empty string. This means the header is not passed to the origin side as it comes from the user side. This header can be removed, based on WAF settings on response body inspection and caching. While forwarding the request to the origin, WAF modifies or adds or removes Accept-Encoding.

## X-Cdn: Served-By-Zenedge

Our platform injects this header to say that we are handling the connection. While forwarding the response to the client, WAF adds X-Cdn: Served-By-Zenedge.

## X-Zen-Fury

This header identifies the WAF node which processed the request via an encrypted token. While forwarding the response to the client, WAF adds X-Zen-Fury.

## X-Cache-Status

WAF can act as a cache server. Based on the configuration, WAF can respect Cache-Control headers or cache based on the caching configuration rules. The status of the cache is reported via the X-Cache-Status response header. The value of the header can be one of the standard values: MISS, BYPASS, EXPIRED, STALE, UPDATING, REVALIDATED, or HIT. In addition, for never cache rules, a non-standard NOTCACHED value will be set.

## Cache-Control
