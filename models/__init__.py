import json
import os
from url import get_key


def save(data):
    s = json.dumps(data, indent=2, ensure_ascii=False)
    dirs = os.path.dirname(os.path.dirname(__file__))
    path = 'data/url.txt'
    path = os.path.join(dirs, path)
    with open(path, 'w+', encoding='utf-8') as f:
        # log('save', path, s, data)
        f.write(s)


def load():
    dirs = os.path.dirname(os.path.dirname(__file__))
    path = 'data/url.txt'
    path = os.path.join(dirs, path)
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        # log('load', s)
        if len(s):
            return json.loads(s)
        else:
            return []


class Shorturl(object):
    key = get_key()
    def __init__(self, url=''):
        self .id =0
        self.ori_url = url
        self.short_url = ''


    @classmethod
    def url_10to64(cls,n):
        d = []
        while (n):
            s = n % 64
            d.append(s)
            n = n // 64
        d = d[::-1]
        for i in range(0, len(d)):
            d[i] =cls. key[d[i]]
        return ''.join(d)


    @classmethod
    def get_id(cls):
        urls = cls.all()
        if urls == []:
            return 1
        else:
            return len(urls)+1


    def set_parm(self):
        self.id = self.get_id()
        self.short_url =self.url_10to64(self.id)

    @classmethod
    def set_dict_new(cls, form: dict):
        url = Shorturl()
        for k, v in form.items():
            setattr(url, k, v)
        return url


    @classmethod
    def all(cls):
        data = load()
        urls = [cls.set_dict_new(i) for i in data]
        return urls

    def __repr__(self):
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return s


    def save(self):
        urls = self.all()
        self.set_parm()
        urls.append(self)
        data = [url.__dict__ for url in urls]
        save(data)


    @classmethod
    def find_by(cls, **kwargs):
        urls = cls.all()
        k, v = '', ''
        for key, value in kwargs.items():
            k, v = key, value
        for i in urls:
            if i.__dict__[k] == v:
                return i
        return None


def test():
    a = Shorturl("first")
    b = Shorturl("second")
    c = Shorturl("three")
    a.save()
    b.save()
    # c.save()
    print(load())
    print(Shorturl.find_by('second'))


if __name__ == "__main__":
    test()
