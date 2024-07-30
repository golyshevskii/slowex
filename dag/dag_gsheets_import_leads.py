from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from scripts.manager import import_gsheets_leads

with DAG(
    dag_id="gsheets_import_leads",
    description="Imports leads from Google Sheets",
    tags=["gsheets", "leads", "analytics"],
    start_date=datetime(2024, 1, 1),
    schedule="0 0 * * *",
    catchup=True,
    max_active_runs=1,
    default_args={"owner": "Analytics", "depends_on_past": False, "retries": 1},
) as dag:
    import_leads = PythonOperator(
        task_id="import_leads",
        python_callable=import_gsheets_leads,
        op_kwargs={
            "from_dtt": "{{ data_interval_start.strftime('%Y-%m-%d %H:%M:%S') }}",
            "to_dtt": "{{ data_interval_end.strftime('%Y-%m-%d %H:%M:%S') }}",
        },
    )

    import_leads
