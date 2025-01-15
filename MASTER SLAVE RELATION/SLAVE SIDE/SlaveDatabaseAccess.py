import firebase_admin
from firebase_admin import credentials, storage, db
import json
import os
import codecs
from datetime import date

class SlaveDatabaseAccess():
    def __init__(self) -> None:
        self.scriptPath = str(os.path.dirname(os.path.realpath(__file__)))
        self.appInitialized = False
        self.acquireCredentials()

        self.ref = db.reference()

        pass

    def acquireCredentials(self):
        jsonKey = {
                    "type": "service_account",
                    "project_id": "masterslaverelation",
                    "private_key_id": "37509a0e07a311fb7652eadc337dbe7b52ba3956",
                    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDDN12x2zukZPFF\nQqDpkoB3wprZNyhQgSQLadxz25ir5MGlYVEsTOhkxsJGDzHGAfiSPLyO151c7Qa+\nb1LIfUR3OW9EqEH2CyIVYNm3bNipsdVInUHm8NDnl8SZUnUHjzPwgF9UkFhosRp0\nHo4mAiYwPRXjs3MzuJ/sVhjfPVKgkS+c2b/gTJOvOb3Dyz6ewYS5IOF9O2M4kpzr\nbgwshzDAS5yjKM1laNHVgFqI9cjXsjD9JnC3Z6VYGixTWJMv/Whk8j+LscARc5Dw\n3+gG84f8DdhagK/47Pb1ic1U8bRD1yQOOYjCcdviiIN6ZqC+B/k+DTIpeknxze/B\ndDbZiMmjAgMBAAECggEAJ5j77t8+5lY5YGim9inq2CAHw+a9zTKcypnjBzc0bS2e\nH/sw+XDyNLriXk6ntHfi4Vrjjn/q4hYMJ6WyH4vVTu++A6mzk4Jnm/mEwAGaozU4\nw51uaDdR0KBG1yjUJz/jc7W+YItU+4ttB7/I6qnF8EP7xC+6vvOEsO435lRshbgB\n+ZPPhwVKfO0xy//LDZAB6usve5NI/e3Rilv+6f6iMnwyQsBLnIb/uH3GdjAig9Ln\nzzBY+apY/cc4DaK8V2GwJ1r9hwaEBeEcTaEg6xnM+ycKD17fQN/GZ9bGZCRZGhMh\n6jEm5Lxh2RZ4MPx8NP62Yr8hViexYqQ/uSTmZelNmQKBgQD/J7/UnfDOmrK8ST0w\n5EMvedjSTYdR6D4OIbm2jOmvvbWhxI7QmEB72OBf7b9jx9cD3mxPWYjvGp9VR6e3\n2MJrqC7YRONlqHmBH5ojBLxpPirqzfcsVxQf6gwIEoceWh/LXxmhzRQY9aPCQGhG\n3iP+sbXeyCQRHkKdBi+US3Mi6wKBgQDD3NEaryNdRyRsEzedfR5alTxJBXTzJIrV\n8Ol9V6OppCYjGXr3XVOy9l3Fvr2i8mJQO/xh+bcHWbeLApYKh3Dq07cq4nk29X8W\n3HF2x7diH++OiLdCELFdxyv1yj6ni3IxXROdPieH1Y6U4w1R8NukejqmTqqC7EI5\nZAKF50gWKQKBgQD6QuqMiD1g56rXsp4qDjk3n7Ni0lgfpkL3aWzV+HBcxx4XhMrv\nHeZhkt7AOFi4bZIfYVGqoo8EtoABDT8bu6c2IMeRqD/BvfUvCOgN4N9L+oXtuAbv\nnplGlDEo2cNdqdf1iVmCsbs8n/H23WVp3QhBD9zqnjOB9sQvb5nLQhWz8QKBgQCs\nmXYn9rjKZXwiRVkYTv8lwidrDgT+k3BJklCgZU/TmdUFz1l+jV7J8bO3JByHcOPU\nYthJGr8BGj3VoYTJaIvIVKQwhX1eQj8pzT+r9dmT/iKkT7R24rD6vB7wLbbC/O63\ns5cqVXCOklJgwCmn0QIt0ozGq8I1N7AwVQKoL6Vl6QKBgQDupQdLkDSOFPiNASG4\nEXwLX3XKn2/zcUXHhCLMqrmoySK1tCqOKbOeqC+AAzG/cfPc+L8JKYtnXQ/tfClk\nqfqypmYXZxamSRXUpv5L6l+nbvI6zx0e4iWXG4cL4TjbmUMnp8XmjGG3Njewzg8S\n01igeQNZr7CjtPLFsaZaatM6Yw==\n-----END PRIVATE KEY-----\n",
                    "client_email": "firebase-adminsdk-qfnwi@masterslaverelation.iam.gserviceaccount.com",
                    "client_id": "114333881942578521363",
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-qfnwi%40masterslaverelation.iam.gserviceaccount.com",
                    "universe_domain": "googleapis.com"
                    }
        cred = credentials.Certificate(jsonKey)
        firebase_admin.initialize_app(cred, {'databaseURL': "https://masterslaverelation-default-rtdb.europe-west1.firebasedatabase.app/"})
        self.appInitialized = True
        pass