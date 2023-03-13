## Create something whilst learning something new
Creating REST API in AWS using AWS API Gateway, Lambda and DynamoDB. This task (Infrastructure) was created using Terraform to allow easy deployment and management of resources in Cloud environment.

**Folder structure**
- *[python_codes](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/)* contains 2 zipped files needed in the Terraform file *[main.tf](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/python_codes/)*
- *[main.tf](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/)* contains 2 zipped files needed in the Terraform file *[main.tf](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/main.tf)
- *[get_function.zip](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/)** contains 2 zipped files needed in the Terraform file *[main.tf](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/get_function.zip)*
- *[post_function.zip](post_function.zip)*

The Terraform folder *[REST_API](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/)* contains 2 zipped files needed in the Terraform file *[main.tf](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/main.tf)* having 2 variables "account_id" and "main_region", can be executed with `terraform apply` and then a subsequent "yes" reply when prompted.
    Executing the terraform file:
    - takes the variables and creates a DynamoDB Table named "users",
    - creates 2 Lambda functions (GET and POST), 
    - creates a IAM role with DynamoDB permissions and attaches the role to the lambda functions, 
    - creates a REST API Gateway with name "userManagement",
    - creates 2 API Gateway methods (GET and POST) and integrates the lambda functions to the corresponding API gateway methods. 
    - It also gives API permission to invoke the Lambda functions and, 
    - finally deploys the API getting back the output of GET and POST method urls as well as the corresponding function url.


#### POST GET METHOD
> API POST Method URL: "https://ycd6tuk2df.execute-api.us-east-1.amazonaws.com/v1/users"


**example body:**
```
'{"first_name":"John", "age":"32"}'
```

**Invocation**
```
curl -X POST -H "Content-Type: application/json" -d '{"first_name":"John", "age":"32"}' https://ycd6tuk2df.execute-api.us-east-1.amazonaws.com/v1/users
```


#### API GET METHOD
> API GET Method URL: "https://ycd6tuk2df.execute-api.us-east-1.amazonaws.com/v1/{user_id}"

To make a GET Request simply click link or copy and paste link in browser and edit 
`{user_id}` with "user id" from making a POST Request or random id (will return error) .

