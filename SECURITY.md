\# Security Policy



\## Supported Versions



| Version | Supported |

|---------|-----------|

| main    | ✅ Yes    |



\## Reporting a Vulnerability



\*\*Please do not report security vulnerabilities through public GitHub issues.\*\*



If you discover a security vulnerability, please report it by opening a

\[GitHub Security Advisory](https://github.com/vivek1251/eks-gitops-platform/security/advisories/new).



Include as much detail as possible:

\- Type of vulnerability

\- File paths and line numbers

\- Steps to reproduce

\- Potential impact



You can expect a response within \*\*48 hours\*\*.



\## Security Best Practices Used in This Project



\- Elasticsearch credentials stored in Kubernetes Secrets, not hardcoded

\- Terraform state excluded from version control via `.gitignore`

\- Docker images pinned to specific versions (no `latest` tags in production)

\- Helm deployments include resource limits to prevent resource exhaustion

\- AWS IAM roles follow least-privilege principle

\- No AWS credentials committed to repository — injected via GitHub Actions secrets

