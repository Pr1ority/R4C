from django.http import HttpResponse

from .utils import generate_excel_file, get_weekly_summary


def download_weekly_summary(request):
    summary = get_weekly_summary()

    excel_file = generate_excel_file(summary)

    response = HttpResponse(
        excel_file.getvalue(),
        content_type='application/'
                     'vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = ('attachment;'
                                       'filename="weekly_robot_summary.xlsx"')
    return response