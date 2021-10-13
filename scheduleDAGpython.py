from airflow.models import DAG
from datetime import datetime
from datetime import timedelta #it expects an integer value
default_args = {
  'owner': 'Engineering',
  'start_date': datetime(2019,11,1),
  'email': ['airflowresults@chris.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 3,
  'retry_delay': timedelta(minutes=20)
}

dag = DAG('update_dataflows', default_args=default_args, schedule_interval='30 12 * * 3')