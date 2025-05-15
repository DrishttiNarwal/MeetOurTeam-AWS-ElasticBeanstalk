# Meet Our Team – Portfolio Deployment on AWS Elastic Beanstalk

This project demonstrates the cloud-based deployment of a "Meet Our Team" portfolio web application using **AWS Elastic Beanstalk**, with integration of services like **Amazon EC2**, **S3**, **IAM**, **Auto Scaling**, and **Elastic Load Balancing**. The application displays detailed team member profiles with links to their GitHub and LinkedIn, aiming to improve visibility and collaboration in dynamic tech teams.

## 🌐 Project Objective

- Deploy a professional portfolio site to AWS using Elastic Beanstalk
- Showcase team member profiles with summaries, skills, and social links
- Apply cloud concepts like scalability, auto-scaling, load balancing, and IAM roles
- Document the end-to-end deployment pipeline and challenges faced

## 🚀 AWS Services Used

- **Elastic Beanstalk** – Application deployment and environment management
- **Amazon EC2** – Scalable virtual compute servers
- **Amazon S3** – Storage of project files and application versions
- **Elastic Load Balancer (ELB)** – Distributes traffic across EC2 instances
- **Auto Scaling** – Dynamically scales EC2 instances based on load
- **AWS IAM** – Secure access control with defined roles and policies
- **CloudWatch** – Monitoring logs and performance metrics

## 🧱 Architecture Overview

- User requests are routed through a Load Balancer
- Elastic Beanstalk handles deployment, scaling, and environment setup
- Application code is fetched from an S3 bucket and deployed on EC2
- IAM roles restrict and manage access to AWS resources securely
- Auto Scaling adjusts compute power based on incoming traffic

## 🛠️ Deployment Steps

1. **Initialize Elastic Beanstalk Environment**  
   Created a new environment via the AWS Elastic Beanstalk console, selecting the appropriate platform (e.g., Node.js or Python).

2. **Upload Files to S3**  
   Zipped the project and uploaded to an S3 bucket for storage and deployment.

3. **Deploy via Elastic Beanstalk**  
   Connected S3 with Elastic Beanstalk to launch the application onto EC2 instances.

4. **Configure ELB and Auto Scaling**  
   Enabled load balancing and auto scaling for performance and reliability.

5. **Set IAM Permissions**  
   Assigned IAM roles to control access and enforce best security practices.

## Application Pages

- Team Main Page
- Individual Profile Pages

## 🧩 Challenges Faced

- Elastic Beanstalk’s limited support for machine learning models
- Transition from Launch Configuration to Launch Template caused deployment issues
- EC2 storage limitations in AWS Free Tier affected TensorFlow model installations

## ✅ Outcomes

- Successfully deployed a scalable and secure portfolio application on AWS
- Gained hands-on experience with core AWS services
- Demonstrated knowledge of cloud deployment, architecture, and troubleshooting
 