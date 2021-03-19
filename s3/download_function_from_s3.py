# -*- coding: utf-8 -*-
import json
import boto3
import os


def download_functions(BUCKET_NAME):
	"""
		download python files from s3 Bucket
	"""
	s3_connect = boto3.resource("s3")
	bucket = s3_connect.Bucket(name=BUCKET_NAME)
	objects = bucket.objects.all()
	for obj in objects:
		file_name = obj.key
		s3_connect.Bucket(BUCKET_NAME).download_file(file_name, "/home/ubuntu/Desktop/" + file_name)
		print (file_name, ' downloaded...')

if __name__ == "__main__":
	download_functions(BUCKET_NAME='functions-scrapy')
