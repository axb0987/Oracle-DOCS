# Protected Request Headers and Response Headers
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-protectedrequestresponseheaders.htm
- Fetched: 2026-09-05 01:38 CDT

# Protected Request Headers and Response Headers

You cannot use header transformation policies to transform certain protected request and response headers.

Header Protected as Request Header Protected as Response Header
access-control-allow-credentials not applicable Yes
access-control-allow-headers not applicable Yes
access-control-allow-methods not applicable Yes
access-control-allow-origin not applicable Yes
access-control-expose-headers not applicable Yes
access-control-max-age not applicable Yes
cdn-loop Yes not applicable
connection Yes Yes
content-length Yes Yes
cookie Yes not applicable
except Yes Yes
keep-alive Yes Yes
opc-request-id Yes Yes
origin Yes not applicable
proxy-authenticate not applicable Yes
proxy-authorization Yes not applicable
public-key-pins not applicable Yes
retry-after not applicable Yes
strict-transport-security not applicable Yes
te Yes Yes
trailers not applicable Yes
transfer-encoding Yes Yes
upgrade Yes Yes
x-content-type-options not applicable Yes
x-forwarded-for Yes not applicable
x-frame-options not applicable Yes
x-real-ip Yes not applicable
