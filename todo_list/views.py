import json
import uuid

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

TASKS = [
    {
        "id": 1,
        "title": "Wash the dishes"
    },
    {
        "id": 42,
        "title": "Find the final answer"
    },
]


@csrf_exempt
def tasks_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        task = {
            "id": uuid.uuid4(),
            "title": data.get("title"),
        }
        return JsonResponse(task, status=201)

    return JsonResponse(TASKS, safe=False, status=200)


@csrf_exempt
def task_view(request, pk):
    if pk not in [task['id'] for task in TASKS]:
        return 404

    if request.method == "DELETE":
        return HttpResponse(status=204)

    return JsonResponse(TASKS[0])
