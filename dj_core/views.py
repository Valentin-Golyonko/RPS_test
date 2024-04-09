from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.generic import View


class SyncDummyView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(data={"message": "SyncDummyView"})


class AsyncDummyView(View):
    async def get(self, request, *args, **kwargs):
        return JsonResponse(data={"message": "AsyncDummyView"})


@require_GET
async def async_dummy_foo(request, *args, **kwargs):
    return JsonResponse(data={"message": "async_dummy_foo"})
