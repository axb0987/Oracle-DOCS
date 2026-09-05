# Certificates for Web Application Firewall
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/certificates_management.htm
- Fetched: 2026-09-05 03:10 CDT

# Certificates for Web Application Firewall

Describes how certificates are added and managed with the web application firewall policy.

To use SSL with your WAF policy, you must add a certificate bundle. The certificate bundle you upload includes the public certificate and the corresponding private key. Self-signed certificates can be used for the internal communication within Oracle Cloud Infrastructure.

Oracle Cloud Infrastructure accepts third-party and self-signed certificates in PEM format only. The following is an example PEM encoded certificate:
```

```

## Obtaining Third-Party SSL Certificates

You can purchase an SSL certificate from a trusted Certificate Authority such as[Symantec](https://www.clickssl.net/platinum-partner-of-symantec-ssl-certificates),[Thawte](https://www.clickssl.net/buy-thawte-ssl-certificates),[RapidSSL](https://www.clickssl.net/cheapest-rapidssl-certificates-provider), or[GeoTrust](https://www.clickssl.net/geotrust-ssl-certificates-authorized-reseller). The certificate issuer provides an SSL certificate that includes a certificate, intermediate certificate, and private key. Use this information, including the intermediate certificate, when adding an SSL certificate to Oracle Cloud Infrastructure.

## Converting to PEM Format

If you receive your certificates and keys in formats other than PEM, you must convert them before you can upload them to the system. You can use[OpenSSL](https://openssl.org/)to convert certificates and keys to PEM format.

## Uploading Certificate Chains

If you have multiple certificates that form a single certification chain, you must include all relevant certificates in one file before you upload them to the system. The following example of a certificate chain file includes four certificates:
```

```

## Submitting Private Keys

If your private key submission returns an error, the most common reasons are your private key is malformed or the system does not recognize the encryption method used for your key.

## Private Key Consistency

If you receive an error related to the private key, you can use OpenSSL to check its consistency:

```

```

This command verifies that the key is intact, the passphrase is correct, and the file contains a valid RSA private key.

## Decrypting a Private key

If the system does not recognize the encryption technology used for your private key, decrypt the key. Upload the unencrypted version of the key with your certificate bundle. You can use OpenSSL to decrypt a private key:

```

```

## Supported SSL Cipher Suites

The following SSL cipher suites are supported:

```

```

## Limitations
Consider the following limitations when adding SSL certificates:
- Each line except the last must contain exactly 64 printable characters. The final line must contain 64 or fewer printable characters. The text editor might save it differently and might have a different number of characters per line.
- To check the number of characters per line, use the following command:`awk '{ print length }' filename.pem`
-
