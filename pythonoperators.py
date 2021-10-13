from airflow.operators.python import PythonOperator
from airflow.models import DAG
from datetime import datetime
example_dag=DAG(dag_id='example',
                start_date=datetime(2021,1,1),
                schedule_interval='0 0 * * *'
                )
# creating a fuction in python
def printchris():
    print('This goes into the logs!')
#creating an instance of the operator
python_op=PythonOperator(task_id='simple_script',
                         #calling python function
                         python_callable=printchris,
                         dag=example_dag
                         )


#Keywords arguments examples
import time
def sleep(length_time):
    time.sleep(length_time)
sleep_task=PythonOperator(task_id='sleep_task',
                          python_callable=sleep,
                          op_kwargs={'length_time':5},
                          dag=example_dag
                          )
print(sleep_task)


# write a python file that downloads and save a file to the system within Airflow.


def pull_file(URL, savepath):
    r = requests.get(URL)
    with open(savepath, 'wb') as f:
        f.write(r.content)   
    # Use the print method for logging
    print(f"File pulled from {URL} and saved to {savepath}")

from airflow.operators.python import PythonOperator

# Create the task
pull_file_task = PythonOperator(
    task_id='pull_file',
    # Add the callable
    python_callable=pull_file,
    # Define the arguments
    op_kwargs={'URL':'http://dataserver/sales.json', 'savepath':'latestsales.json'},
    dag=process_sales_dag
)

#continua
# Import the Operator
from airflow.operators.email_operator import EmailOperator

# Define the task
email_manager_task = EmailOperator(
    task_id='email_manager',
    to='manager@datacamp.com',
    subject='Latest sales JSON',
    html_content='Attached is the latest sales JSON file as requested.',
    files='parsedfile.json',
    dag=process_sales_dag
)

# Set the order of tasks
pull_file_task >> parse_file_task >>email_manager_task