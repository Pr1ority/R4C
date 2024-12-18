import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Robot


@csrf_exempt
def add_robot(request):
    """
    Добавляет робота в базу данных.

    Обрабатывает POST-запрос с JSON-данными и сохраняет их в базу.
    Возвращает JSON-ответ с результатом операции.
    """
    if request.method != 'POST':
        return JsonResponse(
            {'ошибка': 'Некорректный метод запроса. Используйте метод POST.'},
            status=405
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {'ошибка': 'Недопустимые JSON данные.'}, status=400
        )

    required_fields = ['model', 'version', 'created']
    if not all(field in data for field in required_fields):
        return JsonResponse(
            {'ошибка': 'Отсутствуют необходимые поля.'}, status=400
        )

    model = data['model']
    version = data['version']
    created = data['created']

    if len(model) != 2 or len(version) != 2:
        return JsonResponse(
            {'ошибка': 'Модель и версия должны содержать только 2 символа'},
            status=400
        )

    from django.utils.dateparse import parse_datetime
    created_date = parse_datetime(created)
    if not created_date:
        return JsonResponse(
            {'ошибка': 'Поле created должно быть в формате даты и времени'},
            status=400
        )

    try:
        robot = Robot.objects.create(
            model=model, version=version, created=created
        )
        return JsonResponse(
            {'сообщение': 'Робот успешно добавлен.', 'id': robot.id},
            status=201
        )
    except Exception as e:
        return JsonResponse(
            {'ошибка': f'Не удалось добавить робота: {str(e)}'}, status=500
        )
