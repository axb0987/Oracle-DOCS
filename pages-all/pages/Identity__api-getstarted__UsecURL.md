# Using cURL
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm
- Fetched: 2026-09-05 02:17 CDT

# Using cURL

cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.

## Using cURL to Access the REST APIs
- 

Install cURL. See[Step 2: Install cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-get-started.htm#QuickStart__install_curl).
- 

In a command window, set the cURL environment variable,`CURL_CA_BUNDLE`, to the location of your local CA certificate bundle. For information about CA certificate verification using cURL, see:[http://curl.haxx.se/docs/sslcerts.html.](http://curl.haxx.se/docs/sslcerts.html)
Note  
  

See[Authorization](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-managing-authorization.htm)for more information about authorization and authentication requirements.
- 

Invoke cURL and specify one or more of the following command line options, as required, to direct its execution.
- `-d, --data @file.json`: Identifies the request document, in JSON format, on the local machine.
- `-F, --form @file.json`: Identifies form data, in JSON format, on the local machine.
- `-H, --header`: Defines the request header in the format of HEADER: VALUE. The header values depend on which endpoint that you're accessing.
- 

The content type of the request document.
- 

The`X-Client-ID,``API_KEY_ID,`for OAuth 2.0 authorization
- 

The`X-Client-Secret,``API_KEY_SECRET,`for OAuth2.0 authorization
- `-i`: Displays response header information.
- `-X`: Indicates the HTTP request method`(DELETE, GET, POST, PATCH`, or`PUT).`If this option is omitted, the default is GET.

## The cURL Command URL

The URL used with the cURL command is the same as that described in[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)except that you must replace spaces in the URL with plus characters (+) and replace quotes (") with %22 .

Any characters in a URL that are outside the ASCII character set, such as spaces and quotes, must be URL encoded. For example, the following URL contains a filter query that searches for a user with a username either containing`jen`or starting with`bj`. Note that it contains spaces.
```

```

To use this URL in a cURL command line, you would change it to:
```

```

## cURL Command for Sending a GET Request
```

```

## cURL Command for Sending a POST Request
```

```
