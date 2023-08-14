from database.models import User
from datetime import datetime

from database import get_db

# User Registration
def register_user_db(name, email, phone_number, user_city, password):
    db = next(get_db())
    new_user = User(name=name, email=email, phone_number=phone_number,
                    password=password, user_city=user_city, reg_date=datetime.now())
    # Add to db
    db.add(new_user)
    db.commit()
    return new_user.id

# User check on avaability
def check_user_data_db(phone_number, email):
    db = next(get_db())
    # Check user data from db
    checker = db.query(User).filter_by(phone_number=phone_number, email=email).first()
    #If find in DB
    if checker:
        return False
    # in not in DB
    return True
# Check User password in sign in
def check_user_password_db(email, password):
    db = next(get_db())
    # Try to find user
    checker = db.query(User).filter_by(email=email).first()
    # If email exist
    if checker:
        #begin check password
        if checker.password ==password:
            return checker.id
        else:
            return 'Неверный пароль'
    # If email not exist
    return 'Неверная почта'

# get User profile info
def profile_info_db(user_id):
    db = next(get_db())
    # Find user by id
    exact_user = db.query(User).filter_by(id=user_id).first()
    # if find User, send his info
    if exact_user:
        return exact_user.email, exact_user.phone_number, exact_user.id, exact_user.name, exact_user.reg_date, exact_user.user_city
    return 'User not found'

# Change user info
def change_user_data(user_id, change_info, new_data):
    db = next(get_db())
    # Find user in db
    exact_user = db.query(User).filter_by(id=user_id).first()
    # If user exist
    if exact_user:
    # Check what user want to change
        if change_info == 'email':
            exact_user.email = new_data
        elif change_info == 'number':
            exact_user.phone_number = new_data
        elif change_info == 'name':
            exact_user.name = new_data
        elif change_info == 'city':
            exact_user.user_city = new_data
        elif change_info == 'password':
            exact_user.password = new_data
        db.commit()
        return "Данные успешно изменены"
    return 'Пользователь не найден'
