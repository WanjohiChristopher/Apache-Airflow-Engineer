# https://academy.astronomer.io/astronomer-certification-apache-airflow-fundamentals-preparation/731426

waiting_for_data=FileSensor(task_id="waiting_for_data",fs_conn_id="fs_default",filepath="my_file.txt")


