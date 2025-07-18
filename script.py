# Let's first analyze the resume content to extract key information for the website
resume_content = """
BATHINA SIVA PRASAD REDDY 
DevOps Engineer | AWS| Azure | Kubernetes | Automation  
Bengaluru, KA | +91 6363295603 | bathinasivaprasadreddy@gmail.com   
GitHub | LinkedIn 

Professional Summary 
DevOps Engineer with 3.10+ years of experience in designing, building, and managing 
robust CI/CD pipelines, multi-cloud infrastructure, and scalable Kubernetes deployments. 
Proven track record of reducing deployment times, improving system availability, and 
optimizing infrastructure costs. Adept in Terraform, Jenkins, Kubernetes, and cloud 
platforms (AWS & Azure), with a strong focus on automation, reliability, and developer 
productivity. 

Technical Tools 
• Cloud Platforms: AWS (EKS, EC2, S3, IAM), Azure (AKS, VMs, VNet) 
• Containerization & Orchestration: Docker, Kubernetes, Helm 
• Infrastructure as Code: Terraform, Ansible 
• CI/CD: Jenkins, Maven, GitHub Actions 
• Monitoring & Logging: Prometheus, Grafana, ELK 
• Scripting: Bash, Python 
• Version Control: Git, GitHub 
• Tools: SonarQube, Slack, JIRA 

Professional Experience 
DevOps Engineer | Infodot Systems 
Apr 2023 – Present | Project: Medispend (Healthcare Compliance Platform) 
• Built and optimized CI/CD pipelines using Jenkins and Maven, reducing deployment 
time by 20%. 
• Designed Docker image lifecycle following best practices (multi-stage builds, non-
root users, minimal base images). 
• Deployed microservices on EKS (AWS) and AKS (Azure) using Helm, enabling zero-
downtime blue/green and rolling deployments.
• Provisioned and managed infrastructure as code using Terraform with support for 
multi-cloud and multi-region workspaces. 
• Created reusable Ansible playbooks for configuring servers, patch management, 
and post-deployment tasks. 
• Integrated Prometheus & Grafana for monitoring and alerting; decreased 
downtime by 15%. 
• Automated backup and log rotation tasks using custom Bash scripts. 
• Collaborated with developers and QA to integrate Git branching, tagging, and 
rollback strategies into CI workflows. 
• Led internal workshops on CI/CD best practices and cloud-native deployment 
strategies. 
• Resolved critical production issues by tracing performance bottlenecks and 
automating recovery workflows. 

DevOps Engineer | HCL Tech 
Sep 2021 – Apr 2023 | Project: Applied Materials 
• Developed and maintained Jenkins pipelines with declarative syntax, supporting 
multibranch builds and staged testing. 
• Managed Azure resources (VMs, VNets, Web Apps, Storage) using Terraform & 
Ansible. 
• Implemented proactive monitoring with Prometheus and integrated Kibana for 
structured logging. 
• Maintained infrastructure patching using Ansible for all Linux environments. 
• Supported parallel development via branching and Git flow strategies. 
• Managed artifact versioning and deployment using Maven and GitHub. 
• Conducted internal knowledge-sharing sessions on infrastructure automation. 
• Diagnosed and resolved build failures, reducing average issue resolution time. 

Education 
Bachelor of Technology (B. Tech), Madanapalle Institute of Technology & Science (2017 – 
2021) 
Aggregate: 78% 

Architecture Overview  
Project: Medispend - Java Microservices Deployed on EKS/AKS using Jenkins CI/CD 
• Code Repo: GitHub (feature -> release -> main)
• CI/CD: Jenkins + Maven -> Docker -> ECR 
• IaC: Terraform (modular, multi-cloud) -> EKS/AKS 
• Deployment: Helm (rolling + blue/green) 
• Monitoring: Prometheus, Grafana, Alertmanager 
• Logging: ELK, log labels for microservices 
• Security: IAM + RBAC + Secrets Manager 

Key Projects & Microservices 
• Auth & User Service: Handles OAuth2, RBAC, JWT token management 
• Expense Submission Service: Upload & validate receipts (PDF/JPG) 
• Compliance Rules Engine: Applies regulatory logic on transactions 
• Notification Service: Sends alerts via SMS/email using SES/Twilio 
• Audit Trail Service: Immutable event logging for security audits 
• Billing Service: Calculates subscription-based costs per client 
• Search Service: Full-text search using OpenSearch
"""

print("Resume content analyzed successfully.")
print("Key Information Extracted:")
print("- Name: Bathina Siva Prasad Reddy")
print("- Role: DevOps Engineer")
print("- Experience: 3.10+ years")
print("- Location: Bengaluru, KA")
print("- Contact: +91 6363295603, bathinasivaprasadreddy@gmail.com")
print("- Current Company: Infodot Systems")
print("- Previous Company: HCL Tech")
print("- Education: B.Tech from Madanapalle Institute of Technology & Science")
print("- Main Project: Medispend (Healthcare Compliance Platform)")