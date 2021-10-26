class Board(object):
    def __init__(self, id, title, context, writer, regdate, hit):
        self.id = id
        self.title = title
        self.context = context
        self.writer = writer
        self.regdate = regdate
        self.hit = hit

    def json(self):
        return {'id': self.id, 'title':self.title, 'context':self.context, 'writer':self.writer, 'regdate': self.regdate, 'hit': self.hit}

    def json2(self):
        return {'id': self.id, 'title': self.title, 'writer': self.writer, 'regdate': self.regdate, 'hit': self.hit}
