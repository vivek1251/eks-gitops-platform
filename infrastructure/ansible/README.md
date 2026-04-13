\# Ansible Node Hardening



Hardens EKS worker nodes via AWS Systems Manager (SSM).



\## What it does

\- Disables root SSH login

\- Sets max auth tries to 3

\- Disables password authentication

\- Sets file descriptor limits (65536)

\- Enables auditd with privileged command tracking

\- Disables unused kernel modules (usb-storage, cramfs)

\- Applies sysctl network hardening parameters



\## How to run

aws ssm send-command \\

&#x20; --instance-ids <node-instance-id> \\

&#x20; --document-name "AWS-RunAnsiblePlaybook" \\

&#x20; --parameters '{"playbook": \["harden-nodes.yml"]}'

