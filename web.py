from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
)
from models import Shorturl

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route('/index')
def get_index():
    return render_template('index.html')


@app.route('/back', methods=['get'])
def get_back():
    return render_template('back.html')


@app.route('/short', methods=['POST'])
def url_short():
    url = request.form.get('ori_url', '')
    short_url = Shorturl(url)
    short_url.save()
    s_url = request.host + '/sh/' + short_url.short_url
    return render_template('index.html', value=s_url)


@app.route('/sh/<surl>/', methods=['get'])
def url_trans(surl):
    url = Shorturl.find_by(short_url=surl)
    if url:
        if url.ori_url.startswith('http://') or url.ori_url.startswith('https://'):
            return redirect(url.ori_url, 302)
        else:
            return redirect('http://'+url.ori_url,302)
    else:
        return redirect(url_for("/index"))


@app.route('/back', methods=['post'])
def url_back():
    short_url = request.form.get('short_url', '')
    new = short_url.split('/')[-1]
    url = Shorturl.find_by(short_url=new)
    if url:
        return render_template('back.html', value=url.ori_url)
    else:
        return redirect('/back')


if __name__ == '__main__':
    config = dict(
        host='0.0.0.0',
        port=80,
    )
    app.run(**config)
