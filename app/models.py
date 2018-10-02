from app import db


class BucketList(db.Model):
    """ Represents the bucketlist table"""

    __tablename__ = "bucket_lists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_time_stamp())
    date_updated = db.Column(db.DateTime, default=db.func.current_time_stamp(),
    onupdate=db.func.current_time_stamp()
    )

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return BucketList.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return "<Bucketlist: {}>".format(self.name)
