import bcrypt


class Password:
    def hash_pass(self, password):
        return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())

    def check_pass(self, password, hash):
        if not password or not hash:
            return "no password provided"
        if bcrypt.checkpw(password.encode("utf-8"), hash.encode("utf-8")):
            return password
        else:
            return "password not matched"
