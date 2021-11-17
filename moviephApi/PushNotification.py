from .models import Token
from pyfcm import FCMNotification
import os


def sendNotification(title, url, image):
    api_key = os.environ.get("FCM_SECRET")
    tokens = []
    query_token = Token.objects.all()
    data_message = {
        "title": title,
        "url": url,
        "image": image
    }

    for query in query_token:
        tokens.append(query.token)

    push_service = FCMNotification(api_key=api_key)
    push_service.notify_multiple_devices(
        registration_ids=tokens,
        data_message=data_message)