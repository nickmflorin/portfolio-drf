from portfolio.conf import config

AWS_EC2_DOMAIN = config('AWS_EC2_DOMAIN', required=True)
AWS_EC2_IP_ADDRESS = config('AWS_EC2_IP_ADDRESS', required=True)

AWS_ACCESS_KEY_ID = config('AWS_PORTFOLIO_GROUP_ACCESS_KEY_ID', required=True)
AWS_SECRET_ACCESS_KEY = config('AWS_PORTFOLIO_GROUP_SECRET_ACCESS_KEY', required=True)

AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', required=True)
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', required=True)

AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (
    AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
