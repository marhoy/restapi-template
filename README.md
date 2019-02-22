# restapi-template
A template for starting new Flask projects

# Docker usage
## Create docker image
```docker build -t restapi .```

## Run docker container
```docker run -p 5000:5000 --name restapi --rm -d restapi```

# Deploy to Amazon Elastic Beanstalk
- Install eb CLI: ```pip install awsebcli```
- Create eb application: ```eb init -p python-3.6 restapi```. You will be asked to select a region.
- Create environment and deploy to AWS: ```eb create flask-env```
- Update server if you change something: ```eb deploy``` 
