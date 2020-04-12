from portfolio.conf import config

AWS_EC2_DOMAIN = "nickflorin-api.com"
AWS_ACCESS_KEY_ID = config('AWS_PORTFOLIO_GROUP_ACCESS_KEY_ID', required=True)
AWS_SECRET_ACCESS_KEY = config('AWS_PORTFOLIO_GROUP_SECRET_ACCESS_KEY', required=True)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'portfolio20'
AWS_S3_REGION_NAME = 'us-east-2'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.us-east-2.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
