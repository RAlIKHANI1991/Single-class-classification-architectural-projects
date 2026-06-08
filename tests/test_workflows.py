# tests/test_workflows.py

from workflows.pipeline_workflow import PipelineWorkflow


def test_workflow_creation():
    workflow = (PipelineWorkflow())

    assert workflow is not None