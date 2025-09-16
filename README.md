# Serverless Web Application with AWS Lambda and DynamoDB

A serverless web application built with AWS Lambda and Amazon DynamoDB that provides CRUD operations for student records management.

## 🎯 Learning Outcomes

- Understanding how to set up and use AWS Lambda and DynamoDB
- Hands-on experience with API Gateway for serverless architectures
- Familiarity with basic CRUD operations in a cloud environment

## 🏗️ Architecture

```
API Gateway → AWS Lambda → DynamoDB
     ↓            ↓           ↓
  HTTP Requests → Function → StudentRecords Table
```

## 📋 Prerequisites

- AWS Account with appropriate permissions
- AWS CLI configured (optional but recommended)
- Python 3.x
- Postman or curl for testing

## 🚀 Setup Instructions

### 1. DynamoDB Table Setup

1. Navigate to AWS Management Console → DynamoDB
2. Create a new table with the following configuration:
   - **Table Name**: `StudentRecords`
   - **Primary Key**: `student_id` (String)
   - **Partition Key**: `student_id`

### 2. Lambda Function Setup

1. Go to AWS Lambda in the AWS Management Console
2. Create a new Lambda function:
   - **Function Name**: `StudentRecordHandler`
   - **Runtime**: Python 3.x
   - **Permissions**: Attach IAM role with DynamoDB read/write permissions

3. Deploy the provided `lambda_function.py` code

### 3. API Gateway Configuration

1. Navigate to API Gateway in AWS Management Console
2. Create a new REST API:
   - **API Name**: `StudentAPI`
3. Set up the following resources and methods:
   - `POST /students` - Create a new student record
   - `GET /students` - Retrieve student by ID
   - `PUT /students` - Update student record
   - `DELETE /students` - Delete student record
4. Deploy the API and note the Invoke URL

## 📁 Project Structure

```
Serverless-WebApp/
├── lambda_function.py    # Main Lambda function with CRUD operations
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
```

## 🔧 API Endpoints

### Create Student Record
```bash
POST /students
Content-Type: application/json

{
  "student_id": "123",
  "name": "John Doe",
  "course": "Enterprise Software",
  "email": "john.doe@example.com"
}
```

### Get Student Record
```bash
GET /students?student_id=123
```

### Update Student Record
```bash
PUT /students
Content-Type: application/json

{
  "student_id": "123",
  "name": "John Smith",
  "course": "Computer Science",
  "email": "john.smith@example.com"
}
```

### Delete Student Record
```bash
DELETE /students?student_id=123
```

## 🧪 Testing

### Using curl

**Create a student:**
```bash
curl -X POST \
  https://<your-api-id>.execute-api.<region>.amazonaws.com/dev/students \
  -H 'Content-Type: application/json' \
  -d '{
    "student_id": "123",
    "name": "John Doe",
    "course": "Enterprise Software",
    "email": "john.doe@example.com"
  }'
```

**Get a student:**
```bash
curl -X GET \
  https://<your-api-id>.execute-api.<region>.amazonaws.com/dev/students?student_id=123
```

**Update a student:**
```bash
curl -X PUT \
  https://<your-api-id>.execute-api.<region>.amazonaws.com/dev/students \
  -H 'Content-Type: application/json' \
  -d '{
    "student_id": "123",
    "name": "John Smith",
    "course": "Computer Science",
    "email": "john.smith@example.com"
  }'
```

**Delete a student:**
```bash
curl -X DELETE \
  https://<your-api-id>.execute-api.<region>.amazonaws.com/dev/students?student_id=123
```

### Using Postman

1. Import the API collection (if available)
2. Set the base URL to your API Gateway endpoint
3. Test each endpoint with appropriate request bodies

## 📊 DynamoDB Table Schema

| Attribute | Type | Description |
|-----------|------|-------------|
| student_id | String | Primary Key - Unique identifier for student |
| name | String | Student's full name |
| course | String | Course/Program name |
| email | String | Student's email address |

## 🔒 IAM Permissions

Your Lambda function requires the following DynamoDB permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:UpdateItem",
        "dynamodb:DeleteItem"
      ],
      "Resource": "arn:aws:dynamodb:<region>:<account-id>:table/StudentRecords"
    }
  ]
}
```

## 🚨 Error Handling

The Lambda function includes basic error handling for:
- Missing required parameters
- DynamoDB operation failures
- Invalid JSON in request body
- Student not found scenarios

## 📈 Monitoring

Monitor your application using:
- AWS CloudWatch Logs for Lambda function logs
- AWS CloudWatch Metrics for performance monitoring
- DynamoDB CloudWatch metrics for database performance

## 🛠️ Development

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up AWS credentials:
```bash
aws configure
```

3. Test locally using AWS SAM or similar tools

### Deployment

1. Package your Lambda function:
```bash
zip lambda_function.zip lambda_function.py
```

2. Upload to AWS Lambda through the console or CLI

## 📝 Features Implemented

- ✅ Create student records (POST)
- ✅ Read student records (GET)
- ✅ Update student records (PUT)
- ✅ Delete student records (DELETE)
- ✅ Error handling and validation
- ✅ JSON request/response format
- ✅ DynamoDB integration

## 🔍 Troubleshooting

### Common Issues

1. **Permission Denied**: Ensure Lambda has proper DynamoDB permissions
2. **Table Not Found**: Verify table name matches exactly
3. **Invalid JSON**: Check request body format
4. **CORS Issues**: Configure CORS in API Gateway if needed

### Debug Steps

1. Check CloudWatch Logs for detailed error messages
2. Verify API Gateway configuration
3. Test DynamoDB permissions independently
4. Validate request format and parameters

## 📚 Resources

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Amazon DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/)
- [API Gateway Documentation](https://docs.aws.amazon.com/apigateway/)
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## 👨‍💻 Author

**Tanmay Ranaware**  
CMPE 272 - Enterprise Software Development

## 📄 License

This project is part of an academic assignment for CMPE 272.

---

## 🎓 Assignment Reflection

### Challenges Faced
- Setting up proper IAM permissions for Lambda-DynamoDB interaction
- Understanding API Gateway integration with Lambda
- Handling different HTTP methods in a single Lambda function
- Error handling for various edge cases

### Key Learnings
- Serverless architecture benefits and limitations
- DynamoDB NoSQL database operations
- AWS service integration patterns
- Cloud-native application development practices

### Future Improvements
- Add input validation and sanitization
- Implement pagination for large datasets
- Add authentication and authorization
- Implement caching with ElastiCache
- Add comprehensive logging and monitoring
