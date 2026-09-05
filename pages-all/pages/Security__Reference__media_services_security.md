# Securing Media Services
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/media_services_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Media Services

Media Services includes two components, Media Flow and Media Streams, which can be used independently or together and operate on the content stored in Object Storage.

Media Streams is a fully managed service that delivers digital video packaged in a format such as HTTP Live Streaming (HLS) to viewers.

## Security RecommendationsHere are the security recommendations for Media Streams:
- 

Assign least privilege access for IAM users and groups to resource types in media-family.
- 

Use AES 128 encryption.
- 

Keep the validity of the session token minimal. Consider the duration of video and expected viewer behavior such as pause or stall, to decide the token validity.

## Security Policy Examples

For more information on Media Streams policies and examples, see[Media Streams Policies](https://docs.oracle.com/iaas/Content/media-services/mediastreams/ms-iam-policies.htm)
