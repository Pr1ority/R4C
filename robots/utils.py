from datetime import timedelta
from io import BytesIO

from django.db.models import Count
from django.utils import timezone
import openpyxl
from openpyxl.styles import Font

from .models import Robot


def get_weekly_summary():
    """
    Возвращает данные о роботах за последнюю неделю.

    Группировка по модели и версии.
    """
    week_ago = timezone.now() - timedelta(days=7)
    summary = (
        Robot.objects
        .filter(created__gte=week_ago)
        .values('model', 'version')
        .annotate(count=Count('id'))
        .order_by('model', 'version')
    )
    return summary


def generate_excel_file(summary):
    """
    Генерирует Excel-файл со сводкой по роботам.

    Каждый лист представляет собой одну модель робота.
    """
    workbook = openpyxl.Workbook()

    data_by_model = {}
    for entry in summary:
        model = entry['model']
        if model not in data_by_model:
            data_by_model[model] = []
        data_by_model[model].append(entry)

    first_model = True

    for model, data in data_by_model.items():
        if first_model:
            sheet = workbook.active
            sheet.title = model
            first_model = False
        else:
            sheet = workbook.create_sheet(title=model)
        sheet.append(['Модель', 'Версия', 'Количество'])
        header_font = Font(bold=True)
        for cell in sheet[1]:
            cell.font = header_font

        for entry in data:
            sheet.append([entry['model'], entry['version'], entry['count']])

    output = BytesIO()
    workbook.save(output)
    output.seek(0)
    return output
