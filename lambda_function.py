import json
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

def lambda_handler(event, context):
    """
    AWS Lambda function to handle CRUD operations for student records
    """
    try:
        http_method = event['httpMethod']
        
        if http_method == 'POST':
            return create_student(event)
        elif http_method == 'GET':
            return get_student(event)
        elif http_method == 'PUT':
            return update_student(event)
        elif http_method == 'DELETE':
            return delete_student(event)
        else:
            return {
                'statusCode': 405,
                'body': json.dumps({'error': 'Method not allowed'})
            }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def create_student(event):
    """Create a new student record"""
    try:
        student_data = json.loads(event['body'])
        
        # Validate required fields
        required_fields = ['student_id', 'name', 'course']
        for field in required_fields:
            if field not in student_data:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': f'Missing required field: {field}'})
                }
        
        # Check if student already exists
        response = table.get_item(Key={'student_id': student_data['student_id']})
        if 'Item' in response:
            return {
                'statusCode': 409,
                'body': json.dumps({'error': 'Student with this ID already exists'})
            }
        
        # Add student record
        table.put_item(Item=student_data)
        
        return {
            'statusCode': 201,
            'body': json.dumps({
                'message': 'Student record created successfully',
                'student_id': student_data['student_id']
            })
        }
    
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON in request body'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Database error: {str(e)}'})
        }

def get_student(event):
    """Retrieve a student record by student_id"""
    try:
        query_params = event.get('queryStringParameters') or {}
        student_id = query_params.get('student_id')
        
        if not student_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'student_id parameter is required'})
            }
        
        response = table.get_item(Key={'student_id': student_id})
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Student not found'})
            }
        
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Database error: {str(e)}'})
        }

def update_student(event):
    """Update an existing student record"""
    try:
        student_data = json.loads(event['body'])
        
        if 'student_id' not in student_data:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'student_id is required for update'})
            }
        
        student_id = student_data['student_id']
        
        # Check if student exists
        response = table.get_item(Key={'student_id': student_id})
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Student not found'})
            }
        
        # Update student record
        table.put_item(Item=student_data)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Student record updated successfully',
                'student_id': student_id
            })
        }
    
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON in request body'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Database error: {str(e)}'})
        }

def delete_student(event):
    """Delete a student record by student_id"""
    try:
        query_params = event.get('queryStringParameters') or {}
        student_id = query_params.get('student_id')
        
        if not student_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'student_id parameter is required'})
            }
        
        # Check if student exists
        response = table.get_item(Key={'student_id': student_id})
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Student not found'})
            }
        
        # Delete student record
        table.delete_item(Key={'student_id': student_id})
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Student record deleted successfully',
                'student_id': student_id
            })
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Database error: {str(e)}'})
        }
