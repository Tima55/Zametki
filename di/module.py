from domain.interactor.interactor import Interactor
from data.repository import Repository
from presentation.presenter.presenter import Presenter
from presentation.view.i_view import iView


def provide_interactor() -> Interactor:
    return Interactor(repository=Repository(filename="db.json"))


def provide_presenter(view: iView) -> Presenter:
    return Presenter(interactor=provide_interactor(), view=view)