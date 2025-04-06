from prefect import flow

if __name__ == "__main__":
    
    flow.from_source(
        source="https://github.com/nguentamak/ml-workflow-orchestration-with-prefect-v2.git",
        entrypoint="main.py:ml_workflow",
    ).deploy(
        name="ml_workflow_bank_churn",
        work_pool_name="default-agent-pool",
        cron="0 * * * *",
    )