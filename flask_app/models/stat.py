from flask_app.config.mysqlconnection import connectToMySQL
from flask import session

class Stat:
    DB = "ball_stats"
  
    def __init__(self, data):
        self.id = data['id']
        self.points = data['points']
        self.assists = data['assists']
        self.rebounds = data['rebounds']
        self.date = data['date']
        self.opponent = data['opponent']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    

    
    @classmethod
    def get_by_id(cls, stat_id):
        query = "SELECT * FROM stats LEFT JOIN users ON stats.user_id = users.id WHERE stats.id = %(id)s"
        result = connectToMySQL(cls.DB).query_db(query, {"id": stat_id})
        if result:
            return cls(result[0]) 
        return None
    
     

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM stats"
        results = connectToMySQL(cls.DB).query_db(query)
        stats = []

        for s in results:
            stats.append( cls(s) )
        return stats 
    
    
        

    @classmethod
    def add_stat(cls, data):

        query = "INSERT INTO stats (points, assists, rebounds, opponent, date, user_id) VALUES (%(points)s, %(assists)s, %(rebounds)s, %(opponent)s, %(date)s, %(user_id)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
        

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM stats WHERE stats.id = %(id)s"
        return connectToMySQL(cls.DB).query_db(query, {"id": id})

    @classmethod
    def update(cls, stat):
        query = "UPDATE stats SET points=%(points)s, assists=%(assists)s, rebounds=%(rebounds)s, opponent=%(opponent)s, date=%(date)s WHERE id = %(id)s"
        return connectToMySQL(cls.DB).query_db(query, stat) 
    
    @classmethod
    def get_stats_for_user(cls, user_id):
        query = "SELECT * FROM stats WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, {'user_id': user_id})
        stats = []
        for row in results:
            stats.append(cls(row))
        return stats
