## CI/CD deployment plan

Before performing the deployment plan, following improvements has to be done in the current project:
 1. **Add tests** - The project currently does not have any tests. We can include tests on label_mapping, image size, contrast etc of the training and expected test data.
 2. **Include logging** - Include a logging system so that the logs of the preprocessing, training can be exported or easily monitored.
 3. Create a docker image with the requirements needed for this project
 4. **Config file** - Create a config file with the hyperparameters finalized, any other parameters needed for the training or testing of the project. This way we can only touch config file, if a new variation of the parameters resulted in better model. Alternatively this can be uploaded to AWS SSM.


### Deployment Plan Option 1

- **Stack**: Github, AWS CodePipeline, AWS EC2
- **Process**:
  - Use Github for source control (CI). Create branches master and integration.
  - Create github actions so that whenever a push is made to master or integration branch corresponding AWS Codepipeline stack triggers
  - AWS Codepipeline can have following steps
    - Get the repository code from Github
    - Execute tests to ensure deployment can be done, if test fails: fail the pipeline and notify in slack or teams
    - If tests passed: proceed with build and deployment step (CD). Deployment step consists of:
      - Install/update requirements in AWS EC2 instance
      - Package the application and create deployment artifacts
      - Deploy the code in corresponding EC2 instance

Once we finish this setup either we can have a API implementation in EC2 instance to perform realtime or batch processing or we can use *AWS Batch* for near real time or batch processing.

### Deployment Plan Option 2

- **Stack**: Github, Jenkins, AWS S3, AWS ECR, Airflow, AWS Batch
- **Process**:
  - Use Github, same as option 1.
  - Create github actions to trigger a jenkins job upon a push in master or integration branch
  - Jenkins job does the following steps:
    - Get the repository code from Github
    - Install requirements from Pipfile or requirements.txt
    - Run tests, if tests failed: fail the process and notify in slack or teams
    - if tests passed: Upload the model artifact to AWS S3 bucket (enable versioning in AWS S3)
  - Create github actions to trigger jenkins job on a change in Dockerfile or runner file
  - Docker related jenkins job performs following steps
    - get the repository code from Github
    - Build the docker image and push to ECR

Once the above setup is done, do the following:
  - A job that pulls from AWS S3 our deep learning model, reads input data and runs prediction step (fashion_mnist_job)
  - Airflow dag that is scheduled based on project requirements
  - On a schedule airflow submits AWS batch job whose job definition is created using our docker image present in AWS ECR to run fashion_mnist_job and writes results to S3 or where ever they are needed.


Note: Instead of AWS S3 in above step we can use Mlflow. Apart from that all infrastructure and permissions can be controlled by Terraform, CloudFormation in both options.

## Monitoring and KPI's

- Implement and use logging so the logs can be exploited using AWS CLoudWatch, CloudTrail or Athena etc.
- Implement data drift detection system and monitor the results to identify when there is a data drift
- Log metrics or KPI's in Cloudwatch metrics or Grafana
- Create alarms on top of metrics and also add notifications on top of alarms 


## How to proceed
- Define deployment options like above
- Perform PoC, security and use case analysis on top of the options we have at hand
- Select an option and perform MVP
- Create the current architecture diagram and document the process (Confluence etc)