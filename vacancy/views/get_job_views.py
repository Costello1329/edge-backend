import uuid

from rest_framework.views import APIView
from django.core import serializers

from main.response_processing import server_error_response, cors_response, not_found_response, get_success_response
from vacancy.models import Job


class UserView(APIView):

    def get(self, request):
        try:
            id_ = request.query_params.get('id')

            job = Job.objects.filter(id=id_)

            if not job:
                return not_found_response()

            job = job[0]

            data = {
                "id": job.id,
                "premium": job.premium,
                "company": {
                    "name": job.company.name,
                    "industry": job.company.industry,
                    "website": job.company.website,
                    "location": {
                        "country": job.company.location.country,
                        "city": job.company.location.city
                    },
                    "remote": job.company.remote,
                },
                "candidate": {
                    "level": job.candidate.level,
                    "skill": job.candidate.skill,
                    "stack": job.candidate.stack.split(';')
                },
                "offer": {
                    "salary": {
                        "from": job.offer.salary.From,
                        "to": job.offer.salary.to
                    },
                    "description": job.offer.description
                },
                "contact": {
                    "email": job.contact.email,
                    "phone": job.contact.phone,
                    "telegram": job.contact.telegram
                },
            }
            return get_success_response(data)
        except Exception as err:
            print(err)
            return server_error_response()

    def options(self, request, *args, **kwargs):
        return cors_response()
