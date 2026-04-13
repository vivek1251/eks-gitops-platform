\# EKS GitOps Platform



A production-grade Kubernetes platform on AWS demonstrating GitOps, CI/CD, and full-stack observability.



\## Architecture Overview

\- \*\*EKS 1.31\*\* — Managed Kubernetes cluster provisioned with AWS CDK

\- \*\*VPC\*\* — Custom VPC with public/private subnets via CloudFormation

\- \*\*ArgoCD\*\* — GitOps continuous delivery, auto-syncs from GitHub to EKS

\- \*\*GitHub Actions\*\* — CI/CD pipeline with build, test, and deploy stages

\- \*\*Helm\*\* — All workloads packaged as Helm charts

\- \*\*ELK Stack\*\* — Elasticsearch + Kibana + Filebeat (750+ live log events)

\- \*\*CloudWatch Container Insights\*\* — Pod-level CPU/memory/network metrics

\- \*\*ALB Controller\*\* — AWS Load Balancer Controller for ingress

\- \*\*Ansible\*\* — Node hardening playbook

\- \*\*Terraform\*\* — S3 artifact storage with versioning



\## Skills Demonstrated

`AWS CDK` `CloudFormation` `Terraform` `EKS` `Kubernetes` `Helm` `ArgoCD` `GitHub Actions` `Elasticsearch` `Kibana` `Filebeat` `CloudWatch` `ALB` `Ansible` `IAM` `VPC` `S3`



\## Sprints Completed

| Sprint | What was built |

|--------|---------------|

| Sprint 1 | VPC, EKS cluster, ALB Controller, Ansible hardening |

| Sprint 2 | GitHub Actions CI/CD, ArgoCD GitOps, Helm charts |

| Sprint 3 | ELK Stack — 750+ live log events in Kibana |

| Sprint 4 | CloudWatch Container Insights, EKS control plane logging |

| Sprint 5 | Terraform — S3 bucket with versioning |



\## Key Achievements

\- Deployed and managed a multi-node EKS cluster from scratch

\- Implemented full GitOps workflow — push to GitHub auto-deploys to EKS

\- Built end-to-end observability with ELK Stack and CloudWatch

\- Resolved real-world issues: pod scheduling, IAM permissions, resource constraints

