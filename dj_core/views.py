from random import randint

from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.generic import View

from dj_core.models import CustomUser
from main_fast_api import UserSch


class SyncDummyView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(data={"message": "SyncDummyView"})


class AsyncDummyView(View):
    async def get(self, request, *args, **kwargs):
        return JsonResponse(data={"message": "AsyncDummyView"})


@require_GET
async def async_dummy_foo(request, *args, **kwargs):
    return JsonResponse(data={"message": "async_dummy_foo"})


class SyncUserView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(
            data=CustomUser.objects.filter(id=randint(1, 1_000_001))
            .values("id", "username")
            .first()
        )


class AsyncUserView(View):
    async def get(self, request, *args, **kwargs):
        return JsonResponse(
            data=await CustomUser.objects.filter(id=randint(1, 1_000_001))
            .values("id", "username")
            .afirst()
        )
