# Supported Terraform Providers
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/providers.htm
- Fetched: 2026-09-05 02:54 CDT

# Supported Terraform Providers

Review the Terraform providers supported by Resource Manager.

## Minimum OCI Provider Versions

Resource Manager supports the latest version of`terraform-provider-oci`for any Terraform version.

Following are the minimum versions of`terraform-provider-oci`supported for each indicated Terraform version.

Terraform version Minimum supported version of`terraform-provider-oci`
0.12.x 3.16.0
0.13.x 3.16.0
0.14.x 3.16.0
1.0.x 3.30.0

## Third-party Providers

Review Resource Manager stack sourcing of third-party providers.

New and updated stacks fetch providers from[Terraform Registry](https://registry.terraform.io/browse/providers). To update older stacks to use Terraform Registry, see[Using Terraform Registry with an Older Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/update-stack-tf-reg.htm).

See also[Third-party Provider Configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#third-party-providers).

### Older Stacks

Stacks created before Terraform Registry sourcing was available fetch third-party providers from Resource Manager. For details, see the following table.
Note  
  
To update older stacks to fetch third-party providers from Terraform Registry, see[Using Terraform Registry with an Older Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/../Tasks/update-stack-tf-reg.htm).

Third-party Terraform Provider 0.12.x 0.13.x 0.14.x 1.0.x
`[](https://github.com/nbering/terraform-provider-ansible)terraform-provider-ansible`1.0.3 1.0.3 1.0.3 1.0.3
`[](https://registry.terraform.io/providers/hashicorp/archive/latest/docs)terraform-provider-archive`

1.1.0, 1.2.2

1.1.0, 1.2.2

1.1.0, 1.2.2

2.1.0
`[](https://github.com/AviatrixSystems/terraform-provider-aviatrix)terraform-provider-aviatrix`- - - 2.19.1
`[](https://registry.terraform.io/providers/CheckPointSW/checkpoint/latest/docs)terraform-provider-checkpoint`1.0.0, 1.0.3 1.0.0, 1.0.3 1.0.0, 1.0.3 1.4.0
`[](https://github.com/hashicorp/terraform-provider-chef/blob/stable-website/website/docs/index.html.markdown)terraform-provider-chef`0.2.0 0.2.0 0.2.0 0.2.0
`[](https://registry.terraform.io/providers/hashicorp/cloudinit/latest/docs)terraform-provider-cloudinit`1.0.0 1.0.0 1.0.0 2.2.0
`[](https://registry.terraform.io/providers/digitalocean/digitalocean/latest/docs)terraform-provider-digitalocean`

1.13.0

1.13.0

1.13.0 2.7.0
`[](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest/docs)terraform-provider-dyn`1.2.0 1.2.0 1.2.0 1.2.0
`[](https://registry.terraform.io/providers/integrations/github/latest/docs)terraform-provider-github`

2.3.1, 2.9.2

2.3.1, 2.9.2

2.3.1, 2.9.2 2.9.2
`[](https://registry.terraform.io/providers/gitlabhq/gitlab/latest/docs)terraform-provider-gitlab`

2.5.0

2.5.0

2.5.0 3.5.0
`[](https://registry.terraform.io/providers/hashicorp/helm/latest/docs)terraform-provider-helm`

0.9.1, 1.1.1

0.9.1, 1.1.1

0.9.1, 1.1.1 2.1.0
`[](https://registry.terraform.io/providers/hashicorp/http/latest)terraform-provider-http`2.0.0 2.0.0 2.0.0 2.1.0
`[](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs)terraform-provider-kubernetes`

1.8.1, 1.11.2

1.8.1, 1.11.2

1.8.1, 1.11.2 1.11.2
`[](https://registry.terraform.io/providers/hashicorp/local/latest/docs)terraform-provider-local`

1.1.0, 1.2.2, 1.4.0

1.1.0, 1.2.2, 1.4.0

1.1.0, 1.2.2, 1.4.0 2.1.0
`[](https://registry.terraform.io/providers/hashicorp/null/latest/docs)terraform-provider-null`

1.0.0, 2.1.2

1.0.0, 2.1.2

1.0.0, 2.1.2 3.1.0
`[](https://registry.terraform.io/providers/PaloAltoNetworks/panos/latest/docs)terraform-provider-panos`

1.6.2

1.6.2

1.6.2 1.8.1
`[](https://registry.terraform.io/providers/hashicorp/random/latest/docs)terraform-provider-random`

2.1.2, 2.3.0

2.1.2, 2.3.0

2.1.2, 2.3.0 3.1.0
`[](https://registry.terraform.io/providers/hashicorp/template/latest/docs)terraform-provider-template`

1.0.0, 2.1.2

1.0.0, 2.1.2

1.0.0, 2.1.2 2.1.2
`[](https://registry.terraform.io/providers/hashicorp/time/latest)terraform-provider-time`0.6.0 0.6.0 0.6.0 0.7.0
`[](https://registry.terraform.io/providers/hashicorp/tls/latest/docs)terraform-provider-tls`

1.2.0, 2.0.1

1.2.0, 2.0.1

1.2.0, 2.0.1 3.1.0
`[](https://registry.terraform.io/providers/hashicorp/vault/latest/docs)terraform-provider-vault`
