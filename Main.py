# maximisation des profit pour 500€ d'investissement sur 2 ans.
# - chaque action ne peut être utilisé qu'une seul fois
# - que des action complete (pas de fraction d'action)


from Controllers.base import Controller
from Views.base import View


def main():
    view = View()
    logiciel = Controller(view)
    logiciel.run()


if __name__ == "__main__":
    main()
