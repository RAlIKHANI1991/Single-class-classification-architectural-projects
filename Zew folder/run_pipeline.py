# فایل موقت برای ران مدل و تست ها 

from workflows.pipeline_workflow import PipelineWorkflow

if __name__ == "__main__":

    workflow = PipelineWorkflow()

    result = workflow.run()

    print("\n========================")
    print("Pipeline Completed")
    print("========================")
    print(result)