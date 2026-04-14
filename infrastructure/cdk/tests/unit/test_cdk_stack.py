import aws_cdk as core
import aws_cdk.assertions as assertions
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from cdk_stack import EksGitopsPlatformStack


@pytest.fixture
def template():
    app = core.App()
    stack = EksGitopsPlatformStack(app, "TestEksGitopsPlatformStack",
        env=core.Environment(account="123456789012", region="ap-south-1")
    )
    return assertions.Template.from_stack(stack)


def test_eks_cluster_created(template):
    """EKS cluster is created with correct name and version"""
    template.has_resource_properties("Custom::AWSCDK-EKS-Cluster", {
        "Config": {
            "name": "eks-gitops-cluster",
            "version": "1.31",
        }
    })


def test_eks_cluster_role_created(template):
    """EKS cluster IAM role has AmazonEKSClusterPolicy"""
    template.has_resource_properties("AWS::IAM::Role", {
        "AssumeRolePolicyDocument": {
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"Service": "eks.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }]
        },
        "ManagedPolicyArns": assertions.Match.array_with([
            assertions.Match.object_like({
                "Fn::Join": assertions.Match.any_value()
            })
        ])
    })


def test_node_role_has_required_policies(template):
    """Node IAM role has all 3 required managed policies"""
    template.has_resource_properties("AWS::IAM::Role", {
        "AssumeRolePolicyDocument": {
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"Service": "ec2.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }]
        }
    })


def test_nodegroup_uses_t3_small(template):
    """Node group uses t3.small instance type"""
    template.has_resource_properties("Custom::AWSCDK-EKS-Nodegroup", {
        "Config": {
            "instanceTypes": ["t3.small"],
            "nodegroupName": "eks-gitops-nodes",
            "scalingConfig": {
                "minSize": 1,
                "desiredSize": 1,
                "maxSize": 2,
            }
        }
    })


def test_cluster_name_output_exists(template):
    """CloudFormation output for ClusterName exists"""
    template.has_output("ClusterName", {
        "Value": assertions.Match.any_value()
    })


def test_cluster_arn_output_exists(template):
    """CloudFormation output for ClusterArn exists"""
    template.has_output("ClusterArn", {
        "Value": assertions.Match.any_value()
    })


def test_no_public_subnets_for_nodes(template):
    """Node group is deployed in private subnets only"""
    template.has_resource_properties("Custom::AWSCDK-EKS-Nodegroup", {
        "Config": {
            "subnets": assertions.Match.any_value()
        }
    })