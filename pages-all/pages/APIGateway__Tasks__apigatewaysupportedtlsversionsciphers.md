# Supported TLS Versions and Ciphers
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysupportedtlsversionsciphers.htm
- Fetched: 2026-09-05 01:38 CDT

# Supported TLS Versions and Ciphers

Find out about the TLS versions and ciphers supported by API Gateway.

The API Gateway service supports TLS version 1.2.

## Supported Ciphers

The API Gateway service supports the following ciphers with TLS version 1.2.

Certificate Cipher Suite Key Exchange Encryption Bits Cipher Suite Name (IANA) Supported/Deprecated
ECDHE-RSA-AES128-GCM-SHA256 [0xc02f] ECDH AESGCM 128 TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 Supported.
ECDHE-RSA-AES128-SHA256 [0xc027] ECDH AES 128 TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 Deprecated.
ECDHE-RSA-AES256-GCM-SHA384 [0xc030] ECDH AESGCM 256 TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 Supported.
ECDHE-RSA-AES256-SHA384 [0xc028] ECDH AES 256 TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 Deprecated.
DHE-RSA-AES256-GCM-SHA384 [0x9f] DH AESGCM 256 TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 Supported.
DHE-RSA-AES256-SHA256 [0x6b] DH AES 256 TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 Deprecated.
DHE-RSA-AES128-GCM-SHA256 [0x9e] DH AESGCM 128 TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 Supported.
DHE-RSA-AES128-SHA256 [0x67] DH AES 128 TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 Deprecated.

## Deprecated Ciphers

Starting April 1, 2025, the API Gateway service no longer supports the following legacy ciphers:
- ECDHE-RSA-AES128-SHA256
- ECDHE-RSA-AES256-SHA384
- DHE-RSA-AES256-SHA256
-
