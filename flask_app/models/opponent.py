from flask_app.config.mysqlconnection import connectToMySQL



class Opponent:
  DB = "ball_stats"
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']


  @classmethod
  def get_all(cls):
      query = "SELECT * FROM opponents;"

      results = connectToMySQL(cls.DB).query_db(query)
      opponents = []

      for o in results:
        opponents.append( cls(o) )
      return opponents
  
  @classmethod
  def save(cls, data):
     query = "INSERT INTO opponents (name, user_id) VALUES (%(name)s, %(user_id)s);"
     result = connectToMySQL(cls.DB).query_db(query, data)
     return result