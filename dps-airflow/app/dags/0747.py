from datetime import datetime
from airflow.models import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


###############################################
# Parameters
###############################################
spark_app_name = "0747 Pipeline"


###############################################
# DAG Definition
###############################################
dag =  DAG(
    dag_id='0747_pipeline',
    description="This DAG runs a full workflow for 0747.",
    schedule_interval=None,
    start_date=datetime(2022, 2, 26),
    catchup=False,
    tags=['production'],)


document_etl = SparkSubmitOperator(
    task_id="document_etl",
    application="/sparks/production/0747/document_etl.py",
    name=spark_app_name,
    dag= dag
)

paragraph_extract = SparkSubmitOperator(
    task_id="paragraph_extract",
    application="/sparks/production/0747/document_etl.py",
    name=spark_app_name,
    dag= dag
)

field_extract = SparkSubmitOperator(
    task_id="field_extract",
    application="/sparks/production/0747/document_etl.py",
    name=spark_app_name,
    dag= dag
)

ocr = SparkSubmitOperator(
    task_id="ocr",
    application="/sparks/production/0747/document_etl.py",
    name=spark_app_name,
    dag= dag
)

transform_to_json = SparkSubmitOperator(
    task_id="transform_to_json",
    application="/sparks/production/0747/document_etl.py",
    name=spark_app_name,
    dag= dag
)


document_etl >> paragraph_extract >> field_extract >> ocr >> transform_to_json