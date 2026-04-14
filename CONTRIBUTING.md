\# Contributing to EKS GitOps Platform



Thank you for your interest in contributing!



\## Getting Started



1\. Fork the repository

2\. Create a feature branch: `git checkout -b feature/your-feature-name`

3\. Make your changes

4\. Run tests: `cd infrastructure/cdk \&\& pip install -r requirements-dev.txt \&\& pytest tests/`

5\. Commit using conventional commits: `git commit -m "feat: your change"`

6\. Push and open a Pull Request against `main`



\## Commit Message Format



This project follows \[Conventional Commits](https://www.conventionalcommits.org/):



\- `feat:` — new feature

\- `fix:` — bug fix

\- `docs:` — documentation only

\- `security:` — security improvement

\- `test:` — adding or updating tests



\## Local Development



\### Prerequisites

\- AWS CLI v2

\- kubectl 1.31+

\- Terraform 1.5+

\- Helm 3.x

\- Python 3.11+



\### Running CDK Tests

```bash

cd infrastructure/cdk

python -m venv .venv

source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

pip install -r requirements.txt -r requirements-dev.txt

pytest tests/ -v

```



\## Reporting Security Issues



Please do \*\*not\*\* open a public issue for security vulnerabilities.  

See \[SECURITY.md](SECURITY.md) for the responsible disclosure process.

