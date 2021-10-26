class Board(object):
    def __init__(self, id, title, context, writer, regdate, fixdate):
        self.id = id
        self.title = title
        self.context = context
        self.writer = writer
        self.regdate = regdate
        self.fixdate = fixdate

    def json(self):
        return {'id': self.id, 'title':self.title, 'context':self.context, 'writer':self.writer, 'regdate': self.regdate, 'fixdate': self.fixdate}