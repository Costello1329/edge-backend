from rest_framework.views import APIView

from main.response_processing import server_error_response, cors_response, not_found_response, get_success_response
from vacancy.models import Job


class UserView(APIView):
    def post(self, request):
        try:
            jobs = list(Job.objects.filter(verified=True))
            jobs.reverse()

            if "count" in request.data.values() is not None:
                jobs = jobs[0:int(request.data["count"])]

            data = []
            for job in jobs:
                data.append({
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
                    },
                    "contact": {
                        "email": job.contact.email,
                        "phone": job.contact.phone,
                        "telegram": job.contact.telegram
                    },
                })
            return get_success_response(data)
        except Exception as err:
            print(err)
            return server_error_response()

    def options(self, request, *args, **kwargs):
        return cors_response()
