from dagster import Definitions
from dagster_dbt import DbtCliResource
from pathlib import Path
from .project import buy_box_gcp_1_project
from .dags.setup_seed import dbt_seed_pipeline
from .dags.aggregation import aggregation_job, bigquery_client_resource
from .assets import buy_box_gcp_1_dbt_assets
from .schedules import schedules


# Initialize DBT CLI Resource
# dbt_resource = DbtCliResource(
#     project_dir=str(buy_box_gcp_1_project.project_dir),
#     profiles_dir=str(Path(buy_box_gcp_1_project.project_dir)),  
# )

dbt_resource = DbtCliResource(
    project_dir=str(Path("/app/buy_box_gcp_1")), 
    profiles_dir=str(Path("/app/buy_box_gcp_1")), 
)
# Create Definitions object
defs = Definitions(
    assets=[buy_box_gcp_1_dbt_assets],
    jobs=[dbt_seed_pipeline, aggregation_job], 
    schedules=schedules,
    resources={
        "dbt": dbt_resource,
    },
)
