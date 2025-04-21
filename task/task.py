import asyncio
from django.utils import timezone
from asgiref.sync import sync_to_async
from task.models import Task, StatusChoices

async def run_task(task_id):
    try:
        task = await sync_to_async(Task.objects.get)(id=task_id)
    except Task.DoesNotExist:
        return None

    try:
        task.status = StatusChoices.RUNNING.value
        await sync_to_async(task.save)()
        
        await asyncio.sleep(10)
        
        task.status = StatusChoices.COMPLETED.value
        task.completed_at = timezone.now()
        await sync_to_async(task.save)()
    except Exception as e:
        task.status = StatusChoices.FAILED.value
        await sync_to_async(task.save)()
        raise e

    return task
