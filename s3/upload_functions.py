import json
import boto3
from botocore.client import Config
import os

###Upload updated python objects to s3 bucket
def upload_python_objects():
	"""
		Upload python files to s3 Bucket
	"""

	open_config = open('/path/to/file/scrapy-configs.json').read()
	load_config = json.loads(open_config)
	aws_auth = load_config['aws_keys']
	bucket_name = 'functions'
	path = '/home/ubuntu/Desktop/functions/'
	objects = os.listdir(path)
	for file in objects:
		if not os.path.isdir(path + file):
			pass
			aws_access_key = aws_auth['access_key']
			aws_secret_key= aws_auth['secret_key']

			directory = path + '/' + file
			print (file)
			print ('uploading file to s3 bucket, "functions"')
			s3 = boto3.resource(
									's3',
									aws_access_key_id=aws_access_key,
									aws_secret_access_key=aws_secret_key,
									config=Config(signature_version='s3v4')
								)
			s3.meta.client.upload_file(directory, bucket_name, file, ExtraArgs={"ContentType":'application/python', "ACL":'public-read'})
		else:
			print ('{} is a directory...'.format(file))
	print ('Done!!!')

if __name__ == "__main__":
	upload_python_objects()


