from airflow.models import DAG
from airflow.operators.email import EmailOperator
from datetime import datetime
example_dag=DAG(dag_id='example',
                start_date=datetime(2021,1,1),
                schedule_interval='0 0 * * *'
                )
#creating an email operator
email_ops=EmailOperator(task_id='email_System_Update',
                        to='christophernyaga@gmail.com',
                        subject='SmartSignDoctor System',
                        html_content='<h3>System is up and running</h3>',
                        #previously generated file which we are sending
                        files=['/home/Documents/SmartSignDoctor/example.py'],
                        dag=example_dag
                        )

print(email_ops)