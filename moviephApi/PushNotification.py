from models import Token
from pyfcm import FCMNotification


def sendNotification(title, url, image):
    api_key = 'AAAAdo4nMxg:APA91bG2UeEvBgLPSuNQPq7FRNOoezcqwfgYdnnL9g7HpxUAfxI6DkQEdg9OkRQE-xB-zfyl8z9jSFjKDH4a6nnAek9A0KozJWoOs0yGJvOduxGNDZxL4jNKk-EdhXS5Mxr2uSKjmDTG'
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