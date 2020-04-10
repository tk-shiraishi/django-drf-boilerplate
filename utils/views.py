from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class IsPaginationMixin:
    def list(self, request, *args, **kwargs):
        is_pagination = request.GET.get("pagination", True)
        if not is_pagination or is_pagination in ["False", "false"]:
            self.pagination_class = None

        return super().list(request, *args, **kwargs)


class BulkUpdateMixin:
    @action(methods=["PATCH"], detail=False)
    def bulk_update(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        for data in request.data:
            serializer = self.get_serializer(
                instance=queryset.get(pk=data.get("id")),
                data=data,
                many=False,
                partial=True,
            )
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
        return Response(serializer.data, status=HTTP_200_OK)
