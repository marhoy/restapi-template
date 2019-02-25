# restapi-template
A template for starting new Flask projects

# Development and Testing
In order to run the application locally for development and debugging:
```
python3.6 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python application.py
```

To run tests and check that the code is working correctly:
```bash
pip install -r requirements-develop
tox
```
# Docker usage
- Build docker image: `docker build -t restapi .`
- Run docker container from image: `docker run -p 5000:5000 --name restapi --rm -d restapi`

# Deploy to Azure
- Log into the [Azure Portal](https://portal.azure.com/) and create/find a dedicated resource group. Add an appropriate "App Service Plan" to the resource group. For testing, use the B1 plan.
- You could create a resource group an service plan as follows:
```bash
az group create --name myResourceGroup --location "North Europe"
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku B1 --is-linux 
```

## Using the Docker image
- Build and push the docker image to a registry (e.g. hub.docker.com).
- Create a webapp from the docker image:
```bash
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name <app_name> --deployment-container-image-name <docker-ID>/mydockerimage:v1.0.0
```
- Map port 80 to whatever port is exposed by your container (e.g. 5000):
```bash
az webapp config appsettings set --resource-group myResourceGroup --name <app_name> --settings WEBSITES_PORT=5000
```

## As a standalone Web App
- Log into the [Azure Portal](https://portal.azure.com/) and create/find a dedicated resource group. Add an appropriate "App Service Plan" to the resource group. For testing, use the B1 plan.
- Install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) for your OS
- Authenticate: ```az login```
- Create the WebApp, using Python-3.6 and an already existing "Resource Group" and "App Service Plan". The `appname` needs to be _globally_ unique, so add some random characters:
```bash
az webapp create --name <appname> --runtime "PYTHON|3.6" --resource-group aic-webapp-testing --plan WebAppTestingPlan
```
- Log into the [Azure Portal](https://portal.azure.com/), and find your newly created webapp. Click the "Deployment center" and copy the "git clone url". Add the URL as a remote git repository:
```bash
git remote add azure <git_clone_url>
```
- Make sure you have commited all your changes.
- Push your code to the `master` branch on Azure: `git push azure master`. The first time, you will be prompted for a username/password. They can be found under "Deployment Credentials" in the "Deployment center".
- If all goes well, your application is now available at http://<app_name>.azurewebsites.net/
- To update the server, just push again.
- To delete your webapp: `az webapp delete --name <appname> --resource-group aic-webapp-testing`

# Deploy to Amazon Elastic Beanstalk
- Install eb CLI: `pip install awsebcli`
- Create eb application: `eb init -p python-3.6 restapi`. You will be asked to select a region.
- Create environment and deploy to AWS: `eb create -i t3.nano restapi-env`. See [EB pricing](https://aws.amazon.com/elasticbeanstalk/pricing/) for other instance options.
- To open your application: `eb open`
- Log into the [AWS console](https://console.aws.amazon.com/console/home) to view your server
- Update server if you change something: `eb deploy` 
- To terminate and remove the server: `eb terminate restapi-env`

 
