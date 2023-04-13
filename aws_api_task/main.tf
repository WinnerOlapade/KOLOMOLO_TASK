variable "account_id" {
  # Pass Account ID value in as environmental variable. Set environment variable with [export TF_VAR_account_id="insert_value_here"]
  type = string
}

variable "main_region" {
  type    = string
  default = "us-east-1"
}

provider "aws" {
  region = var.main_region
}


# DynamoDB table creation
resource "aws_dynamodb_table" "dynamodb_table" {
  name           = "users"
  hash_key       = "user_id"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5

  attribute {
    name = "user_id"
    type = "S"
  }
}


# Create Lambda role
resource "aws_iam_role" "lambda_role" {
  name = "lambda_role"
  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : {
          "Service" : "lambda.amazonaws.com"
        },
        "Action" : "sts:AssumeRole"
      }
    ]
  })
}


# Creating and Attaching Role Policy
resource "aws_iam_role_policy" "dynamodb-lambda-policy" {
  name = "dynamodb_lambda_policy"
  role = aws_iam_role.lambda_role.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Action" : ["dynamodb:*"],
        "Resource" : "${aws_dynamodb_table.dynamodb_table.arn}"
      }
    ]
  })
}

# Fetch arn of existing IAM policy 
data "aws_iam_policy" "AWSLambdaBasicExecutionRoleA" {
  arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Attach the fetched IAM policy to createc role
resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = data.aws_iam_policy.AWSLambdaBasicExecutionRoleA.arn

}

# Creating POST and GET Lambda functions
resource "aws_lambda_function" "post_function" {
  filename         = "post_function.zip"
  function_name    = "post_function"
  role             = aws_iam_role.lambda_role.arn
  handler          = "post_function.lambda_handler"
  runtime          = "python3.9"
  source_code_hash = filebase64sha256("post_function.zip")
}

resource "aws_lambda_function_url" "post_url" {
  function_name      = aws_lambda_function.post_function.function_name
  authorization_type = "NONE"
}

resource "aws_lambda_function" "get_function" {
  filename      = "get_function.zip"
  function_name = "get_function"
  role          = aws_iam_role.lambda_role.arn
  handler       = "get_function.lambda_handler"
  runtime       = "python3.9"

  source_code_hash = filebase64sha256("get_function.zip")
}

resource "aws_lambda_function_url" "get_url" {
  function_name      = aws_lambda_function.get_function.function_name
  authorization_type = "NONE"
}

// Creating REST API Gateway
resource "aws_api_gateway_rest_api" "rest_api" {
  name        = "userManagement"
  description = "Rest Api with POST and GET methods"

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

// Creating REST API Gateway resources for POST and GET
resource "aws_api_gateway_resource" "api_resource" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  parent_id   = aws_api_gateway_rest_api.rest_api.root_resource_id
  path_part   = "users"
}

resource "aws_api_gateway_resource" "get_resource" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  parent_id   = aws_api_gateway_rest_api.rest_api.root_resource_id
  path_part   = "{user_id}"
}

# Creating and attaching REST API Gateway Methods for POST and GET
resource "aws_api_gateway_method" "api_post_method" {
  rest_api_id   = aws_api_gateway_rest_api.rest_api.id
  resource_id   = aws_api_gateway_resource.api_resource.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "api_get_method" {
  rest_api_id   = aws_api_gateway_rest_api.rest_api.id
  resource_id   = aws_api_gateway_resource.get_resource.id
  http_method   = "GET"
  authorization = "NONE"
}

# Integrating Lambda functions to API
resource "aws_api_gateway_integration" "post_integration" {
  rest_api_id             = aws_api_gateway_rest_api.rest_api.id
  resource_id             = aws_api_gateway_resource.api_resource.id
  http_method             = aws_api_gateway_method.api_post_method.http_method
  type                    = "AWS_PROXY"
  integration_http_method = "POST"
  uri                     = aws_lambda_function.post_function.invoke_arn
}

resource "aws_api_gateway_integration" "get_integration" {
  rest_api_id             = aws_api_gateway_rest_api.rest_api.id
  resource_id             = aws_api_gateway_resource.get_resource.id
  http_method             = aws_api_gateway_method.api_get_method.http_method
  type                    = "AWS_PROXY"
  integration_http_method = "POST"
  uri                     = aws_lambda_function.get_function.invoke_arn
}

# Giving API gateway permissions to invoke Lambda permissions
resource "aws_lambda_permission" "apigw_lambda_get" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.get_function.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "arn:aws:execute-api:${var.main_region}:${var.account_id}:${aws_api_gateway_rest_api.rest_api.id}/*/${aws_api_gateway_method.api_get_method.http_method}${aws_api_gateway_resource.get_resource.path}"
}

resource "aws_lambda_permission" "apigw_lambda" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.post_function.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "arn:aws:execute-api:${var.main_region}:${var.account_id}:${aws_api_gateway_rest_api.rest_api.id}/*/${aws_api_gateway_method.api_post_method.http_method}${aws_api_gateway_resource.api_resource.path}"
}

# Deploy API Gateway
resource "aws_api_gateway_deployment" "api_deploy" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  depends_on  = [aws_api_gateway_integration.get_integration, aws_api_gateway_integration.post_integration]
  lifecycle {
    create_before_destroy = true
  }
}

#Creating Deployment stage name
resource "aws_api_gateway_stage" "api_stage" {
  deployment_id = aws_api_gateway_deployment.api_deploy.id
  rest_api_id   = aws_api_gateway_rest_api.rest_api.id
  stage_name    = "v1"
}

# Print the  exact path of GET and POST,
output "get_url" {
  value = "${aws_api_gateway_stage.api_stage.invoke_url}/{user_id}"
}

output "post_url" {
  value = "${aws_api_gateway_stage.api_stage.invoke_url}/users"

}

output "post_function_url" {
  value      = aws_lambda_function_url.post_url.function_url
  description = "Post function Url"
}
output "get_function_url" {
  value      = aws_lambda_function_url.get_url.function_url
  description = "Get function Url"
}