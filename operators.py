#The BashOperator allows you to specify any given Shell command or script and add it to an Airflow workflow
from airflow.operators.bash import BashOperator

#lets define our dag first
from  airflow.models import DAG
from datetime import datetime

dag=DAG(
        dag_id='bash_operator',
        start_date=datetime(2020,8,13),
        schedule_interval='@hourly',
    
        )
#creating a bash operator

example_bash_operator=BashOperator(task_id='example_bash',
                                   #define bash_command
                                   bash_command='clean.sh',
                                   #defining task dag
                                   dag=dag)

#print
print(example_bash_operator)
# Define a second operator to run the `consolidate_data.sh` script
consolidate = BashOperator(
    task_id='consolidate_task',
    bash_command='consolidate_data.sh',
    dag=dag)

# Define a final operator to execute the `push_data.sh` script
push_data = BashOperator(
    task_id='pushdata_task',
    bash_command='push_data.sh',
    dag=dag)
