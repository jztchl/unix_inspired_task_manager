import asyncio
from django.utils import timezone
from asgiref.sync import sync_to_async
from task.models import Task, StatusChoices
import logging

logger = logging.getLogger(__name__)

async def run_task(task_id):
    try:
        task = await sync_to_async(Task.objects.get)(id=task_id)
    except Task.DoesNotExist:
        logger.error(f"Task with id {task_id} does not exist.")
        return None

    try:
        task.status = StatusChoices.RUNNING.value
        await sync_to_async(task.save)()
        logger.info(f"Task {task_id} status changed to  running.")
        
        await asyncio.sleep(10)
        
        task.status = StatusChoices.COMPLETED.value
        task.completed_at = timezone.now()
        await sync_to_async(task.save)()
        logger.info(f"Task {task_id} status changed to completed.")
        
    except Exception as e:
        task.status = StatusChoices.FAILED.value
        logger.error(f"Task {task_id} failed with error: {e}")
        await sync_to_async(task.save)()
        raise e

    return task
