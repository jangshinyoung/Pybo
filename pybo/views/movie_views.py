from flask import Blueprint,render_template,request
from pybo.movieapi import Mrank
from pybo.naverapi import Movieinfo
from ..forms import MovieInfoForm

bp = Blueprint('movie',__name__,url_prefix='/movie')

@bp.route('/rank/')
def MovieRank():
    rankdata = Mrank()

    return render_template('movie/movierank.html',ranklist=rankdata)

@bp.route('/info/', methods=('GET','POST'))
def MovieInfo():

    form = MovieInfoForm()

    if request.method == "POST" and form.validate_on_submit():
        result = Movieinfo(form.search.data)
        return render_template('movie/movieinfo.html', infolist=result['items'], form=form)

    return render_template('movie/movieinfo.html', form=form)