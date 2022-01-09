from werkzeug.security import safe_str_cmp
from starter_code.models.user import UserModel

def authenticate(username, password):
    """
    Functie dat wordt opgeroepen wanneer gebruiker de /auth endpoint
    oproept met zijn username en wachtwoord
    :param username: Gebruikers usernaam in string
    :param password: Gebruikers wachtwoord in niet-geencrypteerde string
    :return: Een UserModel object als authenticatie voltooid is, anders niets
    """

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    """
    Functie dat opgeroepen wordt wanneer een gebruiker al de authenticatie heeft voltooid,
    en Flask-JWT geverifieerd heeft dat de authorizatie header correct is.
    :param payload: Een dic met 'identity' key, dat de user id is.
    :return: Een UserModel object
    """
    user_id = payload('identity')
    return UserModel.find_by_id(user_id)