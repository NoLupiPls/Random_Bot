import sqlite3

class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
    
    def user_exists(self, user_id):
        result = self.cursor.execute('SELECT id FROM users WHERE user_id = ?', (user_id,))
        return bool(len(result.fetchall()))
    
    def vol_exists(self, user_id, new_count):
        self.cursor.execute('UPDATE users SET count = ? WHERE users_id = ?', (new_count, self.get_user_id(user_id)))
        return self.conn.commit()
    