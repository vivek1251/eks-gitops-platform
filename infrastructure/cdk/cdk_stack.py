from aws_cdk import (
    Stack,
    aws_eks as eks,
    aws_ec2 as ec2,
    aws_iam as iam,
    CfnOutput,
)
from aws_cdk.lambda_layer_kubectl_v31 import KubectlV31Layer
from constructs import Construct


class EksGitopsPlatformStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc.from_vpc_attributes(
            self, "ImportedVpc",
            vpc_id="vpc-0a602d923bed5ed81",
            availability_zones=["ap-south-1a", "ap-south-1b"],
            public_subnet_ids=[
                "subnet-058877c728ef40533",
                "subnet-008e20617a3512475",
            ],
            private_subnet_ids=[
                "subnet-054b484652f04c9e4",
                "subnet-0861e33ae4d7d1949",
            ],
        )

        cluster_role = iam.Role(
            self, "EksClusterRole",
            assumed_by=iam.ServicePrincipal("eks.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEKSClusterPolicy"),
            ]
        )

        cluster = eks.Cluster(
            self, "EksGitopsCluster",
            cluster_name="eks-gitops-cluster",
            version=eks.KubernetesVersion.V1_31,
            kubectl_layer=KubectlV31Layer(self, "KubectlLayer"),
            vpc=vpc,
            vpc_subnets=[ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)],
            default_capacity=0,
            role=cluster_role,
        )

        node_role = iam.Role(
            self, "EksNodeRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEKSWorkerNodePolicy"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEKS_CNI_Policy"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEC2ContainerRegistryReadOnly"),
            ]
        )

        cluster.add_nodegroup_capacity(
            "EksNodeGroup",
            nodegroup_name="eks-gitops-nodes",
            instance_types=[ec2.InstanceType("t3.medium")],
            min_size=1,
            desired_size=2,
            max_size=4,
            node_role=node_role,
            subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
        )

        CfnOutput(self, "ClusterName", value=cluster.cluster_name)
        CfnOutput(self, "ClusterArn", value=cluster.cluster_arn)