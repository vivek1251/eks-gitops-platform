#!/bin/bash
docker pull 585707316406.dkr.ecr.ap-south-1.amazonaws.com/eks-gitops-app:latest
docker stop eks-app || true
docker rm eks-app || true
docker run -d --name eks-app -p 80:80 585707316406.dkr.ecr.ap-south-1.amazonaws.com/eks-gitops-app:latest