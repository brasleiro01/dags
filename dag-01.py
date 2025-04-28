from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(
    dag_id='minha_primeira_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',  # Roda todo dia
    catchup=False,
    tags=['exemplo'],
) as dag:

    inicio = DummyOperator(task_id='inicio')
    fim = DummyOperator(task_id='fim')

    inicio >> fim
