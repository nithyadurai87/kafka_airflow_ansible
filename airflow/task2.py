from datetime import datetime
from airflow import DAG
import os
from airflow.operators.python_operator import PythonOperator

def pushfile():
    push_cmd = 'rsync -arv -e "ssh -i /home/shrini/shrini-freepem.pem" /home/shrini/backups ubuntu@35.166.185.40:/home/ubuntu'
    os.system(push_cmd)

def clr():
    clr_cmd = 'rm -f /home/shrini/backups/*'
    os.system(clr_cmd)

dag = DAG('push_remote', description='Pushing files to remote every day', schedule_interval='20 00 * * *', start_date=datetime(2020, 11, 2), catchup=False)

pushfile_operator = PythonOperator(task_id='pushfile_task', python_callable=pushfile, dag=dag)
clear_operator = PythonOperator(task_id='clearing_task', python_callable=clr, dag=dag)

pushfile_operator >> clear_operator
