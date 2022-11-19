# AWSInstanceTypeChange

To create the lambda function <br />

--> git clone https://github.com/SUTRAPUSHARANKUMARREDDY/AWSInstanceTypeChange.git <br />
--> cd AWSInstanceTypeChange <br />
--> pip3 install --target ./package -r requirements.txt <br />
--> cd package/ <br />
--> zip -r ../AWSInstanceTypeChange.zip . <br />
--> cd .. <br />
--> zip -g AWSInstanceTypeChange.zip InstanceTypeChang.py <br />
--> zip -g AWSInstanceTypeChange.zip constante.py <br />
--> aws lambda create-function --function-name instance_shutdown --zip-file fileb://AWSInstanceTypeChange.zip --runtime python3.8 --role arn:aws:iam::*****:role/ --handler InstanceTypeChang.lambda_handler --timeout 300 <br />



To Update the lambda <br />

-->git clone https://github.com/SUTRAPUSHARANKUMARREDDY/AWSInstanceTypeChange.git <br />
-->cd AWSInstanceTypeChange <br />
-->pip3 install --target ./package -r requirements.txt <br />
-->cd package/ <br />
-->zip -r ../AWSInstanceTypeChange.zip . <br />
-->cd .. <br />
-->zip -g AWSInstanceTypeChange.zip InstanceTypeChang.py <br />
-->zip -g AWSInstanceTypeChange.zip constant.py <br />
-->aws lambda update-function-code --function-name instance_shutdown --zip-file fileb://AWSInstanceTypeChange.zip <br />
