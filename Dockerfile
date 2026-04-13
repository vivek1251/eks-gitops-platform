FROM nginx:alpine
COPY helm/eks-gitops-app/templates/ /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]