from domain.common.enum import BaseEnum


class UserBusinessRulesConsts(BaseEnum):
    MIN_EMAIL_LEN = 5
    MAX_EMAIL_LEN = 254
    MIN_NAME_LEN = 2
    MAX_NAME_LEN = 20
    MIN_SURNAME_LEN = 2
    MAX_SURNAME_LEN = 20
    MIN_LASTNAME_LEN = 2
    MAX_LASTNAME_LEN = 20
    MIN_PASSWORD_LEN = 10
    MAX_PASSWORD_LEN = 128