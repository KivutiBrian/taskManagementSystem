from app import db

class TaskModel(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    createdDate = db.Column(db.String(45), nullable=False)
    startDate = db.Column(db.String(45), nullable=False)
    endDate = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(45), nullable=False)

    def create_task(self):
        db.session.add(self)
        db.session.commit()

    # fetch all records
    @classmethod
    def fetch_records(cls):
        records = TaskModel.query.all()
        return records

    # update record
    @classmethod
    def update_by_id(cls,id,newTitle,newDescription,newCreatedDate,newStartDate,newEndDate,newStatus):
        record = TaskModel.query.filter_by(id=id).first()
        if record:
            record.title = newTitle
            record.description = newDescription
            record.createdDate = newCreatedDate
            record.startDate = newStartDate
            record.endDate = newEndDate
            record.status = newStatus
            db.session.commit()
            return True
        else:
            return False

    # delete record
    @classmethod
    def delete_by_id(cls,id):
        task = TaskModel.query.filter_by(id=id)
        if task.first():
            task.delete()
            db.session.commit()
            return True
        else:
            return False
