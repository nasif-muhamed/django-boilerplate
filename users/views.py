import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .serializers import RegiserUserSerializer
from .docs_schemas import doc_register_schema

logger = logging.getLogger(__name__)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @doc_register_schema()
    def post(self, request):
        logger.debug(f'inside RegisterView {request.data}')
        serializer = RegiserUserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
