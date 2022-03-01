# broken

from extension import db


class Stat(db.Model):
    """
    Track user stats such as # of users, match-ups, success rate.

    Should only have 1 record.
    """
    id = db.Column(db.Integer(), primary_key=True)
    num_page_hits = db.Column(db.Integer())
    num_match_ups = db.Column(db.Integer())
    num_success = db.Column(db.Integer())
    num_failure = db.Column(db.Integer())
    last_used_time = db.Column(db.TIMESTAMP(timezone=True), nullable=False)


class Match(db.Model):
    """
    Store current matches to track if a user is correct.
    """
    id = db.Column(db.Integer(), primary_key=True)
    # leader A
    # leader A picture
    # people A

    # leader B
    # leader B picture
    # people B

    # Date
    # location

    # given? - used to track ready-to-go vs given to player
