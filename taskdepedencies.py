from airflow.models import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
dag=DAG(dag_id='example_dag',
        start_date=datetime(2021,10,13),
        schedule_interval='@daily'

        )
# defining the tasks for both upstream and downstream tasks
#task 1
task1=BashOperator(task_id='task1_id',
                   bash_command='echo hello',
                   dag=dag)
#task 2
task2=BashOperator(task_id='task2_id',
                   bash_command='echo world',
                   dag=dag)
#for the tasks
#upstream task
print(task1>>task2)
#downstream task
print(task1<<task2)

#continuation from datacamp
# Define a new pull_sales task
pull_sales = BashOperator(
    task_id='pullsales_task',
    bash_command='wget https://salestracking/latestinfo?json',
    dag=dag
)

# Set pull_sales to run prior to cleanup
pull_sales >> cleanup

# Configure consolidate to run after cleanup
consolidate<<cleanup<<pull_sales

# Set push_data to run last
push_data<<consolidate<<cleanup<<pull_sales

