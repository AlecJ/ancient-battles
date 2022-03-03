from src.model import db
import enum


class Result(enum.Enum):
    a = "A"
    b = "B"


class Battle(db.Model):
    __tablename__ = 'battles'

    id = db.Column(db.Integer(), primary_key=True)
    battleName = db.Column(db.String(100), nullable=False, unique=True)
    date = db.Column(db.String(100), nullable=False,)
    location = db.Column(db.String(100), nullable=False,)
    answer = db.Column(db.Enum(Result), nullable=False,)
    belligerentA = db.Column(db.String(100), nullable=False,)
    belligerentB = db.Column(db.String(100), nullable=False,)
    leaderAName = db.Column(db.String(100), nullable=False,)
    leaderBName = db.Column(db.String(100), nullable=False,)
    leaderAImageLink = db.Column(db.String(100), nullable=False,)
    leaderBImageLink = db.Column(db.String(100), nullable=False,)
    wikipediaBlurb = db.Column(db.String(450))
    wikipediaLink = db.Column(db.String(100))

    created_time = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    last_read_time = db.Column(db.TIMESTAMP(timezone=True), nullable=False)

    def row_as_dict(self):
        return {
            "id": self.id,
            "battleName": self.battleName,
            "date": self.date,
            "location": self.location,
            "answer": self.answer,
            "belligerentA": self.belligerentA,
            "belligerentB": self.belligerentB,
            "leaderAName": self.leaderAName,
            "leaderBName": self.leaderBName,
            "leaderAImageLink": self.leaderAImageLink,
            "leaderBImageLink": self.leaderBImageLink,
            "wikipediaBlurb": self.wikipediaBlurb,
            "wikipediaLink": self.wikipediaLink,
        }

    def __repr__(self):
        return "Battle(id={}, battleName={}, created_time={})".format(self.id, self.battleName, self.created_time)


class Statistic(db.Model):
    """
    Track user stats such as # of users, match-ups, success rate.

    Should only have 1 record.
    """
    id = db.Column(db.Integer(), primary_key=True)
    num_page_hits = db.Column(db.Integer())
    num_battles = db.Column(db.Integer())
    num_success = db.Column(db.Integer())
    num_failure = db.Column(db.Integer())
    last_used_time = db.Column(db.TIMESTAMP(timezone=True), nullable=False)