from cloudmesh.configuration.Config import Config
# import psycopg2
from google.cloud import bigquery
from google.oauth2 import service_account

config = "~/.cloudmesh/cloudmesh.yaml"
config2 = Config(config_path=config)
# bigquery use same google GCP config
print(config2['cloudmesh.cloud.google.credentials.json_file'])
print(config2['cloudmesh.cloud.google.credentials.project'])
service_account_file = config2[
    'cloudmesh.cloud.google.credentials.json_file']
print(service_account_file)
credentials = service_account.Credentials.from_service_account_file(
    service_account_file)
project_id = config2['cloudmesh.cloud.google.credentials.project']
client = bigquery.Client(credentials=credentials, project=project_id)

query_txt = \
    "SELECT " \
    "CONCAT( 'https://stackoverflow.com/questions/', " \
    "CAST(id as STRING)) as url,  view_count " \
    "FROM `bigquery-public-data.stackoverflow.posts_questions` " \
    "WHERE tags like '%google-bigquery%' ORDER BY view_count DESC LIMIT 10"
# client = bigquery.Client(credentials=credentials, project=project_id)
query_job = client.query(query_txt)
results = query_job.result()
for row in results:
    print(f"{row.url} : {row.view_count} views")
datasets = list(client.list_datasets())
results = datasets
project = client.project
if datasets:
    print(f"Datasets in project {project}:")
    for dataset in datasets:
        print(f"\t{dataset.dataset_id}")
else:
    print(f"{project} project does not contain any datasets.")

print(project_id)
table_id1 = 'employee_table'
dataset_id = 'emp_table'
table_id = client.project + "." + dataset_id + "." + table_id1
table = client.get_table(table_id)
# Table description
print(f"Table id", table.table_id)
print(f"Table schema: ", table.schema)
print("Table description:", table.description)
print(f"Table number of rows", table.num_rows)