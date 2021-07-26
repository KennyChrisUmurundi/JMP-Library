from library.models import Library


def get_hostname(request):
    return request.get_host().split(":")[0].lower()


def get_library(request):

    hostname = get_hostname(request)
    subdomain = hostname.split(".")[0]
    return Library.objects.filter(subdomain=subdomain).first()
