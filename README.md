# AWSInstanceTypeChange

To create the lambda function

-->git clone https://github.com/SUTRAPUSHARANKUMARREDDY/AWSInstanceTypeChange.git
-->cd AWSInstanceTypeChang
-->pip3 install --target ./package -r requirements.txt
-->cd package/
-->zip -r ../AWSInstanceTypeChang.zip .
-->cd ..
-->zip -g AWSInstanceTypeChang.zip InstanceTypeChang.py
-->zip -g AWSInstanceTypeChang.zip constant.py
-->aws lambda create-function --function-name instance_shutdown --zip-file fileb://AWSInstanceTypeChang.zip --runtime python3.8 --role arn:aws:iam::*****:role/ --handler InstanceTypeChang.lambda_handler --timeout 300



To Update the lambda

-->git clone https://github.com/SUTRAPUSHARANKUMARREDDY/AWSInstanceTypeChange.git
-->cd AWSInstanceTypeChang
-->pip3 install --target ./package -r requirements.txt
-->cd package/
-->zip -r ../AWSInstanceTypeChang.zip .
-->cd ..
-->zip -g AWSInstanceTypeChang.zip InstanceTypeChang.py
-->zip -g AWSInstanceTypeChang.zip constant.py
-->aws lambda update-function-code --function-name instance_shutdown --zip-file fileb://AWSInstanceTypeChang.zip
