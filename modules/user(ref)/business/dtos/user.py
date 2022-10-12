"""user models"""
import re
from typing import Optional
from xml.dom import ValidationErr

from odmantic import Model
from pydantic import validator


class User(Model):
    """_summary_

    Args:
        Model (_type_): _description_

    Raises:
        ValidationErr: _description_

    Returns:
        _type_: _description_
    """

    firstname: str
    lastname: str
    email: str
    password: str
    role: Optional[str] = None

    @validator("email")
    def email_str(cls, email):
        """_summary_

        Args:
            email (_type_): _description_

        Raises:
            ValidationErr: _description_

        Returns:
            _type_: _description_
        """
        regex: str = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        com = re.compile(regex)
        if re.fullmatch(com, email):
            return email
        else:
            raise ValidationErr("email not valid")

    @validator("password")
    def password_str(cls, password):
        """_summary_

        Args:
            password (_type_): _description_

        Returns:
            _type_: _description_
        """
        regex: str = (
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        )
        com = re.compile(regex)
        if re.fullmatch(com, password):
            return password
        else:
            return password

    # @validator('role')
    # def role_str(cls,role):
    #     if type(role)==object:
    #         return role
    #     else:
    #         raise ValidationErr("role should be role object")
