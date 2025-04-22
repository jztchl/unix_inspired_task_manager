from task.models import Task, StatusChoices
import asyncio
from asgiref.sync import sync_to_async
import logging
from django.utils import timezone
logger = logging.getLogger(__name__)

running_tasks = {}

async def run_task(task_id):
    try:
      
        task = await sync_to_async(Task.objects.get)(id=task_id)
    except Task.DoesNotExist:
        logger.error(f"Task with id {task_id} does not exist.")
        return None

    try:
        task.status = StatusChoices.RUNNING.value
        await sync_to_async(task.save)()
        logger.info(f"Task {task_id} status changed to running.")

        loop_task = asyncio.create_task(execute_task(task))
        running_tasks[task_id] = loop_task
        await loop_task
        if task.status!= StatusChoices.KILLED.value:
            task.status = StatusChoices.COMPLETED.value
            task.completed_at = timezone.now()
            await sync_to_async(task.save)()
            logger.info(f"Task {task_id} status changed to completed.")

    except Exception as e:
        task.status = StatusChoices.FAILED.value
        await sync_to_async(task.save)()
        logger.error(f"Task {task_id} failed with error: {e}")
        raise e

    finally:
        if task_id in running_tasks:
            del running_tasks[task_id]

    return task

async def execute_task(task):
    try:
        await asyncio.sleep(60)
    except asyncio.CancelledError:
        task.status = StatusChoices.KILLED.value
        await sync_to_async(task.save)()
        logger.info(f"Task {task.id} was killed.")
        return
