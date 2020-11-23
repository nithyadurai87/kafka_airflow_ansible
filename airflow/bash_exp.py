from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

dag = DAG('bash_exp', description='Mysql backup every hour', schedule_interval='00 * * * *', start_date=datetime(2020, 11, 2), catchup=False)

operator = BashOperator(task_id='backup_task', bash_command='mysqldump -u root -ppassword sample > "/home/shrini/backups/"sample_"$(date +"%Y%m%d_%H%M%S").sql"',dag=dag)
