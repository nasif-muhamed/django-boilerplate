from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse
from .serializers import RegiserUserSerializer


def doc_register_schema():
    return extend_schema(
        summary="Register a new user",
        request=RegiserUserSerializer,
        examples=[
            OpenApiExample(
                name="Valid Registration Request",
                description="Example data for registering a new user",
                value={
                    "username": "test_user",
                    "email": "test@example.com",
                    "password": "TestPass123!"
                },
                request_only=True
            )
        ],
        responses={
            201: OpenApiResponse(description="User registered successfully"),
            400: OpenApiResponse(description="Bad request (validation errors)")
        }
    )
