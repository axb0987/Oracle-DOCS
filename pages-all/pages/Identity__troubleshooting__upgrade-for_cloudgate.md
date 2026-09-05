# Upgrading App Gateway for Cloud Gate
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/upgrade-for_cloudgate.htm
- Fetched: 2026-09-05 02:29 CDT

# Upgrading App Gateway for Cloud Gate

Troubleshoot the upgrade path for high-availability with multiple App Gateways.

These are errors you might see if the Cloud Gate deployment mixes incompatible releases, for example, patching directly to R2, or to R3, without patching first to R1. In each case, the solution is to rollback and apply the patches in the correct order.

See[Upgrade Path for High Availability Deployments Using App Gateway Docker Image](https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/../appgateways/upgrade-for_cloudgate.htm).

## Login Loop after Upgrade

If there is an existing Cloud Gate Session, or IAM SSO session, or both, you may see a login loop similar to the loop caused by Cloud Gate Session cookies being too large.

When Cloud Gate cannot decrypt the existing Cloud Gate Session cookie, it will redirect to IAM to kick off authentication (see the`/oauth2/v1/authorize`request).

The initial request to`/smoke/test/oauth/echo`goes to a Cloud Gate node that hasn't been patched to R1. As it cannot detect a valid Cloud Gate Session, the unpatched Cloud Gate redirects to IAM to log in.

The Cloud Gate callback goes to the R2 Cloud Gate node. As the R2 release supports both Block Cipher modes of operation, it is able to decrypt the Cloud Gate State cookie and create a new Cloud Gate Session (encrypted using the new Block Cipher mode of operation).

The /smoke/test/oauth/echo replay request goes to the unpatched Cloud Gate node. And, again, it fails to decrypt the Cloud Gate Session cookie.

This is the login loop.
Sample Logging from cg-trace-main.log
```

```

## Cross-Domain Log out Failure

The cross-domain logout flow may fail when the following conditions are met:
- Third party cookies are disabled.
- There is a Cloud Gate NGINX server which has been patched to R2.
- There are two Cloud Gate NGINX servers which haven't been patched.

When the R2 server initiates logout, the unpatched nodes fail to decrypt the`LOGOUT_DATA`post body submitted to Cloud Gate by IAM.

The cg-trace-main.log file notes decryption failures, such as:

- `all keys failed (may be expected if old data)`
- `decrypt failed (bad key/data?)`

## Failed Login after Upgrade

After successfully signing into IAM, the Cloud Gate callback (`cloudgate/v1/oauth2/callback`) returns 401 if Cloud Gate is unable to decrypt the State cookie.

Sample Logging from cg-trace-main.log
```

```
