import json
import requests
from app.settings import FIREBASE_WEB_API_KEY
from app.models.user import User, UserCreate, UserUpdate, UserIn, UserUpdateIn, UserLogin
from firebase_admin import auth
from app.daos.user import UserDAO


class AuthenticationService:
    SIGNIN_URL = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword'
    EMAIL_VERIFICATION_URL = 'https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode'

    def __init__(self):
        self.user_dao = UserDAO()
        # self.get_current_user = FirebaseCurrentUser()

    def register_user(self, user_data: UserIn) -> User:
        # create user with firebase auth
        user = auth.create_user(
            email=user_data.email,
            password=user_data.password,
            display_name=user_data.name
        )
        # add user with uid to firestore
        return self.user_dao.create(UserCreate(id=user.uid, **user_data.dict()))

    def update_user(self, user_update: UserUpdateIn) -> User:
        user = auth.update_user(
            user_update.id,
            email=user_update.email,
            password=user_update.password,
            display_name=user_update.name
        )
        user_data = UserUpdate(**user_update.dict(exclude={'id'}))
        # update in db
        return self.user_dao.update(user.uid, user_data)

    def delete_user(self, id: str):
        auth.delete_user(id)
        self.user_dao.delete(id)

    def authenticate_user(self, user_login: UserLogin):
        payload = json.dumps({
            "email": user_login.email,
            "password": user_login.password,
            "returnSecureToken": user_login.return_secure_token
        })
        r = requests.post(self.SIGNIN_URL,
                          params={"key": FIREBASE_WEB_API_KEY},
                          data=payload)

        return r.json()

    def send_email_verification(self, id_token: str):
        payload = json.dumps({
            "requestType": "VERIFY_EMAIL",
            "idToken": id_token
        })

        r = requests.post(self.EMAIL_VERIFICATION_URL,
                          params={"key": FIREBASE_WEB_API_KEY},
                          data=payload)

        return r.json()
