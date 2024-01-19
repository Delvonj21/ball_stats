from flask_app.config.mysqlconnection import connectToMySQL





class Stat:
  DB = "ball_stats"
  def __init__(self, data):
    self.id = data['id']
    self.points = data['points']
    self.assists = data['assists']
    self.rebounds = data['rebounds']
    self.date = data['date']
    self.created_at = data['created_at']
    self.updated_at = data['update_at']

  
  
