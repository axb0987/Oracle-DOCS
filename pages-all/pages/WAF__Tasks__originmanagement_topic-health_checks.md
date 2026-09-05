# Health Checks
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/originmanagement_topic-health_checks.htm
- Fetched: 2026-09-05 03:11 CDT

# Health Checks

Describes how to health checks for an edge policy.

Health checks can be enabled when multiple origins are specified.

## Default Settings

- Check URL: / (root/home page)
- Interval: 10 seconds (how often the check is performed)
- Timeout: 5 seconds (timeout after which the check is marked as failed)
- Fail count: 2 (number of failed checks for the origin to be considered down)
- Rise count: 2 (number of successful checks for the origin to be considered up)
- Successful responses: 2xx, 3xx, 4xx, 5xx
Custom health checks can also be configured. The following options are available:
- Enable response text checking (heath checks are looking for the text entered under "Expected response text").
- Specify a host header.

## Using the Console

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- State
- Name
- Policy Type : Select Edge Policy .
- Select the name of the edge policy where you want to configure custom headers for the origins.
The edge policy's details page opens.
- Select Settings under WAF Policy .
The Settings list appears.
- Select the Origin Settings tab.
- Select Edit .
The Origin Management Settings panel opens.
- Check Enable health checks .
- Enter the following information:

- Request : Select the type of health check request:
- GET
- HEAD
- POST
- URL : Enter the URL to visit on the origin when performing the health check.
- Host header : Enter the value of the host header in the HTTP health check request. If this field is left blank, the policy domain is used instead.
- User agent : Enter the value of the user agent header in the HTTP health check request.
- Expected response code group : Select the HTTP response codes that signify the health state from the list. You can select multiple codes.
- Check interval (seconds) : Enter the interval (in seconds) between health checks to the origin.
- Response timeout (seconds) : Enter the time to wait for a reply before marking the health check as failed.
- Healthy threshold (number of times) : Enter the number of successful health checks after which the origin server is marked up.
- Unhealthy threshold (number of times) : Enter the number of failed health checks after which the origin server is marked down.
- Enable response text checking : (optional) Check to check for predefined text in addition to the response code.

Enter the Expected response text in the accompanying box. Health checks search for the given text in a case-sensitive manner within the response body and fail if the text is not found.
- Select Save Changes .
Publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/../Bot/publishing_changes.htm#PublishChanges)
