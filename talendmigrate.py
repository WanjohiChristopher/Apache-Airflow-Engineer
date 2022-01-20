import time
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow import DAG
data = DAG(dag_id='data_migration',
           schedule_interval=None,
                  start_date=datetime(2021,12,14),
                  catchup=False)
migrate=BashOperator(task_id='migrate',
                     bash_command="/home/kreezy/airflow/talend_jobs/ADVENTUREWORKSDynamicSchema_0.1/ADVENTUREWORKSDynamicSchema/ADVENTUREWORKSDynamicSchema_run.sh ",
dag=data)
print(migrate)

