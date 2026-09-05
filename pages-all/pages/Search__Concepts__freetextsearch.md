# Free Text Search
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/freetextsearch.htm
- Fetched: 2026-09-05 03:03 CDT

# Free Text Search

This topic describes how Search handles the search terms that you submit as a free text search.

By default, text entered in the Console search box is interpreted as a free text search. You can use a free text search to conduct a search of any category that Search supports. This includes searches for resources, pages across services in the Console, and documentation.

After you submit a free text search, if you view the results for resources, then you can work with the results by using the resource explorer. The resource explorer offers a basic search mode and an advanced query mode. In basic search mode, you can specify or find and apply filters based on resource attributes. You can also use basic search mode to sort search results. In advanced query mode, you can use structured query language to apply searching and sorting conditions to find specific resource results.

## Matching

Search tries to match search terms against the values of indexed fields. For resources, this means that Search evaluates the value of all indexed resource attributes, from[common attributes](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/queryoverview.htm#resourcetypes__commonattributes)(except the resource type attribute) to attributes specific to a resource type. For services, this includes all page display names and service groups. For documentation, this includes the title and the contents of the topic. (Search doesn't query the topic description, topic category, or keyword metadata.)

To provide matching results to the text entered in a free text search, Search queries all indexed fields by applying the`=`(equals) operator to text that you specified. If you're familiar with advanced queries, the effect is the same as using a`matching`clause. For example, a free text search for the term "net" queries all resource types, service pages, and documentation for the string "net" in any indexed field. If the string appears as part or the whole of a value anywhere in an indexed field, Search considers the found item a matching result. Search doesn't require exact matching, but an exact match does improve a result's ranking.

If the free text search includes a delimiting character (for example, a hyphen), the delimiter causes Search to treat the text on either side of the delimiter as an independent search term. For example, a free text search for "2020-04" looks for the string "2020" and the string "04". If a potential result contains either string, then it's a match.

Free text search matches individual terms from the provided text. Search doesn't try to match specific combinations of characters that you might group by using quotes or by presenting terms in a specific order. Likewise, proximity of search terms doesn't matter. However, if you have more than one search term in a free text search, results that contain multiple matches to the search terms have a higher ranking in the search results.

## Wildcards

In a free text search, you can use wildcards when specifying an IP address. For IPv4 addresses, you can replace any octet (or 8-bit field or byte) of a dotted-decimal IP address, except for the first octet of the network part. For IPv6 addresses, you can replace each 16-bit field of the address with a wildcard, except for the first 16-bit field in the site prefix part of the address.

A wildcard must replace the entire octet or 16-bit field. You can't partially replace an octet or 16-bit field. The remainder of the IP address must meet with expected conventions for IPv4 or IPv6 addressing, as appropriate.
For an IPv4 address, Search translates the IP address, as submitted, to CIDR notation according to the following:
- [0-255].[0-255].[0-255].* becomes [0-255].[0-255].[0-255].0/24
- [0-255].[0-255].*.* becomes [0-255].[0-255].0.0/16
- [0-255].*.*.* becomes [0-255].0.0.0/8
For an IPv6 address, Search translates the IP address to CIDR notation according to the following:
- [0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:* becomes [0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]::/112
- [0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:*:* becomes [0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]::/96
- [0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:*:*:* becomes [0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]::/80
- [0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]:*:*:*:* becomes [0000-ffff]:[0000-ffff]:[0000-ffff]:[0000-ffff]::/64
- [0000-ffff]:[0000-ffff]:[0000-ffff]:*:*:*:*:* becomes [0000-ffff]:[0000-ffff]:[0000-ffff]::/48
- [0000-ffff]:[0000-ffff]:*:*:*:*:*:* becomes [0000-ffff]:[0000-ffff]::/32
- [0000-ffff]:*:*:*:*:*:*:* becomes [0000-ffff]::/16

## Ranking of Results

Search evaluates each potential result for how closely it can match the search term or terms provided. Search also considers how many matches for the exact search term the result contains. Either a close match or multiple matching terms improves the result's ranking. A result's ranking in terms of match doesn't necessarily correlate to its order in a list of results.

When you search for services or documentation, exact matches occupy a higher rank in the results than partial matches. Services or documentation results with a higher rank are listed before results with a lower ranking in terms of match. When you search for resources, the order in which results are listed depends on whether you use the Console and what mode you use to find results. In the Console, in basic search mode, results are listed according to when the resource was created. Newer resources occupy a higher position in the list than older resources. In advanced query mode, results are listed in the order dictated by the`sorted by`
