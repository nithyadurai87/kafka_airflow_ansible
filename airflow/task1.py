from datetime import datetime
from airflow import DAG
import os
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
usr = Variable.get("mysql_username")
pwd = Variable.get("mysql_password")

def backup():
    #backup_cmd = 'mysqldump -u root -ppassword sample > "/home/shrini/backups/"sample_"$(date +"%Y%m%d_%H%M%S").sql"'
    backup_cmd = 'mysqldump -u '+usr+' -p'+pwd+' sample > "/home/shrini/backups/"sample_"$(date +"%Y%m%d_%H%M%S").sql"'
    os.system(backup_cmd)

dag = DAG('mysql_backup', description='Mysql backup every hour', schedule_interval='00 * * * *', start_date=datetime(2020, 11, 2), catchup=False)

backup_operator = PythonOperator(task_id='backup_task', python_callable=backup, dag=dag)
