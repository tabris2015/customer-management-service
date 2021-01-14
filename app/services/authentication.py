from app.models.user import User, UserCreate, UserUpdate, UserIn, UserUpdateIn
from firebase_admin import auth
from fastapi_cloudauth.firebase import FirebaseCurrentUser, FirebaseClaims
from app.daos.user import UserDAO


class AuthenticationService:
    def __init__(self):
        self.user_dao = UserDAO()

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
        # user_update_firebase = {}
        # user_data = user_update.dict()
        # user_update_firebase['email'] = user_data.get('email', None)
        # user_update_firebase['password'] = user_data.get('password', None)
        # user_update_firebase['display_name'] = user_data.get('name', None)
        user = auth.update_user(
            user_update.id,
            email=user_update.email,
            password=user_update.password,
            display_name=user_update.name
        )
        user_data = UserUpdate(**user_update.dict(exclude={'id'}))
        # update in db
        return self.user_dao.update(user_update.id, user_data)


    def delete_user(self):
        pass

    def authenticate_user(self):
        pass

    def get_current_user(self):
        pass

    def get_tokens(self):
        pass
