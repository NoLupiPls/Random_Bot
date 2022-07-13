import sqlite3

class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
    
    def user_exists(self, user_id):
        result = self.cursor.execute('SELECT id FROM users WHERE user_id = ?', (user_id,))
        return bool(len(result.fetchall()))
    
    def vol_exists(self, user_id, count_vol):
        self.cursor.execute('UPDATE users SET count_vol = ? WHERE users_id = ?', (count_vol, user_id,))
        return self.conn.commit()
    
    
    def add_user(self, user_id, count_vol):
        self.cursor.execute('INSERT INTO users (user_id, count_vol) VALUES (?, ?)', (user_id, count_vol,))
        return self.conn.commit()
    '''
    def get_user_id(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id, ))
        return result.fetchone()[0]
    '''
    def close(self):
        self.connection.close()