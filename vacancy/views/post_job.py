import uuid

from django.core.mail import send_mail
from rest_framework.views import APIView
from django.core import serializers

from edge.settings import EMAIL_HOST_USER, CURRENT_HOST
from main.response_processing import server_error_response, cors_response, not_found_response, get_success_response
from vacancy.models import Job, Company, Location, Candidate, Offer, Salary, Contact


class UserView(APIView):

    def post(self, request):
        try:
            company = request.data["company"]
            candidate = request.data["candidate"]
            offer = request.data["offer"]
            contact = request.data["contact"]

            location = Location.objects.create(country=company['location']['country'], city=company['location']['city'])
            company = Company.objects.create(name=company['name'], industry=company['industry'],
                                             website=company['website'],
                                             location=location, remote=company['remote'])

            candidate = Candidate.objects.create(level=candidate['level'], skill=candidate['skill'],
                                                 stack=";".join(candidate['stack']))
            salary = Salary.objects.create(From=offer['salary']['from'], to=offer['salary']['to'])
            offer = Offer.objects.create(salary=salary, description=offer['description'])

            contact = Contact.objects.create(email=contact['email'], phone=contact['phone'],
                                             telegram=contact['telegram'])

            job = Job.objects.create(id=str(uuid.uuid4()), company=company, candidate=candidate, offer=offer,
                                     contact=contact)
            try:
                send_mail(
                    "В edge добавили вакансию;",
                    "Отмодерируйте ее, поставив verified: true, если все хорошо и запостите в канал. Иначе – удалите "
                    "вакансию из базы данных, после этого – попытайтесь связаться с рекрутером по указанному "
                    "email/tg/телефону и объясните причину отказа в публикации. Вот прямая ссылка на объект вакансии в "
                    "базе данных: http://{}/admin/vacancy/job/{}/change/".format(CURRENT_HOST, job.id),
                    EMAIL_HOST_USER,
                    [EMAIL_HOST_USER, "leladzek2000@mail.ru"],
                    fail_silently=False,
                )
            except Exception:
                pass
            return get_success_response({"status": "ok"})
        except Exception as err:
            print(err)
            return server_error_response()

    def options(self, request, *args, **kwargs):
        return cors_response()
