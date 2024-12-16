from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Crop
from .serializers import CropSerializer, CropPriceConversionSerializer
from .permission import IsAdminUserOrReadOnly

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    @action(detail=True, methods=['GET'])
    def convert_price(self, request, pk=None):
        crop = self.get_object()
        unit = request.query_params.get('unit', 'kg')
        
        serializer = CropPriceConversionSerializer(crop, context={'unit': unit})
        return Response(serializer.data)

    @action(detail=False, methods=['DELETE'])
    def bulk_delete(self, request):
        crop_ids = request.data.get('ids', [])
        Crop.objects.filter(id__in=crop_ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['PUT'])
    def bulk_update(self, request):
        crop_updates = request.data
        updated_crops = []

        for crop_data in crop_updates:
            crop_id = crop_data.get('id')
            try:
                crop = Crop.objects.get(id=crop_id)
                serializer = self.get_serializer(crop, data=crop_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    updated_crops.append(serializer.data)
            except Crop.DoesNotExist:
                continue

        return Response(updated_crops)