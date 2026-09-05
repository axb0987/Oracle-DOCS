# Caching Rules
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/cachingrules.htm
- Fetched: 2026-09-05 03:11 CDT

# Caching Rules

Caching rules allow you to selectively cache requested content on Oracle Cloud Infrastructure's edge servers, such as web pages or certain file types.

## Using the Console

[To create a caching rule](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/cachingrules.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- 

Select the name of the WAF Policy you want to add a caching rule. The WAF Policy overview appears.
- Select Caching Rules .
- Select Create Caching Rule .
- In the Create Caching Rule dialog box, enter the following:
- Name: A unique name for the access rule.
- Caching Rule Action: Select one of the following options:
- Cache: Cache the requested content when criteria of the rule is met.
- Caching Duration : The duration to cache content for the caching rule.
- Time Unit : The unit of time for the caching duration.
- Enable Client Caching: Select this check box to specify the duration to cache content in the user's browser.
- Bypass Cache: Allow requests to bypass the cache and be directed to the origin when the criteria of the rule is met.
- Conditions: Select the condition and URL address that must match for the action to be taken. At least one condition must match for the set action to be taken.
- Select Create . The caching rule is added to the Caching Rules list.

[To edit a caching rule](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/cachingrules.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- 

Select the name of the WAF policy you want to edit the Caching Rules for. The WAF policy overview appears.
- Select Caching Rules .
- Select the check box for the caching rule you want to update.
- Select Edit from the Actions drop down menu.
- In the Edit Caching Rule dialog box, make the necessary updates.
- Select Save Changes .

[To delete a caching rule](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/cachingrules.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the name of the WAF policy where you want to delete a caching rule. The WAF policy overview appears.
- Select Caching Rules .
- Select the check box for the caching rule you want to delete.
- Select Delete from the Actions drop down menu.
- In the confirmation dialog box, select Delete .

[To purge the cache](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/cachingrules.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- 

Select the name of the WAF Policy where you want to purge the cache. The WAF Policy overview appears.
- Select Caching Rules .
- Select Purge Cache from the Actions dropdown menu.
- In the Purge Cache dialog box, select the condition and URL address to purge and select Purge .

## Using the API

Use the following API operations to create and manage caching rules that can be applied to your WAF configurations:
- [ListCachingRules](https://docs.oracle.com/iaas/api/#/en/waas/latest/CachingRules/ListCachingRules)
- [UpdateCachingRules](https://docs.oracle.com/iaas/api/#/en/waas/latest/CachingRules/UpdateCachingRules)
- [PurgeCache](https://docs.oracle.com/iaas/api/#/en/waas/latest/PurgeCache/PurgeCache)

## Available Cache Rules Criteria

The criteria of the caching rule determines if the requested content should be cached.
- URL_IS - Matches if the concatenation of requested URL path and query is identical to the contents of the`value`field. For example, if this rule is set to cache the content of`www.example.com/products`, only HTTP requests for`www.example.com/products`will cache.
- URL_STARTS_WITH - Matches if the concatenation of requested URL path and query starts with the contents of the`value`field. For example, if this rule is set to cache content from`www.example.com/products`, all HTTP requests requesting URLs starting with`www.example.com/products`will be cached and subsequent requests will receive content from the cache, including requests for`www.example.com/products/new-product`and`www.example.com/products/old-product`.
- URL_PART_ENDS_WITH - Matches if the concatenation of requested URL path and query ends with the contents of the`value`field. For example, if the rule is set to cache content from URLs that end with`/product.jpg`, HTTP requests for the URLs`www.example.com/products/new-product/product-banner.jpg`and`www.example.com/products/old-product/product-banner.jpg`will be cached and subsequent requests will receive content from the cache.
- URL_PART_CONTAINS - Matches if the concatenation of requested URL path and query contains the contents of the`value`field. If the rule is set to cache content from URLs that contain`/product-banner`, HTTP requests for the URLs`www.example.com/products/new-product/product-banner/blue.jpg`and`www.example.com/products/new-product/product-banner/red.jpg`will be cached and subsequent requests will receive content from the cache.

## Available Cache Rule Actions

A caching rule can be set to take one of two available actions when receiving a request:
- CACHE - Requests matching the criteria of the rule will be cached and subsequent requests will receive content from the cache.
- BYPASS_CACHE - Requests matching the criteria of the rule will bypass the cache and be directed to the origin.

## Cache Duration

Content can be cached for a specified period of time on Oracle Cloud Infrastructure's edge servers or cached locally by the client. The duration is set in the`cachingDuration`and`clientCachingDuration`fields, in ISO 8601 extended format.

## Example of a Caching Rule

```

```

## Best Practices

The order the caching rules is specified in are important. The rules are processed in the order they are specified in and the first matching rule will be used when processing a request. It is best to add rules that bypass cache to the top of the order and caching rules below any bypass rules.

## Purge Caches

Caches can be purged using the[PurgeCache](https://docs.oracle.com/iaas/api/#/en/waas/latest/PurgeCache/PurgeCache)operation. Caches can either be selectively purged by specifying the URL path of a resource or all caches can be purged for the WAF by not specifying any resources to pass to the API.

### Examples

Purge the cache for specified resources:
```

```
