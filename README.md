# restapi-template
A template for starting new Flask projects

# Docker usage
- Build docker image: ```docker build -t restapi .```
- Run docker container from image: ```docker run -p 5000:5000 --name restapi --rm -d restapi```

# Deploy to Amazon Elastic Beanstalk
- Install eb CLI: ```pip install awsebcli```
- Create eb application: ```eb init -p python-3.6 restapi```. You will be asked to select a region.
- Create environment and deploy to AWS: ```eb create restapi-env```
- To open your application: ```eb open```
- Log into the [AWS console](https://console.aws.amazon.com/console/home) to view your server
- Update server if you change something: ```eb deploy``` 
- To terminate and remove the server: ```eb terminate restapi-env```

# Deploy to Azure
- Install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) for your OS
- Authenticate: ```az login```
- Create the web app: ```az webapp up -n <app_name> -l westeurope --sku B1```. Location and pricing tier is optional.
  - The app_name needs to be _globally_ unique, so add some random characters.
  - Typical locations can be ```northeurope``` (Dublin) or ```westeurope``` (Amsterdam)
  - The ```<pricing_tier>``` can be e.g. B1 (Basic Small) or S1 (Standard Small) if you need automatic scaling. See [service plan details](https://azure.microsoft.com/en-us/pricing/details/app-service/plans/) for more details.
- Your application is now available at http://<app_name>.azurewebsites.net/
- Log into the [Azure Portal](https://portal.azure.com/) to administrate the Web App
- Redeploy if you changed anything: ```az webapp up -n <app_name> -l westeurope```
- To terminate and remove the server: ```az group delete --name <resource-group>``` where resource-group is the name of the resource group containing your web app.
