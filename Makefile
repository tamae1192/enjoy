
# 繰り返し使用するコマンドを記載

# 以下フロント関連=========

# 参考コマンド（実行不可）
set-env-dev:
	ENV=dev
	PROJECT=$ENV-count-app
	CF_DISTRIBUTION_ID=<YOUR_CF_DISTRIBUTION_ID>

build-next:
	npm run build
	
get-cf_dist:
	aws cloudfront list-distributions --query "DistributionList.Items[*].Id" --output text

get-cf-domains:
	aws cloudfront list-distributions --query "DistributionList.Items[*].DomainName"


# 以下AWS関連=========

# 参考コマンド（実行不可）
change-aws-profile:
	export AWS_PROFILE=

get-aws-profiles:
	aws configure list-profiles

check-s3:
	aws s3 ls