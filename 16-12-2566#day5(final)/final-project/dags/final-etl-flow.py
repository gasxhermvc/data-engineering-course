from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import logging

from airflow.utils import timezone

default_args = {
    'owner': 'airflow',
}

with DAG (
    'final-etl-flow',
    schedule_interval='*/5 * * * *',
    default_args=default_args,
    start_date=timezone.datetime(2021, 7, 9),
    dagrun_timeout=timedelta(minutes=5),
    tags = ['ETL','Notify'],
    catchup=False,
) as dag :
    process_every_daily_task = BashOperator(
        task_id='final-process',
        bash_command='python /python_scripts/final-process.py',
    dag=dag)
    
    notify_every_daily_task = BashOperator(
        task_id='final-notify',
        bash_command='python /python_scripts/final-notify.py',
    dag=dag)
process_every_daily_task >> notify_every_daily_task