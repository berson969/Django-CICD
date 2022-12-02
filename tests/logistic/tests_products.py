from rest_framework.test import APIClient, APITestCase


class TestAPIView(APITestCase):
    def test_sample_view(self):
        client = APIClient()
        response = client.get('/api/v1/products/')
        self.assertEqual(response.status_code, 200)
