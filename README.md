# S3_Bucket_Creation_using_AWS_Lambda_function
Create a S3 bucket using AWS Lambda

Steps : 

1) Create a Lambda function as mentioned in lambda_function.py

![Screenshot (117)](https://user-images.githubusercontent.com/14953882/214209032-90a666a7-556b-4745-b89a-c8b20a8656b8.png)

2) Modify the Lambda execution role policy to access S3

![Screenshot (118)](https://user-images.githubusercontent.com/14953882/214209247-d7c5e9b5-9b92-47ad-8d6a-7c623d44e30f.png)

3) Configure test event with the below inputs
      {
          "region": "ap-south-1",
          "bucket_name": "test-lambda-bucket-23-1-23"
      }
      
![Screenshot (119)](https://user-images.githubusercontent.com/14953882/214209487-558b4ddf-2071-4346-b23d-a9223c677eab.png)

4) Verify the results under S3 section.

![Screenshot (116)](https://user-images.githubusercontent.com/14953882/214209849-d8b6d444-2030-4a48-a4ab-9fa4d25156e2.png)





