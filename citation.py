# -*- coding: utf-8 -*-
# \file citation.py
# \brief gdesklets-citation it's a fun deskltes with all quotes in french
# \author Jonathan MERCIER
# \version 2.1
# \date 03 July 2012
#
#  LICENSE:
#  gdesklets-citation it's a fun deskltes with all quotes in french
#  Copyright (C) <2009-2012>  <MERCIER Jonathan>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

class MyDate(object):

    def __init__(self, time_array ):
        self.__heure    = time_array[0]
        self.__minute   = time_array[1]
        self.__seconde  = time_array[2]
        self.__initialize()

    def __initialize(self):
        self.ajouteHeure(0)
        self.ajouteMinute(0)
        self.ajouteSeconde(0)

    def getHeure( self ):
        return self.__heure

    def setHeure( self, heure ):
        self.__heure = heure

    def ajouteHeure( self, ajout_heure ):
        self.__heure += ajout_heure
        while( self.__heure >= 24):
            self.__heure -= 24

    def getMinute( self ):
        return self.__minute

    def setMinute( self, minute ):
        self.__minute = minute

    def ajouteMinute( self, ajout_minute ):
        self.__minute += ajout_minute
        while( self.__minute >= 60 ):
            self.__minute -= 60
            self.ajouteHeure( 1 )

    def getSeconde( self ):
        return self.__seconde

    def setSeconde( self, seconde ):
        self.__seconde = seconde

    def ajouteSeconde( self, ajout_seconde ):
        self.__seconde += ajout_seconde
        while( self.__seconde >= 60 ):
            self.__seconde -= 60
            self.ajouteMinute(  1 )

    def time( self ):
        return (self.__heure, self.__minute, self.__seconde)

    def dup( self ):
        return MyDate( self.time() )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.__dict__ != other.__dict__

    def __lt__(self, other):
        result = False
        if(self.heure < other.heure):
            result = True
        elif(self.heure == other.heure):
            if(self.minute < other.minute):
                result = True
            elif(self.minute == other.minute):
                if(self.seconde < other.seconde):
                    result = True
                elif(self.seconde == other.seconde):
                    result = False
                else:
                    result = False
            else:
                result = False
        else:
            result = False
        return  result

    def __le__(self, other):
        result = False
        if(self.heure < other.heure):
            result = True
        elif(self.heure == other.heure):
            if(self.minute < other.minute):
                result = True
            elif(self.minute == other.minute):
                if(self.seconde < other.seconde):
                    result = True
                elif(self.seconde == other.seconde):
                    result = True
                else:
                    result = False
            else:
                result = False
        else:
            result = False
        return  result

    def __gt__(self, other):
        result = False
        if(self.heure > other.heure):
            result = True
        elif(self.heure == other.heure):
            if(self.minute > other.minute):
                result = True
            elif(self.minute == other.minute):
                if(self.seconde > other.seconde):
                    result = True
                elif(self.seconde == other.seconde):
                    result = False
                else:
                    result = False
            else:
                result = False
        else:
            result = False
        return  result

    def __ge__(self, other):
        result = False
        if(self.heure > other.heure):
            result = True
        elif(self.heure == other.heure):
            if(self.minute > other.minute):
                result = True
            elif(self.minute == other.minute):
                if(self.seconde >= other.seconde):
                    result = True
                elif(self.seconde == other.seconde):
                    result = True
                else:
                    result = False
            else:
                result = False
        else:
            result = False
        return  result

    def __add__(self, other):
        return MyDate( (self.heure + other.heure, self.minute + other.minute, self.seconde + other.seconde) )

    #~ def __sub__(self, other):
        #~ return MyDate( (self.heure - other.heure, self.minute - other.minute, self.seconde - other.seconde) )

    heure   = property(getHeure, setHeure)
    minute  = property(getMinute, setMinute)
    seconde = property(getSeconde, setSeconde)


def debugger(text):
    if debug:
        print "Debug(citation.py) %s" % text


#This defines behaviour of preferences keys
def prefs_cb( key, value ):
    debugger("[prefs_cb] key %s value %s" % (key, value) )
    # background image
    if (key == "background_image_visible"):
        Dsp.bg_image.uri                = bg_image
        Dsp.bg_image.visible            = value
        Dsp.bg_image.image_height       = Unit(100,PERCENT)
        Prefs.bg_image_uri.enabled      = value
        Prefs.bg_color_color.enabled    = not value
        if (value):
            Dsp.displaygroup.bg_color   = "#00000000"
        else:
            Dsp.displaygroup.bg_color   = bg_color

    elif (key == "bg_image"):
        if background_image_visible:
            Dsp.bg_image.uri            = bg_image
            Dsp.bg_image.visible        = True
            Dsp.bg_image.image_height   = Unit(100,PERCENT)
            Dsp.displaygroup.bg_color   = "#00000000"
        else:
            Dsp.bg_image.visible        = False
            Dsp.displaygroup.bg_color   = bg_color

    elif (key == "bg_color"):
        if not background_image_visible:
            Dsp.displaygroup.bg_color   = value

    elif (key == "frame_color"):
        Dsp.quoteframe.color            = value

    elif (key == "quote_font"):
        Dsp.quote.font                  = value
        Dsp.quote2.font                 = value

    elif (key == "quote_font_color"):
        Dsp.quote.color                 = value

    elif (key == "quote2_font_color"):
        Dsp.quote2.color                = value
        Dsp.qauthor2.color              = value

    elif (key == "qauthor_font"):
        Dsp.qauthor.font                = value
        Dsp.qauthor2.font               = value

    elif (key == "qauthor_font_color"):
        Dsp.qauthor.color               = value

    elif (key == "qauthor2_font_color"):
        Dsp.qauthor2.color              = value

    elif (key == "size"):
        Dsp.quoteframe.width = Unit(value, PT)
        Dsp.quote.font                  = quote_font
        Dsp.quote2.font                 = quote_font

    elif (key == "interval"):
        global heures, minutes, secondes, t
        if (interval == "daily") or (interval == "hourly") or (interval == "twice"):
            Prefs.heures.enabled        = False
            Prefs.minutes.enabled       = False
            Prefs.secondes.enabled      = False
            if(interval == "daily"):
                    heures = 24
            elif(interval == "twice"):
                    heures = 12
            elif(interval == "hourly"):
                    heures = 1
        elif (interval == "others"):
            Prefs.heures.enabled        = True
            Prefs.minutes.enabled       = True
            Prefs.secondes.enabled      = True
            if( heures == 0 and minutes == 0 and secondes == 0):
                secondes = 1
        else:
            debugger( "Pref: key: %s unknown value: %s" % (key, value) )
        t = MyDate( (heures, minutes, secondes ) )
        initialize_timer(  )

    elif( key == "heures" or key == "minutes" or key == "secondes" ):
        if( heures == 0 and minutes == 0 and secondes == 0):
            secondes = 1
        t = MyDate( (heures, minutes, secondes ) )
        initialize_timer(  )

    elif (key == "citation_type"):
        if( value not in ["celebrity", "bible", "politic", "simpson", "all"] ):
            citation_type = "celebrity"
        affiche_citation()

def initialize_timer(  ):
    global t0, t1, t
    t0 = MyDate( time.time )
    t1 = t + t0
    debugger( "[initialize_timer] t : %dh %dm %ds" %( t.time()  ) )
    debugger( "[initialize_timer] t0: %dh %dm %ds" %( t0.time() ) )
    debugger( "[initialize_timer] t1: %dh %dm %ds" %( t1.time() ) )

def refresh_quote( current_time ):
    global t0, t1, t
    t2 = MyDate( current_time )
    debugger( "[refresh_quote] t0: %dh %dm %ds" %( t0.time() ) )
    debugger( "[refresh_quote] t1: %dh %dm %ds" %( t1.time() ) )
    debugger( "[refresh_quote] t2: %dh %dm %ds" %( t2.time() ) )
    debugger( "[refresh_quote] t : %dh %dm %ds" %( t.time()  ) )
    debugger( "[refresh_quote] t2 >= t1 %s" %( t2 >= t1  ) )
    debugger( "[refresh_quote] =========" )
    if( t2 >= t1 ):
        t0 = t1.dup()
        t1 = t2 + t
        affiche_citation()

# Function

#~ def do_paste():
    #~ import subprocess
    #~ current_citation = Dsp.quote.value
    #~ subprocess.Popen(["-c", "xclip -i"], stdin= subprocess.PIPE, shell=True)
    #~ subprocess.communicate( current_citation )
    #~ subprocess.wait()

def affiche_citation():
    citation_choisis                    = citation_au_hasard()
    Dsp.quote.value                     =  "  %s" % citation_choisis['citation']
    Dsp.qauthor.value                   =  "  %s" % citation_choisis['auteur']
    Dsp.quote2.value                    =  "  %s" % citation_choisis['citation']
    Dsp.qauthor2.value                  =  "  %s" % citation_choisis['auteur']

def citation_au_hasard():
    category = ""
    if( citation_type == "all"):
        random.sequence = ["celebrity", "bible", "politic", "simpson"]
        category        = random.choice
    else:
        category = citation_type

    # choisis un auteur au hasard
    random.sequence = base_de_donnee_de_citation( category )
    citations       = random.choice
    random.sequence = citations['citation']
    citation        = random.choice

    return { 'citation': citation, 'auteur' : citations['auteur'] }

def base_de_donnee_de_citation( category ):
    # Citation
    bdd = None
    if( category == "celebrity" ):
        # A
            # Herm Albright
        albright = [
            u"Vous ne résoudrez peut-être pas tous vos problèmes en adoptant une attitude positive, mais vous agacerez tellement de gens que cela en vaudra la peine."
        ]

            # Isaac Asimov
        asimov = [
            u"Cela ne peut pas se faire du jour au lendemain ... - - On peut avoir commencé du jour au lendemain.",
            u"... la flatterie est une arme précieuse quand on a affaire à des jeunes; surtout quand cela ne vous engage à rien.",
            u"... pratiquer élégamment l'art de se dérober.",
            u"Dans ma fiction je suis attentif à ce que tout soit plausible et à raccorder les morceaux. La vie réelle n'est pas gênée par de telles considérations.",
            u"En dix heures par jour, on a le temps de prendre deux fois plus de retard sur son travail qu'en cinq heures par jour.",
            u"En Science, la phrase la plus excitante que l'on peut entendre, celle qui annonce de nouvelles découvertes, ce n'est pas «Eurêka» mais «c'est drôle».",
            u"Il est parfois utile de dire carrément ce qu'on pense, surtout si l'on a la réputation d'être retors.",
            u"Il n'y a aucun mérite à maintenir la discipline dans des circonstances idéales.",
            u"J'ai toujours eu pour philosophie de croire que les difficultés de la vie s'évanouissent quand on les affronte hardiment.",
            u"J'écris pour la même raison que je respire, parce que si je ne le faisais pas, je mourrais.",
            u"Je considère en tout cas la violence comme une moyen peu économique de parvenir à ses fins. Il y a toujours de meilleures méthodes, encore qu'elles soient parfois moins directes.",
            u"La phrase la plus excitante à entendre en science, celle qui annonce de nouvelles découvertes, n'est pas «Eureka» (j'ai trouvé!), mais plutôt «Tiens, c'est marrant...»",
            u"La violence ... est le dernier refuge de l'incompétence.",
            u"Les mathématiciens manipulent parfois de grands nombres, mais jamais dans leurs revenus.",
            u"Pour convaincre, la vérité ne peut suffire.",
            u"Pour réussir, il ne suffit pas de prévoir. Il faut aussi savoir improviser.",
            u"Quel gaspillage, pour un écrivain, de décrire ses sentiments intimes dans un simple journal!",
            u"Rien dans l'univers n'est aussi intéressant qu'une autre forme de vie intelligente... ni aussi dangereux. Il vaudrait mieux être au courant."
        ]

        # B
            # Sir Francis Bacon
        bacon = [
            u"(Il est sage) de ne pas admettre aveuglément les mystérieuses influences lointaines et de ne pas non plus les rejeter sous prétexte qu'elles seraient contraires à toute vraisemblance",
            u"Avoir pitié de son ennemi, c'est être sans pitié pour soi-même.",
            u"Calomniez, calomniez, il en restera toujours quelque chose.",
            u"Ce que l'on appelle vision haptique, c'est précisément ce sens des couleurs. Ce sens, ou cette vision, concerne d'autant plus la totalité que les trois éléments de la peinture, armature, figure et contour, communiquent et convergent dans la couleur.",
            u"Celui qui donne un bon conseil, construit d'une main, celui qui conseille et donne l'exemple, à deux mains; mais celui qui donne de bonnes leçons et un mauvais exemple construit d'une main et détruit de l'autre.",
            u"Celui qui n'appliquera pas de nouveaux remèdes doit s'attendre à de nouveaux maux; car le temps est le plus grand des innovateurs.",
            u"Celui qui possède femme et enfants a donné des otages à la fortune; car ce sont des obstacles aux grandes entreprises, qu'elles soient vertueuses ou malfaisantes.",
            u"Celui qui s'applique à la vengeance garde fraîches ses blessures.",
            u"Choisir son temps, c'est gagner du temps.",
            u"Dans le noir toutes les couleurs s'accordent.",
            u"Dès qu'il y a génie, il y a quelque chose qui n'est plus d'aucune école, d'aucun temps, opérant une percée - l'art comme processus sans but, mais qui s'accomplit comme tel.",
            u"Dieu Tout-Puissant planta tout d'abord un jardin. Et, vraiment, c'est le plus pur des plaisirs humains.",
            u"Il est vrai qu'un peu de philosophie incline l'esprit de l'homme à l'athéisme, mais une philosophie profonde amène les esprits des hommes à la religion.",
            u"Il est vrai qu'un peu de philosophie incline l'esprit de l'homme à l'athéisme; mais que davantage de philosophie le ramène à la religion.",
            u"Il y a de la superstition à éviter la superstition.",
            u"Il y a des livres dont il faut seulement goûter, d'autres qu'il faut dévorer, d'autres enfin, mais en petit nombre, qu'il faut, pour ainsi dire, mâcher et digérer.",
            u"Je croirais plutôt toutes les fables des légendes et le Talmud et le Coran que cette création universelle n'ait pas de créateur.",
            u"Je voudrais beaucoup ne pas faire des monstres, pourtant tout le monde semble penser que c'est à cela que mes tableaux aboutissent. Si je rends les gens laids, ce n'est pas exprès. J'aimerais les montrer aussi beau qu'ils le sont.",
            u"L'amitié double les joies et réduit de moitié les peines.",
            u"L'Ancien Testament vous promet la prospérité et le Nouveau l'adversité.",
            u"L'épouse est une maîtresse pour l'homme jeune, une compagne pour l'âge mûr, une infirmière pour la vieillesse; l'homme a donc, à tout âge, un prétexte pour se marier.",
            u"L'espoir est un bon petit déjeuner, mais c'est un méchant souper.",
            u"La compréhension n'a pas besoin d'ailes.",
            u"La connaissance est en elle-même puissance.",
            u"La dissimulation est une sagesse abrégée.",
            u"La gloire ressemble au marché: parfois, quand vous y restez quelque temps, les prix baissent.",
            u"La jeunesse est plus apte à inventer qu'à juger, à exécuter qu'à conseiller, à lancer des projets nouveaux qu'à poursuivre des anciens.",
            u"La mouche s'assit sur l'essieu du chariot et dit: «Quelle poussière je soulève!...»",
            u"La nature, pour être commandée, doit être obéie.",
            u"La prospérité découvre nos vices et l'adversité nos vertus.",
            u"La prospérité ne va pas sans craintes ni déplaisirs; l'adversité, sans réconforts ni espérances.",
            u"La superstition est à la religion ce que le singe est à l'homme.",
            u"La vengeance est une justice sauvage.",
            u"La vérité sort plus facilement de l'erreur que de la confusion.",
            u"Le meilleur moyen de conserver un esprit ouvert sont les conseils sincères d'un ami.",
            u"Le silence est la vertu des sots.",
            u"Les enfants adoucissent les peines, mais rendent les malheurs plus amers.",
            u"Les épouses sont pour les jeunes hommes des maîtresses, pour les hommes d'âge mûr des compagnes, et pour les vieillards des gouvernantes.",
            u"Les français sont plus sages qu'il ne semble.",
            u"Les jeunes sont plus aptes à inventer qu'à juger; plus aptes à exécuter qu'à conseiller; plus aptes à entreprendre qu'à gérer.",
            u"Les maisons sont bâties pour être habitées et non point regardées.",
            u"On dit généralement que les Français sont plus sages qu'ils ne paraissent et que les Espagnols paraissent plus sages qu'ils ne sont; mais quoi qu'il en soit de ces nations, il en est certainement ainsi des individus qui les composent.",
            u"On naît. On meurt. C'est mieux si entre les deux on a fait quelque chose.",
            u"On ne commande à la nature qu'en lui obéissant.",
            u"Peu d'hommes s'aperçoivent de ce qu'est la solitude, et combien elle s'étend; car une foule n'est pas une compagnie, et des figures ne sont qu'une galerie de portraits, et la conversation, une cymbale résonnante, là où il n'y a point d'amour.",
            u"Rien n'assure aussi vite la prospérité des uns que les erreurs des autres.",
            u"Se venger, c'est se mettre au niveau de l'ennemi; pardonner, c'est le dépasser.",
            u"Serrer trop fort le pressoir donne un vin qui sent le pépin.",
            u"Si un homme regarde très attentivement, il verra la chance; car si elle est aveugle, elle n'est pas pour autant invisible.",
            u"Toutes les couleurs s'accordent dans l'obscurité.",
            u"Un peu de foi éloigne de Dieu, beaucoup de science y ramène."
        ]

            # Pierre Beaumarchais
        beaumarchais = [
            u"Il n'est pas nécessaire de comprendre les choses afin de faire valoir à leur sujet."
        ]

            # Ambrose Bierce
        bierce = [
            u"Aborigènes: Personnes de moindre importance qui encombrent les paysages d'un pays nouvellement découvert. Ils cessent rapidement d'encombrer; ils fertilisent le sol.",
            u"Abstinent: personne faible qui cède à la tentation de se refuser un plaisir.",
            u"Absurdité: Affirmation manifestement incompatible avec son opinion propre.",
            u"Accomplissement: La fin de l'effort et le début de l'ennui.",
            u"Adage: Sagesse désossée pour dents branlantes.",
            u"Administration: dans les affaires publiques, ingénieuse abstraction conçue pour recevoir les attaques et les coups destinés au Premier Ministre ou au Président. Ecran à l'épreuve des malotrus et des tracassiers.",
            u"Air: substance nutritive fournie par une généreuse Providence pour engraisser les pauvres.",
            u"Alliance: En politique internationale, union de deux voleurs qui ont leurs mains si profondément enfoncées dans les poches l'un de l'autre qu'il leur est difficile de s'en prendre séparément à un troisième.",
            u"Amitié: Embarcation assez grande pour porter deux personnes par beau temps, mais une seule en cas de tempête.",
            u"Amnistie: Magnanimité d'un pays envers des coupables qu'il serait trop onéreux de sanctionner.",
            u"Amour: Folie temporaire que l'on peut guérir par le mariage ou en retirant le patient du champ d'influence qui est à la source de l'indisposition.",
            u"Antipathie: Sentiment que nous inspire l'ami d'un ami.",
            u"Aphorisme: Sagesse prédigérée.",
            u"Ardeur: Etat particulier de l'amour sans l'expérience.",
            u"Armure: Sorte d'habit porté par un homme dont le tailleur est un forgeron.",
            u"Assisté: Individu qui compte sur la générosité publique pour un soutien que vous-mêmes n'êtes pas en position de pouvoir obtenir.",
            u"Auto-évident: Evident pour une seule personne à l'exclusion de toute autre.",
            u"Autosatisfaction: Evaluation erronée.",
            u"Avouer: Confesser une faute. Dévoiler les fautes d'autrui est un grand devoir imposé par l'amour de la vérité.",
            u"Bacchus: Divinité complaisante inventée par les anciens pour excuser leurs excès de boisson.",
            u"Baromètre: ingénieux instrument qui nous indique le temps qu'il fait.",
            u"Bataille: Manière de défaire avec les dents un noeud politique qui ne veut pas céder avec la langue.",
            u"Beauté: Pouvoir qui permet à la femme de charmer un amoureux et de terrifier un mari.",
            u"Bébé: Créature difforme à l'âge, au sexe et à la condition indéterminés, hautement remarquable par la violence des sympathies et des antipathies qu'elle provoque chez les autres, sans exprimer elle-même de sentiment ni d'émotion.",
            u"Bien-être: Etat d'esprit produit par la contemplation des ennuis d'autrui.",
            u"Blé: céréale dont on arrive, non sans peine, à tirer un assez bon whisky et qu'on utilise pour faire du pain.",
            u"Bonheur: Agréable sensation qui naît de la contemplation de la misère d'autrui.",
            u"Bouche: chez l'homme, la porte d'entrée de l'âme; chez la femme, l'issue du coeur.",
            u"Bourreau: Dans certains Etats d'Amérique, ses fonctions sont désormais assurées par un électricien.",
            u"Bruit: Puanteur dans l'oreille. Musique non domestiquée. Produit principal et signe authentique de civilisation.",
            u"Cadavre: Produit fini dont nous sommes la matière première.",
            u"Calomnier: Attribuer malicieusement à quelqu'un les actions vicieuses que l'on n'a pas eu la tentation ou l'opportunité de commettre soi-même.",
            u"Canon: Instrument utilisé dans la rectification des frontières nationales.",
            u"Cerveau: Appareil avec lequel nous pensons que nous pensons.",
            u"Chat: Automate doux et indestructible fourni par la Nature pour prendre des coups de pied quand quelque chose ne va pas dans le cercle familial.",
            u"Chemin de fer: Le plus important des dispositifs mécaniques qui nous permettent de nous déplacer de là où nous sommes à là où nous ne serons pas mieux.",
            u"Chiure de mouche: Signe primitif de ponctuation.",
            u"Chrétien: Personne qui croit que le Nouveau Testament est un livre d'inspiration divine admirablement adapté aux besoins spirituels de son voisin. Personne qui suit les enseignements du Christ tant qu'ils ne sont pas incompatibles avec une vie de péché.",
            u"Ciel: Endroit où les méchants cessent de vous assommer avec la bavardage de leurs affaires personnelles, et où les gentils écoutent avec attention tandis que vous exposez les vôtres.",
            u"Cimetière: Coin de banlieue isolé où les parents du disparu rivalisent de mensonges, où les poètes écrivent à la cible, et où les tailleurs de pierre prennent l'orthographe pour objet de leurs paris.",
            u"Cirque: Endroit où les chevaux, les poneys et les éléphants sont autorisés à voir des hommes, des femmes et des enfants se conduire comme des idiots.",
            u"Citation: Répétition erronée d'une déclaration d'autrui. Extrait repris avec des erreurs.",
            u"Clairvoyance: Capacité pour une personne, généralement féminine, de voir ce qui est invisible pour son patron - à savoir que c'est un abruti.",
            u"Clarinette: Instrument de torture utilisé par une personne qui a du coton dans les oreilles. Il y a deux instruments qui sont pires qu'une clarinette - deux clarinettes.",
            u"Comestible: Susceptible d'être mangé et digéré, comme un ver pour un crapaud, un crapaud pour un serpent, un serpent pour un cochon, un cochon pour l'homme et l'homme pour le ver.",
            u"Commerce: Sorte de transaction à travers laquelle A dépouille B des biens de C et en compensation de laquelle B soulage des poches de D de l'argent de E.",
            u"Compromis: Sorte d'ajustement d'intérêts divergents qui consiste à donner à chaque adversaire la satisfaction de penser qu'il a eu ce qu'il ne devait pas obtenir, et qu'il n'est privé de rien, sinon de ce qui lui était véritablement dû.",
            u"Condoléances: Manière de démontrer que le deuil est un moindre mal à côté de la sympathie.",
            u"Conférencier: Homme qui met sa main dans sa poche, sa langue dans votre oreille et sa foi dans votre patience.",
            u"Confident(e): Personne instruite par A des secrets de B, confiés personnellement par ce dernier à C.",
            u"Connaissance: personne que l'on connaît assez pour lui emprunter de l'argent, mais pas assez pour lui en prêter.",
            u"Connaisseur: Spécialiste qui sait tout à propos d'une chose et rien à propos de tout le reste.",
            u"Conservateur: Politicien qui affectionne les maux existants, qu'il ne faut pas confondre avec le Libéral qui souhaite les remplacer par d'autres.",
            u"Consulter: Rechercher l'approbation d'autrui pour un projet déjà bien arrêté.Consolation: Lorsque l'on constate qu'un homme meilleur est plus infortuné que soi.",
            u"Conversation: Foire où chacun propose ses petits articles mentaux, chaque exposant étant trop préoccupé par l'arrangement de ses propres marchandises pour s'intéresser à celles de ses voisins.",
            u"Corsaire: Politicien des mers.",
            u"Critiques: L'une des nombreuses méthodes qu'affectionnent les imbéciles pour perdre leurs amis.",
            u"Curiosité: Vilain défaut de l'esprit féminin. L'envie de savoir si oui ou non une femme se consume de curiosité est l'une des passions les plus actives et les plus insatiables de l'âme masculine.",
            u"Cynique: Grossier personnage dont la vision déformée voit les choses comme elles sont, et non comme elles devraient être. De là l'ancienne coutume scythe d'arracher les yeux d'un cynique pour améliorer sa perspective.",
            u"Dédain: Sentiment d'un homme prudent envers un ennemi qui est trop formidablement à l'abri pour être attaqué.",
            u"Déluge: Premier essai remarqué de baptême collectif, qui lessiva tous les péchés (et les pécheurs) de la création.",
            u"Dentiste: Prestidigitateur qui, tout en mettant du métal dans votre bouche, subtilise des pièces dans votre poche.",
            u"Dérision: Manière de montrer que la personne qui en subit les attaques est dénuée des heureuses qualités qui distinguent ceux qui l'attaquent.",
            u"Destinée: Justification du Tyran pour ses crimes, excuse de l'imbécile pour ses échecs.",
            u"Détresse: Maladie contractée à l'exposition de la prospérité d'un ami.",
            u"Deux fois: Une fois de trop.",
            u"Dictateur: Chef d'une nation qui préfère la pestilence du despotisme à la plaie de l'anarchie.",
            u"Diplomatie: L'art patriotique de mentir pour son pays.",
            u"Discussion: Moyen de confirmer les autres dans leurs erreurs.",
            u"Distance: La seule chose que les riches soient prêts à accorder aux pauvres, en souhaitant qu'ils la gardent.",
            u"Duel: Formalité préliminaire à la réconciliation de deux ennemis.",
            u"Ecriture: Livres sacrés de notre sainte religion, à ne pas confondre avec les récits profanes et mensongers sur lesquels sont fondés toutes les autres croyances.",
            u"Education: Ce qui révèle, dans les manières et les façons d'un imbécile, son manque d'intelligence.",
            u"Egoïste: Dénué de respect pour l'égoïsme des autres.",
            u"Egotiste: Personne de goût médiocre, plus intéressée par elle-même que par moi.",
            u"Eloquence: Art de convaincre les imbéciles par la parole de ce que le cheval blanc d'Henri IV est effectivement blanc. Cela inclut le talent de prouver que le cheval blanc est également de n'importe quelle autre couleur.",
            u"Emancipation: Changement de tutelle de la tyrannie d'autrui au despotisme de soi-même.",
            u"Emeute: Divertissement populaire donné pour des militaires par des spectateurs innocents.",
            u"En diplomatie, l'ultimatum est la dernière exigence avant les concessions.",
            u"Epitaphe: Inscription sur une tombe, montrant que les vertus acquises par le trépas ont un effet rétroactif.",
            u"Epousée: femme qui a un bel avenir de bonheur derrière elle.",
            u"Erudition: Poussière tombée d'un livre dans un crâne vide.",
            u"Et en effet, le bons sens vient aisément prouver - Et les faits confirmer sans conteste que les hommes - Ne sont pas tous menteurs; il en est qui sont morts.",
            u"Evangéliste: Porteur de bonnes nouvelles, particulièrement (dans un sens religieux) de celles qui assurent notre propre salut et la damnation de nos voisins.",
            u"Excentricité: Manière de se faire valoir qui est si facile à mettre en oeuvre que les imbéciles l'utilisent pour mettre en relief leur nullité.",
            u"Excuser (s'): Poser les fondations d'une future offense.",
            u"Exilé: Personne qui sert son pays en résidant à l'étranger, sans être pour autant ambassadeur.",
            u"Expérience: Lucidité qui nous permet de reconnaître comme une fâcheuse vieille connaissance la folie que nous venons de commettre.",
            u"Faire plaisir: Poser les fondations d'une structure de contrainte.",
            u"Fantôme: Signe extérieur évident d'une frayeur interne.",
            u"Félicitations: Politesse de la jalousie.",
            u"Fidélité: Vertu particulière de ceux qui ne sont pas loin d'être trompés.",
            u"Foi: Croyance sans preuve dans ce qui est affirmé par quelqu'un qui parle sans savoir, ou qui pense sans comparer.",
            u"Frontières: En géographie politique, ligne imaginaire entre deux nations, séparant les droits imaginaires de l'une des droits imaginaires de l'autre.",
            u"Généalogie: liste des ascendants de quelqu'un, partir d'un lointain ancêtre qui ne se souciait guère en son temps d'établir la sienne.",
            u"Guillotine: machine qui, à juste titre, fait hausser les épaules à un Français.",
            u"Habitude: Entrave à la liberté.",
            u"Hier: Enfance de la jeunette, jeunesse de la maturité, passé révolu de la vieillesse.",
            u"Histoire: Compte rendu hautement douteux d'événements historiques hautement futiles, causés par des chefs d'une haute scélératesse et des soldats particulièrement stupides.",
            u"Homéopathe: L'humoriste de la profession médicale.",
            u"Hypocrite: Personne qui, professant des vertus qu'il ne respecte pas, rend évident l'avantage de sembler être ce qu'il dédaigne.",
            u"Ignare: Personne ignorante peu familiarisée avec certains domaines du savoir qui vous sont familiers, et qui ont des domaines de prédilection auxquels vous n'entendez rien.",
            u"Il n'y a rien de nouveau sous le soleil, mais il y a aussi tout un tas de vieux trucs que nous ignorons.",
            u"Imagination: Entrepôt d'idées, dont le poète et le menteur sont copropriétaires.",
            u"Index: Doigt pointé qui, si on le suit, montre deux malfaiteurs.",
            u"Ingrat: Individu qui reçoit un avantage d'un autre, ou qui est un objet de charité.Indifférent: Imparfaitement sensible aux distinctions entre les choses.",
            u"Injustice: Fardeau qui, de tous ceux que nous chargeons sur d'autres et transportons nous-mêmes, est le plus léger dans les mains et le plus lourd sur l'échine.",
            u"Insurrection: Révolution qui a échoué. Tentative infructueuse pour substituer le désordre à un mauvais gouvernement.",
            u"Intention: Prévalence dans l'esprit d'un ensemble d'influences sur un autre ensemble; effet dont la cause est l'imminence, immédiate ou lointaine, de l'exécution d'un acte involontaire.",
            u"Interprète: Individu qui permet à deux personnes de langues différentes de se comprendre mutuellement, en répétant à chacune ce qu'il aurait été intéressant pour l'interprète que l'autre eût déclaré.",
            u"Inventeur: Personne qui fait un ingénieux arrangement de roues, de leviers et de ressorts, et qui croit que c'est la civilisation.",
            u"Jaloux: Qui s'intéresse indûment à la préservation de quelque chose qui ne peut être perdu que s'il n'est pas bien gardé.",
            u"Journal intime: Relation quotidienne de la partie de notre existence que nous pouvons nous raconter sans rougir.",
            u"Kleptomane: Riche voleur.",
            u"L'orthographe est une science qui consiste à écrire les mots d'après l'oeil et non d'après l'oreille.",
            u"La beauté chez les femmes et la distinction chez les hommes ont ceci en commun: ils sont pour l'imbécile une forme de crédibilité.",
            u"La femme serait plus charmante si l'on pouvait tomber dans ses bras sans tomber dans ses mains.",
            u"La jarretière est un ruban élastique destiné à empêcher une femme de sortir de ses bas et de désoler le pays.",
            u"La persévérance est une vertu obscure qui permet la médiocrité d'obtenir un succès sans gloire.",
            u"La politique est la conduite des affaires publiques pour le profit des particuliers.",
            u"La recrue est celui qui se distingue d'un civil par son uniforme et d'un soldat par sa démarche.",
            u"La satiété est un sentiment qu'on éprouve pour une assiette après avoir mangé son contenu.",
            u"Le bonheur est une sensation agréable que nous éprouvons au spectacle du malheur d'autrui.",
            u"Le dos est la partie du corps de vos amis que vous avez le privilège de contempler dans l'adversité.",
            u"Le surmenage est une dangereuse maladie affectant les hauts fonctionnaires désireux d'aller à la pêche.",
            u"Le vrai égoïste est celui qui n'a aucune considération pour l'égoïsme d'autrui.",
            u"Les calamités sont de deux sortes: le malheur qui nous atteint et le coup de chance qui arrive aux autres.",
            u"Les femmes seraient charmantes si on pouvait tomber dans leurs bras sans tomber dans leur mains.",
            u"Longévité: prolongation peu commune de la crainte de la mort.",
            u"Lundi: Dans les pays chrétiens, lendemain du jour du tiercé.",
            u"Lycée: 1/ Ecole antique où l'on s'entretenait de morale et de philosophie. 2/ Ecole moderne où l'on discute de football.",
            u"Maladie qui rend le patient incapable de tenir sa langue quand vous avez envie de parler.",
            u"Mammifères (n.): Famille d'animaux vertébrés dont les femelles, à l'état de nature, allaitent leurs petits, mais, une fois civilisées et éclairées, les confient à une nourrice ou utilisent un biberon.",
            u"Mariage: Communauté composée d'un maître, d'une maîtresse et de deux esclaves, l'ensemble ne faisant que deux personnes.",
            u"Ministre: Personne qui agit avec un grand pouvoir et une faible responsabilité.",
            u"Ne remets jamais au lendemain ce que tu peux ne pas faire du tout.",
            u"Nous connaissons mieux nos propres besoins que ceux des autres. Satisfaire les siens relève de la bonne gestion.",
            u"On reconnaît un homme à la façon dont il gère son entreprise.",
            u"Opposition: En politique, le parti qui empêche le gouvernement de s'emballer en lui coupant les jarrets.",
            u"Paix: Dans les affaires internationales, période de duperie entre deux périodes de combats.",
            u"Patience: Forme mineure de désespoir, déguisée en vertu.",
            u"Patriotisme: Matériau combustible susceptible de servir de torche à quiconque ambitionne d'illuminer son nom.",
            u"Persévérance: Humble vertu qui permet aux médiocres de parvenir à un succès peu glorieux.",
            u"Philosophie: route qui mène de nulle part à rien.",
            u"Piéton: partie changeante (et audible) de la chaussée pour une automobile.",
            u"Politesse: Forme la plus acceptable de l'hypocrisie.",
            u"Présage: Signe que quelque chose arrivera si rien ne se passe.",
            u"Prier: Demander que les lois de l'univers soient annulées en faveur d'un unique pétitionnaire, indigne de son propre aveu.",
            u"Qu'est-ce qu'un abstinent après tout? Un faible qui cède à la tentation de se refuser un plaisir.",
            u"Quand on veut, on pourrait.",
            u"Radiesthésiste: Personne qui utilise une baguette divinatoire pour prospecter le métal précieux dans la poche d'un imbécile.",
            u"Raisonner: Peser des probabilités sur la balance du désir.",
            u"Raseur: Personne qui vous parle quand vous souhaitez qu'elle écoute.",
            u"Réalisme: Art de dépeindre la nature telle qu'elle est vue par les crapauds. Charme qui ressort d'un paysage peint par une taupe, ou d'une histoire écrite par un asticot.",
            u"Réflexion: Démarche de l'esprit à travers laquelle nous percevons avec clarté notre relation avec les événements du passé, et qui nous rend capable d'éviter à l'avenir les périls que nous ne rencontrerons plus.Reconsidérer: Chercher une justification pour une décision déjà prise.",
            u"Rien n'est plus logique que la persécution. La tolérance religieuse est une sorte de manque de foi.",
            u"Savoir: Forme d'ignorance qui distingue les studieux.",
            u"Sénat: Groupe de gentlemen d'un certain âge chargés de hautes responsabilités et de sombres méfaits.",
            u"Seul: En mauvaise compagnie.",
            u"Singe: Animal arboricole qui se sent également très à l'aise dans les arbres généalogiques.",
            u"Société: système ingénieux pour obtenir des bénéfices individuels sans responsabilité individuelle.",
            u"Soumission: patience dans l'inconfort, mais dans l'espoir d'une revanche qui en vaille la peine.",
            u"Souris: Animal dont le chemin est jonché de femmes évanouies.",
            u"Travail: l'un des processus par lesquels A accroît la propriété de B.",
            u"Tu n'embrasseras pas la femme de ton voisin, sauf si la tienne a succombé à ses caresses.",
            u"Un bon conseil vaut mieux que de le suivre.",
            u"Un dépôt est une contribution charitable à l'avenir de votre banque.",
            u"Un égocentrique est une personne de bien peu de goût, beaucoup plus intéressée par elle-même que par moi.",
            u"Un plébiscite est un vote populaire destiné à bien établir l'autorité du souverain.",
            u"Un saint est un pécheur mort, revu et corrigé.",
            u"Une personne qui parle lorsque vous désirez qu'elle vous écoute.",
            u"Vanité: Hommage d'un sot au premier imbécile venu.",
            u"Vénération: attitude spirituelle d'un homme à l'égard de Dieu, et d'un chien à l'égard de l'homme.",
            u"Vieillesse: période de notre existence pendant laquelle nous composons avec les vices que nous chérissons encore, en vitupérant ceux que nous n'avons plus la hardiesse de pratiquer.",
            u"Vilain défaut de l'esprit féminin: L'envie de savoir si oui ou non une femme se consume de curiosité est l'une des passions les plus actives et les plus insatiables de l'âme masculine.",
            u"Violon: Instrument qui titille les oreilles humaines par le frottement d'une queue de cheval sur les boyaux d'un chat.",
            u"Voisin: Personne qu'on nous demande d'aimer comme nous-mêmes, et qui fait tout ce qu'il peut pour nous faire désobéir.",
            u"Whangdepootenawah: Dans la langue Ojibwa, désastre. Affliction inattendue qui frappe très très fort."
        ]

            # Otto Von Bismarck
        bismarck = [
            u"Ce n'est pas par des discours et des votes de majorité que les grandes questions de notre époque seront résolues, mais par le fer et par le sang.",
            u"En politique, il faut toujours suivre le droit chemin. On est sûr de n'y rencontrer personne.",
            u"Gouverner est l'art de mener des hommes imparfaits avec des lois imparfaites.",
            u"La politique n'est pas une science comme se l'imaginent beaucoup de professeurs, mais un art.",
            u"La politique n'est pas une science exacte.",
            u"Les grandes questions de notre temps ne sont pas tranchées par des discours et des motions majoritaires ..., mais par le fer et par le sang.",
            u"Provoquez donc une émeute pendant que vous avez encore une armée pour l'étouffer.",
            u"Quand, à propos d'une idée, on dit qu'on est d'accord sur le principe, cela signifie que l'on n'a pas la moindre intention de la mettre à exécution.",
            u"Si Eve avait eu à recoudre les feuilles de vigne de son mari, elle n'aurait pas écouté si longtemps le serpent!",
            u"Un journaliste, c'est quelqu'un qui a manqué sa vocation."
        ]

            # Wernher von Braun
        braun = [
            u"Demain, apprendre l'espace en ville sera aussi utile que d'apprendre à conduire.",
            u"Nous sommes capables de défier les lois de la pesanteur, mais, quelquefois, nous nous trouvons submergés par la paperasse."
        ]

        # C
            # Truman Capote
        capote = [
            u"L'art et la vérité peuvent partager le même lit sans que ça les empêche d'être incompatibles.",
            u"Les corbeaux sont très malins... Si on leur taille la langue en deux, on peut leur apprendre à parler.",
            u"Tous les chiens, quand ils sont dans l'embarras, se mettent à bâiller."
        ]

            # Jimmy Carter
        carter = [
            u"J'ai regardé beaucoup de femmes avec concupiscence. J'ai commis bien des fois l'adultère dans mon coeur... et Dieu me pardonne."
        ]

            # Sir Winston Leonard Spencer Churchill
        churchill = [
            u"(Alors qu'on lui demandait quelle devait être la principale qualité d'un politicien) - - C'est la capacité de prédire ce qui va arriver demain, le mois prochain, et l'année prochaine; et, après, d'expliquer pourquoi cela ne s'est pas passé.",
            u"A l'époque, il était plus sage qu'aujourd'hui; il me demandait souvent mon avis.",
            u"A la guerre, la maxime «sécurité d'abord» mène tout droit à la ruine.",
            u"Agissez comme s'il était impossible d'échouer.",
            u"Après la guerre, deux choix s'offraient à moi: finir ma vie comme député, ou la finir comme alcoolique. Je remercie Dieu d'avoir si bien guidé mon choix: je ne suis plus député!",
            u"Aux examens on nous pose toujours des questions dans des domaines qu'on ne connaît pas et jamais dans ceux qu'on connaît bien.",
            u"Avec Staline, quand on avait dix à partager, il disait: «Bien! On ne parle pas des cinq qui sont à moi. Qu'est-ce qu'on fait avec les cinq vôtres?»",
            u"C'est un de ces orateurs qui, quand ils se lèvent, ne savent pas ce qu'ils vont dire, quand ils parlent, ne savent pas de quoi ils parlent et, quand ils se sont rassis, ne savent pas ce qu'ils ont dit.",
            u"C'est une belle chose d'être honnête, mais il est également important d'avoir raison.",
            u"C'est une bonne chose pour un homme peu cultivé de lire des dictionnaires de citations.",
            u"Ce n'est pas la fin. Ce n'est même pas le commencement de la fin. Mais, c'est peut-être la fin du commencement.",
            u"Ce n'est que quand il fait nuit que les étoiles brillent.",
            u"Christophe Colomb était le premier socialiste: il ne savait pas où il allait, il ignorait où il se trouvait et faisait tout ça aux frais des autres.",
            u"Comité: Un groupe de personnes incapables de faire quoi que ce soit par elles-mêmes qui décident collectivement que rien ne peut être fait!",
            u"Construire peut être le fruit d'un travail long et acharné. Détruire peut être l'oeuvre d'une seule journée.",
            u"De temps en temps, les hommes tombent sur la vérité. La plupart se relèvent comme si rien n'était.",
            u"En Angleterre, tout est permis, sauf ce qui est interdit. En Allemagne, tout est interdit, sauf ce qui est permis. En France, tout est permis, même ce qui est interdit. En U.R.S.S., tout est interdit, même ce qui est permis.",
            u"En avalant les méchantes paroles qu'on ne profère pas, on ne s'est jamais abîmé l'estomac.",
            u"En temps de guerre, la vérité est si précieuse qu'elle devrait toujours être protégée par un rempart de mensonges.",
            u"En vin, je suis un amateur facile, je ne me contente que du meilleur.",
            u"Epargner est une très bonne chose. Surtout quand vos parents l'on fait pour vous.",
            u"Et moi, si j'étais votre mari, je le boirais, ce thé!",
            u"Etre homme politique, c'est être capable de dire à l'avance ce qui va arriver demain, la semaine prochaine, le mois prochain et l'année prochaine. Et d'être capable, après, d'expliquer pourquoi rien de tout cela ne s'est produit.",
            u"Il est meilleur d'être irresponsable et dans le vrai que responsable et dans l'erreur.",
            u"Il est toujours sage de regarder en avant, mais il est difficile de regarder plus loin qu'on ne peut voir.",
            u"Il est une bonne chose de lire des livres de citations, car les citations lorsqu'elles sont gravées dans la mémoire vous donnent de bonnes pensées.",
            u"Il était tellement bête que ses collègues s'en étaient aperçus.",
            u"Il n'y a aucun mal à changer d'avis, pourvu que ce soit dans le bon sens.",
            u"Il n'y a pas de contes plus beaux que ceux que la vie a elle même composé.",
            u"Il n'y a pas de meilleur placement pour un pays que de mettre du lait dans des enfants.",
            u"Il n'y a qu'une réponse à la défaite, et c'est la victoire.",
            u"Il n'y a rien de négatif dans le changement, si c'est dans la bonne direction.",
            u"Il ne sert à rien de dire «Nous avons fait de notre mieux». Il faut réussir à faire ce qui est nécessaire.",
            u"Il vaut mieux faire l'information que la recevoir; il vaut mieux être acteur que critique.",
            u"Il y a peu de vertus que les Polonais ne possèdent et peu d'erreurs qu'ils n'aient commises.",
            u"J'ai retiré plus de choses de l'alcool que l'alcool ne m'en a retirées.",
            u"J'aime les porcs. Les chiens nous regardent avec vénération. Les chats nous toisent avec dédain. Les cochons nous considèrent comme des égaux.",
            u"Jamais dans le champ des conflits humains tant de gens n'ont dû autant à si peu.",
            u"Je n'ai rien à offrir que du sang, du labeur, des larmes et de la sueur.",
            u"Je ne crois aux statistiques que lorsque je les ai moi-même falsifiées.",
            u"Je ne suis pas difficile, je me satisfais aisément du meilleur.",
            u"Je suis prêt, pour ma part, à me présenter devant le Créateur et à l'affronter. Mais Lui, est-il préparé à cette épreuve?",
            u"Jeune homme, étudiez l'histoire, étudiez l'histoire. C'est dans l'histoire que résident tous les secrets de l'art de gouverner.",
            u"L'Angleterre s'écroule dans l'ordre, et la France se relève dans le désordre.",
            u"L'écriture est une aventure. Au début c'est un jeu, puis c'est une amante, ensuite c'est un maître et ça devient un tyran.",
            u"L'epargne est une bonne chose, surtout si vos parents l'ont faite pour vous.",
            u"L'extérieur du cheval exerce une influence bénéfique sur l'intérieur de l'homme.",
            u"L'histoire me sera indulgente car j'ai l'intention de l'écrire.",
            u"La chance n'existe pas; ce que vous appelez chance, c'est l'attention aux détails.",
            u"La critique peut être désagréable, mais elle est nécessaire. Elle est comme la douleur pour le corps humain: elle attire l'attention sur ce qui ne va pas.",
            u"La démocratie est le pire des régimes politiques... si on fait abstraction de tous les autres.",
            u"La démocratie est un mauvais système, mais elle est le moins mauvais de tous les systèmes.",
            u"La dictature - dévotion-fétiche pour un homme - est une chose éphémère. Un état de société où l'on ne peut pas exprimer ses pensées, où des enfants dénoncent leurs parents à la police, un tel état de société ne peut pas durer longtemps.",
            u"La grande leçon de la vie, c'est que parfois, ce sont les fous qui ont raison.",
            u"La mort et la douleur seront nos compagnons de voyage, les privations notre vêtement, la constance et la vaillance notre seul bouclier.",
            u"La politique est plus dangereuse que la guerre... A la guerre, vous ne pouvez être tué qu'une seule fois. En politique, plusieurs fois.",
            u"La responsabilité est le prix de la grandeur.",
            u"La Russie est un rébus enveloppé de mystère au sein d'une énigme.",
            u"La vie? Le voyage vaut la peine d'être fait une fois.",
            u"Le cheval est dangereux devant, dangereux derrière et inconfortable au milieu",
            u"Le chien lève vers vous des yeux implorants, le chat vous regarde de haut. Mais parlez-moi du cochon! Le cochon, lui, vous regarde droit dans les yeux, d'égal à égal.",
            u"Le courage, c'est ce qu'il faut se lever et parler; le courage est aussi ce qu'il faut pour s'asseoir et écouter.",
            u"Le défaut du capitalisme c'est qu'il répartit inégalement la richesse; la qualité du socialisme c'est qu'il répartit également la misère.",
            u"Le golf consiste à mettre une balle de 4 cm de diamètre sur une boule de 40.000 km de tour et à frapper la petite, non la grande.",
            u"Le meilleur argument contre la démocratie est une conversation de cinq minutes avec l'électeur moyen.",
            u"Le pouvoir de l'homme s'est accru dans tous les domaines, excepté sur lui-même",
            u"Le secret de ma vitalité? Je n'ai dans le sang que des globules rouges: l'alcool a tué depuis belle lurette tous mes globules blancs.",
            u"Le succès c'est être capable d'aller d'échec en échec sans perdre son enthousiasme.",
            u"Le vice inhérent au capitalisme consiste en une répartition inégale des richesses. La vertu inhérente au socialisme consiste en une égale répartition de la misère.",
            u"Le vrai génie réside dans l'aptitude à évaluer l'incertain, le hasardeux, les informations conflictuelles.",
            u"Les empires du futur seront spiriturels.",
            u"Les hommes trébuchent parfois sur la vérité, mais la plupart se redressent et passent vite leur chemin comme si rien ne leur était arrivé.",
            u"Ma croix la plus lourde, c'est la croix de Lorraine.",
            u"Tout le monde savait que ce truc-là etait impossible a faire. Jusqu'au jour où est arrivé quelqu'un qui ne le savait pas, et qui l'a fait.",
            u"Un bon diplomate est quelqu'un qui peut égorger son voisin sans qu'il s'en aperçoive.",
            u"Un bon politicien est celui qui est capable de prédire l'avenir et qui, par la suite, est également capable d'expliquer pourquoi les choses ne se sont pas passées comme il l'avait prédit.",
            u"Un conciliateur c'est quelqu'un qui nourrit un crocodile en espérant qu'il sera le dernier à être mangé.",
            u"Un fanatique est quelqu'un qui ne veut pas changer d'avis et qui ne veut pas changer de sujet.",
            u"Un pessimiste voit la difficulté dans chaque opportunité, un optimiste voit l'opportunité dans chaque difficulté.",
            u"Un rideau de fer est descendu sur l'Europe.",
            u"Une pomme par jour éloigne le médecin, pourvu que l'on vise bien.",
            u"Vous vouliez la paix, vous vouliez sauver l'honneur: vous aurez la guerre et le déshonneur!"
        ]

            # Confucius
        confucius = [
            u"Agis avec gentillesse, mais n'attends pas de la reconnaissance.",
            u"Agissez envers les autres comme vous aimeriez qu'ils agissent envers vous.",
            u"Apprendre sans réfléchir est vain. Réfléchir sans apprendre est dangereux.",
            u"Après une faute, ne pas se corriger, c'est la vraie faute.",
            u"Avoir assez d'empire sur soi-même pour juger des autres par comparaison avec nous, et agir envers eux, comme nous voudrions que l'on agît envers nous-mêmes, c'est ce qu'on peut appeler la doctrine de l'humanité; il n'y a rien au-delà.",
            u"C'est seulement quand le froid de l'hiver est arrivé qu'on s'aperçoit que le pin et le cyprès perdent leurs feuilles après tous les autres arbres.",
            u"C'est un tort égal de pécher par excès ou par défaut.",
            u"Ce n'est pas un malheur d'être méconnu des hommes, mais c'est un malheur de les méconnaître.",
            u"Ce que tu ne voudrais pas que l'on te fasse, ne l'inflige pas aux autres.",
            u"Celui qui a une conduite vicieuse et ne se corrige pas, celui-là peut être appelé vicieux.",
            u"Celui qui aime à apprendre est bien près du savoir.",
            u"Celui qui dans ses entreprises cherche uniquement son intérêt propre excite beaucoup de mécontentement.",
            u"Celui qui déplace la montagne, c'est celui qui commence à enlever les petites pierres.",
            u"Celui qui est sévère envers lui-même et indulgent envers les autres évite les mécontentements.",
            u"Celui qui gouverne un peuple en lui donnant de bons exemples est comme l'étoile polaire, qui demeure immobile pendant que toutes les autres se meuvent autour d'elle.",
            u"Celui qui ne craint pas de promettre de grandes choses a de la peine à les exécuter.",
            u"Celui qui ne progresse pas chaque jour, recule chaque jour.",
            u"Celui qui ne réfléchit pas et n'établit pas son plan longtemps à l'avance trouvera les difficultés à sa porte.",
            u"Celui qui ne sait pas ce que c'est que la vie, comment saura-t-il ce que c'est que la mort?",
            u"Celui qui plante la vertu ne doit pas oublier de l'arroser souvent.",
            u"Celui qui repasse dans son esprit ce qu'il sait déjà, et par ce moyen acquiert de nouvelles connaissances, pourra bientôt enseigner les autres.",
            u"Celui qui sait obéir saura ensuite commander.",
            u"Celui qui se livre à l'étude de la sagesse a en vue les émoluments qu'il en peut retirer.",
            u"Celui qui, à quarante ans, est encore haï, le restera jusqu'à la fin de ses jours.",
            u"Ceux dont la connaissance est innée sont des hommes tout à fait supérieurs. Puis viennent ceux qui acquièrent cette connaissance par l'étude. Enfin, ceux qui, même dans la détresse, n'étudient pas: c'est le peuple.",
            u"Ceux qui vivent avec extravagance sont facilement vains, et ceux qui mènent une vie simple sont facilement vulgaires. Je préfère les gens vulgaires aux snobs.",
            u"Chaque classe d'hommes tombe dans un excès qui lui est particulier. On peut connaître la vertu d'un homme en observant ses défauts.",
            u"Choisissez un travail que vous aimez et vous n'aurez pas à travailler un seul jour de votre vie.",
            u"Comment un homme dépourvu des vertus qui sont propres à l'homme peut-il cultiver la musique?",
            u"Dépasser le but, c'est ne pas l'atteindre.",
            u"Dépasser les limites n'est pas un moindre défaut que de rester en deçà.",
            u"Deux hommes qui suivent des voies différentes ne peuvent se rencontrer.",
            u"Ecoutez beaucoup, afin de diminuer vos doutes; soyez attentif à ce que vous dites, afin de ne rien dire de superflu; alors, vous commettrez rarement des fautes.",
            u"Entendre les plaideurs et rendre la justice, je le puis tout comme un autre. L'important serait de faire qu'il n'y eût plus de plaideurs.",
            u"Entendre ou lire sans réfléchir est une occupation vaine; réfléchir sans livre ni maître est dangereux.",
            u"Est vraiment sage celui qui, sans présumer d'avance qu'on cherche à le tromper ou qu'on se méfie de lui, est capable de déjouer au moment voulu les ruses.",
            u"Etre riche et honoré par des moyens iniques, c'est comme le nuage flottant qui passe.",
            u"Etudier tout en répétant, n'est-ce pas source de plaisir?",
            u"Examine si ce que tu promets est juste et possible, car la promesse est une dette.",
            u"Exige beaucoup de toi-même et attends peu des autres. Ainsi beaucoup d'ennuis te seront épargnés.",
            u"Faire quelque chose de remarquable vaut mieux qu'être remarqué.",
            u"Hélas! Je n'ai encore vu personne qui aimât la vertu comme on aime la beauté corporelle.",
            u"Il est des jeunes pousses destinées à ne jamais fleurir. Il en est d'autres qui fleurissent mais ne portent jamais de fruits.",
            u"Il est parfois des moissons qui n'arrivent pas à fleurir; il en est aussi qui, après avoir fleuri, n'ont pas de grain.",
            u"Il est rare de trouver un homme qui se livre trois ans à l'étude, sans avoir en vue un salaire.",
            u"Il fait bon s'étendre, la tête reposée sur son bras replié, après un frugal repas de légumes, arrosé d'un verre d'eau.",
            u"Il faut que le disciple de la sagesse ait le coeur grand et courageux. Le fardeau est lourd et le voyage est long.",
            u"Il faut se garder de trois fautes: parler sans y être invité, ce qui est impertinence; ne pas parler quand on y est invité, ce qui est de la dissimulation; parler sans observer les réactions de l'autre, ce qui est de l'aveuglement.",
            u"Il n'est pas nécessaire d'aller vite, le tout est de ne pas s'arrêter.",
            u"Il n'y a que les pères et les mères qui s'affligent véritablement de la maladie de leurs enfants.",
            u"J'entends et j'oublie. - Je vois et je me souviens. - Je fais et je comprends.",
            u"Je n'ai pas encore vu un homme qui ait pu apercevoir ses défauts et qui s'en soit blâmé intérieurement.",
            u"Je ne cherche pas à connaître les réponses, je cherche à comprendre les questions.",
            u"Je ne m'attends pas à trouver un saint aujourd'hui. Si je pouvais seulement trouver un sage, je m'en contenterais.",
            u"Je ne peux rien pour qui ne se pose pas de questions.",
            u"Je ne puis apprendre à parler à qui ne s'efforce pas de parler.",
            u"Je ne veux ni ne rejette rien absolument, mais je consulte toujours les circonstances.",
            u"Je voudrais que les vieillards puissent vivre en paix, que tous les amis soient fidèles et que les jeunes gens aiment leurs aînés.",
            u"Jen K'iou dit: «Maître, ce n'est pas que votre Voie me déplaise; mais je n'ai pas la force de la mettre en pratique.» Le Maître répondit: «Celui qui vraiment n'en a pas la force tombe épuisé à mi-chemin. Quant à vous, vous vous assignez des limites.»",
            u"Ki houen Sseu réfléchissait à plusieurs reprises avant de faire une chose. Le Maître, l'ayant appris, dit: «Il suffit de réfléchir deux fois.»",
            u"L'archer a un point commun avec l'homme de bien: quand sa flèche n'atteint pas le centre de la cible, il en cherche la cause en lui-même.",
            u"L'énergie des esprits est abondante. On la regarde sans la voir. On l'écoute sans l'entendre. Sa substance et sa forme ne peuvent être perçues. Bien que l'on ne puisse la toucher, elle est manifeste, pareille à l'Océan, et sa réalité ne peut être niée.",
            u"L'erreur est égale, que l'on dépasse les bornes ou que l'on reste en deçà.",
            u"L'expérience est une bougie qui n'éclaire que celui qui la porte.",
            u"L'expérience est une lanterne attachée dans notre dos, qui n'éclaire que le chemin parcouru.",
            u"L'homme accompli ne craint pas d'apprendre même de ses subordonnés.",
            u"L'homme de bien chérit la vertu, l'homme de peu les bien matériels. L'homme de bien porte en lui le sens de la loi, l'homme de peu ne pense que privilèges.",
            u"L'homme de bien est droit et juste, mais non raide et inflexible; il sait se plier mais pas se courber.",
            u"L'homme de bien ne demande rien qu'à lui-même; l'homme de peu demande tout aux autres.",
            u"L'homme de bien préfère être lent à parler mais prompt à agir.",
            u"L'homme de bien se révèle dans les grandes occasions; l'homme de peu ne s'accomplira jamais que dans les petites tâches.",
            u"L'homme de bien situe la justice au-dessus de tout. Un homme de bien qui a la bravoure mais qui ignore la justice sera un rebelle. L'homme médiocre qui a la bravoure mais qui ignore la justice sera un brigand.",
            u"L'homme honorable commence par appliquer ce qu'il veut enseigner; ensuite il enseigne.",
            u"L'homme sage apprend de ses erreurs, - L'homme plus sage apprend des erreurs des autres.",
            u"L'homme sage n'est pas comme un vase ou un instrument qui n'a qu'un usage; il est apte à tout.",
            u"L'homme supérieur c'est celui qui d'abord met ses paroles en pratique, et ensuite parle conformément à ses actions.",
            u"L'homme supérieur demande tout à lui-même; l'homme vulgaire demande tout aux autres.",
            u"L'homme supérieur est amical sans être familier; l'homme vulgaire est familier sans être amical.",
            u"L'homme supérieur est celui qui a une bienveillance égale pour tous, et qui est sans égoïsme et sans partialité.",
            u"L'homme supérieur est influencé par la justice; l'homme vulgaire est influencé par l'amour du gain.",
            u"L'homme supérieur ne se tourmente pas.",
            u"L'homme supérieur se tient dans le juste milieu.",
            u"L'homme vulgaire est celui qui n'a que des sentiments d'égoïsme sans disposition bienveillante pour tous les hommes en général.",
            u"L'invariabilité dans le milieu est ce qui constitue la vertu.",
            u"L'ouvrier qui veut bien faire son travail doit commencer par aiguiser ses instruments.",
            u"La conduite du sage est sans saveur, comme l'eau.",
            u"La connaissance est la clé du pouvoir, de la sagesse.",
            u"La conscience est la lumière de l'intelligence pour distinguer le bien du mal.",
            u"La joie est en tout; il faut savoir l'extraire.",
            u"La nature fait les hommes semblables, la vie les rend différents.",
            u"La prodigalité conduit à l'arrogance, et la parcimonie à l'avarice. L'arrogance est pire que l'avarice.",
            u"La sagesse parfaite est-elle si éloignée après tout? Quand je désire la trouver, elle est à portée de ma main.",
            u"La vertu attire toujours la vertu.",
            u"La vertu ne reste pas comme une orpheline abandonnée.",
            u"La Vertu ne va jamais seule; elle attire toujours des imitateurs.",
            u"La vie de l'homme dépend de sa volonté: sans volonté, elle serait abandonnée au hasard.",
            u"La voie du juste milieu n'est pas suivie. Les hommes intelligents vont au-delà, les ignorants restent en deçà. Les sages veulent trop faire, et l'homme de peu pas assez. C'est ainsi que tout homme boit et mange, et peu savent juger des saveurs.",
            u"La vraie faute est celle qu'on ne corrige pas.",
            u"Le bois pourri ne peut être sculpté.",
            u"Le coeur de la femme est aussi instable qu'une goutte d'eau sur une fleur de lotus.",
            u"Le commerce du sage est sans valeur et il perfectionne; le commerce de l'homme de peu est agréable, et il corrompt.",
            u"Le contentement apporte le bonheur, même dans la pauvreté. Le mécontentement apporte la pauvreté même dans la richesse.",
            u"Le Maître ne parlait pas des choses extraordinaires, ni des actes de violence, ni des troubles, ni des esprits.",
            u"Le milieu est le point le plus voisin de la sagesse, il vaut autant ne pas l'atteindre que le dépasser.",
            u"Le premier axiome de l'humanisme confucéen est: - Etudier, apprendre par l'expérience.",
            u"Le prince ne doit pas craindre de n'avoir pas une population nombreuse, mais de ne pas avoir une juste répartition des biens.",
            u"Le problème des hommes, c'est qu'ils négligent leur propre champ pour aller ensemenser celui des autres.",
            u"Le sage a honte de ses défauts, mais n'a pas honte de s'en corriger.",
            u"Le sage demande à lui-même la cause de ses fautes, l'insensé la demande aux autres.",
            u"Le sage donne son principal soin à la racine.",
            u"Le sage est calme et serein. L'homme de peu est toujours accablé de soucis.",
            u"Le silence est un ami qui ne trahit jamais.",
            u"Le tout est plus grand que la somme des parties.",
            u"Les anciens étaient avares de mots par crainte de ne pouvoir les confirmer dans leurs actes.",
            u"Les fautes des hommes sont relatives à l'état de chacun.",
            u"Les pères ne veulent pas reconnaître les défauts de leurs enfants, ni les laboureurs la fertilité de leurs terres.",
            u"Lorsque l'on se cogne la tête contre un pot et que cela sonne creux, ça n'est pas forcément le pot qui est vide.",
            u"Lorsque les mots perdent leur sens, les gens perdent leur liberté.",
            u"Lorsque tu fais quelque chose, sache que tu auras contre toi, ceux qui voudraient faire la même chose, ceux qui voulaient le contraire, et l'immense majorité de ceux qui ne voulaient rien faire.",
            u"Lorsque vous travaillez pour les autres, faites-le avec autant d'ardeur que si c'était pour vous-même.",
            u"Mieux vaut étudier que jeûner tout un jour et veiller toute une nuit pour méditer en vain.",
            u"Ne cherchez pas à vous immiscer dans les affaires dont vous n'avez pas la charge.",
            u"Ne choisis tes amis que parmi tes égaux.",
            u"Ne parlez jamais de vous, ni en bien, car on ne vous croirait pas, ni en mal car on ne vous croirait que trop.",
            u"Ne pas instruire qui peut comprendre vos paroles c'est l'appauvrir. Instruire qui ne peut comprendre est perdre ses paroles. Le sage ne fait ni l'un ni l'autre.",
            u"Ne pas se laisser imprégner par les calomnies, ni se laisser meurtrir par les accusations; cela peut s'appeler lucidité. Ne pas se laisser imprégner par les calomnies, ni se laisser meurtrir par les accusations, c'est la lucidité d'un homme qui voit loin.",
            u"Ne vous affligez pas de ce que les hommes ne vous connaissent pas; affligez-vous de ne pas connaître les hommes.",
            u"Ne vous souciez pas d'être sans emploi; souciez-vous plutôt d'être digne d'un emploi. Ne vous souciez pas de n'être pas remarqué; cherchez plutôt à faire quelque chose de remarquable.",
            u"Ne vous souciez pas de n'être pas remarqué; cherchez plutôt à faire quelque chose de remarquable.",
            u"Négligez et vous perdrez. Cherchez et vous trouverez. Mais chercher ne conduit à trouver que si nous cherchons ce qui est en nous.",
            u"Notre plus grande gloire n'est point de tomber, mais de savoir nous relever chaque fois que nous tombons.",
            u"Nous sommes frères par la nature, mais étrangers par l'éducation.",
            u"Nulle pierre ne peut être polie sans friction, nul homme ne peut parfaire son expérience sans épreuve.",
            u"On ne doit jamais penser à la distance, quelle qu'elle soit, qui nous sépare de la vertu.",
            u"On peut connaître la vertu d'un homme en observant ses défauts.",
            u"On peut forcer le peuple à suivre les principes de la justice et de la raison; on ne peut pas le forcer à les comprendre.",
            u"On peut tuer le général d'une armée mais non l'ambition dans le coeur de l'homme.",
            u"On s'égare rarement en s'imposant soi-même des règles sévères.",
            u"On trouve des disciples de la sagesse qui ne sont pas parfaits; on n'a jamais vu un homme sans principes qui fût parfait.",
            u"Oublie les injures, n'oublie jamais les bienfaits.",
            u"Pas trop d'isolement; pas trop de relations; le juste milieu, voilà la sagesse.",
            u"Plutôt que de maudire les ténèbres, allumons une chandelle, si petite soit-elle.",
            u"Quand l'oiseau est prés de mourir, son chant devient triste; quand l'homme est prés de mourir, ses paroles portent l'empreinte de la vertu.",
            u"Quand la haine ou la faveur de la multitude s'attache à un homme, il faut examiner pourquoi.",
            u"Quand les riches maigrissent, les pauvres crèvent.",
            u"Quand on désire savoir, on interroge. Quand on veut être capable, on étudie. Revoyez sans arrêt ce que vous savez déjà. Etudiez sans cesse du nouveau. Alors vous deviendrez un Maître.",
            u"Quand on lui montre la lune du doigt, l'imbécile regarde le doigt.",
            u"Quand on ne sait pas ce qu'est la vie, comment pourrait-on connaître la mort?",
            u"Quand on peut accomplir sa promesse sans manquer à la justice, il faut tenir sa parole.",
            u"Quand père et fils sont d'accord, la famille prospère.",
            u"Quand un homme a faim, mieux vaut lui apprendre à pêcher que de lui donner un poisson.",
            u"Quand un prince se conduit en prince, un ministre en ministre, un père en père, un fils en fils, un pays est gouverné.",
            u"Quand vous plantez une graine une fois, vous obtenez une seule et unique récolte. Quand vous instruisez les gens, vous en obtenez cent.",
            u"Quand vous voyez un homme sage, pensez à l'égaler en vertu. Quand vous voyez un homme dépourvu de sagesse, examinez-vous vous-même.",
            u"Quatre chevaux attelés ne peuvent ramener dans la bouche des paroles imprudentes.",
            u"Que j'ai donc de la chance! Toutes les fois que je commets une erreur, il y a toujours quelqu'un pour la découvrir.",
            u"Que l'on s'efforce d'être pleinement humain et il n'y aura plus de place pour le mal.",
            u"Qui comprend le nouveau en réchauffant l'ancien peut devenir un maître.",
            u"Qui ne connaît la valeur des mots ne saurait connaître les hommes.",
            u"Qui ne se préoccupe pas de l'avenir lointain, se condamne aux soucis immédiats.",
            u"Qui se laisse guider par son seul profit s'attire haine et rancune.",
            u"Quiconque a entendu les cris d'un animal qu'on tue ne peut plus jamais manger de sa chair.",
            u"Rappelle-toi que ton fils n'est pas ton fils, mais le fils de son temps.",
            u"Rendez le bien pour le bien et la justice pour le mal.",
            u"Rien n'est jamais sans conséquence, - En conséquence, rien n'est jamais gratuit.",
            u"Rien ne sert de parler des choses qui sont déjà accomplies, ni de faire des remontrances sur celles qui sont déjà très avancées, ni de blâmer ce qui est passé.",
            u"Sans principes communs, ce n'est pas la peine de discuter.",
            u"Savoir que l'on sait ce que l'on sait, et savoir que l'on ne sait pas ce que l'on ne sait pas: voilà la véritable science.",
            u"Se peut-il qu'un homme soit moins sage qu'un oiseau?",
            u"Se regarder scrupuleusement soi-même, ne regarder que discrètement les autres.",
            u"Se vaincre soi-même, rendre à son coeur l'honnêteté qu'il tenait de la nature, voilà la vertu parfaite ... Il dépend de chacun d'être parfaitement vertueux.",
            u"Si l'homme a deux oreilles et une bouche, c'est pour écouter deux foix plus qu'il ne parle.",
            u"Si tu veux juger des moeurs d'un peuple, écoute sa musique.Si tu sais aimer les bonnes choses de la vie, tu sais aussi aimer la vertu.",
            u"Si vous refusez d'instruire un homme qui a les dispositions requises, vous perdez un homme. Si vous enseignez un homme qui n'a pas les dispositions nécessaires, vous perdez vos instructions. Un sage ne perd ni les hommes ni ses enseignements.",
            u"Sous un bon gouvernement, la pauvreté est une honte; sous un mauvais gouvernement, la richesse est aussi une honte.",
            u"Trois sortes d'amis sont utiles, trois sortes d'amis sont néfastes. - Les utiles: un ami droit, un ami fidèle, un ami cultivé. - Les néfastes: un ami faux, un ami mou, un ami bavard.",
            u"Tuer un homme pour sauver le monde, ce n'est pas agir pour le bien du monde. S'immoler soi-même pour le bien du monde, voilà qui est bien agir.",
            u"Un bol de riz avec de l'eau et le coude pour oreiller, voilà un état qui a sa satisfaction.",
            u"Un homme de bien est celui qui ne prêche pas ce qu'il faut faire tant qu'il n'a pas fait ce qu'il prône.",
            u"Un homme dépourvu de sincérité et de fidélité est un être incompréhensible à mes yeux. C'est un grand char sans flèche, un petit char sans timon; comment peut-il se conduire dans le chemin de la vie?",
            u"Un homme sans foi: je ne sais ce qu'il faut en faire. Un grand char sans joug, un petit char sans collier, comment peut-on le faire avancer?",
            u"Un mot perd l'affaire, un homme détermine le sort d'un empire.",
            u"Un prince sage donne aux choses les noms qui leur conviennent, et chaque chose doit être traitée d'après la signification du nom qu'il lui donne.",
            u"Une image vaut mille mots.",
            u"Une injustice n'est rien, si on parvient à l'oublier.",
            u"Une petite impatience ruine un grand projet.",
            u"Veux-tu apprendre à bien vivre, apprends auparavant à bien mourir.",
            u"Veux-tu que je t'enseigne le moyen d'arriver à la connaissance? Ce qu'on sait, savoir qu'on le sait; ce qu'on ne sait pas, savoir qu'on ne le sait pas: c'est savoir véritablement.",
            u"Vous ne savez pas comment servir les hommes. - Comment sauriez-vous servir les dieux?"
        ]

        # D
            # Jacques Boularan Deval
        deval = [
            u"A la caserne, on ne fait rien, mais on le fait tôt et ensemble.",
            u"Ce qui suffit à notre bonheur ne suffit pas toujours à notre plaisir.",
            u"Connais-toi, mais réserve-toi des surprises.",
            u"Dieu aima les oiseaux et inventa les arbres. L'homme aima les oiseaux et inventa les cages.",
            u"Il arrive souvent de ne rien obtenir parce que l'on ne tente rien.",
            u"Il faut trois jours à la Justice pour décider de la mort d'un homme, et des années pour décider d'un héritage.",
            u"Il ne manque aux douceurs de la solitude que de pouvoir être endurées.",
            u"L'amitié vit de silence, l'amour en meurt.",
            u"L'unique liberté des peuples est celle de changer de maîtres.",
            u"La vieillesse, c'est, dans la vie d'un homme, l'époque où, quand il flirte, il ne peut plus se rappeler pourquoi.",
            u"Le bonheur qu'on veut avoir gâte celui qu'on a déjà.",
            u"Le médecin fait souvent plus de bien en arrivant qu'il n'en a fait en sortant.",
            u"Notre corps est une demeure dont - avec l'âge - il faut condamner des pièces faute de pouvoir les chauffer toutes.",
            u"On fait beaucoup pour gagner un coeur mais très peu pour le garder.",
            u"Plus un secret a de gardiens, plus il s'échappe.",
            u"Quand une science est à bout d'arguments, elle élargit son vocabulaire.",
            u"Tel n'est frugal que par égard pour sa luxure.",
            u"Tous les sots sont périlleux.",
            u"Un bon livre est celui qu'on trouve toujours plein après l'avoir vidé.",
            u"Un désespoir d'amour n'est éternel que si l'on meurt tout de suite.",
            u"Un grand auteur dramatique est celui qui n'écrit pas que de mauvaises pièces.",
            u"Une joie partagée est une double joie. Un chagrin partagé est un demi-chagrin."
        ]

            # Will Durant
        durant = [
            u"Toute science commence comme philosophie et se termine en art."
        ]

        # E
            # Thomas Alva Edison
        edison = [
            u"Je n'ai pas échoué. J'ai juste trouvé 10 000 moyens qui ne fonctionnent pas.",
            u"Je ne me décourage pas car toute tentative infructueuse qu'on laisse derrière soi constitue un autre pas en avant.",
            u"Je vais rendre l'électricité si bon marché que seuls les riches pourront se payer le luxe d'utiliser des bougies.",
            u"La valeur d'une idée dépend de son utilisation.",
            u"Le génie est fait de un pour cent d'inspiration et de quatre-vingt-dix-neuf pour cent de transpiration.",
            u"S'il y a une meilleure façon de le faire... trouvez-la!"
        ]

            # Albert Einstein
        einstein = [
            u"(Einstein parle de la géométrie d'Euclide) - Si quelqu'un, en l'éveil de son intelligence, n'a pas été capable de s'enthousiasmer pour une telle architecture, alors jamais il ne pourra réellement s'initier à la recherche théorique.",
            u"Avec la gloire, je deviens de plus en plus stupide, ce qui, je le reconnais, est un phénomène très courant.",
            u"C'est la théorie qui décide de ce que nous pouvons observer.",
            u"C'est le devoir de chaque homme de rendre au monde au moins autant qu'il en a reçu.",
            u"C'est le rôle essentiel du professeur d'éveiller la joie de travailler et de connaître.",
            u"Ce n'est pas à cause de l'attraction terrestre que des gens tombent... amoureux!",
            u"Ce qu'il y a de plus incompréhensible dans l'univers, c'est qu'il soit compréhensible.",
            u"Ce qui fait la vraie valeur d'un être humain, c'est de s'être délivré de son petit moi.",
            u"Ce qui m'intéresse vraiment c'est de savoir si Dieu avait un quelconque choix en créant le monde.",
            u"Celui qui ne peut plus éprouver ni étonnement ni surprise est pour ainsi dire mort; ses yeux sont éteints.",
            u"Celui qui ressent sa propre vie et celle des autres comme dénuées de sens est fondamentalement malheureux, puisqu'il n'a aucune raison de vivre.",
            u"Cette conviction, liée à un sentiment profond d'une raison supérieure, se dévoilant dans le monde de l'expérience, traduit pour moi l'idée de Dieu.",
            u"Ceux qui aiment marcher en rangs sur une musique: ce ne peut être que par erreur qu'ils ont reçu un cerveau, une moelle épinière leur suffirait amplement.",
            u"Chère postérité, si tu n'es pas devenue plus juste, plus pacifique et de façon générale plus rationnelle que nous ne le sommes, alors que le diable t'emporte. Après avoir exprimé ce voeu pieux avec tout mon respect, je suis, ou j'étais, votre Albert Einstein",
            u"Définissez-moi d'abord ce que vous entendez par Dieu et je vous dirai si j'y crois.",
            u"Deux choses sont infinies: l'univers et la bêtise humaine, en ce qui concerne l'univers, je n'en ai pas acquis la certitude absolue.",
            u"Dieu est subtil, mais il n'est pas malveillant.",
            u"Dieu ne joue pas aux dés.",
            u"En apparence, la vie n'a aucun sens, et pourtant, il est impossible qu'il n'y en ait pas un!",
            u"Il devient indispensable que l'humanité formule un nouveau mode de pensée si elle veut survivre et atteindre un plan plus élevé.",
            u"Il est étrange que la science, qui jadis semblait inoffensive, se soit transformée en un cauchemar faisant trembler tout le monde.",
            u"Il est hélas devenu évident aujourd'hui que notre technologie a dépassé notre humanité.",
            u"Il est plus difficile de désagréger un préjugé qu'un atome.",
            u"Il n'existe pas d'autre éducation intelligente que d'être soi-même un exemple, même si l'on ne pouvait empêcher que ce fût un monstre!",
            u"Il n'y a rien de tel qu'une question idiote, seulement une réponse idiote.",
            u"Il y a deux façons de concevoir sa vie. - Une est de penser que les miracles n'existent pas - et l'autre de penser que chaque chose est un miracle.",
            u"Inventer, c'est penser à côté.",
            u"J'affirme que le sentiment religieux cosmique est le motif le plus puissant et le plus noble de la recherche scientifique.",
            u"J'aime penser que la lune est là même si je ne la regarde pas.",
            u"J'ignore la nature des armes qu'on utilisera pour la prochaine guerre mondiale. Mais pour la quatrième, on se battra à coup de pierres.",
            u"Je détermine l'authentique valeur d'un homme d'après une seule règle: à quel degré et dans quel but l'homme s'est libéré de son Moi?",
            u"Je n'ai pas de talents particuliers. Je suis juste passionnément curieux.",
            u"Je n'ai pas échoué, j'ai trouvé dix mille moyens qui ne fonctionnent pas.",
            u"Je ne dors pas longtemps, mais je dors vite.",
            u"Je ne pense jamais au futur. Il vient bien assez tôt.",
            u"Je sais pourquoi tant de gens aiment couper du bois. C'est une activité où l'on voit tout de suite le résultat.",
            u"Je suis réellement un homme quand mes sentiments, mes pensées et mes actes n'ont qu'une finalité: celle de la communauté et de son progrès.",
            u"Je suis satisfait de ma vie ces dernières années. J'ai gardé ma bonne humeur et je ne prends ni moi-même ni les autres au sérieux.",
            u"Je veux connaître les pensées de Dieu; tout le reste n'est que détail.",
            u"L'école devrait toujours avoir pour but de donner à ses élèves une personnalité harmonieuse, et non de les former en spécialiste.",
            u"L'effort d'unir sagesse et pouvoir aboutit rarement et seulement très brièvement.",
            u"L'effort vers la connaissance représente un de ces buts indépendants, sans lesquels, pour moi, une affirmation consciente de la vie n'existe pas pour l'homme qui déclare penser.",
            u"L'enseignement devrait être ainsi: celui qui le reçoit le recueille comme un don inestimable mais jamais comme une contrainte pénible.",
            u"L'ensemble de ce qui compte ne peut pas être compté, et l'ensemble de ce qui peut être compté ne compte pas.",
            u"L'escalier de la science est l'échelle de Jacob, il ne s'achève qu'aux pieds de Dieu.",
            u"L'Etat est notre serviteur et nous n'avons pas à en être les esclaves.",
            u"L'éternel mystère du monde est son intelligibilité.",
            u"L'étude, en général, la poursuite de la vérité et la beauté sont des domaines dans lesquels il nous est permis de rester enfant toute la vie.",
            u"L'extrême netteté, la clarté, et la certitude ne s'acquièrent qu'au prix d'un immense sacrifice: la perte de la vue d'ensemble.",
            u"L'homme et sa sécurité doivent constituer la première préoccupation de toute aventure technologique.",
            u"L'homme évite habituellement d'accorder de l'intelligence à autrui, sauf quand par hasard il s'agit d'un ennemi.",
            u"L'homme solitaire pense seul et crée des nouvelles valeurs pour la communauté.",
            u"L'idée qu'un électron exposé à un rayonnement choisit en toute liberté la manière ou la direction où il doit sauter m'est insupportable. S'il en était ainsi, j'aimerais mieux être cordonnier ou même employé dans un bistrot que physicien.",
            u"L'imagination est plus importante que le savoir.",
            u"La bureaucratie réalise la mort de toute action.",
            u"La chose la plus difficile à comprendre au monde c'est l'impôt sur le revenu!",
            u"La connaissance s'acquiert par l'expérience, tout le reste n'est que de l'information.",
            u"La croyance dans l'action des démons se trouve à la racine de notre concept de causalité.",
            u"La distinction entre le passé, le présent et le futur n'est qu'une illusion, aussi tenace soit-elle.",
            u"La fantaisie est plus importante que le savoir.",
            u"La folie est de toujours se comporter de la même manière et de s'attendre à un résultat différent.",
            u"La joie de contempler et de comprendre, voilà le langage que me porte la nature.",
            u"La majorité des imbéciles reste invincible et satisfaite en toutes circonstances.",
            u"La perfection des moyens et la confusion des buts semblent caractériser notre époque.",
            u"La personnalité créatrice doit penser et juger par elle-même car le progrès moral de la société dépend exclusivement de son indépendance. Sinon la société est inexorablement vouée à l'échec, comme l'être humain privé de la possibilité de communiquer.",
            u"La pire des institutions grégaires se prénomme l'armée. Je la hais. Si un homme peut éprouver quelque plaisir à défiler en rang et aux sons d'une musique, je méprise cet homme... Il ne mérite pas un cerveau humain puisqu'une moelle épinière le satisfait.",
            u"La plus belle chose que nous puissions éprouver, c'est le côté mystérieux de la vie. C'est le sentiment profond qui se trouve au berceau de l'art et de la science véritable.",
            u"Les Etats-Unis d'Amérique forment un pays qui est passé directement de la barbarie à la décadence sans jamais avoir connu la civilisation.",
            u"Les grands esprits ont toujours rencontré une opposition farouche des esprits médiocres.",
            u"Les machines un jour pourront résoudre tous les problèmes, mais jamais aucune d'entre elles ne pourra en poser un!",
            u"Mais c'est la personne humaine, libre, créatrice et sensible qui façonne le beau et le sublime, alors que les masses restent entraînées dans une ronde infernale d'imbécillité et d'abrutissement.",
            u"Mon idéal politique est l'idéal démocratique. Chacun doit être respecté en tant que personne, et personne ne doit être divinisé.",
            u"N'essayez pas de devenir un homme qui a du succès. - Essayez de devenir un homme qui a de la valeur.",
            u"Ne blâmez pas la loi de la gravité si vous tombez en amour.",
            u"Ne faites rien contre votre conscience, même si l'Etat vous le demande.",
            u"Ne t'inquiète pas si tu as des difficultés en maths, je peux t'assurer que les miennes sont bien plus importantes!",
            u"Nous aurons le destin que nous aurons mérité.",
            u"Passé un certain âge, lire détourne trop l'esprit de ses activités créatrices. Un homme qui lit trop et qui fait trop peu d'efforts cérébraux prend vite des habitudes de paresse d'esprit.",
            u"Peu d'être sont capables d'exprimer posément une opinion différente des préjugés de leur milieu. La plupart des êtres sont mêmes incapables d'arriver à formuler de telles opinions.",
            u"Placez votre main sur un poêle une minute et ça vous semble durer une heure. Asseyez vous auprès d'une jolie fille une heure et ça vous semble durer une minute. C'est ça la relativité.",
            u"Pour être un membre irréprochable parmi une communauté de moutons, il faut avant toute chose être soi-même un mouton.",
            u"Quand un scarabée aveugle rampe à la surface d'un globe, il ne remarque pas que le chemin qu'il a suivi est courbe; j'ai eu la chance de m'en apercevoir.",
            u"Que chacun raisonne en son âme et conscience, qu'il se fasse une idée fondée sur ses propres lectures et non d'après les racontars des autres.",
            u"Qui a fait l'expérience de penser dans un autre domaine l'emporte toujours sur celui qui ne pense pas du tout ou très peu.",
            u"Rare est le nombre de ceux qui regardent avec leurs propres yeux et qui éprouvent avec leur propre sensibilité.",
            u"Reconnaissons à la base de tout travail scientifique d'une certaine envergure, une conviction bien comparable au sentiment religieux, puisqu'elle accepte un monde fondé en raison, un monde intelligible!",
            u"Rendez les choses aussi simples que possible, mais pas plus simples.",
            u"Rien n'est jamais entièrement noir.",
            u"Rien n'est plus proche du vrai que le faux.",
            u"Rien ne peut être aussi bénéfique à la santé humaine et augmenter les chances de survie de la vie sur terre que d'opter pour une diète végétarienne.",
            u"S'il n'y a pas de prix à payer, c'est que cela ne vaut rien.",
            u"Se sacrifier au service de la vie équivaut à une grâce.",
            u"Si l'idée n'est pas a priori absurde, elle est sans espoir.",
            u"Si les faits ne correspondent pas à la théorie, changez les faits.",
            u"Si vous ne pouvez expliquer un concept à un enfant de six ans, c'est que vous ne le comprenez pas complètement.",
            u"Soit A un succès dans la vie. Alors A = x + y + z, où x = travailler, y = s'amuser, z = se taire.",
            u"Tout ce qui est vraiment grand et inspiré n'a été réalisé que par des individus travaillant librement.",
            u"Trois idéaux ont éclairé ma route et m'ont souvent redonné le courage d'affronter la vie avec optimisme: la bonté, la beauté et la vérité.",
            u"Un estomac creux n'est pas un bon conseiller politique.",
            u"Un être humain est une partie du tout que nous appelons «Univers»... Une partie limitée dans le Temps et dans l'Espace.",
            u"Un problème sans solution est un problème mal posé.",
            u"Une personne qui n'a jamais commis d'erreurs n'a jamais innové.",
            u"Vous n'êtes pas assez bon pour vous permettre d'être si modeste!",
            u"«Hasard» est le nom que Dieu prend quand il ne veut pas qu'on le reconnaisse."
        ]

        # F
            # Benjamin Franklin
        franklin = [
            u"A vingt ans, la volonté est reine; à trente, c'est l'esprit; à quarante, le jugement.",
            u"Aimes-tu la vie? Alors ne gaspille pas ton temps, car il est l'essence de la vie.",
            u"Aucune nation n'a jamais été ruinée par le commerce.",
            u"Ayez vos yeux bien ouverts avant de vous marier, et mi-clos quand vous serez mariés.",
            u"Cherche en les autres pour leurs vertus, en toi pour les vices.",
            u"Combien respecte la naissance du Christ! Combien respecte ces enseignements! Je suppose qu'il est plus facile de se souvenir des dates de vacances que de commandements!",
            u"Combien respectent la naissance du Christ! Combien respectent ces enseignements! Je suppose qu'il est plus facile de se souvenir des dates de vacances que de commandements!",
            u"Comme dit le bonhomme Richard, les femmes, le vin, le jeu et la mauvaise foi diminuent la fortune et augmentent les besoins. Il en coûte plus cher pour entretenir un vice, que pour élever deux enfants.",
            u"Dans toutes vos liaisons amoureuses, préférez plutôt les femmes mûres aux jeunes filles ... car elles ont une plus grande connaissance du monde.",
            u"Faute d'un clou le fer fut perdu, - Faute d'un fer le cheval fut perdu, - Faute d'un cheval le cavalier fut perdu, - Faute d'un cavalier la bataille fut perdue, - Faute d'une bataille le royaume fut perdu. - Et tout cela faute d'un clou de fer à cheval.",
            u"Femmes, vin, jeu et tromperie. - Font la fortune petite et les besoins grands.",
            u"Il est plus facile de résister au premier de ses désirs qu'à tous ceux qui le suivent.",
            u"Il n'y a jamais eu de bonne guerre ni de mauvaise paix.",
            u"Je ne dirai du mal de personne et je dirai tout le bien que je sais de tout le monde.",
            u"L'expérience est une école sévère, mais les fous n'apprendront dans aucune autre.",
            u"L'expérience tient une école où les leçons coûtent cher; mais c'est la seule où les insensés puissent s'instruire, comme dit le bonhomme Richard.",
            u"L'humanité se divise en trois catégories: ceux qui ne peuvent pas bouger, ceux qui peuvent bouger, et ceux qui bougent.",
            u"L'oisiveté est comme la rouille; elle use plus que le travail.",
            u"L'optimiste est celui qui croit que le mariage est moins onéreux que les fiançailles.",
            u"La bière est la preuve que Dieu nous aime et veut que nous soyons heureux.",
            u"La paresse chemine si lentement que la pauvreté la rattrape.",
            u"La possession de l'argent n'est avantageuse que par l'usage qu'on en fait.",
            u"Le bon sens, tout le monde en a besoin, peu l'ont et chacun croit l'avoir.",
            u"Le coeur du fou est dans sa bouche, mais la bouche du sage se trouve dans son coeur.",
            u"Le seul intérêt de l'argent est son emploi.",
            u"Les créanciers ont meilleure mémoire que les débiteurs.",
            u"Manger de la viande, c'est commettre un homicide involontaire.",
            u"Ne remettez pas au lendemain ce que vous pouvez faire le jour même.",
            u"On n'est jamais trop âgé pour s'instruire.",
            u"Où il y a mariage sans amour, il y aura amour sans mariage.",
            u"Quand il y a mariage sans amour, il y a amour sans mariage.",
            u"Quand on a bonne conscience, c'est Noël en permanence.",
            u"Qui boit vite paie lentement.",
            u"Qui ne veut être conseillé, ne peut être aidé.",
            u"Si l'homme réalisait la moitié de ses désirs, il doublerait ses peines.",
            u"Si les hommes sont si mauvais avec le secours de la religion, que seraient-ils sans elle?",
            u"Si quelqu'un vous dit qu'il est autre moyen de faire fortune que par le travail et l'économie, fuyez-le, c'est un imposteur.",
            u"Si vous voulez récolter les louanges, vous devez semer les graines. Mots gentils et actes utiles.",
            u"Si vous voulez savoir la valeur de l'argent, essayez d'en emprunter.",
            u"Souvenez-vous que le temps est de l'argent.",
            u"Tel qui vit d'espoir meurt à jeun.",
            u"Tout homme à deux patries: la sienne et puis la France.",
            u"Trois déménagements valent un incendie.",
            u"Tu me dis, j'oublie. Tu m'enseignes, je me souviens. Tu m'impliques, j'apprends.",
            u"Un clou manquait, et le cheval perdit son fer; à cause de ce fer manquant, le cheval fut perdu; n'ayant plus de cheval, le cavalier fut perdu; capturé et tué par l'ennemi, tout cela à cause d'un clou de fer à cheval.",
            u"Un sac vide tient difficilement debout.",
            u"Une grande beauté, une force formidable, de grandes richesses ne sont pas vraiment d'un grand intérêt; un coeur juste surpasse tout cela."
        ]

        # G
            # Edmond de Goncourt
        goncourt = [
            u"Au premier... Monsieur veut-il l'ascenseur? me jette le concierge.",
            u"Des pêcheurs improvisés débitent, à 2 francs pièce, des brochetons gros comme des goujons, pêchés on ne sait où.",
            u"Je ferais tirer une centaine d'épreuves sur papier collé et je m'amuserais à les aquareller de toutes les colorations qui se lèvent des brumes aqueuses de la Seine.",
            u"La barque du prince était suivie de batelets, où était la fine fleur des femmes de la haute société orléaniste.",
            u"Mon pauvre et cher frère ... qui n'a pas repris connaissance depuis jeudi à deux heures de l'après-midi. J'écoute l'anhélance de sa respiration.",
            u"Nittis a chez lui des vues de Paris, enlevées au pastel, qui m'enchantent. C'est l'air brouillardeux de Paris, c'est le gris de son pavé, c'est la silhouette diffuse du passant.",
            u"On a calculé qu'avec l'aurification des dents, générale chez tout le monde aux Etats-Unis, il y avait 750 millions d'or dans les cimetières.",
            u"Un modèle qu'il fait poser, lui a confié qu'à treize ans, elle avait perdu sa grand'mère, qu'on l'avait fait monter dans l'unique voiture de deuil avec un vieux parent, et que ce vieux parent l'avait dévirginisée, dans le trajet au cimetière."
        ]

        # H
            # Bob Hope
        hope = [
            u"Ils étaient très durs... Ils attachaient leurs tomates à l'extrémité d'un yo-yo, pour vous toucher deux fois.",
            u"L'âge, c'est lorsque les bougies commencent à coûter plus cher que le gâteau.",
            u"Les gens qui envoient des baisers sont de sacrés paresseux."
        ]

        # I


        # J
            # Thomas Jefferson
        jefferson = [
            u"C'est en général un voeu coupable que de souhaiter la guerre et le trouble entre les nations, mais ce souhait devient pieux lorsque c'est le seul moyen de dissoudre leurs combinaisons criminelles.",
            u"Dans la presse, seules les publicités disent la vérité.",
            u"Décidez que vous ne serez jamais oisif. Personne n'aura l'occasion de se plaindre qu'il n'a pas le temps s'il ne le prend jamais. C'est fabuleux ce que l'on peut faire quand on est toujours en train de faire quelque chose.",
            u"L'arbre de la liberté devrait, de temps en temps, être arrosé du sang des tyrans, car c'est un engrais naturel.",
            u"L'honnêteté est le premier chapitre du livre de la sagesse.",
            u"La paix, le commerce, une honnête amitié avec toutes les nations, d'étroites alliances avec aucune.",
            u"Les mères font les hommes.",
            u"Pour tout homme, le premier pays est sa patrie, et le second, c'est la France.",
            u"]e crois à la chance et je m'aperçois que, plus je travaille dur, plus j'en ai."
        ]


        # Juan Ramon Jimenez
        jimenez = [
            u"Qui apprend une nouvelle langue acquiert une nouvelle âme.",
            u"En chaque sens sont les cinq autres.",
            u"Qu'il est triste de tout aimer - sans savoir ce que l'on aime!",
            u"Qui apprend une nouvelle langue acquiert une nouvelle âme."
        ]

        # K
            # John Fitzgerald Kennedy
        kennedy = [
            u"A vouloir étouffer les révolutions pacifiques, on rend inévitables les révolutions violentes.",
            u"Certaines personnes voient les choses comme elles sont et se demandent: pourquoi? Moi, je vois les choses comme elles pourraient être et je me dit: pourquoi pas?",
            u"Ceux qui rendent une révolution pacifique impossible rendront une révolution violente inévitable.",
            u"Diriger et apprendre ne sont pas dissociables.",
            u"Il n'y a que lorsque nous possédons, avec certitude, des armes en quantité suffisante que nous aurons la certitude de ne pas nous en servir.",
            u"Il ne faut jamais se laisser abattre.",
            u"Il ne faut pas chercher à rajouter des années à sa vie - mais plutôt essayer de rajouter de la vie à ses années.",
            u"Il y a trois choses vraies: Dieu, la sottise humaine et le rire. Puisque les deux premières dépassent notre entendement, nous devons nous arranger au mieux avec la troisième.",
            u"L'art de la réussite consiste à savoir s'entourer des meilleurs.",
            u"L'art est le fruit de la créativité des gens libres.",
            u"L'humanité devra mettre un terme à la guerre, ou la guerre mettra un terme à l'humanité.",
            u"La grande révolution dans l'histoire de l'homme, passée, présente et future, est la révolution de ceux qui sont résolus à être libres.",
            u"La victoire a cent pères, mais la défaite est orpheline.",
            u"Le meilleur temps pour réparer sa toiture, c'est lorsque le soleil brille.",
            u"Le temps est un outil, pas un lit pour dormir.",
            u"Le vrai politique, c'est celui qui sait garder son idéal tout en perdant ses illusions.",
            u"N'oublions jamais que l'art n'est pas une forme de propagande; c'est une forme de vérité.",
            u"Ne demande pas ce que ton pays peut faire pour toi, demande ce que tu peux faire pour ton pays.",
            u"Ne négocions jamais avec nos peurs. Mais n'ayons jamais peur de négocier.",
            u"Ne nous reposons pas sur nos acquis, mais efforçons-nous de construire la paix, de vouloir que la paix soit dans le coeur et dans l'esprit de chacun.",
            u"Ne sacrifiez jamais vos convictions politiques pour être dans l'air du temps.",
            u"Nos problèmes ont été créés par l'homme et nous pouvons donc les résoudre. Nos possibilités ne connaissent pas de limites. Aucun problème humain ne va au delà de nos capacités.",
            u"Nos progrès en tant que nation dépendront de nos progrès en matière d'éducation. L'esprit humain est notre ressource fondamentale.",
            u"Nous avons besoin d'hommes qui savent rêver à des choses inédites.",
            u"Nous devons penser l'éducation comme un moyen de développer nos plus grandes capacités.",
            u"Nous devons utiliser le temps comme outil et non comme repose-pied.",
            u"Nous ne pourrons pas tout faire dans les cent premiers jours. Ni dans les mille premiers jours, ni pendant toute la durée de notre mandat, ni même peut-être pendant toute notre vie sur cette planète. Mais, commençons!",
            u"Nous ne pouvons assurer la paix qu'en préparant la guerre.",
            u"On connait une nation aux hommes qu'elle produit, mais aussi à ceux dont elle se souvient et qu'elle honore.",
            u"On ne savait pas que c'était impossible, alors on l'a fait.",
            u"Pardonnez à vos ennemis, mais n'oubliez jamais leurs noms.",
            u"Pourquoi tenez-vous tant à devenir Président? - - -Est-ce que vous réalisez la responsabilité que je porte? Je suis la seule personne entre Nixon et la Maison-Blanche.",
            u"Quand il est dur d'avancer, ce sont les durs qui avancent.",
            u"Quand le pouvoir pousse l'homme à l'arrogance, la poésie lui rappelle la richesse de l'existence. Quand le pouvoir corrompt, la poésie purifie.",
            u"Si la société libre ne parvient pas à améliorer le sort de la majorité des pauvres, elle ne pourra pas sauver la minorité des riches.",
            u"Si les découvertes scientifiques ont à la fois donné à l'humanité le pouvoir de créer et le pouvoir de détruire, alors elles sont en même temps un énorme défi et une grande épreuve.",
            u"Tout le monde veut le progrès. - Mais le progrès requiert le changement... - et le changement reste impopulaire.",
            u"Trop souvent nous nous contentons du confort de l'opinion sans faire l'effort de penser.",
            u"Un homme fait ce qu'il a à faire malgré les conséquences sur sa vie, les obstacles, les dangers et la pression; c'est la base de toute morale humaine.",
            u"Washington est une ville qui possède l'efficacité du Sud et le charme du Nord."
        ]

            # Soren Aabye Kierkegaard
        kierkegaard = [
            u"... il faut une grande prudence si on veut flatter.",
            u"... il n'est pas du tout difficile de séduire une jeune fille, mais d'en trouver une qui vaille la peine d'être",
            u"... il n'y a rien sur quoi plane autant de séduction et de malédiction que sur un secret.",
            u"... l'amour ne se trouve que dans la liberté, et ce n'est qu'en elle qu'il y a de la récréation et de l'amusement éternel.",
            u"... l'angoisse en soi n'est pas belle, elle ne l'est qu'à l'instant où l'on s'aperçoit de l'énergie qui la surmonte.",
            u"... la femme est substance, l'homme est réflexion.",
            u"... la nature féminine est un abandon sous forme de résistance.",
            u"... la vie est un chemin.",
            u"... on ne peut pas savoir ce qu'un homme en son désespoir peut songer à risquer.",
            u"... plus on se cache, plus il est désagréable d'être surpris.",
            u"... qu'est-ce que les romans nous apprennent de l'amour? Rien que des mensonges qui aident à abréger la tâche.",
            u"... quelle arme est aussi tranchante, aussi pénétrante, dans son mouvement aussi luisante et, grâce à cela, aussi décevante qu'un regard?",
            u"... un déshabillage spirituel.",
            u"... un moyen très utile pour se mettre en rapport avec une jeune fille, c'est de lui prêter des livres.",
            u"A chaque femme correspond un séducteur. Son bonheur, ce n'est que de le rencon",
            u"Amener une jeune fille à voir dans l'abandon total l'unique tâche de sa liberté.",
            u"Aussi longtemps que l'éternel et l'historique restent extérieurs l'un à l'autre, l'historique n'est que l'occasion.",
            u"C'est là le paradoxe suprême de la pensée que de vouloir découvrir quelque chose qu'elle-même ne puisse penser",
            u"C'est pourquoi tous ceux qui ont vraiment été au service de l'idéal ont aussi recommandé le célibat. Se marier rend notre rapport à l'idéal si difficile que c'est d'ordinaire synonyme d'y renoncer.",
            u"Car la nature féminine est un abandon sous forme de résistance.",
            u"Ce que les philosophes disent de la réalité est souvent aussi décevant que l'affiche qu'on a pu voir chez un marchand de bric-à-brac: «ici on repasse». Apporte-t-on son linge à repasser, on est dupé: l'enseigne est à vendre.",
            u"Croire, c'est, étant soi-même et voulant l'être, plonger en Dieu à travers sa propre transparence.",
            u"Dans une nuit sombre rien n'est plus dangereux pour les autres bateaux que de mettre des feux qui trompent plus que l'obscurité.",
            u"Derrière le monde dans lequel nous vivons, loin à l'arrière-plan, se trouve un autre monde; leur rapport réciproque ressemble à celui qui existe entre les deux scènes qu'on voit parfois au théâtre, l'une derrière l'autre.",
            u"Dès ma première enfance, une flèche de la douleur s'est plantée dans mon coeur. Tant qu'elle y reste, je suis ironique - si on l'arrache, je meurs.",
            u"En toute occasion où ma réflexion s'applique à l'amour, je ne retiens que contradiction.",
            u"Hélas, la porte du bonheur ne s'ouvre pas vers l'intérieur, et il ne sert donc à rien de s'élancer contre elle pour la forcer. Elle s'ouvre vers l'extérieur. Il n'y a rien à faire.",
            u"Il est révoltant qu'un homme dirige sur des sentiers faux un voyageur ignorant le chemin à prendre et le laisse ensuite seul dans son erreur. Cependant, n'est-il pas plus révoltant encore d'amener quelqu'un à se fourvoyer en lui-même?",
            u"Il est trop peu d'en aimer une seule... en aimer le plus grand nombre possible, voilà qui est jouir, voilà qui est vivre.",
            u"Il ne faut pas dire du mal du paradoxe, passion de la pensée: le penseur sans paradoxe est comme l'amant sans passion, une belle médiocrité.",
            u"J'ai trouvé en moi l'être le plus intéressant que je sache.",
            u"J'aimerais écrire une réplique au Journal du Séducteur. Ce serait une figure féminine - journal d'une hétaïre qui vaudrait la peine qu'on l'esquisse.",
            u"J'avouerai toujours qu'une jeune fille est une professeur-né et qu'on peut toujours apprendre d'elle, sinon autre chose, tout au moins l'art de la tromper ...",
            u"Je méprise un juge lorsqu'il arrache l'aveu d'un délinquant par la promesse de la liberté. Un tel juge renonce à sa force et à son talent.",
            u"Je parle de préférence avec de vieilles bonnes femmes qui racontent des potins de ménage, ensuite avec des fous et, en dernier lieu, avec des gens très raisonnables.",
            u"Je suis un ami de la liberté de penser, et aucune pensée n'est assez absurde pour que je n'aie pas le courage de la retenir.",
            u"L'amour est pourtant une chose simple, mais le mariage...",
            u"L'essentiel est de savoir déceler ce qu'une femme peut donner et ce que par suite, elle demande.",
            u"L'éternel féminin nous attire vers le bas.",
            u"L'idée que Dieu est amour, dans le sens qu'il est toujours le même, est si abstraite qu'au fond elle équivaut au scepticisme.",
            u"L'impossibilité de la communication directe est le secret de la souffrance du Christ.",
            u"L'individu, dans son angoisse non pas d'être coupable mais de passer pour l'être, devient coupable.",
            u"L'unique façon sérieuse de comprendre quelque chose est de devenir soi-même ce que l'on comprend.",
            u"La chrétienté a aboli le christianisme sans trop le savoir.",
            u"La femme sauve-t-elle par-ci par-là un homme de ses débauches et en fait un homme rangé, mais elle pervertit tous les hommes qui se marient en les enfermant dans la finitude et la médiocrité.",
            u"La galanterie ne coûte rien, elle est tout profit et elle est la condition de toute jouissance érotique. Elle est, de l'homme à la femme, le code secret de la volupté des sens.",
            u"La jouissance proprement dite ne réside pas dans la chose dont on jouit, mais dans l'idée qu'on s'en fait.",
            u"La meilleure preuve de la misère de l'existence est celle qu'on tire de la contemplation de sa magnificence.",
            u"La mère aimante apprend à son enfant à marcher seul.",
            u"La raison d'être de la chrétienté est de rendre si possible le christianisme impossible.",
            u"La résistance est le péché de l'intelligence.",
            u"La vie ne se comprend que par un retour en arrière, mais on ne la vit qu'en avant.",
            u"Le fond éternel de l'amour, c'est que les individus ne naissent l'un pour l'autre que dans son instant suprême.",
            u"Le génie ne désire jamais ce qui n'existe pas.",
            u"Le mariage est et restera le voyage de découverte le plus important que l'homme puisse entreprendre.",
            u"Le plaisir est décevant, les possibilités jamais.",
            u"Le réel n'est pas plus nécessaire que le possible, car le nécessaire est absolument différent des deux.",
            u"Les hommes sont vraiment absurdes. Ils n'usent jamais des libertés dont ils jouissent, mais ils réclament celles qu'ils n'ont pas; ils ont la liberté de pensée, ils demandent la liberté de parole.",
            u"Les jeunes filles parlent généralement avec beaucoup de dédain des hommes embarrassés, mais secrètement elles les aiment bien.",
            u"Manquer de possible signifie que tout nous est devenu nécessité et banalité.",
            u"Oh! Nature merveilleuse, profonde et énigmatique, tu donnes la parole aux hommes, mais l'éloquence du baiser aux jeunes filles!",
            u"On dit que l'expérience rend sage. Que de déraison dans ce propos! Sans rien au-dessus d'elle, c'est elle qui nous rendrait fou.",
            u"On eût dit que cet homme traversait la vie sans laisser de trace... et l'on peut même prétendre qu'il ne faisait pas de victimes.",
            u"On n'est jamais timide que dans la mesure où on est vu, mais on est toujours vu que dans la mesure où on voit.",
            u"On ne peut comprendre la vie qu'en regardant en arrière; on ne peut la vivre qu'en regardant en avant.",
            u"Plus on pense de façon objective, moins on existe.",
            u"Plutôt bien pendu que mal marié.",
            u"Pour un homme cultivé, voir une farce c'est comme jouer à la loterie, sans le désagrément de gagner de l'argent.",
            u"Prie pour avoir toujours tort à l'égard de Dieu.",
            u"Qu'aime l'amour? L'infinité. - Que craint l'amour? Des bornes.",
            u"Qu'il est beau d'être épris et intéressant de le savoir; ce n'est pas la même chose.",
            u"Quand deux êtres s'éprennent l'un de l'autre, il importe d'avoir le courage de rompre; car on a tout à perdre en persistant et rien à gagner.",
            u"Quand une jeune fille a tout donné, elle a tout perdu.",
            u"Que les gens sont absurdes! Ils ne se servent jamais des libertés qu'ils possèdent, mais réclament celles qu'ils ne possèdent pas; ils ont la liberté de pensée, ils exigent la liberté de parole.",
            u"Quel vin est aussi pétillant, savoureux, enivrant, que l'infini des possibles!",
            u"Quelqu'un qui parle comme un livre est extrêmement ennuyeux à écouter parfois, cependant, parler ainsi peut être utile, car, chose curieuse, un livre a ceci de particulier qu'il peut être interprété comme on veut.",
            u"S'introduire comme un rêve dans l'esprit d'une jeune fille est un art, en sortir est un chef-d'oeuvre.",
            u"Sans le péché, point de sexualité, et sans sexualité, point d'histoire.",
            u"Se taire est dans le camp de la réflexion, c'est savoir parler, notamment de toute autre chose.",
            u"Seuls les grands esprits sont exposés à ce que j'appelle des paradoxes, qui ne sont autre chose que des pensées grandioses, mais imparfaites.",
            u"Si on ne sait pas à un tel point se mettre en rapport avec l'âme d'une jeune fille, mieux vaut ne jamais se laisser aller à vouloir séduire, car il sera alors impossible d'éviter ces deux écueils: d'être questionné sur l'avenir et catéchisé sur la foi.",
            u"Si on ne sait pas faire de l'amour cet absolu auprès de quoi toute autre histoire disparaît, on ne devrait jamais se hasarder à aimer, même pas si on se mariait dix fois.",
            u"Toute jeune fille par rapport au labyrinthe de son coeur est une Ariane, qui tient le fil grâce auquel on peut s'y retrouver, mais elle ne sait s'en servir elle-même.",
            u"Toute relation érotique doit être vécue de manière qu'il vous soit facile d'en évoquer une image avec tout ce qu'il y a de beau en elle.",
            u"Toute tribulation embellit les êtres.",
            u"Très tôt dans ma jeunesse, je ne pouvais comprendre comment on s'y prenait pour écrire un livre, ce que je saisis très bien à présent; par contre, je ne conçois pas maintenant qu'on puisse en avoir envie.",
            u"Un garçon commence immédiatement à se développer et y met beaucoup de temps, une jeune fille naît pendant longtemps et naît femme faite, mais l'instant de cette naissance arrive tard.",
            u"Un roi sans royaume est une figure ridicule, mais une guerre entre prétendants à la succession dans un royaume sans territoire l'emporte sur tous les ridicules.",
            u"Une condition capitale pour toute jouissance, c'est de se limiter.",
            u"Une jeune fille devrait toujours s'éprendre d'un zéphyr; nul humain ne sait comme lui, en la lutinant, rehausser sa beauté.",
            u"Une jeune fille qui veut plaire en se faisant intéressante plaira surtout à elle-même.",
            u"Une mauvaise conscience peut rendre la vie intéressante.",
            u"Venez, sommeil et mort; vous ne promettez rien, vous tenez tout."
        ]

            # Martin Luther King
        king = [
            u"Ce à quoi tu te tiens, ce sur quoi tu t'appuies, c'est là véritablement ton Dieu.",
            u"Ce qui ne peut s'enseigner que par des coups et au prix de la violence ne portera que de mauvais fruits.",
            u"Il n'y a pas de plus adorable, tendre et charmante relation que celle d'un bon mariage.",
            u"L'humanité est comme un paysan ivre à cheval: quand on la relève d'un côté, elle tombe de l'autre.",
            u"La bière est oeuvre de l'homme, le vin celle de Dieu.",
            u"La Vérité est plus forte que l'éloquence, le savoir supérieur à l'érudition.",
            u"Le vin est fort, le roi est plus fort, les femmes le sont plus encore, mais la vérité est plus forte que tout.",
            u"Les cloches appellent à l'office et n'y vont jamais.",
            u"Mon coeur déborde de gratitude envers la musique qui, si souvent m'a consolé et qui m'a attiré de grands malheurs.",
            u"Nous sommes des mendiants, c'est bien vrai",
            u"Pour les vivants, de l'eau. Pour les morts, du vin. Cette règle s'applique aux poissons.",
            u"Que le feu te consume, parce que tu as corrompu la vérité divine!",
            u"Qui n'aime point le vin, les femmes ni les chants, - Restera sot toute sa vie durant.",
            u"Voici en quoi consiste la vie chrétienne: vouloir en toutes choses ce que Dieu veut, vouloir sa gloire, et ne rien désirer pour soi-même, ni ici-bas, ni dans l'au-delà."
        ]

            # Karl Kraus
        kraus = [
            u"De temps en temps, une femme est un substitut convenable à la masturbation. Mais bien sur, il faut beaucoup d'imagination",
            u"Il y a deux sortes d'écrivains. Ceux qui le sont, et ceux qui ne le sont pas. Chez les premiers, le fond et la forme sont ensemble comme l'âme et le corps; chez les seconds, le fond et la forme vont ensemble comme le corps et l'habit.",
            u"Ils traitent une femme comme une boisson désaltérante. Que les femmes aient soif, ils ne veulent pas le tolérer.",
            u"L'un écrit parce qu'il voit; l'autre, parce qu'il entend.",
            u"La capacité de douter, après s'être promptement décidé, est la plus haute et la plus virile.",
            u"La langue est la mère, non la fille, de la pensée.",
            u"La langue sera la baguette qui trouve les sources de pensée.",
            u"La psychanalyse est cette maladie dont elle prétend être le remède.",
            u"Le diable est optimiste s'il pense pouvoir rendre les hommes pires qu'ils ne sont.",
            u"Le moraliste doit toujours faire comme s'il venait au monde pour la première fois; l'artiste, comme si c'était une fois pour toutes.",
            u"Le plaisir érotique est une course d'obstacles. L'obstacle le plus attrayant et le plus populaire est la morale.",
            u"Les américains aiment tout ce qu'ils n'ont pas, en particulier les antiquités et les manifestations de la vie intérieure.",
            u"Mais où est-ce que je prends donc tout ce temps pour ne pas lire tant de choses?",
            u"Ne pas avoir d'idées et savoir les exprimer: c'est ce qui fait le journaliste.",
            u"On doit à chaque fois écrire comme si l'on écrivait pour la première et la dernière fois. Dire autant de choses que si l'on faisait ses adieux, et les dire aussi bien que si l'on faisait ses débuts.",
            u"On doit lire tous les écrivains deux fois, les bons et les mauvais. Les uns, on les reconnaîtra; les autres, on les démasquera.",
            u"Pourquoi certain écrit-il? Parce qu'il n'a pas assez de caractère pour ne pas écrire.",
            u"Qui ne pense pas pense qu'on n'aurait une pensée que lorsqu'on l'a et qu'on la revêt de mots. Il ne comprend pas qu'en vérité ne l'a que celui qui a le mot, dans lequel croît la pensée.",
            u"Seule une langue qui a le cancer incline aux formations nouvelles.",
            u"Un aphorisme n'a pas besoin d'être vrai, mais il doit survoler la vérité. Il doit la dépasser d'un trait.",
            u"Une pensée n'est légitime que si on a le sentiment de se surprendre en flagrant délit de plagiat de soi."
        ]

        # L

            # Lao-Tseu
        lao_tseu = [
            u"Apprend à écrire tes blessures dans le sable et à graver tes joies dans la pierre.",
            u"Arrêtez le mal avant qu'il n'existe; calmez le désordre avant qu'il n'éclate.",
            u"Aucun de nous ne sait ce que nous savons tous, ensemble.",
            u"Bien que trente rayons convergent au milieu, - C'est le vide médian qui fait marcher le char.",
            u"C'est du vide que dépend l'usage.",
            u"C'est la conscience humaine du Beau qui différencie le Beau du Laid.",
            u"Ce qui est au-dessus de la vertu est non-vertu.",
            u"Ce qui est au-dessus du bon est souvent pire que le mauvais.",
            u"Ce qui est dur et fort va vers la mort. Ce qui est doux et faible va vers la vie.",
            u"Celui qui connaît sa force et garde la faiblesse est la vallée de l'empire.",
            u"Celui qui excelle à commander une armée n'a pas une ardeur belliqueuse.",
            u"Celui qui excelle à employer les hommes se met au-dessous d'eux.",
            u"Celui qui excelle ne discute pas, - Il maîtrise sa science et se tait.",
            u"Celui qui parle beaucoup est souvent réduit au silence.",
            u"Celui qui s'approuve lui-même ne brille pas.",
            u"Celui qui s'oppose, se déplace sur sa voie. Celui qui est faible, sa voie est utilisée.",
            u"Celui qui sait être constant a une âme large et celui qui a une âme large est juste.",
            u"Celui qui sait ne parle pas, celui qui parle ne sait pas.",
            u"Celui qui sait s'arrêter ne périclite jamais.",
            u"Celui qui se conduit vraiment en chef ne prend pas part à l'action.",
            u"Celui qui se dresse sur ses pieds ne peut se tenir droit.",
            u"Ceux qui savent ne parlent pas, ceux qui parlent ne savent pas.",
            u"Chaque pas est une victoire.",
            u"Connaître les autres, c'est sagesse. Se connaître soi-même, c'est sagesse supérieure. - Imposer sa volonté aux autres, c'est force. Se l'imposer à soi-même, c'est force supérieure.",
            u"Connaître par non-connaissance est très élevé.",
            u"Créer, non posséder; oeuvrer, non retenir; accroître, non dominer.",
            u"Etre conscient de la difficulté permet de l'éviter.",
            u"Etre courageux sans compassion mène à la mort.",
            u"Etre humain: c'est aimer les hommes. Etre sage: c'est les connaître.",
            u"Gouverne le mieux qui gouverne le moins.",
            u"Il est plus intelligent d'allumer une toute petite lampe, que de te plaindre de l'obscurité.",
            u"L'arme acérée du royaume ne doit pas être montrée au peuple.",
            u"L'eau peut agir sans poisson, - Mais le poisson ne peut agir sans eau.",
            u"L'échec est le fondement de la réussite.",
            u"L'être qu'on peut nommer n'est pas l'être suprême.",
            u"L'homme content de son sort ne connaît pas la ruine.",
            u"L'homme d'une vertu supérieure est une vallée.",
            u"L'homme de bien est comme l'eau.",
            u"L'homme n'est pas fait pour construire des murs mais pour construire des ponts.",
            u"L'homme qui ne tente rien ne se trompe qu'une fois.",
            u"L'homme supérieur pratique la vertu sans y songer, l'homme vulgaire la pratique avec intention.",
            u"L'humilité sert à agir avec puissance.",
            u"La distance, âme du beau.",
            u"La plus grande révélation est le silence.",
            u"La plus grande vertu est comme l'eau, elle est bonne pour toutes choses.",
            u"La seule façon d'accomplir est d'être.",
            u"La vertu suprême ignore la vertu: c'est pourquoi elle est la vertu. - La vertu secondaire cultive la vertu: c'est pourquoi elle n'est pas la vertu. - La vertu suprême n'agit pas et n'a pas de raison d'agir.",
            u"La vertu, immuable, ne quitte pas l'homme avec la mort, elle retourne au nourrisson.",
            u"La voie de l'homme sage s'exerce sans lutter.",
            u"La voie est comme un bol vide - Que nul usage ne comble.",
            u"La voie qui peut s'énoncer - N'est pas la voie pour toujours - Le nom qui peut la nommer - N'est pas le nom pour toujours.",
            u"Le bonheur naît du malheur, le malheur est caché au sein du bonheur.",
            u"Le bonheur repose sur le malheur, le malheur couve sous le bonheur. Qui connaît leur apogée respective?",
            u"Le ciel arme de pitié ceux qu'il ne veut pas voir détruits.",
            u"Le ciel et la terre ne sont pas humains ou bienveillants à la manière des hommes, ils considèrent tous les êtres comme si c'étaient des chiens de paille qui ont servi dans les sacrifices.",
            u"Le ciel, la terre, mille et mille choses sont nés de l'existence et l'existence est née du néant.",
            u"Le faible vainc le fort, le souple vainc le dur, - Voie et vertu de l'eau.",
            u"Le filet du ciel est immense et ses mailles sont écartées, mais il n'y a pas un méchant qui puisse l'éviter.",
            u"Le grave est la racine du léger, le calme est le maître du mouvement.",
            u"Le plus grand arbre est né d'une graîne menue; une tour de neuf étages est partie d'une poignée de terre.",
            u"Le plus grand conquérant est celui qui sait vaincre sans bataille.",
            u"Le sage gouverne par le non-faire - Il enseigne par le non-dire - Il ne refuse rien à la foule des êtres - Mais il nourrit chacun sans se l'approprier.",
            u"Le sage ne veut pas être estimé comme le jade, ni méprisé comme la pierre.",
            u"Le sage paraît lent, mais il sait former des plans habiles.",
            u"Le sage peut découvrir le monde sans franchir sa porte. Il voit sans regarder, accomplit sans agir.",
            u"Le sage redoute la célébrité comme l'ignominie.",
            u"Le sage venge ses injures par des bienfaits.",
            u"Le saint ne s'attache pas à ses mérites, et c'est pourquoi ils ne le quittent point.",
            u"Les choses ne changent pas. Change ta façon de les voir, cela suffit.",
            u"Les cinq saveurs émoussent le goût de l'homme.",
            u"Les mots de vérité manquent souvent d'élégance. Les paroles élégantes sont rarement vérités.",
            u"Les paroles sincères ne sont pas élégantes; - Les paroles élégantes ne sont pas sincères.",
            u"Lorsqu'on a fait de grandes choses et obtenu de la gloire, il faut se retirer à l'écart.",
            u"Lorsqu'un homme élevé entend la Voie - Il l'embrasse avec zèle. - Lorsqu'un homme médiocre entend la Voie - Il l'écoute et l'oublie. - Lorsqu'un homme grossier entend la Voie - Il éclate de rire - La Voie s'il ne riait pas ne serait plus la Voie.",
            u"Mes paroles sont très faciles à pratiquer. Dans le monde personne ne peut les comprendre, personne ne peut les pratiquer.",
            u"Mieux vaut allumer une bougie que maudire les ténèbres.",
            u"N'exalte pas les hommes de mérite - On cessera de batailler - Ne fais nul cas des choses rares - On cessera de dérober.",
            u"Paie le mal avec la justice, et la bonté avec la bonté.",
            u"Parole parée n'est pas sincère.",
            u"Peux-tu tout voir et tout connaître - En cultivant le non-agir? - Elève les êtres, nourris-les - Sans chercher à les asservir.",
            u"Plus il y a de lois, et plus il y a de voleurs.",
            u"Plus le sage donne aux autres, plus il possède.",
            u"Plus on va loin, plus la connaissance baisse.",
            u"Pour gouverner un grand royaume, on doit imiter celui qui fait cuire un petit poisson.",
            u"Quand la crainte ne veille pas, il arrive ce qui était à craindre.",
            u"Quand le ciel veut sauver un homme, il lui envoie l'amour!",
            u"Quand les gros maigrissent, les maigres meurent.",
            u"Quelle belle conception les anciens avaient de la mort: repos des bons, terreur des méchants! La mort, c'est l'épreuve de la vertu.",
            u"Qui accumule des richesses a beaucoup à perdre.",
            u"Qui accumule en sa maison l'or et le jade, - N'en pourra défendre l'entrée.",
            u"Qui domine les autres est fort. Qui se domine est puissant.",
            u"Qui ne pête ni ne rote est voué à l'explosion.",
            u"Quiconque veut s'emparer du monde et s'en servir cour à l'échec - Le monde est un vase sacré qui ne supporte pas - Qu'on s'en empare et qu'on s'en serve. - Qui s'en sert, le détruit, - Qui s'en empare, le perd.",
            u"Renoncez à l'étude et vous n'aurez aucun souci.",
            u"Retour le mouvement de la Vie, - Faiblesse sa coutume, - Toutes choses sous le ciel - Naissent de ce qui est, - Ce qui est de ce qui n'est pas.",
            u"Rien ici-bas, n'est plus souple, moins résistant que l'eau, pourtant il n'est rien qui vienne mieux à bout du dur et du fort.",
            u"Sans franchir la porte, on peut connaître le monde.",
            u"Savoir se contenter de ce que l'on a: c'est être riche.",
            u"Se voir soi-même, c'est être clairvoyant.",
            u"Ses mérites étant accomplis le saint homme ne s'y attache pas.",
            u"Si un jour quelqu'un te fait du mal, ne cherche pas à te venger, assieds toi au bord de la rivière, et bientôt tu verras son cadavre passer.",
            u"Si vous croyez savoir, vous ne savez pas.",
            u"Sois avare de tes paroles, et les choses s'arrangeront d'elles-mêmes.",
            u"Tout le monde tient le beau pour le beau, - C'est en cela que réside la laideur. - Tout le monde tient le bien pour le bien, - C'est en cela que réside le mal.",
            u"Trop loin à l'est, c'est l'ouest.",
            u"Un voyage de mille lieues commence toujours par un premier pas.",
            u"Un vrai chef ne paraît pas martial. Qui sait se battre ne s'emporte pas. Qui saura vaincre évitera d'affronter. Qui saura manier les hommes s'abaissera..."
        ]

            # John Lennon
        lennon = [
            u"La vie, c'est ce qui arrive quand on a d'autres projets.",
            u"Le travail, c'est la vie, vous savez, et sans lui il n'y a que peur et insécurité.",
            u"Nous resplendissons tous comme la lune et les étoiles et le soleil..."
        ]

            # Abraham Lincoln
        lincoln = [
            u"A chaque fois que j'entends quelqu'un défendre l'esclavage, j'ai une énorme envie de lui voir appliqué personnellement.",
            u"Aucun homme n'a assez de mémoire pour réussir dans le mensonge.",
            u"C'est détruire mes ennemis que d'en faire mes amis.",
            u"Ce que je veux savoir avant tout, ce n'est pas si vous avez échoué, mais si vous avez su accepter votre échec.",
            u"De même que je ne voudrais pas être un esclave, je ne voudrais pas être un maître. Telle est ma conception de la démocratie. Tout ce qui en diffère, et la différence est d'autant plus grande, n'est point de la démocratie.",
            u"Des mesures non constitutionnelles peuvent devenir légitimes quand elles sont indispensables.",
            u"Dieu doit aimer les pauvres, autrement il n'en aurait pas créé autant.",
            u"En donnant la liberté aux esclaves nous assurons celle des hommes libres. Ce que nous offrons est aussi honorable pour nous que ce que nous préservons.",
            u"Je ne sais pas qui était mon grand-père. Je suis intéressé davantage de savoir ce que va devenir son petit-fils.",
            u"La perte d'un ennemi ne compense pas celle d'un ami.",
            u"Le capital est seulement le fruit du travail et il n'aurait jamais pu exister si le travail n'avait tout d'abord existé.",
            u"Le Seigneur préfère les gens communs, c'est pourquoi il en fait autant.",
            u"Mieux vaut ne pas changer d'attelage au milieu du gué.",
            u"On ne perd rien de précieux en prenant son temps.",
            u"On peut modifier l'action de l'homme dans une certaine mesure, on ne saurait changer la nature humaine.",
            u"On peut tromper une partie du peuple tout le temps et tout le peuple une partie du temps, mais on ne peut pas tromper tout le peuple tout le temps.",
            u"Que l'on me donne six heures pour couper un arbre, j'en passerai quatre à préparer ma hâche.",
            u"Rappelez-vous toujours que votre intention de réussir est plus importante que toute autre chose.",
            u"Seul peut critiquer celui qui est prêt à aider.",
            u"Si l'esclavage n'est pas mauvais, rien n'est mauvais.",
            u"Si vous cherchez le mal parmi les hommes, vous le trouverez; - Si vous cherchez le bien, vous le trouverez aussi.",
            u"Si vous trouvez que l'éducation coûte cher, essayez l'ignorance.",
            u"Un bulletin de vote est plus fort qu'une balle de fusil.",
            u"Un gouvernement du peuple, par le peuple, pour le peuple.",
            u"Voulez-vous dire que les Blancs sont intellectuellement supérieurs aux Noirs et ont donc le droit de les réduire à l'esclavage? Cette règle fait de vous l'esclave du premier homme dont l'intellect est supérieur au vôtre.",
            u"Vous ne pouvez pas aider les hommes continuellement en faisant pour eux ce qu'ils pourraient et devraient faire eux-mêmes."
        ]

        # M
            # Henry Louis Mencken
        mencken = [
            u"C'est un péché de penser du mal d'autrui, mais c'est rarement une erreur.",
            u"Il est dans la probabilité que mille choses arrivent qui sont contraires à la probabilité.",
            u"Il est maintenant presque autorisé pour une catholique de recourir aux mathématiques pour éviter d'être enceinte, mais il lui est encore interdit de se servir de la physique et de la chimie.",
            u"L'amour est la croyance erronée que certaines femmes sont différentes des autres.",
            u"L'amour est le triomphe de l'imagination sur l'intelligence.",
            u"L'hérédité est un phénomène auquel un homme croit jusqu'à ce que son fils se conduise comme un idiot.",
            u"L'homme est naturellement polygame. Il a toujours une femme qui le mène par le bout du nez et une autre qui est pendue à ses basques.",
            u"L'optimiste achète à un Juif et veut vendre à un Ecossais.",
            u"La bigamie consiste à avoir une femme en trop. La monogamie aussi d'ailleurs.",
            u"La dermatologie est la meilleure des spécialités: le malade ne meurt jamais et ne guérit pas.",
            u"La seule liberté que l'homme simple désire vraiment, c'est celle de démissionner de son job, de se faire dorer au soleil et de se gratter là où ça le démange.",
            u"Le cynique est celui qui, lorsqu'il sent un parfum de fleurs, cherche le cercueil.",
            u"Le malheur de l'homme et la cause de presque toutes ses calamités est sa capacité prodigieuse de croire à l'impossible.",
            u"Le principal apport du protestantisme à la pensée humaine est la preuve massive de l'ennui que dégage Dieu.",
            u"Le progrès existe, c'est certain. L'américain moyen paie maintenant en impôts deux fois ce qu'il avait avant en guise de salaire.",
            u"Le puritanisme: la peur incessante que quelqu'un, quelque part, puisse être heureux.",
            u"Le seul caractère qui distingue l'homme des autres vertébrés supérieurs est une timidité excessive, sa faculté de s'alarmer, et son incapacité de se lancer dans l'aventure sans une foule derrière lui.",
            u"Les célibataires connaissent mieux les femmes que les hommes mariés, sinon ils seraient mariés.",
            u"Les hommes et les femmes sont au moins d'accord sur un point: ils n'ont aucune confiance dans les femmes.",
            u"Les hommes ont une vie plus agréable que les femmes. Premièrement, ils se marient plus tard et, deuxièmement, ils meurent plus tôt!",
            u"Les hommes savent mieux organiser leur vie que les femmes: ils se marient plus tard et meurent plus tôt.",
            u"Néanmoins, il est encore plus difficile pour le singe moyen de croire qu'il descend de l'homme.",
            u"Quand deux femmes s'embrassent, je pense toujours aux champions de boxe qui se serrent la main avant le match.",
            u"Quand un diplomate dit «oui», cela signifie «peut-être»; - Quand il dit «peut-être», cela veut dire «non»; - Et quand il dit «non», ce n'est pas un diplomate.",
            u"Quand un homme et une femme sont mariés, ils ne deviennent plus qu'un; la première difficulté est de décider lequel.",
            u"Un idéaliste est quelqu'un qui, remarquant qu'une rose sent meilleur qu'un chou, conclut qu'elle fera une meilleure soupe.",
            u"Un optimiste est celui qui achète à un Juif et veut vendre à un Ecossais.",
            u"Une célébrité est une personne qui est connue de nombreuses personnes qu'elle est heureuse de ne pas connaître.",
            u"Une guerre laisse le pays avec trois armées: une armée d'infirmes, une armée de pleureuses, et une armée de voleurs."
        ]

        # N
            # Friedrich Nietzsche
        nietzsche = [
            u"... celui qui un jour veut apprendre à voler, celui-là doit d'abord apprendre à se tenir debout et à marcher et à courir, à grimper et à danser - ce n'est pas du premier coup d'aile que l'on conquiert l'envol!",
            u"... il n'y a de résurrections que là où il y a des tombeaux.",
            u"... le danseur n'a-t-il pas ses oreilles dans ses orteils!",
            u"... qu'y aurait-il donc à créer s'il y avait des dieux?",
            u"A certains hommes tu ne dois pas donner la main, mais seulement la patte: et je veux que ta patte ait aussi des griffes.",
            u"A lutter avec les mêmes armes que ton ennemi, tu deviendras comme lui.",
            u"A quoi l'on peut mesurer la sagesse. - L'augmentation de la sagesse se laisse mesurer exactement d'après la diminution de bile.",
            u"A vrai dire, la foi n'a pas encore réussi à déplacer de vraies montagnes, quoique cela ait été affirmé par je ne sais plus qui; mais elle sait placer des montagnes où il n'y en a point.",
            u"Absorption et non-absorption de poisons: Le seul argument définitif qui, de tout temps, ait empêché les hommes d'absorber un poison, ce n'est pas la crainte de la mort qu'il pourrait occasionner, mais son mauvais goût.",
            u"Aimez la paix comme le moyen de nouvelles guerres, et la paix brève plus que la longue.",
            u"Apprendre à détourner les yeux de soi-même pour voir beaucoup de choses, - cette dureté est nécessaire à tous ceux qui gravissent des montagnes.",
            u"Beaucoup de courtes folies, - c'est ce qui, chez nous, se nomme amour. Et votre mariage finit beaucoup de courtes folies, en une longue bêtise.",
            u"But du châtiment: Le châtiment a pour but de rendre meilleur celui qui châtie, - c'est là le dernier recours pour les défenseurs du châtiment.",
            u"C'est entre ce qui est le plus semblable que l'apparence fait les plus beaux mensonges; car c'est par-dessus le plus petit abîme qu'il est le plus difficile de tendre un pont.",
            u"C'est la partie de son corps qui est au-dessous de la ceinture qui fait que l'homme ne se prend pas si facilement pour un dieu.",
            u"Ce n'est pas l'histoire, mais l'art qui exprime la vraie vie.",
            u"Ce n'est pas le doute qui rend fou: c'est la certitude.",
            u"Ce n'est pas quand elle est sale que celui qui accède à la connaissance répugne à descendre dans l'eau de la vérité, c'est quand elle est peu profonde.",
            u"Ce qu'il y a de grand en l'homme, c'est qu'il est un pont et non but: ce que l'on peut aimer en l'homme, c'est qu'il est une transition et un déclin.",
            u"Ce qu'on fait par amour l'est toujours par-delà le bien et le mal.",
            u"Ce qui détruit les illusions, les siennes et celles des autres, la nature le punit avec toute la rigueur d'un tyran.",
            u"Ce qui se dit la nuit ne voit jamais le jour.",
            u"Ce sont les paroles les moins tapageuses qui suscitent la tempête, et les pensées qui mènent le monde arrivent sur des ailes de colombes.",
            u"Celui qu'entoure la flamme de la jalousie, celui-là en fin de compte, pareil au scorpion, tourne contre lui-même son dard empoisonné.",
            u"Celui qui ne veut agir et parler qu'avec justesse finit par ne rien faire du tout.",
            u"Celui qui sait commander trouve toujours ceux qui doivent obéir.",
            u"Chaque homme cache en lui un enfant qui veut jouer.",
            u"Chasser l'ennui à tout prix est vulgaire, comme de travailler sans plaisir.",
            u"Comment on gagne les gens courageux. - On amène les gens courageux à une action en la leur exposant plus périlleuse qu'elle n'est.",
            u"Confession: On oublie sa faute quand on l'a confessée à un autre, mais d'ordinaire l'autre ne l'oublie pas.",
            u"Connaître, c'est comprendre toute chose au mieux de nos intérêts.",
            u"Contre la vanité - - Ne t'enfle pas, autrement - La moindre piqûre te fera crever.",
            u"Contre mainte défense: La façon la plus perfide de nuire à une cause, c'est de la défendre, intentionnellement avec de mauvaises raisons.",
            u"Créer, - voilà la grande délivrance de la souffrance, voilà ce qui rend la vie légère.",
            u"Danger dans la voix: Avec une voix forte dans la gorge on est presque incapable de penser des choses subtiles.",
            u"Danger du langage pour la liberté de l'esprit: Chaque mot est un préjugé.",
            u"Dans la vengeance et en amour, la femme est plus barbare que l'homme.",
            u"Dans la véritable conscience du savoir, il n'y a ni grandes, ni petites choses.",
            u"De tout temps, on a pris les «beaux sentiments» pour des arguments.",
            u"Des goûts et des couleurs on ne discute pas... et pourtant on ne fait que ça!",
            u"Deviens qui tu es! Fais ce que toi seul peut faire.",
            u"Deviens sans cesse celui que tu es, sois le maître et le sculpteur de toi-même.",
            u"Dieu a aussi son enfer: c'est son amour des hommes.",
            u"Dieu est une réponse aux embarras de l'intelligence.",
            u"Du pays des anthropophages: Dans la solitude le solitaire se ronge le coeur; dans la multitude c'est la foule qui le lui ronge. Choisis donc!",
            u"Echelle de mesure pour tous les jours. - On se trompera rarement si l'on ramène les actions extrêmes à la vanité, les médiocres à l'habitude et les mesquines à la peur.",
            u"Encens: Le Bouddha dit: «Ne flatte pas ton bienfaiteur!» Que l'on répète ces paroles dans une église chrétienne; - immédiatement elles nettoient l'air de tout ce qui est chrétien.",
            u"Ennemis de la vérité: Les convictions sont des ennemis de la vérité plus dangereux que les mensonges.",
            u"Et il existe des choses si bien inventées qu'on croirait la poitrine d'une femme: utile et agréable à la fois.",
            u"Et méfie-toi des bons et des justes, ils aiment à crucifier ceux qui s'inventent leur propre vertu - ils haïssent le solitaire.",
            u"Et nul ne ment autant qu'un homme indigné.",
            u"Et souvent il y a plus de bravoure à se retenir et à passer: pour se réserver pour un ennemi plus digne.",
            u"Etre dupe: Dès que vous voulez agir, il vous faut fermer les portes du doute, - disait un homme d'action. - Et ne crains-tu pas, de cette façon, d'être dupe? - rétorqua un contemplatif.",
            u"Etre libre, c'est vivre nu et sans honte.",
            u"Explications mystiques: Les explications mystiques sont considérées comme profondes; en réalité il s'en faut de beaucoup qu'elles soient même superficielles.",
            u"Féconder le passé et enfanter l'avenir: que tel soit mon présent.",
            u"Habitude: Toute habitude rend notre main plus spirituelle et notre esprit plus malhabile.",
            u"Homme de caractère: Un homme paraît avoir du caractère beaucoup plus souvent parce qu'il suit toujours son tempérament que parce qu'il suit toujours ses principes.",
            u"Il est difficile de vivre avec des humains, parce qu'il est difficile de se taire.",
            u"Il faut avoir besoin d'esprit pour arriver à avoir de l'esprit.",
            u"Il faut avoir un chaos en soi-même pour accoucher d'une étoile qui danse.",
            u"Il faut protéger les forts des faibles.",
            u"Il faut se mettre en face de la poésie pour écrire de bonne prose! Car la prose est une guerre contre la poésie, une guerre aimable et incessante: tout son charme consiste à échapper sans cesse à la poésie, à la contredire, constamment.",
            u"Il faut toujours choisir soigneusement ses ennemis, parce qu'on finit par leur ressembler.",
            u"Il ne faut pas avoir trop raison quand on veut avoir les rieurs de son côté; avoir un tantinet tort est même une preuve de bon goût.",
            u"Il y a toujours un peu de folie dans l'amour. Mais il y a toujours aussi un peu de raison dans la folie.",
            u"Je ne fais pas l'aumône, je ne suis pas assez pauvre pour cela.",
            u"Je ne veux pas que mes disciples fassent et pensent comme moi. Je veux qu'ils trouvent leur propre voie, comme je l'ai fait moi-même.",
            u"Je suis trop fier pour croire qu'un homme m'aime. Cela supposerait qu'il sache qui je suis.",
            u"Je vous enseigne le surhumain. L'homme n'existe que pour être dépassé. Qu'avez-vous fait pour le dépasser?",
            u"Jusqu'à présent toute grande philosophie fut la confession de son auteur, une sorte de mémoires involontaires.",
            u"L'amour d'un seul être est une barbarie, car on le pratique aux dépens de tous les autres.",
            u"L'amour est l'état dans lequel les hommes ont les plus grandes chances de voir les choses telles qu'elles ne sont pas.",
            u"L'amour ne veut pas la durée; il veut l'instant et l'éternité.",
            u"L'art et rien que l'art, nous avons l'art pour ne point mourir de la vérité.",
            u"L'effort des philosophes tend à comprendre ce que les contemporains se contentent de vivre.",
            u"L'homme doit être éduqué pour la guerre, - la femme pour le repos du guerrier; - Tout le reste est sottises!",
            u"L'homme est une corde tendue entre l'animal et le surhumain - une corde par-dessus un abîme.",
            u"L'homme ne se contente pas de ne pas savoir. Il faut être très humain pour dire «c'est une chose que je ne sais pas», pour s'accorder de l'ignorance.",
            u"L'homme souffre si profondément qu'il a dû inventer le rire.",
            u"L'injustice ne se trouve jamais dans les droits inégaux, elle se trouve dans la prétention à des droits égaux.",
            u"L'instinct sexuel, l'ivresse, la cruauté, tous font partie des plus anciennes fêtes de l'humanité.",
            u"L'instruction publique: L'instruction, dans les grands Etats, sera toujours tout au plus médiocre, par la même raison qui fait que, dans les grandes cuisines, on cuisine tout au plus médiocrement.",
            u"La bêtise des bons est insondable.",
            u"La connaissance est pour l'humanité un magnifique moyen de s'anéantir elle-même.",
            u"La connaissance tue l'action, pour agir il faut être obnubilé par l'illusion.",
            u"La culture, c'est avant tout une unité de style qui se manifeste dans toutes les activités d'une nation.",
            u"La femme est la seconde faute de Dieu.",
            u"La flamme n'est pas aussi lumineuse pour elle-même que pour les autres qu'elle éclaire: de même aussi le sage.",
            u"La liberté, c'est avoir la volonté de répondre de soi.",
            u"La méchanceté est rare. - La plupart des hommes sont bien trop occupés d'eux-mêmes pour être méchants.",
            u"La musique offre aux passions le moyen de jouir d'elles-mêmes.",
            u"La souffrance d'autrui est chose qui doit s'apprendre.",
            u"La vérité est une femme: ses voiles, ses pudeurs et ses mensonges lui appartiennent essentiellement.",
            u"La vérité ne tolère pas d'autres dieux: La foi en la vérité commence avec le doute au sujet de toutes les «vérités» en quoi l'on a cru jusqu'à présent.",
            u"Le beau temps ne serait pas si les orages n'existaient pas!",
            u"Le bonheur est une femme.",
            u"Le calme dans l'action: Comme une chute d'eau en se précipitant devient plus lente et plus aérienne, ainsi d'ordinaire le grand homme accomplit l'action avec plus de calme que ne le faisait attendre son désir impétueux avant l'action.",
            u"Le christianisme a fait boire du poison à Eros: il n'en est pas mort, mais il est devenu vicieux.",
            u"Le christianisme et l'alcool, les deux plus grands agents de corruption.",
            u"Le concubinage, lui aussi, a été corrompu par le mariage.",
            u"Le futur appartient à celui qui a la plus longue mémoire.",
            u"Le luxe est une forme de triomphe permanent sur tous ceux qui sont pauvres, arriérés, impuissants, malades, inassouvis.",
            u"Le mauvais goût a son droit autant que le bon goût.",
            u"Le verdict du passé est toujours le verdict d'un oracle. Vous ne le comprendrez que si vous êtes les architectes de l'avenir, les connaisseurs du présent.",
            u"Les certitudes inébranlables sont des ennemis de la vérité, plus graves que le mensonge.",
            u"Les convictions sont des prisons.",
            u"Les hommes ont été considérés comme libres pour pouvoir être jugés et punis, pour pouvoir être coupables.",
            u"Les insectes piquent, non par méchanceté, mais parce que, eux aussi, veulent vivre; il en est de même des critiques; ils veulent notre sang et non pas notre douleur.",
            u"Les singes sont bien trop bons pour que l'homme puisse descendre d'eux.",
            u"Mauvaise mémoire: L'avantage de la mauvaise mémoire est qu'on jouit plusieurs fois des mêmes choses pour la première fois.",
            u"Motif de l'attaque. - On n'attaque pas seulement pour faire du mal à quelqu'un, pour le vaincre, mais peut-être aussi pour le seul plaisir de prendre conscience de sa force.",
            u"On ne reste parfois fidèle à une cause que parce que ses adversaires ne cessent pas d'être insipides.",
            u"On peut promettre des actions, mais non des sentiments, car ceux-ci sont involontaires.",
            u"Où que tu soies, creuse profond.",
            u"Pour comprendre une chose complètement, il faut la regarder d'un oeil d'amour et d'un oeil de haine.",
            u"Puissance sans victoires: La connaissance la plus forte (celle de l'absolue non-liberté de la volonté humaine) est pourtant celle qui aboutit aux résultats les plus pauvres: car elle a toujours eu l'adversaire le plus fort, la vanité humaine.",
            u"Qu'est-ce que le génie? - Avoir un but élevé et vouloir les moyens d'y parvenir.",
            u"Que d'hommes se pressent vers la lumière, non pas pour voir mieux mais pour mieux briller.",
            u"Que dit ta conscience? - «Tu dois devenir celui que tu es.»",
            u"Qui ne croit en lui-même, ment toujours.",
            u"Qui se sait profond s'efforce d'être clair; qui aimerait passer pour profond aux yeux de la foule s'efforce d'être obscur.",
            u"Rire: Rire, c'est se réjouir d'un préjudice, mais avec bonne conscience.",
            u"Rousseau, cette tarentule morale.",
            u"Sans cruauté, pas de fête: c'est ce que nous apprend la plus ancienne et la plus longue histoire de l'homme - et il y a même dans le châtiment tant de fête.",
            u"Sans la musique, la vie serait une erreur.",
            u"Si Dieu avait voulu devenir un objet d'amour, il aurait dû commencer par renoncer à rendre la justice: - un juge, et même un juge clément, n'est pas un objet d'amour.",
            u"Si tu plonges longtemps ton regard dans l'abîme, l'abîme te regarde aussi.",
            u"Tant que la vie est ascendante, bonheur et instinct sont identiques.",
            u"Tous les grands hommes sont de grands travailleurs, infatigables non seulement à inventer, mais encore à rejeter, passer au crible, modifier, arranger.",
            u"Tout ce qui a son prix est de peu de valeur.",
            u"Tout ce qui ne me tue pas me rend plus fort.",
            u"Toute communauté - un jour, quelque part, d'une manière ou d'une autre - rend «commun».",
            u"Truc de prophète: Pour deviner à l'avance les façons d'agir d'hommes ordinaires, il faut admettre qu'ils font toujours la moindre dépense d'esprit pour se libérer d'une situation désagréable.",
            u"Tu vas voir les femmes? N'oublie pas ton fouet.",
            u"Un concept est une invention à laquelle rien ne correspond exactement, mais à laquelle nombre de choses ressemblent.",
            u"Un peuple est un détour que prend la nature pour parvenir à six ou sept grands hommes - et pour les éviter ensuite.",
            u"Une chose qui convainc n'est pas vraie pour autant. Elle est seulement convaincante.",
            u"Une des erreurs de logique les plus ordinaires est celle-ci: quelqu'un est envers nous véridique et sincère, donc il dit la vérité. C'est ainsi que l'enfant croit aux jugements de ses parents, le chrétien aux affirmations du fondateur de l'Eglise.",
            u"Une heure d'ascension dans les montagnes fait d'un gredin et d'un saint deux créatures à peu près semblables. La fatigue est le plus court chemin vers l'égalité, vers la fraternité.",
            u"Une maladie des hommes: Contre la maladie des hommes qui consiste à se mépriser, le remède le plus sûr est qu'ils soient aimés d'une femme habile.",
            u"Vénérez la maternité, le père n'est jamais qu'un hasard.",
            u"Vers la lumière: Les hommes se pressent vers la lumière, non pour mieux voir, mais pour mieux briller. - On considère volontiers comme une lumière celui devant qui l'on brille.",
            u"Veux-tu avoir la vie facile? Reste toujours près du troupeau, et oublie-toi en lui.",
            u"Vivre, c'est repousser quelque chose qui veut mourir.",
            u"«Connais-toi toi-même», voilà toute la science. C'est seulement quand la connaissance des choses sera achevée que l'homme se connaîtra lui-même. Car les choses ne sont que les limites de l'homme.",
            u"«Est-il vrai que le bon Dieu est présent partout? demanda une petite fille à sa mère: mais je trouve cela inconvenant.» - Une indication pour les philosophes!",
            u"«Nous avons inventé le bonheur», diront les derniers hommes et ils cligneront de l'oeil."
        ]

        # O




        # P
            # Pablo Picasso
        picasso = [
            u"Antisociale, ridicule et tout à fait inadéquate à la saine mentalité du prolétariat.",
            u"Auparavant ... un tableau était une somme d'additions. Chez moi, un tableau est une somme de destructions.",
            u"C'est dangereux le succès. On commence à se copier soi-même et se copier soi-même est plus dangereux que de copier les autres... c'est stérile.",
            u"C'est dans le travail d'une vie que réside la véritable séduction.",
            u"Ce n'est pas ce que l'artiste fait qui compte, mais ce qu'il est.",
            u"Certains peintres transforment le soleil en un point jaune; d'autres transforment un point jaune en soleil.",
            u"Chercher ne signifie rien en art. Ce qui compte, c'est trouver.",
            u"Dans chaque enfant il y a un artiste. Le problème est de savoir comment rester un artiste en grandissant.",
            u"De nos jours, l'on ne va plus à l'asile, on fonde le cubisme.",
            u"Donnez-moi un musée et je le remplirai.",
            u"En peinture on peut tout essayer. On a le droit, même. A condition de ne jamais recommencer.",
            u"Faut-il peindre ce qu'il y a sur un visage? Ce qu'il y a dans un visage? Ou ce qui se cache derrière un visage?",
            u"J'ai mis toute ma vie à savoir dessiner comme un enfant.",
            u"J'essaie toujours de faire ce que je ne sais pas faire, c'est ainsi que j'espère apprendre à le faire.",
            u"Je fais un tableau, ensuite je le détruis. Mais à la fin du compte rien n'est perdu. Le rouge que j'ai enlevé d'une part se trouve quelque part ailleurs.",
            u"Je mets dans mes tableaux tout ce que j'aime. Tant pis pour les choses, elles n'ont qu'à s'arranger entre elles.",
            u"Je n'évolue pas, je suis. Il n'y a, en art, ni passé, ni futur. L'art qui n'est pas dans le présent ne sera jamais.",
            u"Je ne peins pas ce que je vois, je peins ce que je pense.",
            u"Je ne peux pas vivre sans amour. S'il n'y avait plus un seul humain, j'aimerais une plante, un bouton de porte.",
            u"L'amour est une ortie qu'il faut moissonner chaque instant si l'on veut faire la sieste étendu à son ombre.",
            u"L'art est un mensonge qui nous permet de dévoiler la vérité.",
            u"L'art lave notre âme de la poussière du quotidien.",
            u"L'art n'est pas chaste, on devrait l'interdire aux ignorants innocents, ne jamais mettre en contact avec lui ceux qui y sont insuffisamment préparés. Oui, l'art est dangereux. Ou s'il est chaste, ce n'est pas de l'art.",
            u"L'art nègre? Connais pas.",
            u"La jeunesse est la période où l'on se déguise, où l'on cache sa personnalité. C'est une période de mensonges sincères.",
            u"La peinture n'est pas faite pour décorer les appartements. C'est un instrument de guerre offensive contre l'ennemi.",
            u"La vieillesse ne se guérit pas, elle se prépare.",
            u"Le goût est l'ennemi de la créativité.",
            u"Le métier, c'est ce qui ne s'apprends pas.",
            u"Le travail est nécessaire pour l'homme. Il en a inventé le réveil-matin.",
            u"Les accidents, essayer de les éviter... c'est impossible. Ce qui est accidentel révèle l'homme.",
            u"Les autres parlent, moi je travaille.",
            u"Les bons artistes copient, les grands artistes volent.",
            u"Les ordinateurs sont inutiles. Ils ne savent que donner des réponses.",
            u"On devient jeune à soixante ans. Malheureusement, c'est trop tard.",
            u"Personne ne peut s'intéresser à suivre un homme qui, les yeux fixés au sol, regarde si la fortune ne placera pas un portefeuille sur son chemin.",
            u"Pour apprendre quelque chose aux gens, il faut mélanger ce qu'ils connaissent avec ce qu'ils ignorent.",
            u"Pour que des tableaux se vendent cher, il faut qu'ils aient été vendus très bon marché au début.",
            u"Pourquoi je suis communiste? C'est bien simple: je possède un milliard et je veux le garder.",
            u"Quand je n'ai pas de bleu, je mets du rouge.",
            u"Qui voit la figure humaine correctement? Le photographe, le miroir ou le peintre?",
            u"S'il y avait une seule vérité, on ne pourrait pas faire cent toiles sur le même thème.",
            u"Si l'on sait exactement ce qu'on va faire, à quoi bon le faire?",
            u"Tout acte de création est d'abord un acte de destruction.",
            u"Tout ce qui peut être imaginé est réel.",
            u"Tout l'intérêt de l'art se trouve dans le commencement. Après le commencement, c'est déjà la fin.",
            u"Toutes les images que nous avons de la nature, c'est aux peintres que nous les devons. C'est par eux que nous les percevons. Rien que cela devrait les rendre suspects.",
            u"Un cheval ne va pas tout seul dans les brancards.",
            u"Un tableau ne vit que par celui qui le regarde."
        ]

            # Louis Pasteur
        pasteur = [
            u"Ayez le culte de l'esprit critique.",
            u"C'est sous l'impression d'un sentiment presque divin que tout à l'heure vous avez acclamé ces hommes supérieurs.",
            u"Ce sont les Grecs qui nous ont légué le plus beau mot de notre langue: le mot «enthousiasme» - du grec en theo, un Dieu intérieur.",
            u"Il ne suffit pas de connaître la vérité, il faut encore la proclamer.",
            u"Il y a plus de philosophie dans une bouteille de vin que dans tous les livres.",
            u"La chance ne sourit qu'aux esprits bien préparés.",
            u"La grandeur des actions humaines se mesure à l'inspiration qui les fait naître.",
            u"La grandeur des actions humaines se mesure à l'inspiration qui les faits naître.",
            u"La science n'a pas de patrie.",
            u"Le hasard ne favorise que les gens préparés.",
            u"Le vin est la plus saine et la plus hygiénique des boissons",
            u"Quand on est arrivé à la certitude, on éprouve l'une des plus grandes joies que puisse ressentir l'âme humaine.",
            u"Un repas sans vin est comme un jour sans soleil."
        ]

        # Q

        # R
            # Francois de La Rochefoucauld
        rochefoucauld = [
            u"Aimez le chocolat à fond, sans complexe ni fausse honte, car rappelez-vous: «sans un grain de folie, il n'est point d'homme raisonnable».",
            u"Assez de gens méprisent le bien, mais peu savent le donner.",
            u"C'est en quelque sorte se donner part aux belles actions, que de les louer de bon coeur.",
            u"C'est être véritablement honnête homme que de vouloir être toujours exposé à la vue des honnêtes gens.",
            u"C'est plus souvent par orgueil que par défaut de lumières qu'on s'oppose avec tant d'opiniâtreté aux opinions les plus suivies: on trouve les premières places prises dans le bon parti, et on ne veut point des dernières.",
            u"C'est plutôt par l'estime de nos propres sentiments que nous exagérons les bonnes qualités des autres, que par l'estime de leur mérite; et nous voulons nous attirer des louanges, lorsqu'il semble que nous leur en donnons.",
            u"C'est presque toujours la faute de celui qui aime de ne pas connaître quand on cesse de l'aimer.",
            u"C'est une ennuyeuse maladie que de conserver sa santé par un trop grand régime.",
            u"C'est une espèce de bonheur, de connaître jusqu'à quel point on doit être malheureux.",
            u"C'est une espèce de coquetterie de faire remarquer qu'on n'en fait jamais.",
            u"C'est une grande folie que de vouloir être sage tout seul.",
            u"C'est une grande habileté que de savoir cacher son habileté.",
            u"Ce n'est d'ordinaire que dans de petits intérêts où nous prenons le hasard de ne pas croire aux apparences.",
            u"Ce n'est pas assez d'avoir de grandes qualités; il en faut avoir l'économie.",
            u"Ce n'est pas toujours par valeur et par chasteté que les hommes sont vaillants et que les femmes sont chastes.",
            u"Ce n'est pas un grand malheur d'obliger des ingrats, mais c'en est un insupportable d'être obligé à un malhonnête homme.",
            u"Ce qu'on nomme libéralité n'est le plus souvent que la vanité de donner, que nous aimons mieux que ce que nous donnons.",
            u"Ce que les hommes ont nommé amitié n'est qu'une société, qu'un ménagement réciproque d'intérêts, et qu'un échange de bons offices; ce n'est enfin qu'un commerce où l'amour-propre se propose toujours quelque chose à gagner.",
            u"Ce qui a le plus contribué à sa réputation est de savoir donner un beau jour à ses défauts.",
            u"Ce qui fait le mécompte dans la reconnaissance qu'on attend des grâces que l'on a faites, c'est que l'orgueil de celui qui donne, et l'orgueil de celui qui reçoit, ne peuvent convenir du prix du bienfait.",
            u"Ce qui fait que l'on est souvent mécontent de ceux qui négocient, est qu'ils abandonnent presque toujours l'intérêt de leurs amis pour l'intérêt du succès de la négociation, qui devient le leur par l'honneur d'avoir réussi à ce qu'ils avaient entrepris.",
            u"Ce qui fait que la plupart des femmes sont peu touchées de l'amitié, c'est qu'elle est fade quand on a senti de l'amour.",
            u"Ce qui fait que la plupart des petits enfants plaisent, c'est qu'ils sont encore renfermés dans cet air et dans ces manières que la nature leur a donnés, et qu'ils n'en connaissent point d'autres.",
            u"Ce qui fait que les amants et les maîtresses ne s'ennuient point d'être ensemble, c'est qu'ils parlent toujours d'eux-mêmes.",
            u"Ce qui fait que si peu de personnes sont agréables dans la conversation, c'est que chacun songe plus à ce qu'il veut dire qu'à ce que les autres disent.",
            u"Ce qui nous donne tant d'aigreur contre ceux qui nous font des finesses, c'est qu'ils croient être plus habiles que nous.",
            u"Ce qui nous empêche d'ordinaire de faire voir le fond de notre coeur à nos amis, n'est pas tant la défiance que nous avons d'eux, que celle que nous avons de nous-mêmes.",
            u"Ce qui nous empêche souvent de nous abandonner à un seul vice est que nous en avons plusieurs.",
            u"Ce qui nous fait croire si facilement que les autres ont des défauts, c'est la facilité que l'on a de croire ce qu'on souhaite.",
            u"Ce qui nous rend la vanité des autres insupportable, c'est qu'elle blesse la nôtre.",
            u"Ce qui nous rend si changeants dans nos amitiés, c'est qu'il est difficile de connaître les qualités de l'âme, et facile de connaître celles de l'esprit.",
            u"Ce qui paraît générosité n'est souvent qu'une ambition déguisée qui méprise de petits intérêts, pour aller à de plus grands.",
            u"Ce qui rend les douleurs de la honte et de la jalousie si aiguës, c'est que la vanité ne peut servir à les supporter.",
            u"Ce qui se trouve le moins dans la galanterie, c'est de l'amour.",
            u"Celui qui croit pouvoir trouver en soi-même de quoi se passer de tout le monde se trompe fort; mais celui qui croit qu'on ne peut se passer de lui se trompe encore davantage.",
            u"Celui qui vit sans folie n'est pas si sage qu'il le croit.",
            u"Celui-là n'est pas raisonnable à qui le hasard fait trouver la raison, mais celui qui la connaît, qui la discerne, et qui la goûte.",
            u"Ces grandes et éclatantes actions qui éblouissent les yeux.",
            u"Cette clémence dont on fait une vertu se pratique tantôt par vanité, quelquefois par paresse, souvent par crainte, et presque toujours par tous les trois ensemble.",
            u"Ceux qu'on condamne au supplice affectent quelquefois une constance et un mépris de la mort qui n'est en effet que la crainte de l'envisager. De sorte qu'on peut dire que cette constance et ce mépris sont à leur esprit ce que le bandeau est à leurs yeux.",
            u"Ceux qui croient avoir du mérite se font un honneur d'être malheureux, pour persuader aux autres et à eux-mêmes qu'ils sont dignes d'être en butte à la fortune.",
            u"Ceux qui ont eu de grandes passions se trouvent toute leur vie heureux, et malheureux, d'en être guéris.",
            u"Ceux qui s'appliquent trop aux petites choses deviennent ordinairement incapables des grandes.",
            u"Chacun dit du bien de son coeur et personne n'en ose dire de son esprit.",
            u"Comme c'est le caractère des grands esprits de faire entendre en peu de paroles beaucoup de choses, les petits esprits au contraire ont le don de beaucoup parler, et de ne rien dire.",
            u"Comment prétendons-nous qu'un autre puisse garder notre secret, si nous ne pouvons le garder nous-mêmes.",
            u"Dans l'adversité de nos meilleurs amis, nous trouvons quelque chose qui ne nous déplaît pas.",
            u"Dans l'amitié comme dans l'amour on est souvent plus heureux par les choses qu'on ignore que par celles que l'on sait.",
            u"Dans l'amour la tromperie va presque toujours plus loin que la méfiance.",
            u"Dans la vieillesse de l'amour comme dans celle de l'âge on vit encore pour les maux, mais on ne vit plus pour les plaisirs.",
            u"Dans les grandes affaires on doit moins s'appliquer à faire naître des occasions qu'à profiter de celles qui se présentent.",
            u"Dans les premières passions les femmes aiment l'amant, et dans les autres elles aiment l'amour.",
            u"Dans toutes les existences, on note une date où bifurque la destinée, soit vers une catastrophe, soit vers le succès.",
            u"Dans toutes les professions chacun affecte une mine et un extérieur pour paraître ce qu'il veut qu'on le croie. Ainsi on peut dire que le monde n'est composé que de mines.",
            u"De tous nos défauts, celui dont nous demeurons le plus aisément d'accord, c'est de la paresse; nous nous persuadons qu'elle tient à toutes les vertus paisibles et que, sans détruire entièrement les autres, elle en suspend seulement les fonctions.",
            u"De toutes les passions violentes, celle qui sied le moins mal aux femmes, c'est l'amour.",
            u"Détromper un homme préoccupé de son mérite est lui rendre un aussi mauvais office que celui que l'on rendit à ce fou d'Athènes, qui croyait que tous les vaisseaux qui arrivaient dans le port étaient à lui.",
            u"Dieu a permis, pour punir l'homme du péché originel, qu'il se fît un dieu de son amour-propre pour en être tourmenté dans toutes les actions de sa vie.",
            u"En amour celui qui est guéri le premier est toujours le mieux guéri.",
            u"En vieillissant on devient plus fou et plus sage.",
            u"Force gens veulent être dévots, mais personne ne veut être humble.",
            u"Il arrive quelquefois des accidents dans la vie d'où il faut être un peu fou pour se bien tirer.",
            u"Il arrive souvent que des choses se présentent plus achevées à notre esprit qu'il ne les pourrait faire avec beaucoup d'art.",
            u"Il doit y avoir une certaine proportion entre les actions et les desseins si on en veut tirer tous les effets qu'elles peuvent produire.",
            u"Il en est du véritable amour comme de l'apparition des esprits; tout le monde en parle, mais peu de gens en ont vu.",
            u"Il est aussi facile de se tromper soi-même sans s'en apercevoir qu'il est difficile de tromper les autres sans qu'ils s'en aperçoivent.",
            u"Il est aussi honnête d'être glorieux avec soi-même qu'il est ridicule de l'être avec les autres.",
            u"Il est aussi ordinaire de voir changer les goûts qu'il est extraordinaire de voir changer les inclinations.",
            u"Il est de certaines bonnes qualités comme des sens: ceux qui en sont entièrement privés ne les peuvent apercevoir ni les comprendre.",
            u"Il est de la reconnaissance comme de la bonne foi des marchands: elle entretient le commerce; et nous ne payons pas parce qu'il est juste de nous acquitter, mais pour trouver plus facilement des gens qui nous prêtent.",
            u"Il est difficile d'aimer ceux que nous n'estimons point; mais il ne l'est pas moins d'aimer ceux que nous estimons beaucoup plus que nous.",
            u"Il est difficile de définir l'amour. Dans l'âme c'est une passion de régner, dans les esprits c'est une sympathie, et dans le corps ce n'est qu'une envie cachée et délicate de posséder ce que l'on aime après beaucoup de mystères.",
            u"Il est difficile de juger si un procédé net, sincère et honnête est un effet de probité ou d'habileté.",
            u"Il est du véritable amour comme de l'apparition des esprits: tout le monde en parle, mais peu de gens en ont vu.",
            u"Il est impossible d'aimer une seconde fois ce qu'on a véritablement cessé d'aimer.",
            u"Il est plus aisé d'être sage pour les autres que de l'être pour soi-même.",
            u"Il est plus aisé de connaître l'homme en général que de connaître un homme en particulier.",
            u"Il est plus difficile d'être fidèle à sa maîtresse quand on est heureux que quand on en est maltraité",
            u"Il est plus difficile de dissimuler les sentiments que l'on a que de feindre ceux que l'on n'a pas.",
            u"Il est plus difficile de s'empêcher d'être gouverné que de gouverner les autres.",
            u"Il est plus facile d'éteindre un premier désir que de satisfaire tous ceux qui le suivent.",
            u"Il est plus facile de paraître digne des emplois qu'on n'a pas que de ceux que l'on exerce.",
            u"Il est plus facile de prendre de l'amour quand on n'en a pas, que de s'en défaire, quand on en a.",
            u"Il est plus honteux de se défier de ses amis que d'en être trompé.",
            u"Il est plus nécessaire d'étudier les hommes que les livres.",
            u"Il est quelquefois agréable à un mari d'avoir une femme jalouse; il entend toujours parler de ce qu'il aime.",
            u"Il est souvent plus grand d'avouer ses fautes que de n'en pas commettre.",
            u"Il faut demeurer d'accord à l'honneur de la vertu que les plus grands malheurs des hommes sont ceux où ils tombent par les crimes.Il faut de plus grandes vertus pour soutenir la bonne fortune que la mauvaise.",
            u"Il faut écouter ceux qui parlent, si on veut en être écouté.",
            u"Il faut gouverner la fortune comme la santé: en jouir quand elle est bonne, prendre patience quand elle est mauvaise, et ne faire jamais de grands remèdes sans un extrême besoin.",
            u"Il faut peu de choses pour rendre le sage heureux; rien ne peut rendre un fol content; c'est pourquoi presque tous les hommes sont misérables.",
            u"Il faut que les jeunes gens qui entrent dans le monde soient honteux ou étourdis: un air capable et composé se tourne d'ordinaire en impertinence.",
            u"Il faut tenir à une résolution parce qu'elle est bonne, et non parce qu'on l'a prise.",
            u"Il n'appartient qu'aux grands hommes d'avoir de grands défauts.",
            u"Il n'est jamais plus difficile de bien parler que quand on a honte de se taire.",
            u"Il n'est pas si dangereux de faire du mal à la plupart des hommes que de leur faire trop de bien.",
            u"Il n'est rien de plus naturel ni de plus trompeur que de croire qu'on est aimé.",
            u"Il n'y a guère d'homme assez habile pour connaître tout le mal qu'il fait.",
            u"Il n'y a guère d'occasion où l'on fit un méchant marche de renoncer au bien qu'on dit de nous, à condition de n'en dire point de mal.",
            u"Il n'y a guère de gens qui ne soient honteux de s'être aimés quand ils ne s'aiment plus.",
            u"Il n'y a guère de personnes qui dans le premier penchant de l'âge ne fassent connaître par où leur corps et leur esprit doivent défaillir.",
            u"Il n'y a guère de poltrons qui connaissent toujours toute leur peur.",
            u"Il n'y a pas moins d'éloquence dans le ton de la voix, dans les yeux et dans l'air de la personne, que dans le choix des paroles.",
            u"Il n'y a pas quelquefois moins d'habileté à savoir profiter d'un bon conseil qu'à se bien conseiller soi-même.",
            u"Il n'y a point d'accidents si malheureux dont les habiles gens ne tirent quelque avantage, ni de si heureux que les imprudents ne puissent tourner à leur préjudice.",
            u"Il n'y a point d'éloges qu'on ne donne à la prudence. Cependant elle ne saurait nous assurer du moindre événement.",
            u"Il n'y a point d'homme qui se croie en chacune de ses qualités au-dessous de l'homme du monde qu'il estime le plus.",
            u"Il n'y a point de déguisement qui puisse longtemps cacher l'amour où il est, ni le feindre où il n'est pas.",
            u"Il n'y a point de gens qui aient plus souvent tort que ceux qui ne peuvent souffrir d'en avoir.",
            u"Il n'y a point de passion où l'amour de soi-même règne si puissamment que dans l'amour; et on est toujours plus disposé à sacrifier le repos de ce qu'on aime qu'à perdre le sien.",
            u"Il n'y a point de sots si incommodes que ceux qui ont de l'esprit.",
            u"Il n'y a qu'une sorte d'amour, mais il y a mille différentes copies.",
            u"Il n'y a que ceux qui sont méprisables qui craignent d'être méprisés.",
            u"Il n'y a que les personnes qui ont de la fermeté qui puissent avoir une véritable douceur; celles qui paraissent douces n'ont d'ordinaire que de la faiblesse, qui se convertit aisément en aigreur.",
            u"Il ne faut pas s'offenser que les autres nous cachent la vérité, puisque nous nous la cachons si souvent à nous-mêmes.",
            u"Il ne peut y avoir de règle dans l'esprit ni dans le coeur des femmes, si le tempérament n'en est d'accord.",
            u"Il ne sert de rien d'être jeune sans être belle, ni d'être belle sans être jeune.",
            u"Il s'en faut bien que ceux qui s'attrapent à nos finesses ne nous paraissent aussi ridicules que nous nous le paraissons à nous-mêmes quand les finesses des autres nous ont attrapés.",
            u"Il s'en faut bien que l'innocence ne trouve autant de protection que le crime.",
            u"Il s'en faut bien que nous connaissions tout ce que nos passions nous font faire.",
            u"Il s'en faut bien que nous ne connaissions toutes nos volontés.",
            u"Il semble que c'est le diable qui a tout exprès placé la paresse à la frontière de plusieurs vertus.",
            u"Il semble que la nature ait prescrit à chaque homme dès sa naissance des bornes pour les vertus et pour les vices.",
            u"Il semble que la nature, qui a si sagement disposé les organes de notre corps pour nous rendre heureux, nous ait aussi donné l'orgueil pour nous épargner la douleur de connaître nos imperfections.",
            u"Il semble que nos actions aient des étoiles heureuses ou malheureuses à qui elles doivent une grande partie de la louange et du blâme qu'on leur donne.",
            u"Il suffit quelquefois d'être grossier pour n'être pas trompé par un habile homme.",
            u"Il vaut mieux employer notre esprit à supporter les infortunes qui nous arrivent qu'à prévoir celles qui nous peuvent arriver.",
            u"Il y a dans la jalousie plus d'amour-propre que d'amour.",
            u"Il y a dans le coeur humain une génération perpétuelle de passions, en sorte que la ruine de l'une est presque toujours l'établissement d'une autre.",
            u"Il y a de belles choses qui ont plus d'éclat quand elles demeurent imparfaites que quand elles sont trop achevées.",
            u"Il y a de bonnes qualités qui dégénèrent en défauts quand elles sont naturelles.",
            u"Il y a de bons mariages, mais il n'y en a point de délicieux.",
            u"Il y a de certaines larmes qui nous trompent souvent nous-mêmes après avoir trompé les autres.",
            u"Il y a de certains défauts qui, bien mis en oeuvre, brillent plus que la vertu même.",
            u"Il y a de méchantes qualités qui font de grands talents.",
            u"Il y a des affaires et des maladies que les remèdes aigrissent en certains temps; et la grande habileté consiste à connaître quand il est dangereux d'en user.",
            u"Il y a des crimes qui deviennent innocents, et même glorieux, par leur éclat, leur nombre et leur excès; de là vient que les voleries publiques sont des habiletés, et que prendre des provinces injustement s'appelle faire des conquêtes.",
            u"Il y a des faussetés déguisées qui représentent si bien la vérité que ce serait mal juger que de ne s'y pas laisser tromper.",
            u"Il y a des folies qui se prennent comme les maladies contagieuses.",
            u"Il y a des gens de qui l'on peut ne jamais croire du mal sans l'avoir vu; mais il n'y en a point en qui il nous doive surprendre en le voyant.",
            u"Il y a des gens dégoûtants avec du mérite, et d'autres qui plaisent avec des défauts.",
            u"Il y a des gens destinés à être sots, qui ne font pas seulement des sottises par leur choix, mais que la fortune même contraint d'en faire.",
            u"Il y a des gens dont tout le mérite consiste à dire et à faire des sottises utilement, et qui gâteraient tout s'ils changeaient de conduite.",
            u"Il y a des gens niais qui se connaissent et qui emploient habilement leur niaiserie.",
            u"Il y a des gens qu'on approuve dans le monde, qui n'ont pour tout mérite que les vices qui servent au commerce de la vie.",
            u"Il y a des gens qui n'auraient jamais été amoureux s'ils n'avaient jamais entendu parler de l'amour.",
            u"Il y a des gens qui ressemblent aux vaudevilles, qu'on ne chante qu'un certain temps.",
            u"Il y a des gens si remplis d'eux-mêmes que, lorsqu'ils sont amoureux, ils trouvent moyen d'être occupés de leur passion sans l'être de la personne qu'ils aiment.",
            u"Il y a des héros en mal comme en bien.",
            u"Il y a des méchants qui seraient moins dangereux s'ils n'avaient aucune bonté.",
            u"Il y a des personnes à qui les défauts siéent bien, et d'autres qui sont disgraciées avec leurs bonnes qualités.",
            u"Il y a des personnes si légères et si frivoles qu'elles sont aussi éloignées d'avoir de véritables défauts que des qualités solides.",
            u"Il y a des rechutes dans les maladies de l'âme, comme dans celles du corps. Ce que nous prenons pour notre guérison n'est le plus souvent qu'un relâche ou un changement de mal.",
            u"Il y a des reproches qui louent, et des louanges qui médisent.",
            u"Il y a deux sortes de constance en amour: l'une vient de ce que l'on trouve sans cesse dans la personne que l'on aime de nouveaux sujets d'aimer, et l'autre vient de ce que l'on se fait un honneur d'être constant.",
            u"Il y a diverses sortes de curiosité: l'une d'intérêt, qui nous porte à désirer d'apprendre ce qui nous peut être utile, et l'autre d'orgueil, qui vient du désir de savoir ce que les autres ignorent.",
            u"Il y a du mérite sans élévation, mais il n'y a point d'élévation sans quelque mérite.",
            u"Il y a encore plus de gens sans intérêt que sans envie.",
            u"Il y a peu d'honnêtes femmes qui ne soient lasses de leur métier.",
            u"Il y a peu de femmes dont le mérite dure plus que la beauté.Il y a peu de choses impossibles d'elles-mêmes; et l'application pour les faire réussir nous manque plus que les moyens.",
            u"Il y a plus de défauts dans l'humeur que dans l'esprit.",
            u"Il y a plusieurs remèdes qui guérissent de l'amour, mais il n'y en a point d'infaillibles.",
            u"Il y a quelque différence entre un esprit de feu et un esprit brillant: un esprit de feu va plus loin et avec plus de rapidité; un esprit brillant a de la vivacité, de l'agrément et de la justesse.",
            u"Il y a souvent plus d'orgueil que de bonté à plaindre les malheurs de nos ennemis; c'est pour leur faire sentir que nous sommes au-dessus d'eux que nous leur donnons des marques de compassion.",
            u"Il y a un excès de biens et de maux qui passe notre sensibilité.",
            u"Il y a une certaine reconnaissance vive qui ne nous acquitte pas seulement des bienfaits que nous avons reçus, mais qui fait même que nos amis nous doivent en leur payant ce que nous leur devons.",
            u"Il y a une certaine sorte d'amour dont l'excès empêche la jalousie.",
            u"Il y a une inconstance qui vient de la légèreté de l'esprit ou de sa faiblesse, qui lui fait recevoir toutes les opinions d'autrui, et il y en a une autre, qui est plus excusable, qui vient du dégoût des choses.",
            u"Il y a une infinité de conduites qui paraissent ridicules, et dont les raisons cachées sont très sages et très solides.",
            u"L'absence diminue les médiocres passions et augmente les grandes, comme le vent éteint les bougies et allume le feu.",
            u"L'accent du pays où l'on est né demeure dans l'esprit et dans le coeur, comme dans le langage.",
            u"L'air bourgeois se perd quelquefois à l'armée; mais il ne se perd jamais à la cour.",
            u"L'ambition ne me travaille point. Je ne crains guère de choses et ne crains aucunement la mort.",
            u"L'amour aussi bien que le feu ne peut subsister sans un mouvement continuel; et il cesse de vivre dès qu'il cesse d'espérer ou de craindre.",
            u"L'amour de la gloire, la crainte de la honte, le dessein de faire fortune, le désir de rendre notre vie commode et agréable, et l'envie d'abaisser les autres, sont souvent les causes de cette valeur si célèbre parmi les hommes.",
            u"L'amour de la justice n'est pour la plupart des hommes que la crainte de souffrir l'injustice.",
            u"L'amour est à l'âme de celui qui aime ce que l'âme est au corps qu'elle anime.",
            u"L'amour prête son nom à un nombre infini de commerces qu'on lui attribue, et où il n'a non plus de part que le Doge à ce qui se fait à Venise.",
            u"L'amour, tout agréable qu'il est, plaît encore plus par les manières dont il se montre que par lui-même.",
            u"L'amour-propre est l'amour de soi-même et de toutes choses pour soi.",
            u"L'amour-propre est le plus grand de tous les flatteurs.",
            u"L'amour-propre est plus habile que le plus habile homme du monde.",
            u"L'amour-propre nous augmente ou nous diminue les bonnes qualités de nos amis à proportion de la satisfaction que nous avons d'eux; et nous jugeons de leur mérite par la manière dont ils vivent avec nous.",
            u"L'approbation que l'on donne à ceux qui entrent dans le monde vient souvent de l'envie secrète que l'on porte à ceux qui y sont établis.",
            u"L'art de savoir bien mettre en oeuvre de médiocres qualités dérobe l'estime et donne souvent plus de réputation que le véritable mérite.",
            u"L'attachement ou l'indifférence que les philosophes avaient pour la vie n'était qu'un goût de leur amour-propre, dont on ne doit non plus disputer que du goût de la langue ou du choix des couleurs.",
            u"L'avarice est plus opposée à l'économie que la libéralité.",
            u"L'avarice produit souvent des effets contraires; il y a un nombre infini de gens qui sacrifient tout leur bien à des espérances douteuses et éloignées, d'autres méprisent de grands avantages à venir pour de petits intérêts présents.",
            u"L'aversion du mensonge est souvent une imperceptible ambition de rendre nos témoignages considérables, et d'attirer à nos paroles un respect de religion.",
            u"L'éducation que l'on donne d'ordinaire aux jeunes gens est un second amour-propre qu'on leur inspire.",
            u"L'élévation est au mérite ce que la parure est aux belles personnes.",
            u"L'enfer des femmes, c'est la vieillesse.",
            u"L'envie d'être plaint, ou d'être admiré, fait souvent la plus grande partie de notre confiance.",
            u"L'envie de parler de nous, et de faire voir nos défauts du côté que nous voulons bien les montrer, fait une grande partie de notre sincérité.",
            u"L'envie est détruite par la véritable amitié, et la coquetterie par le véritable amour.",
            u"L'envie est plus irréconciliable que la haine.",
            u"L'espérance et la crainte sont inséparables, et il n'y a point de crainte sans espérance ni d'espérance sans crainte.",
            u"L'esprit de la plupart des femmes sert plus à fortifier leur folie que leur raison.L'espérance, toute trompeuse qu'elle est, sert au moins à nous mener à la fin de la vie par un chemin agréable.",
            u"L'esprit est toujours la dupe du coeur",
            u"L'esprit ne saurait jouer longtemps le personnage du coeur.",
            u"L'esprit nous sert quelquefois à faire hardiment des sottises.",
            u"L'extrême avarice se méprend presque toujours; il n'y a point de passion qui s'éloigne plus souvent de son but, ni sur qui le présent ait tant de pouvoir au préjudice de l'avenir.",
            u"L'extrême ennui sert à nous désennuyer.",
            u"L'extrême plaisir que nous prenons à parler de nous-mêmes nous doit faire craindre de n'en donner guère à ceux qui nous écoutent.",
            u"L'homme croit souvent se conduire lorsqu'il est conduit; et pendant que par son esprit il tend à un but, son coeur l'entraîne insensiblement à un autre.",
            u"L'homme le plus simple qui a de la passion persuade mieux que le plus éloquent qui n'en a point.",
            u"L'honnêteté des femmes est souvent l'amour de leur réputation et de leur repos.",
            u"L'honneur acquis est caution de celui qu'on doit acquérir.",
            u"L'humilité est l'autel sur lequel Dieu veut qu'on lui fasse des sacrifices.",
            u"L'humilité est la véritable preuve des vertus chrétiennes: sans elle nous conservons tous nos défauts, et ils sont seulement couverts par l'orgueil qui les cache aux autres, et souvent à nous-mêmes.",
            u"L'humilité n'est souvent qu'une feinte soumission, dont on se sert pour soumettre les autres. ...",
            u"L'hypocrisie est un hommage que le vice rend à la vertu.",
            u"L'imagination ne saurait inventer tant de diverses contrariétés qu'il y en a naturellement dans le coeur de chaque personne.",
            u"L'intention de ne jamais tromper nous expose à être souvent trompés.",
            u"L'intérêt met en oeuvre toutes sortes de vertus et de vices.",
            u"L'intérêt parle toutes sortes de langues, et joue toutes sortes de personnages, même celui de désintéressé.",
            u"L'intérêt que l'on accuse de tous nos crimes mérite souvent d'être loué de nos bonnes actions.",
            u"L'intérêt, qui aveugle les uns, fait la lumière des autres.",
            u"L'on fait plus souvent des trahisons par faiblesse que par un dessein formé de trahir.",
            u"L'orgueil a plus de part que la bonté aux remontrances que nous faisons à ceux qui commettent des fautes; et nous ne les reprenons pas tant pour les en corriger que pour leur persuader que nous en sommes exempts.",
            u"L'orgueil a ses bizarreries, comme les autres passions; on a honte d'avouer que l'on ait de la jalousie, et on se fait honneur d'en avoir eu, et d'être capable d'en avoir."
        ]

            # Jean Jacques Rousseau
        rousseau = [
            u"A moins qu'une belle femme ne soit un ange, son mari est le plus malheureux des hommes.",
            u"A quoi bon chercher notre bonheur dans l'opinion d'autrui, si nous pouvons le trouver en nous-mêmes?",
            u"Ah! qu'on a de peine à briser les noeuds qui lient nos coeurs à la terre! et qu'il est sage de la quitter aussitôt qu'ils sont rompus!",
            u"Ah! que veux-tu qu'un coeur brûlé d'amour fasse durant tant de siècles? L'absence même serait moins cruelle.",
            u"Ainsi nous tenons à tout, nous nous accrochons à tout ...",
            u"Aliéner, c'est donner ou vendre.",
            u"Alors mes yeux se dessillèrent; je sentis mon malheur, j'en gémis, mais je n'en prévis pas les suites.",
            u"Apercevoir, c'est sentir; comparer, c'est juger; juger et sentir ne sont pas la même chose.",
            u"Appropriez l'éducation de l'homme à l'homme, et non pas à ce qui n'est point lui.",
            u"Après avoir fait les délices des sociétés les plus aimables, il mourut de douleur sur un vil grabat.",
            u"Après de longues angoisses, au lieu du désespoir qui semblait devoir être enfin mon partage, j'ai retrouvé la sérénité.",
            u"Au fond, c'est moins le coup que la crainte qui tourmente, quand on s'est blessé.",
            u"Au fond, l'argent n'est pas la richesse, il n'en est que le signe; ce n'est pas le signe qu'il faut multiplier, mais la chose représentée.",
            u"Au lieu de soulager mes maux, je n'ai fait que les augmenter en m'exposant à votre disgrâce, et je sens que le pire de tous est de vous déplaire.",
            u"Au moins se doit-on à soi-même de rendre honneur à l'humanité souffrante ou à son image, et de ne point s'endurcir le coeur à l'aspect de ses misères.",
            u"Au reste, il ne faut jamais souffrir qu'aucune loi tombe en désuétude. Fût-elle indifférente, fût-elle mauvaise, il faut l'abroger formellement, ou la maintenir en vigueur.",
            u"Aussi simple et aussi novice qu'auparavant je ne restai pas même affriandé de jolies femmes.",
            u"Autant le toucher concentre ses opérations autour de l'homme, autant la vue étend les siennes au delà de lui; c'est là ce qui rend celles-ci trompeuses: d'un coup d'oeil un homme embrasse la moitié de son horizon.",
            u"Avant de songer à détruire un usage établi, on doit avoir bien pesé ceux qui s'introduiront à sa place.",
            u"Avec un sang brûlant de sensualité presque dès ma naissance, je me conservai pur de toute souillure jusqu'à l'âge où les tempéraments les plus froids et les plus tardifs se développent.",
            u"Badin, folâtre, inépuisable, séduisant dans la conversation, souriant toujours et ne riant jamais, il disait du ton le plus élégant les choses les plus grossières, et les faisait passer.",
            u"C'est ainsi qu'Empédocle reprochait aux Agrigentins d'entasser les plaisirs comme s'ils n'avaient qu'un jour à vivre et de bâtir comme s'ils ne devaient jamais mourir.",
            u"C'est dans les siècles les plus dépravés qu'on aime les leçons de la morale la plus parfaite. Cela dispense de les pratiquer.",
            u"C'est l'affluence des hôtes qui détruit l'hospitalité.",
            u"C'est un excellent moyen de bien voir les conséquences des choses, que de sentir vivement tous les risques qu'elles nous font courir.",
            u"C'est une bonne et honnête fille, qui me sert depuis vingt ans avec l'attachement d'une fille à son père, plutôt que d'une domestique à son maître.",
            u"C'est une prévoyance très nécessaire de sentir qu'on ne peut tout prévoir.",
            u"C'est, je crois, par toutes ces raisons que les jeunes filles acquièrent si vite un petit babil agréable, qu'elles mettent de l'accent dans leurs propos ...",
            u"C'était une rupture, mais dans des termes tels que la plus infernale haine les peut dicter.",
            u"Car enfin, tu as beau dire, une certaine coquetterie maligne et railleuse désoriente encore plus les soupirants que le silence ou le mépris.",
            u"Ce ne sont pas des saillies, et ce n'est pas même proprement de la finesse: mais c'est une délicatesse exquise, qui ne frappe jamais et qui plaît toujours.",
            u"Ce sont les grandes occasions qui font les grands hommes.",
            u"Ce sont les petites précautions qui conservent les grandes vertus.",
            u"Celui de tous mes écrits où ces principes sont manifestés avec le plus de hardiesse, pour ne pas dire d'audace.",
            u"Cependant voyez la différence: ce pain bis, que vous trouvez si bon, vient du blé recueilli par ce paysan; son vin noir et grossier, mais désaltérant et sain, est du cru de sa vigne.",
            u"Ces deux mots patrie et citoyen doivent être effacés des langues modernes.",
            u"Cet être qui veut et qui peut, cet être actif par lui-même, cet être enfin, quel qu'il soit, qui meut l'univers et ordonne toutes choses, je l'appelle Dieu.",
            u"Cette admirable institution des patrons et des clients fut un chef-d'oeuvre de politique et d'humanité.",
            u"Cette femme a un petit garçon fort gentil, mais boiteux, qui, clopinant avec ses béquilles, s'en va d'assez bonne grâce demander l'aumône aux passants.",
            u"Chacun avance plus ou moins selon son génie, son goût, ses besoins, ses talents, son zèle, et les occasions qu'il a de s'y livrer.",
            u"Chaque homme apporte en naissant un caractère, un génie et des talents qui lui sont propres.",
            u"Combien de vertus apparentes cachent souvent des vices réels!",
            u"Conscience! Conscience! Instinct divin, immortelle et céleste voix.",
            u"D'autres goûts avaient un peu attiédi l'affection paternelle depuis que je vivais loin de lui.",
            u"D'un ton grave et d'un accent appuyé.",
            u"Dans le commencement de la vie, où la mémoire et l'imagination sont encore inactives, l'enfant n'est attentif qu'à ce qui affecte actuellement ses sens; ...",
            u"Dans le hameau cette maison a quelque apparence.",
            u"Dans les inextricables tortuosités de ce labyrinthe j'arrangerais, au milieu de huit ou dix boîtes d'attrapes, une autre boîte presque semblable, bien garnie de bonbons.",
            u"Dans toutes les questions de morale difficiles comme celle-ci, je me suis toujours bien trouvé de les résoudre par le dictamen de ma conscience, plutôt que par les lumières de ma raison.",
            u"De belles couleurs bien nuancées plaisent à la vue, mais ce plaisir est purement de sensation. C'est le dessin, c'est l'imitation qui donne à ces couleurs de la vie et de l'âme ... .",
            u"De cela même qui semble mettre le goût au-dessous d'eux, et rendre plus méprisable le penchant qui nous y livre, je conclurais au contraire que le moyen le plus convenable pour gouverner les enfants est de les mener par leur bouche.",
            u"De là vient l'extrême difficulté que je trouve à écrire. Mes manuscrits, raturés, barbouillés, mêlés, indéchiffrables, attestent la peine qu'ils m'ont coûtée.",
            u"Depuis que le monde existe on n'a jamais vu deux amants en cheveux blancs soupirer l'un pour l'autre.",
            u"Des événements imprévus nous barrèrent, et ce projet en demeura là.",
            u"Des ministres, des parents, des cagots, des quidams de toute espèce, venaient de Genève et de Suisse, non pas comme ceux de France, pour m'admirer et me persifler, mais pour me tancer et catéchiser.",
            u"Deux femmes qui ont des secrets aiment à babiller ensemble.",
            u"Deux jeunes époux, unis sous d'heureux auspices, sortant du lit nuptial, et portant à la fois dans leurs regards languissants et chastes l'ivresse des doux plaisirs qu'ils viennent de goûter, l'aimable sécurité de l'innocence ...",
            u"Diderot ne datait jamais ses lettres. Mme d'Epinay, Mme d'Houdetot ne dataient guère les leurs que du jour de la semaine.",
            u"Diminuez donc les désirs, c'est comme si vous augmentiez les forces.",
            u"Du reste, que j'aie abandonné les échecs, ou qu'en jouant je ne sois remis en haleine, je n'ai jamais avancé d'un cran depuis cette première séance.",
            u"Elle avait là-dessus une simplicité de coeur, une franchise plus éloquente que des ergoteries, et qui souvent embarrassait jusqu'à son confesseur, car elle ne lui déguisait rien.",
            u"Elle était à la conversation comme si elle n'avait eu autre chose à faire.",
            u"Elle leur donne des conseils; elle accommode leurs différends.",
            u"Emile n'aura ni bourrelets, ni paniers roulants, ni chariots, ni lisières; ou du moins, dès qu'il commencera de savoir mettre un pied devant l'autre, on ne le soutiendra que sur les lieux pavés, et l'on ne fera qu'y passer en hâte.",
            u"En buvant et baragouinant nous achevâmes de nous familiariser et dès la fin du repas nous devînmes inséparables",
            u"En entassant des imputations contradictoires, la calomnie se découvre elle-même: mais la malignité est aveugle et la passion ne raisonne pas.",
            u"En général, les croyants font Dieu comme ils sont eux-mêmes; les bons le bon, les méchants font le méchant.",
            u"En n'asservissant les honnêtes femmes qu'à de tristes devoirs, on a banni du mariage tout ce qui pouvait le rendre agréable aux hommes.",
            u"En tout état de cause, un dénonciateur qui se cache joue un rôle odieux, bas, lâche.",
            u"En voyant déjà commencer la décadence de l'Angleterre ... je me laisse bercer au fol espoir que la nation française, à son tour victorieuse, viendra peut-être un jour me délivrer de la triste captivité où je vis.",
            u"En voyant moins, on imaginera plus.",
            u"Encore un coup, le vrai bonheur ne se décrit pas, il se sent, et se sent d'autant mieux qu'il peut le moins se décrire, parce qu'il ne résulte pas d'un recueil de faits, mais qu'il est un état permanent.",
            u"Enfant encore, et livré à moi-même, alléché par des caresses, séduit par la vanité.",
            u"Et dans ce monde et dans l'autre, les méchants sont toujours bien embarrassants.",
            u"Et le prince seul a droit de battre monnaie attendu que lui seul a droit d'exiger que son témoignage fasse autorité parmi tout un peuple.",
            u"Et quand, entraîné par le plaisir d'écrire, j'ajoutais à des choses réelles des ornements inventés, j'avais plus de tort encore parce qu'orner la vérité par des fables c'est en effet la défigurer.",
            u"Etre aimé de tout ce qui m'approchait était le plus vif de mes désirs.",
            u"Exister pour nous c'est sentir. Notre sensibilité est antérieure à notre intelligence et nous avons des sentiments avant des idées.",
            u"Faire route à pied par un beau temps, dans un beau pays, sans être pressé, et avoir pour terme de ma course un objet agréable: voilà de toutes les manières de vivre celle qui est le plus à mon goût.",
            u"Généralement, les gens qui savent peu parlent beaucoup, et les gens qui savent beaucoup parlent peu.",
            u"Ici se forge le premier anneau de cette longue chaîne dont l'ordre social est formé.",
            u"Ignores-tu qu'il est des tentations déshonorantes qui n'approchèrent jamais d'une âme honnête, qu'il est même honteux de les vaincre, et que se précautionner contre elles est moins s'humilier que s'avilir?",
            u"Il a été reconnu que la bouillie n'est pas une nourriture fort saine. Le lait cuit et la farine crue font beaucoup de saburre, et conviennent mal à notre estomac.",
            u"Il convient que l'impôt soit payé par celui qui emploie la chose taxée plutôt que par celui qui la vend.",
            u"Il est aisé de convaincre un enfant que ce qu'on lui veut enseigner est utile: mais ce n'est rien de le convaincre, si l'on ne sait le persuader.Il écrivit au pasteur dont la salope était paroissienne, et fit en sorte d'assoupir l'affaire ...",
            u"Il est faux qu'à s'en abstraire par vertu l'on se fasse mépriser.",
            u"Il est permis d'endormir son auditoire, mais non pas l'impatienter.",
            u"Il est utile à l'homme de connaître tous les lieux où l'on peut vivre, afin de choisir ensuite ceux où l'on peut vivre le plus commodément.",
            u"Il était moins à l'étroit, moins gêné, moins comprimé dans l'amios qu'il n'est dans ses langes.",
            u"Il faut avoir déjà beaucoup appris de choses pour savoir demander ce qu'on ne sait pas.",
            u"Il faut bien mentir quelquefois quand on est évêque.",
            u"Il faut parler tant qu'on peut par les actions, et ne dire que ce qu'on ne saurait faire.",
            u"Il faut rougir de faire une faute, et non de la réparer.",
            u"Il importe de s'accoutumer d'abord à être mal couché; c'est le moyen de ne plus trouver de mauvais lit.",
            u"Il n'est jamais permis de détériorer une âme humaine pour l'avantage des autres, ni de faire un scélérat pour le service des honnêtes gens.",
            u"Il n'y a pas de véritable action sans volonté.",
            u"Il n'y a point de liberté sans loi.",
            u"Il n'y a point naturellement pour l'homme de médecin plus sûr que son propre appétit ...",
            u"Il n'y a que la force de l'Etat qui fasse la liberté de ses membres.",
            u"Il n'y a que le délire de ma passion qui puisse voiler l'horreur de ma situation présente.",
            u"Il ne faut accorder aux sens quand on veut leur refuser quelque chose.",
            u"Il ne faut point refuser pour refuser, mais pour faire valoir ce qu'on accorde.",
            u"Il ne put se contenir; il m'apostropha avec une brutalité qui scandalisa tout le monde.",
            u"Il ne s'exprimait jamais sur mon compte qu'en termes outrageants, méprisants, sans me désigner autrement que par ce petit cuistre.",
            u"Il parvint, malgré des concurrents très jaloux, à être élu définiteur de sa province.",
            u"Il prit sur-le-champ la résolution de s'enfuir la nuit suivante, et rien ne put l'en faire démordre.",
            u"Il supporta toutes ces pertes avec un courage apparent; mais son coeur ne cessa de saigner en dedans tout le reste de sa vie, et sa santé ne fit plus que décliner.",
            u"Il y a deux sortes de dépendance: celle des choses, qui est de la nature; celle des hommes, qui est de la société.",
            u"Il y a donc trois sortes d'aristocratie: naturelle, élective, héréditaire. La première ne convient qu'a des peuples simples; le troisième est le pire de tous les gouvernements. La deuxième est le meilleur; c'est l'aristocratie propement dite.",
            u"Il y a souvent plus de stupidité que de courage dans une constance apparente.",
            u"Il y a toujours vingt à parier contre un qu'un gentilhomme descend d'un fripon.",
            u"Ils ne m'empêcheront pas de jouir de mon innocence, et d'achever mes jours en paix malgré eux.",
            u"Ils ont fait de leurs lois un dédale immense où la mémoire et la raison se perdent également.",
            u"Insensiblement ce grand mouvement s'apaise, ce chaos se débrouille, chaque chose vient se mettre à sa place.",
            u"J'achevai ce travail tout en en faisant d'autres, et trouvant toujours qu'un changement d'ouvrage est un véritable délassement.",
            u"J'adjure tout homme sincère de dire s'il ne sent pas au fond de son âme qu'il y a dans le trafic de soi-même quelque chose de servile et de bas.",
            u"J'ai consulté les auteurs; je n'ai trouvé que des charlatans qui se font un jeu de tromper les hommes sans autre loi que leur intérêt, sans autre dieu que leur réputation.",
            u"J'ai dit des vérités aux hommes; ils les ont mal prises; je ne dirai plus rien.",
            u"J'ai remarqué que les enfants ont rarement peur du tonnerre, à moins que les éclats ne soient affreux et ne blessent réellement l'organe de l'ouïe; autrement cette peur ne leur vient que quand ils ont appris que le tonnerre blesse ou tue quelquefois.J'ai été tellement agité, balloté, tiraillé par les passions d'autrui ...",
            u"J'ai toujours cru que le beau n'était que le bon mis en action, que l'un tenait intimement à l'autre, et qu'ils avaient tous deux une source commune dans la nature bien ordonnée.",
            u"J'ai toujours pris un singulier plaisir à apprivoiser les animaux, surtout ceux qui sont craintifs et sauvages.",
            u"J'ai toujours remarqué que les gens faux sont sobres, et la grande réserve de la table annonce assez souvent des moeurs feintes et des âmes troubles.",
            u"J'aimai mieux laisser subsister l'offense, et me bannir pour jamais de ma patrie, que d'y rentrer par des moyens violents et dangereux."
        ]

            # Franklin Delano Roosevelt
        roosevelt = [
            u"A certaines générations, il est beaucoup donné. A d'autres, au contraire, il est beaucoup demandé.",
            u"Faites quelque chose et, si ça ne réussi pas, essayez autre chose.",
            u"Gouverner, c'est maintenir les balances de la justice égales pour tous.",
            u"Il est dur d'échouer mais il est pire de n'avoir jamais tenté de réussir.",
            u"La seule chose que nous ayons à craindre est la crainte elle-même.",
            u"La seule limite à nos réalisations de demain sera nos doutes d'aujourd'hui.",
            u"Les caresses n'ont jamais transformé un tigre en chaton.",
            u"Les chutes futures des dictatures coûtent à l'humanité bien plus que n'importe quelle chute d'une démocratie.",
            u"Les livres sont la lumière qui guide la civilisation.",
            u"Un réactionnaire est un somnambule qui marche à reculons."
        ]

        # S
            # George Bernard Shaw
        shaw = [
            u"(Shakespeare) avait été à l'école et savait autant de latin et de grec qu'en retiennent la plupart des bacheliers: c'est-à-dire rien, au point de vue pratique.",
            u"A la nomination d'une petite minorité corrompue, la démocratie substitue l'élection par une masse incompétente.",
            u"A notre époque, on se refuse à croire que le plomb puisse être transformé en or... jusqu'au moment où on reçoit la facture du plombier.",
            u"A quoi sert l'argent s'il faut travailler pour en avoir?",
            u"A supposer qu'une femme déclare son amour à un homme au cours des cinq actes d'une pièce, celle-ci n'est monotone que s'il s'agit du même homme.A quoi servent les cartouches dans une bataille? Moi, à la place, j'emporte toujours du chocolat.",
            u"Après avoir entendu un certain nombre de récitals de piano, rien ne me détend plus que de m'asseoir dans le fauteuil du dentiste et de me faire plomber quelques dents.",
            u"Au Ciel, un ange n'a rien d'exceptionnel.",
            u"Aucun homme n'est l'égal d'une femme, si ce n'est avec un tisonnier et une paire de souliers à clous. Et encore, même ainsi, ne l'est-il pas toujours.",
            u"Aucune femme ne peut se débarasser de sa mère. Il devrait n'y avoir que des femmes, pas des mères.",
            u"Aussi longtemps que nous aurons des prisons, peu importe par qui les cellules sont occupées.",
            u"Avoir du bon sens est inné. Avoir suffisamment de bon sens fait le génie.",
            u"Beaucoup de gens ne sont jamais jeunes; quelques personnes ne sont jamais vieilles.",
            u"Ce ne sont pas les heures qui sont précieuses, ce sont les minutes.",
            u"Ce qu'il y a de désastreux dans la plupart des mariages, c'est que les deux conjoints sont épris de la même femme.",
            u"Ce que je suis, je le sais: un monument de publicité.",
            u"Ce qui flatte réellement un homme, c'est qu'on le juge digne dêtre flatté.",
            u"Celui qui désire une vie de bonheur avec une belle femme ressemble à celui qui veut jouir du goût du vin en ayant la bouche toujours pleine.",
            u"Celui qui peut, agit. Celui qui ne peut pas, enseigne.",
            u"Ceux que nous appelions des brutes eurent leur revanche quand Darwin nous prouva qu'ils étaient nos cousins.",
            u"Comme tous les jeunes gens, vous exagérez beaucoup la différence entre une jeune femme et une autre.",
            u"Dans la guerre, le courage et l'impétuosité sont de bons serviteurs. Mais ce sont de mauvais maîtres...",
            u"De nos jours, l'homme du monde est celui qui a assez d'argent pour faire ce que feraient tous les sots, s'ils en avaient les moyens: c'est-à-dire consommer sans produire.",
            u"De toutes les perversions sexuelles, la chasteté est la plus dangereuse.",
            u"Depuis que j'ai appris à rire de moi-même, je ne m'ennuie plus jamais.",
            u"Des gens qui croient dévotement à l'existence de personnages célestes sont tout aussi fous que ceux qui croient les voir.",
            u"Dieu a oublié d'en déposer le brevet, de sorte que le premier imbécile peut en faire autant.",
            u"Donnez aux femmes le droit de vote et, dans cinq ans, vous aurez un impôt sur les célibataires.",
            u"Est-ce qu'on peut arriver au Paradis une demi-heure avant que le diable sache qu'on est mort?",
            u"Est-ce que cela porte vraiment malheur de se marier un vendredi? - - Bien sûr! Pourquoi voulez-vous que le vendredi fasse exception?",
            u"Etre bigame, c'est avoir une femme de trop; être monogame aussi.",
            u"Etre patriote, c'est croire que votre pays a raison parce que vous y êtes né.",
            u"Grattez un Anglais et vous trouverez un protestant.",
            u"Il est beaucoup plus dangereux d'être un saint qu'un conquérant.",
            u"Il est dangereux d'être sincère, à moins d'être également stupide.",
            u"Il est toujours dangereux pour un homme de se montrer sincère - à moins qu'il ne soit totalement stupide.",
            u"Il n'y a pas d'amour plus sincère que celui de la bonne chère.",
            u"Il n'y a qu'une seule religion, bien qu'il y en ait un centaine de versions.",
            u"Il n'y a que le cadavre qui puisse supporter avec patience le Requiem de Brahms.",
            u"Il ne sait rien et croît tout savoir. Cela présage indubitablement une carrière politique.",
            u"Il y a ceux qui voient les choses telles qu'elles sont et se demandent pourquoi, et il y a ceux qui imaginent les choses telles qu'elles pourraient être et se disent... pourquoi pas?",
            u"Il y a des fous partout, même dans les asiles.",
            u"Il y a deux sortes de savants: les spécialistes, qui connaissent tout sur rien, et les philosophes, qui ne connaissent rien sur tout.",
            u"Il y a deux tragédies dans la vie. L'une est de ne pas obtenir ce que l'on désire ardemment, et l'autre de l'obtenir.",
            u"Il y a trois sortes de personnes à qui on ne peut demander du bons sens: un homme qui aime, une femme qui aime, une femme qui n'aime pas.",
            u"Isadora Duncan: une femme dont on aurait dit que le visage avait été sculpté dans du sucre, puis léché.",
            u"J'ai peur que nous ne devions rendre le monde honnête avant de pouvoir dire honnêtement à nos enfants que l'honnêteté est la meilleure politique.",
            u"J'avais un ami qui hésitait entre les diverses formes de suicide. Finalement, c'est le mariage qu'il a choisi.",
            u"Je fais de mon mieux pour être partial.",
            u"Je me cite souvent: cela apporte du piment à ma conversation.",
            u"Je n'observe jamais aucune règle de conduite. J'ai donc cessé d'en donner.",
            u"Je ne crois pas en la moralité. Je suis un disciple de Bernard Shaw.",
            u"Je ne résiste jamais à la tentation car j'ai découvert que ce qui est mauvais pour moi ne me tente pas.",
            u"Je ne vois pas bien pourquoi les hommes qui croient aux électrons se considèrent comme moins crédules que les hommes qui croient aux anges.",
            u"Je pense que l'on pourrait améliorer le choeur des alléluias en le plongeant environ dix minutes dans l'eau bouillante.",
            u"Je peux pardonner à Alfred Nobel d'avoir inventé la dynamite. Mais seul un ennemi avéré du genre humain a pu inventer le prix Nobel.",
            u"Je possède ce don d'observation appelé vulgairement cynisme par ceux qui en sont dépourvus.",
            u"Je suis contre l'avortement. Tuer un être humain avant qu'il ne soit né est impardonnable. C'est une preuve d'impatience.",
            u"Je suis le plus spontané des orateurs du monde parce que chaque geste et chaque réplique on été soigneusement répétés.",
            u"Je suppose que vous pensez rarement. Il y a très peu de gens qui pensent plus de trois ou quatre fois par an. Moi qui vous parle, je dois ma célébrité à ce que je pense une ou deux fois par semaine.",
            u"L'adolescence est l'âge où les enfants commencent à répondre eux-mêmes aux questions qu'ils posent.",
            u"L'alcool est un anesthésique qui permet de supporter l'opération de la vie.",
            u"L'alcool est un produit très nécessaire... Il permet au Parlement de prendre à onze heures du soir des décisions qu'aucun homme sensé ne prendrait à onze heures du matin.",
            u"L'Angleterre et l'Amérique sont séparées par la même langue.",
            u"L'argent du prix Nobel, c'est comme une bouée de sauvetage envoyée à un nageur ayant déjà atteint la côte en toute sécurité.",
            u"L'argent ne vaut rien pour l'homme qui a plus que le nécessaire.",
            u"L'assassinat est la forme extrême de la censure.",
            u"L'assassinat sur l'échafaud est la forme la plus exécrable d'assassinat, parce qu'il est investi de l'approbation de la société.",
            u"L'avenir du théâtre est sombre. Shakespeare est mort, Molière est mort, et moi-même je ne me sens pas très bien.",
            u"L'ennui de certaines conversations, c'est que les causeurs y parlent trop haut pour que leurs propos puissent nous endormir.",
            u"L'esclavage humain a atteint son point culminant à notre époque sous forme de travail librement salarié.",
            u"L'expérience nous apprend que l'homme n'apprend jamais rien de l'expérience.",
            u"L'explication du malheur de bien des gens, c'est qu'ils ont le temps de se demander s'ils sont heureux ou s'ils ne le sont pas.",
            u"L'homme est le seul animal qui rougisse; c'est d'ailleurs le seul animal qui ait à rougir de quelque chose.",
            u"L'homme le plus inquiet d'une prison est le directeur.",
            u"L'homme qui écoute la raison est perdu: la raison fait des esclaves de tous ceux qui ne sont pas assez forts pour la maîtriser.",
            u"L'homme raisonnable s'adapte au monde; l'homme déraisonnable s'obstine à essayer d'adapter le monde à lui-même. Tout progrès dépend donc de l'homme déraisonnable.",
            u"L'humanité serait depuis longtemps heureuse, si tout le génie que les hommes mettent à réparer leurs bêtises, ils l'employaient à ne pas les commettre.",
            u"L'hypocrisie est l'hommage que la vérité paie à l'erreur.",
            u"L'obéissance simule la subordination, exactement comme la crainte de la police simule l'honnêteté.",
            u"La décadence ne peut trouver d'agents que lorsqu'elle porte le masque du progrès.",
            u"La démocratie est une technique qui nous garantit de ne pas être mieux gouvernés que nous le méritons.",
            u"La façon la plus sûre de ruiner un homme qui ne sait pas gérer son argent est de lui en donner davantage encore.",
            u"La femme est l'addition des ennuis, la soustraction du porte-monnaie, la multiplication des ennemis et la division des hommes.",
            u"La férocité est la caractéristique des taureaux et autres végétariens.",
            u"La grandeur n'est qu'une des sensations de la petitesse.",
            u"La jeunesse, quelle chose merveilleuse, quel crime de la laisser gaspiller par les enfants!",
            u"La lecture est un stratagème qui dispense de réfléchir.",
            u"La liberté signifie la responsabilité. C'est pourquoi la plupart des hommes la craignent.",
            u"La ligne de conduite la plus prudente consiste non à être exigeant dans notre attachement aux choses anciennes ou téméraires et peu pratique à l'égard des choses nouvelles, mais à tirer le meilleur parti possible des unes et des autres.",
            u"La maison familiale est une prison pour les jeunes filles et une maison de correction pour les femmes.",
            u"La minorité a quelquefois raison, la majorité a toujours tort.",
            u"La mode selon laquelle nous pensons change comme la mode selon laquelle nous nous habillons et ... pour la plupart des gens, il est difficile, sinon impossible, de penser autrement que suivant la mode de leur époque.",
            u"La modestie n'est pas une vertu mais seulement de la prudence.",
            u"La monarchie constitutionnelle est un moyen pour combiner l'inertie d'une idole de bois avec la crédibilité en une idole de chair et de sang.",
            u"La mort ne m'impressionne pas, j'ai moi-même, en effet, l'intention bien arrêtée de mourir un jour.",
            u"La peur pousse les hommes à n'importe quelle décision extrême, et la peur inspirée par un être supérieur est un mystère qu'aucun raisonnement ne peut chasser.",
            u"La pudeur est la conspiration du silence de l'impudeur.",
            u"La règle d'or, c'est qu'il n'y a pas de règles d'or.",
            u"La solitude de Dieu est Sa force.",
            u"La vertu consiste non à s'abstenir mais à ne pas le désirer.",
            u"La vie est trop courte pour être prise au sérieux.",
            u"La vie ne cesse pas d'être gaie parce quelqu'un meurt, tout comme elle ne cesse pas d'être sérieuse quand les gens rient.",
            u"Le bonheur, est comme le blé: on ne devrait pas avoir le droit d'en consommer si on n'en produit pas.",
            u"Le châtiment d'un menteur n'est pas qu'on ne le croit pas, c'est qu'il ne peut croire personne.",
            u"Le Christ doit-il donc périr dans les tourments à chaque époque pour sauver ceux qui n'ont point d'imagination?",
            u"Le crime est le magasin de détail du magasin de gros que nous appelons loi pénale.",
            u"Le drame est né de l'union de deux vieux désirs: le désir de danser, et celui d'entendre une histoire. La danse est devenue déclamation, et l'histoire, situation.",
            u"Le mariage n'est pas une loterie. A la loterie il y a des gagnants.",
            u"Le mariage, c'est l'histoire d'un jeune homme et d'une jeune fille qui cueillent une fleur et reçoivent une avalanche sur la tête.",
            u"Le martyre est la seule façon pour un homme de devenir célèbre sans talent.",
            u"Le meilleur moyen de se familiariser avec un sujet, c'est de lui consacrer un livre.",
            u"Le métier de soldat est l'art du lâche; c'est l'art d'attaquer sans merci quand on est fort, et de se tenir loin du danger quand on est faible. Voilà tout le secret de la victoire.",
            u"Le nationalisme se dresse entre l'Irlande et la lumière du monde.",
            u"Le patriotisme est votre conviction que ce pays est supérieur à tous les autres, parce que vous y êtes né.",
            u"Le pessimiste? Un homme qui en veut à tous les autres hommes parce qu'il les trouve aussi dégoûtants que lui!",
            u"Le pire péché envers nos semblables, ce n'est pas de les haïr, mais de les traiter avec indifférence; c'est là l'essence de l'inhumanité.",
            u"Le plus grand des maux et le pire des crimes, c'est la pauvreté.",
            u"Le plus grand service que quiconque puisse rendre au pays et à l'humanité est peut-être d'élever une famille.",
            u"Le premier amour réclame seulement un peu de sottise et beaucoup de curiosité.",
            u"Le principal inconvénient des instruments à vent est qu'ils prolongent la vie du musicien.",
            u"Le sacrifice de nous-mêmes nous permet de sacrifier les autres sans honte.",
            u"Le seul sport que j'aie jamais pratiqué, c'est la marche à pied, quand je suivais les enterrements de mes amis sportifs.",
            u"Le silence est l'expression la plus parfaite du mépris.",
            u"Le succès ne consiste pas à ne jamais faire d'erreur mais à ne jamais faire la même erreur deux fois.",
            u"Le vin ordinaire, l'eau potable des Français.",
            u"Le whisky est une mauvaise chose, surtout le mauvais whisky.",
            u"Les Américains sont heureux quand ils peuvent ajouter une maisonnette à leur garage.",
            u"Les Anglais n'ont aucun respect pour leur langue et ils ne veulent pas apprendre à leurs enfants à la parler correctement. Il est impossible à un Anglais d'ouvrir la bouche sans se faire mépriser ou détester par un autre Anglais.",
            u"Les animaux sont mes amis... et je ne mange pas mes amis.",
            u"Les architectes dissimulent leurs erreurs sous du lierre; les médecins sous la terre et les ménagères sous de la mayonnaise.",
            u"Les choses que les gens veulent absolument savoir ne les regardent généralement pas.",
            u"Les critiques dramatiques sont aussi creux qu'il est possible de l'être sans s'écrouler physiquement.",
            u"Les critiques ne sont pas différents des autres hommes: ils voient ce qu'ils cherchent et non ce qui est sous leurs yeux.",
            u"Les esprits supérieurs comprennent toujours difficilement qu'ils soulèvent des fureurs en faisant ressortir les stupidités de gens relativement bornés.",
            u"Les êtres humains sont les seuls animaux dont j'aie réellement peur.",
            u"Les gens du commun ne prient guère, ils mendient uniquement.",
            u"Les gens qui arrivent à quelque chose dans ce monde sont ceux qui se lèvent, qui recherchent les circonstances qu'ils désirent et qui, s'ils ne les trouvent pas, les créent.",
            u"Les hommes raisonnables s'adaptent au monde dans lequel nous vivons. Les hommes déraisonnables persistent à vouloir adapter ce monde à eux-mêmes. Autrement dit, le progrès ne peut venir que des hommes déraisonnables.",
            u"Les journaux sont incapables apparemment de faire la distinction entre un accident de bicyclette et le déclin d'une civilisation.",
            u"Les livres gagnent toujours à ne pas être lus: regardez nos classiques.",
            u"Les lois du succès au théâtre tiennent en deux articles. Article premier: elles n'ont pas changé depuis deux mille ans. Article deux: personne ne les connaît.",
            u"Les rapports de supérieur à inférieur interdisent les bonnes manières.",
            u"Les vieillards sont dangereux: ils se moquent bien de ce qui peut arriver après eux.",
            u"Liberté implique responsabilité. C'est là pourquoi la plupart des hommes la redoutent.",
            u"Lord X sera chez lui tel jour de telle heure à telle heure. - G.-B. Shaw aussi.",
            u"Lorsqu'un imbécile fait quelque chose dont il a honte, il déclare toujours que c'est son devoir.",
            u"Lorsque Dieu a créé l'homme et la femme, il a bêtement oublié d'en déposer le brevet si bien que maintenant, le premier imbécile venu peut en faire autant.",
            u"Ma façon de plaisanter, c'est de dire la vérité. C'est la plaisanterie la plus drôle du monde.",
            u"Ma méthode est de prendre le plus de soucis possible pour trouver la chose qu'il faut dire, et ensuite de la dire avec une légèreté extrême.",
            u"Ma spécialité est d'avoir raison quand les autres ont tort.",
            u"Même pour son bien, je ne veux obliger personne à me considérer comme son auteur favori.",
            u"Mens sana in corpore sano est une maxime absurde. - Le corps est le produit de l'esprit sain.",
            u"Mieux vaut finir sa vie dans les bras d'une femme que dans les deux bras d'un fauteuil.",
            u"N'essaie pas d'être immortel, tu serais voué à l'échec.",
            u"Ne faites pas aux autres ce que vous voudriez qu'ils vous fissent. Il se peut que leurs goûts ne soient pas les mêmes.",
            u"Nos écoles enseignent la morale féodale corrompue par le commerce et offre comme modèles d'hommes illustres et qui ont réussi le militaire conquérant, le baron voleur et le profiteur.",
            u"Notre pays est la seule nation au monde où il y a autant de problèmes qu'ailleurs.",
            u"Nous n'avons pas perdu la foi, nous l'avons simplement reportée de Dieu sur les professions médicales.",
            u"Nous n'avons pas plus le droit de consommer du bonheur sans en créer que de consommer de la richesse sans travailler.",
            u"On appelle cercle de famille un endroit où l'enfant est encerclé.",
            u"On aura une bonne idée du degré d'éducation d'un homme et d'une femme, en observant la façon dont ils se conduisent pendant une scène de ménage.",
            u"On compare souvent le mariage à une loterie. C'est une erreur, car à la loterie, on peut parfois gagner.",
            u"On lui donnerait n'importe quel âge entre dix-huit et cinquante-ans, car il appartient à cette catégorie d'hommes qui ne se flétrissent jamais, car ils n'ont jamais eu de floraison.",
            u"On ne chasse pas à sa perte lorsqu'on court après une femme. Ce qui est dangereux, c'est de la rattraper.",
            u"On peut beaucoup plus largement se passer des hommes que des femmes; c'est pourquoi c'est eux qu'on sacrifie dans la guerre.",
            u"On peut trouver des choses obscènes dans tous les livres, excepté dans l'annuaire des téléphones.",
            u"On voit des choses et on se demande pourquoi elles existent. Moi je rêve de choses qui n'ont jamais existé et je me demande pourquoi pas?",
            u"Patriotisme, opinion public, devoir parental, discipline, religion, morale, ne sont que de jolis noms pour le mot intimidation",
            u"Plus un homme accepte d'obéir à l'autorité accréditée, moins il accepte qu'une personne sans autorité accréditée lui donne des ordres.",
            u"Pour celui qui a mal aux dents, même si c'est la fin du monde, il n'y a rien de plus important qu'un rendez-vous chez le dentiste.",
            u"Pour éteindre le remords, il n'est que de renouveler souvent l'acte qui l'a fait naître.",
            u"Prenez garde à l'homme dont le dieu est dans les cieux.",
            u"Quand les domestiques sont traités comme des êtres humains, ce n'est plus la peine de les garder.",
            u"Quand on se noie, on pense à sa famille qui va se demander d'abord pourquoi on est en retard pour le thé et ensuite ce qui va se passer étant donné qu'on n'a pas fait de testament.",
            u"Quand quelque chose est marrant, cherchez-y soigneusement une vérité cachée.",
            u"Quand un homme désire tuer un tigre, il appelle cela sport; quand un tigre désire le tuer, il appelle cela férocité.",
            u"Quand un homme et une femme sont mariés, ils ne font plus qu'un. La première difficulté est de décider lequel.",
            u"Quand un homme, enseignant ce qu'il ne sait pas à quelqu'un qui n'a aucune aptitude pour l'apprendre, lui donne un diplôme, ce dernier a complété son éducation d'homme comme il faut.",
            u"Quand une femme du monde dit non, cela veut dire peut-être; quand elle dit peut-être, cela veut dire oui; et quand elle dit oui, ce n'est pas une femme du monde.",
            u"Quand vous lisez une biographie, rappelez-vous que la vérité n'est pas faite pour être publiée.",
            u"Quand, en ce monde, un homme a quelque chose à dire, la difficulté n'est pas de le lui faire dire, mais de l'empêcher de le dire trop souvent.",
            u"Quelle belle chose la jeunesse! Quel crime de la laisser gâcher par les jeunes.",
            u"Rien n'est jamais accompli par un homme raisonnable.",
            u"Si les Anglais peuvent survivre à leur cuisine, ils peuvent survivre à tout.",
            u"Si tous les économistes étaient mis bout à bout, ils n'atteindraient pas une conclusion.",
            u"Si tu as une pomme, que j'ai une pomme, et que l'on échange nos pommes, nous aurons chacun une pomme. Mais si tu as une idée, que j'ai une idée et que l'on échange nos idées, nous aurons chacun deux idées.",
            u"Si vous allez au Paradis sans qualifications particulières pour ce genre d'endroit, vous risquez de ne guère vous y plaire.",
            u"Si vous offensez votre prochain, il vaut mieux ne pas le faire à demi.",
            u"Tant que je désire quelque chose, j'ai une raison de vivre... La satisfaction, c'est la mort.",
            u"Telle que nous la concevons, la vie à la maison n'est guère plus naturelle que la cage pour un perroquet.",
            u"Tout gouvernement qui vole Pierre pour payer Paul dépend toujours du soutien de Paul.",
            u"Tout homme de plus de quarante ans est une canaille.",
            u"Toutes les grandes vérités commencent par être des blasphèmes.",
            u"Toutes les professions sont des conspirations contre les profanes.",
            u"Trop fatigué pour travailler, j'écrivais des livres.",
            u"Un bourgeois est un homme modérément honnête, avec une épouse modérément fidèle, et des enfants modérément élevés, tous deux buveurs modérés, qui vivent dans une maison modérément confortable.",
            u"Un érudit est un paresseux qui passe son temps à étudier. Prenez garde à ses erreurs: elles sont plus dangereuses que ses lacunes.",
            u"Un homme cultivé est un oisif qui tue le temps en étudiant.",
            u"Un homme modérément honnête avec une femme modérément fidèle, tous deux buveurs modérés, dans une maison modérément saine, voilà le vrai type de la classe bourgeoise.",
            u"Un homme sans domicile est un vagabond: un homme avec deux domiciles est un libertin.",
            u"Un homme se décrit toujours inconsciemment lui-même quand il décrit quelqu'un d'autre.",
            u"Un idéologue est quelqu'un qui s'est donné pour tâche de rendre l'homme meilleur que l'humanité.",
            u"Un lion ne saurait être bien redoutable. Il n'a pas d'idéal, pas de religion, pas d'opinion politique, pas de courtoisie, pas d'éducation.",
            u"Un opéra, c'est une histoire où un baryton fait tout pour empêcher un ténor de coucher avec une soprano.",
            u"Un révolutionnaire est celui qui désire mettre au rancart l'ordre social existant, afin d'en essayer un autre.",
            u"Une banque vous prête un parapluie quand il fait beau et vous le reprend quand il pleut.",
            u"Une femme s'inquiète de l'avenir jusqu'à ce qu'elle ait trouvé un mari, tandis qu'un homme ne s'inquiète de l'avenir que lorsqu'il a trouvé une femme.",
            u"Une vie de bonheur! Il n'est pas d'homme capable de l'endurer: ce serait l'enfer sur terre.",
            u"Vivre ce n'est pas se trouver, c'est se créer.",
            u"Vous me demandez si je connais les femmes. Euh... - Une des choses que je ne sais pas sur elles est ce qu'elles peuvent bien se dire pendant que nous, les hommes, nous parlons.",
            u"Vous n'avez pas plus le droit de consommer le bonheur sans le produire que de consommer la santé sans la produire.",
            u"Vous voyez les choses; et vous demandez «pourquoi?». Mais je rêve de choses qui n'existent pas encore; et je demande «pourquoi pas?»."
        ]

            # Socrates
        socrates = [
            u"Ce que tu veux me dire, est-ce vrai? Est-ce bien? Est-ce utile? Sinon je ne veux pas l'entendre.",
            u"Ce qui fait l'homme, c'est sa grande faculté d'adaptation.",
            u"Ceux qui désirent le moins de choses sont les plus près des dieux.",
            u"Dans tous les cas, mariez-vous. Si vous tombez sur une bonne épouse, vous serez heureux. Si vous tombez sur une mauvaise, vous deviendrez philosophe, ce qui est excellent pour l'homme.",
            u"Existe-t-il pour l'homme un bien plus précieux que la Santé?",
            u"Il faut manger pour vivre, et non vivre pour manger.",
            u"Il n'y a point de travail honteux.",
            u"Il vaut mieux subir l'injustice que de la commettre.",
            u"Je crois qu'on ne peut mieux vivre qu'en cherchant à devenir meilleur, ni plus agréablement qu'en ayant la pleine conscience de son amélioration.",
            u"Je ne suis ni Athénien, ni Grec, mais un citoyen du monde.",
            u"Je sais que je ne sais rien.",
            u"Je te battrais, si je n'étais pas en colère.",
            u"L'âme déréglée est comme un tonneau percé à cause de sa nature insatiable.",
            u"L'amour seul connaît le secret de s'enrichir en donnant.",
            u"L'écriture ne peut saisir le savoir, car le savoir, contrairement à l'information, n'existe pas en dehors de l'homme.",
            u"L'homme doit s'élever au-dessus de la Terre - aux limites de l'atmosphère et au-delà - ainsi seulement pourra-t-il comprendre tout à fait le monde dans lequel il vit.",
            u"L'homme est le seul des animaux à croire à des dieux.",
            u"La plus intelligente est celle qui sait qu'elle ne sait pas.",
            u"La première clé de la grandeur est d'être en réalité ce que nous semblons être.",
            u"La renommée est le parfum des actions héroïques.",
            u"Le bonheur c'est le plaisir sans remords.",
            u"Le mal vient de ce que l'homme se trompe au sujet du bien.",
            u"Le mépris est de dimension infinie...",
            u"Le temps malgré tout a trouvé la solution malgré toi.",
            u"Les autres hommes vivent pour manger, tandis que je mange pour vivre.",
            u"Mieux vaut encore subir l'injure que la commettre.",
            u"N'oublie jamais que tout est éphémère, alors tu ne seras jamais trop joyeux dans le bonheur, ni trop triste dans le chagrin.",
            u"Nos jeunes aiment le luxe, ont de mauvaises manières, se moquent de l'autorité et n'ont aucun respect pour l'âge. A notre époque, les enfants sont des tyrans.",
            u"Nul n'est méchant volontairement.",
            u"O Pan! Et vous, divinités de ces ondes, donnez-moi la beauté intérieure de l'âme!",
            u"On compte plus facilement ses moutons que ses amis.",
            u"On ne peut mieux vivre qu'en cherchant à devenir meilleur, ni plus agréablement qu'en ayant la pleine conscience de son amélioration.",
            u"Que celui qui veut mouvoir le monde se meuve d'abord lui-même.",
            u"Que voulez-vous que je lui apprenne? Il ne m'aime pas.",
            u"Rien n'est trop difficile pour la jeunesse.",
            u"Si un âne te donne un coup de pied, ne lui rends pas.",
            u"Tout ce que je sais, c'est que je ne sais rien, tandis que les autres croient savoir ce qu'ils ne savent pas.",
            u"Un homme doit-il se marier? Quoi qu'il fasse, il se repentira.",
            u"Un homme qui a faim n'examine pas la sauce.",
            u"Un trésor de belles maximes est préférable à un amas de richesses.",
            u"Une vie sans examen ne vaut pas la peine d'être vécue.",
            u"Vous pouvez cacher aux autres une action répréhensible, mais jamais à vous-même."
        ]


        # T
            # Henry David Thoreau
        thoreau = [
            u"A quoi bon emprunter sans cesse le même vieux sentier? Vous devez tracer des sentiers vers l'inconnu.",
            u"Ce n'est pas par leur architecture mais plutôt par la puissance de leur pensée abstraite que les nations devraient essayer de se perpétuer dans la mémoire des hommes.",
            u"Ce qu'il y a de plus singulier dans la vie de l'homme, ce n'est pas sa soumission mais son opposition aux instincts. Il aspire à une vie surnaturelle.",
            u"Ce qu'un homme pense de lui-même, voilà ce qui règle ou plutôt indique son destin.",
            u"Chaque génération se moque des vieilles modes, mais suit religieusement les nouvelles.",
            u"Comme si l'on pouvait tuer le temps sans insulter à l'éternité.",
            u"En tuant le temps on blesse l'éternité.",
            u"Est-ce dans le bouquet que la fleur est plus belle, ou bien dans le pré où elle pousse, quand nous nous sommes mouillé les pieds pour aller la chercher?",
            u"Frapper à la racine du mal équivaut à en couper mille branches.",
            u"Il est aussi difficile de se voir soi-même que de regarder en arrière sans se retourner.",
            u"Il est plus désirable de cultiver le respect du bien que le respect de la loi.",
            u"Il existe de nos jours des professeurs de philosophie, mais de philosophes, point.",
            u"Il faut deux personnes pour dire la vérité - une pour la dire et l'autre pour l'écouter.",
            u"Il n'est pas d'individu plus fatalement malavisé que celui qui consume la plus grande partie de sa vie à la gagner.",
            u"Il n'y a qu'un remède à l'amour: aimer davantage.",
            u"Il semble que nous ne faisons que languir dans l'âge mûr pour dire les rêves de notre enfance, et ils s'évanouissent de notre mémoire avant que nous ayons pu apprendre leur langage.",
            u"Il y a deux sortes d'auteurs: les uns écrivent l'histoire de leur temps, les autres leur biographie.",
            u"Impossible d'écrire bien et sincèrement si on ne le fait pas dans la joie. Le corps, le sens doivent travailler avec l'esprit; l'expression est l'acte du corps tout entier.",
            u"J'ai la nostalgie d'une de ces vieilles routes sinueuses et inhabitées qui mènent hors des villes... une route qui conduise aux confins de la terre... où l'esprit est libre...",
            u"Jamais la loi n'a rendu les hommes plus justes d'une seule once, mais, en raison du respect qu'ils lui portent, il arrive chaque jour que même des gens dotés des meilleures dispositions se fassent les agents de l'injustice.",
            u"Je préférerais m'asseoir sur un potiron et le posséder bien à moi que d'être à plusieurs sur un coussin de velours.",
            u"L'art de la vie, de la vie du poète, c'est d'être occupé sans avoir rien à faire.",
            u"L'expérience est dans les doigts et dans la tête. Le coeur n'a pas d'expérience.",
            u"L'homme qui n'est qu'intelligence, l'homme prosaïque, est une fleur stérile qui n'a que des étamines; le poète est une fleur féconde et complète.",
            u"L'homme qui se dévoue entièrement à ses semblables risque de passer à leurs yeux pour un être sans valeur et égoïste, tandis que celui qui ne leur consacre qu'une petite partie de lui-même est appelé du nom de bienfaiteur et de philanthrope.",
            u"La nature n'est rien, si ce n'est qu'elle fait s'exprimer l'homme et qu'elle le reflète.",
            u"La perdrix aime les pois, mais pas ceux qui l'accompagnent dans la casserole.",
            u"Le poème de la création ne s'arrête jamais; mais rares sont les oreilles capables de le capter.",
            u"Les faits les plus intéressants et les plus beaux sont en eux-mêmes poésie.",
            u"Les hommes sont nés pour réussir et non pour échouer.",
            u"Lorsque les vieilles gens vous diront que vous ne pouvez faire quelque chose, essayez, et vous découvrirez que vous pouvez le faire. Que les vieux agissent comme des vieux, les jeunes comme des jeunes.",
            u"Ni la contrainte, ni la sévérité, ne vous ouvriront l'accès de la vraie sagesse, mais bien l'abandon et une joie enfantine. Quoi que ce soit que vous vouliez apprendre, abordez-le avec gaieté.",
            u"Nous empoisonnons notre vie par des détails. Simplifions, simplifions.",
            u"Nous ne saurions nous passer de nos péchés; ils sont la grand-route de la vertu.",
            u"On pourrait définir le ciel comme l'endroit que les hommes évitent.",
            u"Plutôt que l'amour, que l'argent, que la gloire, - Donnez-moi la vérité.",
            u"Presque tous les hommes savent gagner de l'argent, mais il n'y en a pas un sur un million qui sache le dépenser. Qui le saurait n'en aurait jamais gagné.",
            u"Quelle flamme pourrait égaler le rayon de soleil d'un jour d'hiver?",
            u"Rien n'est autant à craindre que la crainte elle-même.",
            u"Si je ne suis pas moi, qui le sera?",
            u"Si vous avez fait des châteaux en l'air, vous n'avez pas travaillé en vain, car c'est là que tous devraient être. Maintenant, mettez dessous les fondations.",
            u"Sous un gouvernement qui emprisonne injustement, la place de l'homme juste est aussi en prison.",
            u"Un homme grognon, grossier, original, silencieux, un homme mal dressé; voilà de l'espérance."
        ]

            # Mark Twain
        twain= [
            u"A chaque fois que vous vous retrouvez du côté de la majorité, il est temps de faire une pause et de réfléchir.",
            u"A Paris, quand je leur parle en français, les gens me regardent avec des yeux ronds. Je n'ai jamais réussi à obtenir que ces imbéciles comprennent leur propre langue.",
            u"A quatorze ans, je trouvais mon père tellement ignorant que j'avais peine à le souffrir; mais, à vingt et un ans, je fus étonné de constater tout ce qu'il avait appris dans l'espace de sept ans.",
            u"Adam est le seul homme qui, quand il disait quelque chose d'épatant, était sûr que personne ne l'avait dit avant lui.",
            u"Agis toujours bien, tu feras plaisir à quelques-uns et étonneras les autres.",
            u"Aux obsèques du Président Gibson, le cortège avait à peu près trois kilomètres de longueur, ainsi d'ailleurs que le magnifique sermon du pasteur Smith, dont nul ne peut se vanter d'avoir connu la fin.",
            u"Avec un bon compliment, je peux vivre deux mois.",
            u"C'est beau d'être vertueux, mais apprendre aux autres à l'être, c'est encore plus beau... et tellement plus facile.",
            u"C'est la différence d'opinion qui fait les courses de chevaux.",
            u"C'est par piston qu'on entre au paradis. Si c'était au mérite, mon chien y entrerait et moi je resterais dehors.",
            u"C'est plus facile d'avoir des principes quand on est bien nourri.",
            u"Ce fut admirable de découvrir l'Amérique, mais il l'eût été plus encore de passer à côté.",
            u"Cesser de fumer c'est la chose la plus facile... Je sais parce que je l'ai fait 50 fois.",
            u"Ceux qui sont pour la liberté sans agitation sont des gens qui veulent la pluie sans orage.",
            u"Chacun de nous est une lune, avec une face cachée que personne ne voit.",
            u"Consommée avec modération, l'eau ne peut pas faire de mal.",
            u"Dans le doute dites la vérité.",
            u"De bons amis, de bons livres et la conscience somnolente, voilà le secret du bonheur.",
            u"De nos jours, le plus grand problème du mariage est la difficulté de subvenir avec un seul salaire aux besoins de sa femme et à ceux de l'Etat.",
            u"De toutes les expériences que tu vis, retiens seulement la sagesse qu'elles renferment.",
            u"Détournez-vous de ceux qui vous découragent de vos ambitions. C'est l'habitude des mesquins. Ceux qui sont vraiment grands vous font comprendre que vous aussi pouvez le devenir.",
            u"Dieu créa l'homme, puis il eut peur qu'il ne s'ennuyât et lui donna la femme. Peu après, pris de remords, Dieu eut peur qu'elle ne l'ennuyât et lui envoya le tabac.",
            u"Efforçons-nous de vivre de telle sorte que, quand nous ne seront plus, le croque-mort lui-même pleure à notre enterrement.",
            u"Faites attention, lorsque vous lisez des livres sur la santé, vous pourriez mourir d'une faute d'impression.",
            u"Il est étrange de constater que le courage physique est très répandu alors que le courage moral est si rare.",
            u"Il faut toujours au moins trois semaines pour préparer un bon discours improvisé.",
            u"Il n'y a que deux cas dans lesquels l'homme ne devrait pas spéculer en bourse. - 1. Quand il n'en a pas les moyens. - 2. Quand il en a les moyens.",
            u"Il y a des gens qui, à propos de certains problèmes, font preuve d'une grande tolérance. C'est souvent parce qu'ils s'en foutent.",
            u"Il y a deux moments dans la vie d'un homme où il ne devrait pas spéculer: lorsqu'il ne peut pas se le permettre et lorsqu'il le peut.",
            u"Il y a trois choses qu'une femme est capable de réaliser avec rien: un chapeau, une salade et une scène de ménage.",
            u"Il y a trois sortes de mensonges: les mensonges, les sacrés mensonges et les statistiques.",
            u"Ils ne savaient que c'était impossible, alors ils l'ont fait.",
            u"J'étais étrangement beau. Si beau, que les objets inanimés tels que locomotives et télégraphistes s'arrêtaient pour me regarder. A San Francisco, par temps pluvieux, on me prenait souvent pour le beau temps.",
            u"Je choisirais le paradis pour le climat... et l'enfer pour la compagnie!",
            u"Je fus très heureux d'être capable de répondre rapidement et c'est ce que je fis. Je répondis que je ne savais pas.",
            u"Je n'aime pas l'idée d'avoir à choisir entre le ciel et l'enfer: j'ai des amis dans les deux.",
            u"L'art de la prophétie est extrêmement difficile, surtout en ce qui concerne l'avenir.",
            u"L'épargne est une magnifique réalité, spécialement quand nos parents l'ont pratiquée.",
            u"L'habit fait le moine. Les gens nus ont pas ou peu d'influence sur la société.",
            u"L'homme raisonnable s'adapte au monde; l'homme déraisonnable persiste à vouloir adapter le monde à lui-même. C'est pourquoi le progrès ne peut venir que de ce dernier.",
            u"L'une des preuves de l'immortalité de l'âme est que des myriades de gens le croient. Ils ont cru aussi que la terre était plate...",
            u"La bonne éducation consiste à cacher tout le bien que nous pensons de nous-mêmes et le peu de bien que nous pensons des autres.",
            u"La formation c'est tout. La pêche a commencé par être une amande amère; le chou-fleur n'est jamais qu'un chou qui a été au collège.",
            u"La musique de Wagner est meilleure qu'on ne le croirait à l'entendre.",
            u"La pudeur est née avec l'invention du vêtement.",
            u"La vérité est la chose la plus précieuse que nous ayons. Economisons-la.",
            u"La vérité est plus étrange que la fiction. C'est parce que la fiction est basée uniquement sur des choses possibles alors que la vérité ne l'est pas.",
            u"Le fait de fumer m'a sauvé la vie. Figurez-vous, en effet, qu'à chaque fois que je vais mal, le médecin me supprime le cigare. Et je guéris! Mon Dieu, où en serais-je si je n'avais pas fumé le cigare!...",
            u"Le golf est une agréable promenade gâchée par une petite balle blanche.",
            u"Le lit est l'endroit le plus dangereux du monde: 80% des gens y meurent.",
            u"Le mot juste est un agent puissant.",
            u"Le nom du plus grand des inventeurs: accident.",
            u"Le rôle d'un ami, c'est de se trouver à votre côté quand vous êtes dans l'erreur puisque tout le monde sera à côté de vous quand vous aurez raison.",
            u"Le seul moyen de conserver sa santé est de manger ce qu'on ne veut pas, de boire ce qu'on n'aime pas et de faire ce qu'on aimerait éviter de faire.",
            u"Le travail, c'est tout ce que l'on est obligé de faire; le jeu, c'est tout ce qu'on fait sans y être obligé.",
            u"Les Allemands prennent un morceau de verbe, le placent ici, comme un piquet, puis se saisissent de l'autre morceau, le plantent bien plus loin, comme un autre piquet, et, entre ces deux limites, ils entassent de l'allemand.",
            u"Les baisers d'une jolie fille sont comme les cornichons. Dès qu'on arrive à en attraper un, les autres suivent sans difficulté.",
            u"Les classiques sont les livres que tout le monde peut se vanter d'avoir lus, puisque personne ne les lit.",
            u"Les faits sont têtus. Il est plus facile de s'arranger avec les statistiques.",
            u"Les radicaux inventent de nouvelles idées. Quand elles sont usées, les conservateurs les adoptent.",
            u"Les riches qui pensent que les pauvres sont heureux ne sont pas plus bêtes que les pauvres qui pensent que les riches le sont.",
            u"Les rides devraient être tout simplement la trace des sourires.",
            u"Lorsqu'un Allemand cultivé plonge dans une phrase, vous ne le revoyez plus jusqu'à ce qu'il réapparaisse de l'autre côté de l'Atlantique, le verbe à la bouche.",
            u"Lorsque vous dites la vérité, vous n'avez à vous souvenir de rien.",
            u"Ma façon de plaisanter est de dire la vérité. C'est la meilleure plaisanterie au monde.",
            u"Mettez tous vos oeufs dans le même panier - et surveillez le panier.",
            u"Milles excuses et aucune bonne raison.",
            u"Mon cher ami, - Je vous envoie M. Untel, faites ce qu'il vous demande ou tuez-le, cela m'est bien égal. - Bien à vous. - P.S.: Si vous choisissez de le tuer, ayez la bonté de m'en informer pour que je puisse prévenir sa famille.",
            u"N'apprenez jamais à faire quoi que ce soit; si vous n'apprenez pas, vous trouverez toujours quelqu'un d'autre qui le fera à votre place.",
            u"N'avons-nous pas eu tous les fous de la ville de notre côté? Et n'y a-t-il pas une grosse majorité dans chaque ville?",
            u"Octobre est un mois particulièrement dangereux pour spéculer en bourse. Mais il y en a d'autres: juillet, janvier, septembre, avril, novembre, mai, mars, juin, décembre, août et février.",
            u"On ne se débarrasse pas d'une habitude en la flanquant par la fenêtre; il faut lui faire descendre l'escalier marche par marche.",
            u"On pourrait citer de nombreux exemples de dépenses inutiles. Les murs des cimetières: ceux qui sont dedans ne peuvent pas en sortir, et ceux qui sont à l'extérieur ne veulent pas y entrer.",
            u"Plus d'une chose insignifiante a pris de l'ampleur grâce à une bonne publicité.",
            u"Pourquoi dépenser de l'argent pour faire établir votre arbre généalogique? Faites de la politique et vos adversaires s'en chargeront.",
            u"Quant aux adjectifs: dans le doute, biffez-les.",
            u"Que m'importe qu'un homme soit juif, chinois, indien, noir ou blanc, il me suffit de savoir qu'il est un homme, il ne peut rien être de pire.",
            u"Si vous dites la vérité, vous n'avez plus à vous souvenir de quoi que ce soit.",
            u"Si vous recueillez un chien mourant de faim et lui asurez le bien-être, il ne vous mordra pas. C'est la principale différence entre le chien et l'homme.",
            u"Un Anglais fait les choses parce qu'elles ont déjà été faites, un Américain parce qu'elles n'ont pas été faites.",
            u"Un banquier, c'est quelqu'un qui vous prête un parapluie par beau temps et vous le reprend lorsqu'il commence à pleuvoir.",
            u"Un jour, mon berceau fut placé à côté de celui d'un autre enfant. L'un de nous deux mourut. Depuis, je ne sais pas lequel est vivant: lui ou moi?...",
            u"Un mensonge peut faire le tour de la terre le temps que la vérité mette ses chaussures.",
            u"Une des différences les plus marquantes entre un chat et un mensonge est qu'un chat n'a que neuf vies.",
            u"Vous ne pouvez vous fier à votre jugement si votre imagination laisse à désirer."
        ]

        # V
            # Voltaire
        voltaire = [
            u"... la Grèce, berceau des arts et des erreurs, et où l'on poussa si loin la grandeur et la sottise de l'esprit humain ...",
            u"... la plaisanterie expliquée cesse d'être plaisanterie: tout commentateur de bons mots est un sot.",
            u"A Alphonse Allais, avec le regret de ne pas l'avoir connu.",
            u"A ce fatal berceau l'instinct m'a rappelé.",
            u"A la cour, mon fils, l'art le plus nécessaire - N'est pas de bien parler, mais de savoir se taire.",
            u"Ah! je vois bien qu'il en est des hommes comme des plus vils animaux; tous peuvent nuire.",
            u"Ah! S'il nous faut des fables, que ces fables soient au moins l'emblème de la vérité!",
            u"Aime la vérité mais pardonne à l'erreur.",
            u"Ainsi presque tout est imitation. Il en est des livres comme du feu de nos foyers, on va prendre le feu chez son voisin, on l'allume chez soi, on le communique à d'autres et il appartient à tous.",
            u"Aristote, qu'on a expliqué de mille façons, parce qu'il était inintelligible ...",
            u"Au lieu donc de nous étonner et de nous plaindre du malheur et de la brièveté de la vie, nous devons nous étonner et nous féliciter de notre bonheur et de sa durée.",
            u"Avez-vous demandé à un crapaud ce qu'est pour lui la beauté?",
            u"Brutus: - Avais-tu résolu d'opprimer ta patrie? - D'abandonner ton père au pouvoir absolu? - De trahir tes serments? - - Titus: - Je n'ai rien résolu. - Plein d'un mortel poison dont l'horreur me dévore, - Je m'ignorais moi-même et je me cherche encore.",
            u"C'est l'amour de nous-même qui assiste l'amour des autres; c'est par nos besoins mutuels que nous sommes utiles au genre humain; c'est l'éternel lien des hommes.",
            u"C'est n'être bon à rien que n'être bon qu'à soi.",
            u"C'est une absurdité, c'est un outrage au genre humain, c'est un attentat contre l'Etre infini et suprême de dire: Il y a une vérité essentielle à l'homme, et Dieu l'a cachée",
            u"Ce monde est un vaste naufrage: sauve qui peut!",
            u"Ce qu'il y a de pis, c'est que la guerre est un fléau inévitable.",
            u"Ce que nous appelons le hasard n'est et ne peut être que la cause ignorée d'un effet connu.",
            u"Ce qui n'est que difficile ne plaît point à la longue.",
            u"Ceux qui ont avancé que tout est bien ont dit une sottise: il fallait dire que tout est au mieux.",
            u"Chaque profession a un vice et un danger qui lui sont attachés ...",
            u"Ci-gît Voltaire - de l'Académie française. - Il a franchi le seuil - Et n'a quitté son fauteuil - Que pour le Père-Lachaise.",
            u"Courtes lettres et longues amitiés, tel est ma devise.",
            u"Crois-moi, la liberté, que tout mortel adore, - Que je veux leur ôter, mais que j'admire encore, - Donne à l'homme un courage, inspire une grandeur, - Qu'il n'eût jamais trouvés dans le fond de son coeur.",
            u"D'un bout du monde à l'autre on ment et l'on mentit. - Nos neveux mentiront, comme ont fait nos ancêtres.",
            u"De toutes les superstitions, la plus dangereuse, n'est-ce pas celle de haïr son prochain pour ses opinions?",
            u"Demandez à un crapaud ce qu'il pense de la beauté ... . Il vous répondra que c'est sa femelle avec deux gros yeux ronds sortant de sa petite tête, une gueule large et plate, un ventre jaune, un dos brun.",
            u"Descends du haut des cieux, auguste Vérité! - Répands sur mes écrits ta force et ta clarté.",
            u"Dieu bénira les âmes tendres; il y a je ne sais quoi de réprouvé à être insensible.",
            u"Dieu fit la douce illusion - Pour les heureux fous du bel âge; - Pour les vieux fous, l'ambition, - Et la retraite pour le sage.",
            u"Dieu n'a créé les femmes que pour apprivoiser les hommes.",
            u"Dire le secret d'autrui est une trahison, dire le sien est une sottise.",
            u"En ouvrages de goût, en musique, en poésie, en peinture, c'est le goût qui tient lieu de montre; et celui qui n'en juge que par des règles en juge mal.",
            u"En philosophie, il faut se défier de ce qu'on croit entendre trop aisément, aussi bien que des choses qu'on n'entend pas.",
            u"En se dépêchant trop, on ne fait rien qui vaille.",
            u"En tout temps, en tous lieux, le public est injuste, - Horace s'en plaignait sous l'empire d'Auguste.",
            u"Et cependant un fripon de libraire, - Des beaux esprits écumeur mercenaire, - Vendeur adroit de sottise et de vent, - En souriant d'une mine matoise, - Lui mesurait des livres à la toise, - Car Monseigneur est surtout fort savant.",
            u"Et dans les factions, comme dans les combats, - Du triomphe à la chute il n'est souvent qu'un pas.",
            u"Et qui pardonne au crime en devient complice.",
            u"Et voilà comme on écrit l'histoire; puis fiez-vous à Messieurs les savants.",
            u"Examine-t-on ce qu'on désire?",
            u"Exterminez, grands dieux, de la terre où nous sommes, - Quiconque avec plaisir répand le sang des hommes!",
            u"Femme sage est plus que femme belle.",
            u"Guerre: «Le merveilleux de cette entreprise infernale, c'est que chaque chef des meurtriers fait bénir ses drapeaux et invoque dieu solennellement avant d'aller exterminer son prochain.»",
            u"Il a porté toutes les vertus des héros à un excès où elles sont aussi dangereuses que les vices opposés.",
            u"Il croyait que les lois étaient faites pour secourir les citoyens autant que pour les intimider.",
            u"Il est à propos que le peuple soit guidé et non pas qu'il soit instruit.",
            u"Il est dans la beauté et dans la vertu un charme invincible qui fait tomber les portes de fer, et qui amollit les coeurs de bronze!",
            u"Il faut aimer, et très tendrement, les créatures; il faut aimer sa patrie, sa femme, son père, ses enfants; et il faut si bien les aimer que Dieu nous les fait aimer malgré nous. Les principes contraires ne sont propres qu'à faire de barbares raisonneurs.",
            u"Il faut bien quelquefois se battre contre ses voisins, mais il ne faut pas brûler ses compatriotes pour des arguments.",
            u"Il fut l'ami du roi, et le roi fut alors le seul monarque de la terre qui eût un ami.",
            u"Il me semble aussi qu'on s'était fait une loi de ne point citer; mais un dictionnaire sans citation est un squelette",
            u"Il n'est permis qu'à un aveugle de douter que les Blancs, les Nègres, les albinos, les Hottentots, les Lapons, les Chinois, les Américains soient des races entièrement différentes.",
            u"Il n'y a point de grand conquérant qui ne soit grand politique.",
            u"Il n'y a point de hasard; tout est épreuve, ou punition, ou récompense, ou prévoyance.",
            u"Il n'y a rien de plus ridicule qu'un médecin qui ne meurt pas de vieillesse.",
            u"Il n'y pas de plus grand plaisir que de revoir un vieil ami, à part peut-être de s'en faire un nouveau.",
            u"Il prit pour sa devise: malheur est bon à quelque chose. Combien d'honnêtes gens dans le monde ont pu dire: malheur n'est bon à rien!",
            u"Il se figurait alors les hommes tels qu'ils sont en effet, des insectes se dévorant les uns les autres sur un petit atome de boue.",
            u"Il vaut mieux hasarder de sauver un coupable que de condamner un innocent.",
            u"Il y avait trois dames de Paris assez laides à la Cour; on disait que c'étaient des ponts sans garde-fous, parce que personne ne voulait passez dessus.",
            u"J'ai décidé d'être heureux parce que c'est bon pour la santé.",
            u"J'aime les fables des philosophes, je ris de celles des enfants, et je hais celles des imposteurs.",
            u"J'arriverai peut-être un jour au pays où il ne manque rien; mais jusqu'à présent personne ne m'a donné de nouvelles positives de ce pays-là.",
            u"J'avoue que le genre humain n'est pas tout à fait si méchant que certaines gens le crient dans l'espérance de le gouverner.",
            u"Je compterais plus sur le rôle d'un homme espérant une grande récompense que sur celui d'un homme l'ayant reçue.",
            u"Je crois que vous vous êtes laissé entraîner aux grands principes du machiavélisme: ruinez qui pourrait un jour vous ruiner; assassinez votre voisin qui pourrait devenir assez fort pour vous tuer.",
            u"Je hais vos idées, mais je me ferai tuer pour que vous ayez le droit de les exprimer.",
            u"Je n'aime point à citer; c'est d'ordinaire une besogne épineuse: on néglige ce qui précède et ce qui suit l'endroit qu'on cite, et on s'expose à mille querelles.",
            u"Je ne suis pas chrétien, mais c'est pour t'aimer mieux.",
            u"Je suis bien malade: tout baisse chez moi, hormis mes tendres sentiments pour vous.",
            u"Je suis comme les ruisseaux: je suis clair parce que je ne suis pas profond.",
            u"L'amour est une étoffe tissée par la nature et brodée par l'imagination.",
            u"L'amour propre est un ballon gonflé de vent dont il sort des tempêtes quand on y fait une piqure.",
            u"L'art de la médecine consiste à distraire le malade pendant que la nature le guérit.",
            u"L'autre jour, au fond d'un vallon, - Un serpent piqua Jean Fréron. - Que pensez-vous qu'il arriva? - Ce fut le serpent qui creva.",
            u"L'éducation développe les facultés, mais ne les crée pas.",
            u"L'enthousiasme est une maladie qui se gagne...",
            u"L'esprit est le contraire de l'argent; moins on en a, plus on est satisfait.",
            u"L'homme est libre au moment qu'il veut l'être.",
            u"L'instant où nous naissons est un pas vers la mort.",
            u"L'intérêt que j'ai à croire une chose n'est pas une preuve de l'existence de cette chose.",
            u"L'opinion est si bien la reine du monde que quand la raison veut la combattre, la raison est condamnée à mort.",
            u"L'univers m'embarrasse, et je ne puis songer - Que cette horloge existe et n'ait pas d'horloger.",
            u"La crainte suit le crime, et c'est son châtiment.",
            u"La discorde est le plus grand mal du genre humain, et la tolérance en est le seul remède.",
            u"La douleur est aussi nécessaire que la mort.",
            u"La géographie est le seul art dans lequel les derniers ouvrages sont toujours les meilleurs.",
            u"La lecture agrandit l'âme, et un ami éclairé la console.",
            u"La liberté consiste à ne dépendre que des lois.",
            u"La Marianne de Tristan, jouée la même année que le Cid, conserva cent ans sa réputation et l'a perdue sans retour. Comment une mauvaise pièce peut-elle durer cent ans?",
            u"La patrie est aux lieux où l'âme est enchaînée.",
            u"La philosophie pénètre dans le Nord; l'impératrice de Russie dit que ce n'est qu'une aurore boréale; et moi je pense que cette nouvelle lumière sera permanente.",
            u"La poésie est une espèce de musique: il faut l'entendre pour en juger.",
            u"La politique a sa source dans la diversité plus que dans la grandeur de l'esprit humain.",
            u"La religion forcée n'est plus religion: il faut persuader, et non contraindre. La religion ne se commande point.",
            u"La religion juive, mère du christianisme, grand-mère du mahométisme, battue par son fils et par son petit-fils.",
            u"La superstition est à la religion ce que l'astrologie est à l'astronomie, la fille très folle d'une mère très sage.",
            u"La vérité est un fruit qui ne doit être cueilli que s'il est tout à fait mûr.",
            u"Le christianisme n'enseigne que la simplicité, l'humanité, la charité; vouloir le réduire à la métaphysique, c'est en faire une source d'erreurs.",
            u"Le fanatisme est un monstre qui ose se dire le fils de la religion.",
            u"Le fanatisme et les contradictions sont l'apanage de la nature humaine.",
            u"Le fanatisme, peste des âmes.",
            u"Le monde ressemble à une vieille coquette qui déguise son âge.",
            u"Le nombre infini de maladies qui nous tue est assez grand; et notre vie est assez courte pour qu'on puisse se passer du fléau de la guerre.",
            u"Le pain dans sa patrie vaut encore mieux que des biscuits en pays étranger.",
            u"Le paradis terrestre est où je suis.",
            u"Le peuple ressemble à des boeufs, à qui il faut un aiguillon, un joug et du foin.",
            u"Le plus sûr est donc de n'être sûr de rien.",
            u"Le seul moyen d'obliger les hommes à dire du bien de vous, c'est d'en faire.",
            u"Le superflu, cette chose si nécessaire.",
            u"Le temps, qui seul fait la réputation des hommes, rend à la fin leurs défauts respectables.",
            u"Le travail éloigne de nous trois grands maux: l'ennui, le vice et le besoin.",
            u"Le travail n'est pas fait pour l'homme et la preuve, c'est que ça le fatigue.",
            u"Les bavards sont les plus discrets des hommes; ils parlent pour ne rien dire.",
            u"Les compliments sont le protocole des sots.",
            u"Les faiblesses des hommes font la force des femmes.",
            u"Les faux brillants se trouvent plus aisément que les pierres précieuses.",
            u"Les femmes ressemblent aux girouettes: elles se fixent quand elles se rouillent.",
            u"Les français commencèrent à se rendre recommandables surtout par les graces et les politesses de l'esprit: c'était l'aurore du bon goût.",
            u"Les Français sont le peuple le plus intelligent de la terre.",
            u"Les Français sont malins et sont grands chansonniers.",
            u"Les hommes en général ressemblent aux chiens qui hurlent quand ils entendent de loin d'autres chiens hurler.",
            u"Les hommes sont dévorés de plus d'envie, de soins, et d'inquiétudes, qu'une ville assiégée n'éprouve de fléaux.",
            u"Les inventions les plus étonnantes et les plus utiles ne sont pas celles qui font le plus d'honneur à l'esprit humain.",
            u"Les justes éloges ont un parfum que l'on réserve pour embaumer les morts.",
            u"Les larmes sont le langage muet de la douleur."
        ]

        # W

            # Andy Warhol
        warhol = [
            u"A l'avenir, chacun aura son quart d'heure de célébrité mondiale.",
            u"Acheter est bien plus américain que penser.",
            u"Certaines personnes, même des personnes intelligentes, disent que la violence peut être belle. Je ne comprends pas cela parce qu'il n'y a que de beaux instants et de tels instants ne sont jamais beaux pour moi.",
            u"Je voudrais être une machine.",
            u"L'amour fantasmé vaut bien mieux que l'amour vécu. Ne pas passer à l'acte, c'est très excitant.",
            u"L'art des affaires est l'étape qui succède à l'art. J'ai commencé comme artiste commercial, et je veux finir comme artiste d'affaires. Après avoir fait ce qu'on appelle de «l'art», ou ce qu'on veut, je me suis mis à l'art des affaires",
            u"L'art, c'est déjà de la publicité. La Joconde aurait pu servir de support à une marque de chocolat, à Coca Cola ou à tout autre chose.",
            u"Le businnes-art est l'étape qui suit l'art. J'ai commencé comme artiste commercial et je voudrais finir comme businnes-artiste.",
            u"Le mauvais goût fait passer le temps plus vite.",
            u"Mes peintures ne correspondent jamais à ce que j'avais prévu, mais je ne suis jamais surpris.",
            u"Ne fais pas attention à ce que l'on écrit sur toi. Contente-toi de le mesurer.",
            u"Nous cherchons plus à durer que nous n'essayons de vivre.",
            u"On dit que le temps change les choses, mais en fait le temps ne fait que passer et nous devons changer les choses nous-mêmes.",
            u"On n'imagine pas combien de gens accrochent un tableau de la chaise électrique dans leur salon - surtout si les couleurs du tableau vont bien avec celles des rideaux.",
            u"Si vous voulez tout savoir sur Andy Warhol, regardez simplement la surface de mes peintures, de mes films et de moi-même. Je suis là. Il n'y a rien derrière.",
            u"Tout le monde se ressemble et agit de la même façon, et nous ne faisons que progresser dans cette voie."
        ]

            # Oscar Wilde
        wilde = [u"Oscar Wilde",
            u"Aucune carte du monde n'est digne d'un regard si le pays de l'utopie n'y figure pas.",
            u"Aujourd'hui beaucoup de gens meurent d'un bon sens terre à terre et s'aperçoivent trop tard que les seules choses qu'ils regrettent sont leurs propres erreurs.",
            u"Aujourd'hui la plupart des gens se consument dans je ne sais quelle sagesse terre à terre et découvrent, quand il n'en est plus temps, que les folies sont les seules choses qu'on ne regrette jamais.",
            u"Aujourd'hui les gens connaissent le prix de tout et la valeur de rien.",
            u"C'est lorsqu'il parle en son nom que l'homme est le moins lui-même. Donnez-lui un masque et il vous dira la vérité.",
            u"Celui qui cherche une femme belle, bonne et intelligente, n'en cherche pas une mais trois.",
            u"Ceux qui essaient de mener le peuple ne peuvent le faire qu'en suivant la foule.",
            u"Ceux qui trouvent de belles significations aux belles choses sont cultivés. Pour eux, il existe un espoir.",
            u"Ceux qui trouvent de vilaines significations aux belles choses sont corrompus sans être charmants. C'est une faute.",
            u"Chaque saint a un passé, et chaque pécheur un avenir.",
            u"Citer les mots de quelqu'un, c'est mettre sous verre une collection de beaux papillons qui ont perdu leur lumière et leur éclat.",
            u"Comme les femmes aiment à faire les choses dangereuses. C'est une des qualités que j'admire le plus en elles. Une femme flirtera avec n'importe qui au monde, aussi longtemps qu'on la regardera...",
            u"Comment a-t-on pu dire que l'homme est un animal raisonnable! Il est tout ce qu'on veut, sauf raisonnable.",
            u"D'une joie même, le souvenir a son amertume, et le rappel d'un plaisir n'est jamais sans douleur.",
            u"De nos jours tous les grands hommes ont leurs disciples et c'est toujours Judas qui rédige la biographie.",
            u"De nos jours, on survit à tout sauf à la mort.",
            u"Démocratie: L'oppression du peuple par le peuple pour le peuple.",
            u"Derrière chacune des choses exquises qui existaient se cachait quelque chose de tragique.",
            u"Dieu, en créant l'homme, a quelque peu surestimé ses capacités.",
            u"Dire aux gens ce qu'il faut lire est en général inutile ou nuisible, car la véritable appréciation de la littérature est une question de tempérament et ne s'enseigne pas.",
            u"Dire qu'un livre est moral ou immoral n'a pas de sens, un livre est bien ou mal écrit c'est tout.",
            u"Effacer le passé, on le peut toujours: c'est une affaire de regret, de désaveu, d'oubli. Mais on n'évite pas l'avenir.",
            u"En ce monde, il n'y a que deux tragédies. L'une consiste à ne pas obtenir ce qu'on désire et l'autre à l'obtenir. Cette dernière est une réelle tragédie.",
            u"Il n'y a que les esprits légers pour ne pas juger sur les apparences. Le vrai mystère du monde est le visible, et non l'invisible.",
            u"Il ne faut pas oublier que, tandis que le partage de la joie en accroît l'étendue sur cette terre, le partage de la douleur n'en diminue pas la somme.",
            u"Il ne faut pas perdre un ami pour un bon mot; sauf si le mot est meilleur que l'ami.",
            u"Il ne faut regarder ni les choses, ni les personnes. Il ne faut regarder que dans les miroirs, car les miroirs ne nous montrent que des masques.",
            u"Il ne peut pas exister de bonne influence. Toute influence est immorale - immorale du point de vue scientifique.",
            u"J'adore être comédien. C'est tellement plus réel que la vie.",
            u"J'ai les goûts les plus simples du monde. Je me contente du meilleur.",
            u"J'ai mis tout mon génie dans ma vie; je n'ai mis que mon talent dans mes oeuvres.",
            u"J'ai toujours pensé que travailler dur était l'occupation de ceux qui n'avaient rien d'autre à faire.",
            u"J'aime les hommes qui ont un avenir et les femmes qui ont un passé.",
            u"J'aime les personnes bien plus que les principes et, plus que tout au monde, j'aime les personnes sans principes.",
            u"Je choisis mes amis pour leur bonne présentation, mes connaissances pour leur bon caractère et mes ennemis pour leur bonne intelligence. Un homme ne peut être trop soigneux dans le choix de ses ennemis.",
            u"Je déteste les discussions, elles vous font parfois changer d'avis.",
            u"Je n'ai pas peur de la Mort. Ce qui me terrifie, c'est l'approche de la Mort.",
            u"Je ne parle jamais pendant la musique, du moins pendant la bonne musique. Si l'on en entend de mauvaise, c'est un devoir de la couvrir par le bruit d'une conversation.",
            u"Je ne puis m'empêcher de détester ma famille. Cela vient, je crois, de ce que l'on ne peut supporter chez les autres ses propres défauts.",
            u"Je ne remets jamais au lendemain ce que je puis faire le surlendemain.",
            u"Je ne voyage jamais sans mes mémoires. Il faut toujours avoir quelque chose de sensationnel à lire dans le train.",
            u"Je peux résister à tout, sauf à la tentation.",
            u"Je vis tellement au-dessus de mes revenus qu'en vérité nous menons, eux et moi, une existence entièrement séparée.",
            u"L'art est toujours plus abstrait que nous ne l'imaginons. La forme et la couleur nous parlent de forme et de couleur, et tout s'arrête là.",
            u"L'artiste n'entend rien prouver. Tout se prouve, même ce qui est vrai.",
            u"L'égoïsme n'est pas vivre comme on le désire, mais demander aux autres de vivre comme on veut qu'ils vivent.",
            u"L'expérience est le nom que chacun donne à ses erreurs.",
            u"L'homme est un animal raisonnable qui se met régulièrement en colère lorsqu'on lui demande d'agir en accord avec les préceptes de la raison.",
            u"L'homme peut croire l'impossible mais jamais il ne pourra croire à l'improbable.",
            u"L'homme veut être le premier amour de la femme, alors que la femme veut être le dernier amour de l'homme.",
            u"L'immoralité est un mythe inventé par les honnêtes gens pour expliquer la curieuse attirance qu'exercent les autres.",
            u"L'indifférence est la revanche que prend le monde sur les médiocres.",
            u"L'opinion publique n'existe que là où il n'y a pas d'idées.",
            u"La beauté est dans les yeux de celui qui regarde.",
            u"La conversation doit tout aborder mais ne rien approfondir.",
            u"La différence entre littérature et journalisme, c'est que le journalisme est illisible et que la littérature n'est pas lue.",
            u"La fidélité est dans la vie sentimentale ce qu'est la fixité des idées dans la vie intellectuelle: un aveu de faillite.",
            u"La littérature anticipe toujours la vie. Elle ne la copie point, mais la moule à ses fins.",
            u"La meilleure façon de résister à la tentation, c'est d'y céder.",
            u"La mode est une forme de laideur si fatiguante qu'il faut en changer tous les trois mois.",
            u"La moralité des arts consiste dans l'usage parfait d'un moyen imparfait.",
            u"La nouvelle génération est épouvantable. J'aimerais tellement en faire partie.",
            u"La philosophie nous apprend à supporter sereinement le malheur des autres.",
            u"La pitié, c'est le côté par où une oeuvre s'ouvre aux hommes sur l'infini. Je suis entré dans ma geôle avec un coeur de pierre. Mon coeur s'y est brisé, et je sais maintenant que la pitié est ce qu'il y a de plus beau au monde.",
            u"La preuve que la mode est ridicule, c'est qu'elle change tout le temps.",
            u"La seule différence entre le caprice et la passion d'une vie, c'est que le caprice dure un peu plus longtemps.",
            u"La seule façon de se comporter avec une femme est de faire l'amour avec elle si elle est jolie, et avec une autre si elle ne l'est pas.",
            u"La société pardonne souvent au criminel, jamais elle ne pardonne au rêveur.",
            u"La véritable perfection d'un homme réside, non dans ce qu'il a, mais dans ce qu'il est.",
            u"La vérité est rarement pure et jamais simple.",
            u"La vie est une chose bien trop importante pour qu'on en parle sérieusement.",
            u"La vraie vie est si souvent celle qu'on ne vit pas.",
            u"Le cynisme consiste à voir les choses telles qu'elles sont et non telles qu'elles devraient être.",
            u"Le devoir, c'est ce qu'on attend des autres.",
            u"Le manque de sincérité est-il une chose si terrible? Je ne le pense pas. C'est simplement une méthode qui nous permet de multiplier nos personnalités.",
            u"Le mariage est la principale cause de divorce. - L'amour rend aveugle, le mariage rend la vue. - Les hommes se marient par lassitude, les femmes par curiosité... - Les deux sont déçus.",
            u"Le mariage est la seule condamnation à vie qui peut être suspendue pour mauvaise conduite.",
            u"Le monde a été créé par des idiots afin que les sages puissent y vivre.",
            u"Le problème des loisirs est d'empêcher les autres de gâcher les vôtres.",
            u"Le scepticisme est le commencement de la foi.",
            u"Le seul charme du passé, c'est qu'il est le passé.",
            u"Les amateurs de musique ont ceci de pénible qu'ils nous demandent toujours d'être totalement muet au moment même où nous souhaiterions être absolument sourd.",
            u"Les célibataires riches devraient payer de plus lourds impôts. Il n'est pas juste que certains hommes soient plus heureux que d'autres.",
            u"Les femmes gâchent les plus belles histoires d'amour en voulant qu'elles soient éternelles.",
            u"Les femmes nous donnent l'or de leur vie, mais elles nous le reprennent en menue monnaie.",
            u"Les femmes ont beaucoup plus de chance que les hommes sur cette terre, beaucoup plus de choses leur sont interdites.",
            u"Les femmes partagent nos plaisirs, doublent nos tourments et triplent nos dépenses.",
            u"Les femmes sont faites pour être aimées, non pour être comprises.",
            u"Les Français sont si fiers de leurs vins qu'ils ont donné à certaines de leurs villes le nom d'un grand cru.",
            u"Les gens bien élevés contredisent les autres. - Les sages se contredisent eux-mêmes.",
            u"Les grands événements du monde, a-t-on dit, se passent dans le cerveau. C'est aussi dans le cerveau, et dans le cerveau seul, que se passent les grands péchés du monde.",
            u"Les hommes sont si lâches: ils violent toutes les lois du monde et ont peur du qu'en-dira-t-on.",
            u"Les jeunes gens s'imaginent que l'argent c'est tout. Et quand ils deviennent vieux, ils en sont sûr.",
            u"Les jeunes gens voudraient être fidèles et ne le sont pas; les vieux voudraient être infidèles et ne le peuvent plus.",
            u"Les livres qu'on ne relit pas sans cesse avec plaisir ne valent pas la peine d'être lus.",
            u"Les questions ne sont jamais indiscrètes. Mais parfois les réponses le sont.",
            u"Les tragédies des autres sont toujours d'une banalité désespérante.",
            u"Les vieux croient à tout; les gens d'âge mûr mettent tout en doute; les jeunes savent tout.",
            u"Ne soyez pas fier de vos défauts. Vous pourriez bien les perdre en vieillissant.",
            u"Nous sommes tous dans le caniveau, mais certains d'entre nous regardent les étoiles.",
            u"Nul ne rencontre deux fois l'idéal. Combien peu le rencontrent même une fois!",
            u"On a conscience avant. On prend conscience après. Ou plutôt, c'est elle qui vous prend!",
            u"On devrait toujours être amoureux. C'est la raison pour laquelle on ne devrait jamais se marier.",
            u"On dit que les riches ne pensent qu'à l'argent... C'est faux... les pauvres y pensent bien davantage.",
            u"On ne devrait jamais prendre parti en quoi que ce soit. Prendre parti est le commencement de la sincérité et le sérieux ne tarde pas à se manifester. Et l'on devient ennuyeux.",
            u"Où l'homme cultivé saisit un effet, l'homme sans culture attrape un rhume.",
            u"Perdre un de ses parents peut-être regardé comme un malheur. Perdre les deux ressemble à de la négligence.",
            u"Qu'on parle de vous, c'est affreux. Mais il y a une chose pire: c'est qu'on n'en parle pas.",
            u"Quand la pauvreté se faufile par la porte, d'un coup d'aile l'amour entre par la fenêtre.",
            u"Quand les dieux veulent nous punir, ils exaucent nos prières.",
            u"Quand les gens nous parlent des autres, ils sont d'habitude ennuyeux. Quand ils parlent d'eux-mêmes, ils sont presque toujours intéressants.",
            u"Quand les gens sont d'accord avec moi, j'ai toujours le sentiment que je dois me tromper.",
            u"Quand nous sommes heureux, nous sommes toujours bons, mais quand nous sommes bons, nous ne sommes pas toujours heureux.",
            u"Quand on a un beau jeu, il ne faut jamais tricher.",
            u"Quand un homme commet quelque sottise incompréhensible, c'est toujours sous la dictée des plus nobles motifs.",
            u"Quand une femme se remarie, c'est qu'elle détestait son premier mari, quand un homme se remarie, c'est qu'il adorait sa première femme.",
            u"Quand, jadis, je rencontrais Verlaine, je ne rougissais pas de lui. J'étais riche, joyeux, couvert de gloire, et pourtant je sentais que d'être vu près de lui m'honorait... même quand Verlaine était ivre.",
            u"Quant aux présages, ça n'existe pas: la destinée ne nous envoie pas de hérauts; elle est trop sage... ou trop cruelle pour cela.",
            u"Qui veut de la cohérence? Les imbéciles et les doctrinaires, les ennuyeux qui poussent leurs principes jusqu'à la fin amère de l'action, jusqu'à la reductio ad absurdum de leur mise en pratique. Pas moi.",
            u"Rien, si ce n'est les sens, ne peut guérir l'âme, de même que rien, si ne n'est l'âme, ne peut guérir les sens.",
            u"S'aimer soi-même, c'est l'assurance d'une longue histoire d'amour.",
            u"Sachez que je puis croire toutes choses, pourvu qu'elles soient franchement incroyables.",
            u"Seuls les idiots sont brillants au petit déjeuner.",
            u"Si Adam avait été homosexuel, personne ne serait là pour le dire.",
            u"Si la vie avait une seconde édition, ah! comme je corrigerais les épreuves!",
            u"Si un homme manque d'imagination au point de ne pouvoir produire de preuves à l'appui d'un mensonge, il ferait mieux de dire la vérité tout de suite.",
            u"Tant qu'une femme peut paraître dix ans plus jeune que sa propre fille, elle est parfaitement satisfaite.",
            u"Tout comme la poésie, la sculpture ou la peinture, la vie a ses chefs-d'oeuvres précieux.",
            u"Un expert, c'est un homme ordinaire qui donne son avis... quand il n'est pas à la maison.",
            u"Un gentleman est quelqu'un qui ne blesse jamais les sentiments d'autrui sans le faire exprès.",
            u"Un peu de sincérité est dangereux, beaucoup de sincérité est fatal.",
            u"Un poète peut survivre à tout, sauf à une faute d'impression.",
            u"Une fatalité s'attache à toutes les bonnes résolutions. - On les prend toujours trop tôt.",
            u"Une femme commence par résister aux avances d'un homme. Ensuite, elle l'empêche de s'enfuir.",
            u"Une idée qui n'est pas dangereuse ne mérite pas d'être appelée une idée.",
            u"Vingt années d'aventures amoureuses font d'une femme une ruine; vingt ans de mariage, un monument public.",
            u"Vivre est ce qu'il y a de plus beau au monde, la plupart des gens existent, c'est tout.",
            u"Votre jeunesse s'en ira, votre beauté avec elle, et vous découvrirez tout à coup qu'il faudra faire votre deuil des triomphes, ou bien vous contenter des triomphes médiocres, rendus plus amers que des défaites par le souvenir glorieux du passé.",
            u"Votre sonnet est destiné à la postérité, mais je doute qu'il atteigne son adresse."
        ]

        bdd =[
            {'auteur':"Herm Albright"                           ,       'citation':albright     ,       'bind':"albright"       },
            {'auteur':"Isaac Asimov"                            ,       'citation':asimov       ,       'bind':"asimov"         },
            {'auteur':"Sir Francis Bacon"                       ,       'citation':bacon        ,       'bind':"bacon"          },
            {'auteur':"Pierre Beaumarchais"                     ,       'citation':beaumarchais ,       'bind':"beaumarchais"   },
            {'auteur':"Ambrose Bierce"                          ,       'citation':bierce       ,       'bind':"bierce"         },
            {'auteur':"Otto Von Bismarck"                       ,       'citation':bismarck     ,       'bind':"bismarck"       },
            {'auteur':"Wernher von Braun"                       ,       'citation':braun        ,       'bind':"braun"          },
            {'auteur':"Truman Capote"                           ,       'citation':capote       ,       'bind':"capote"         },
            {'auteur':"Jimmy Carter"                            ,       'citation':carter       ,       'bind':"carter"         },
            {'auteur':"Sir Winston Leonard Spencer Churchill"   ,       'citation':churchill    ,       'bind':"churchill"      },
            {'auteur':"Confucius"                               ,       'citation':confucius    ,       'bind':"confucius"      },
            {'auteur':"Jacques Boularan Deval"                  ,       'citation':deval        ,       'bind':"deval"          },
            {'auteur':"Will Durant"                             ,       'citation':durant       ,       'bind':"durant"         },
            {'auteur':"Thomas Alva Edison"                      ,       'citation':edison       ,       'bind':"edison"         },
            {'auteur':"Albert Einstein"                         ,       'citation':einstein     ,       'bind':"einstein"       },
            {'auteur':"Benjamin Franklin"                       ,       'citation':franklin     ,       'bind':"franklin"       },
            {'auteur':"Edmond de Goncourt"                      ,       'citation':goncourt     ,       'bind':"goncourt"       },
            {'auteur':"Bob Hope"                                ,       'citation':hope         ,       'bind':"hope"           },
            {'auteur':"Thomas Jefferson"                        ,       'citation':jefferson    ,       'bind':"jefferson"      },
            {'auteur':"Juan Ramon Jimenez"                      ,       'citation':jimenez      ,       'bind':"jimenez"        },
            {'auteur':"John Fitzgerald Kennedy"                 ,       'citation':kennedy      ,       'bind':"kennedy"        },
            {'auteur':"Soren Aabye Kierkegaard"                 ,       'citation':kierkegaard  ,       'bind':"kierkegaard"    },
            {'auteur':"Martin Luther King"                      ,       'citation':king         ,       'bind':"king"           },
            {'auteur':"Karl Kraus"                              ,       'citation':kraus        ,       'bind':"kraus"          },
            {'auteur':"Lao-Tseu"                                ,       'citation':lao_tseu     ,       'bind':"lao_tseu"       },
            {'auteur':"John Lennon"                             ,       'citation':lennon       ,       'bind':"lennon"         },
            {'auteur':"Abraham Lincoln"                         ,       'citation':lincoln      ,       'bind':"lincoln"        },
            {'auteur':"Henry Louis Mencken"                     ,       'citation':mencken      ,       'bind':"mencken"        },
            {'auteur':"Friedrich Nietzsche"                     ,       'citation':nietzsche    ,       'bind':"nietzsche"      },
            {'auteur':"Louis Pasteur"                           ,       'citation':pasteur      ,       'bind':"pasteur"        },
            {'auteur':"Pablo Picasso"                           ,       'citation':picasso      ,       'bind':"picasso"        },
            {'auteur':"Francois de La Rochefoucauld"            ,       'citation':rochefoucauld,       'bind':"rochefoucauld"  },
            {'auteur':"Franklin Delano Roosevelt"               ,       'citation':roosevelt    ,       'bind':"roosevelt"      },
            {'auteur':"Jean Jacques Rousseau"                   ,       'citation':rousseau     ,       'bind':"rousseau"       },
            {'auteur':"George Bernard Shaw"                     ,       'citation':shaw         ,       'bind':"shaw"           },
            {'auteur':"Socrates"                                ,       'citation':socrates     ,       'bind':"socrates"       },
            {'auteur':"Henry David Thoreau"                     ,       'citation':thoreau      ,       'bind':"thoreau"        },
            {'auteur':"Mark Twain"                              ,       'citation':twain        ,       'bind':"twain"          },
            {'auteur':"Voltaire"                                ,       'citation':voltaire     ,       'bind':"voltaire"       },
            {'auteur':"Andy Warhol"                             ,       'citation':warhol       ,       'bind':"warhol"         },
            {'auteur':"Oscar Wilde"                             ,       'citation':wilde        ,       'bind':"wilde"          }
        ]
    elif( category == "bible" ):
        # Bible
        ecclesiaste = [
            u"Ce qui est tordu ne peut être droit, ce qui manque ne peut être compté.",
            u"L'envie et la colère abrègent les jours.",
            u"Instruire un sot, c'est recoller des tessons.",
            u"Un ami fidèle est un abri robuste ; qui le trouve a trouvé un trésor.",
            u"Le paresseux ressemble à une bouse de vache : Quiconque la ramasse secoue sa main.",
            u"Un ami fidèle n'a pas de prix, et pas de poids pour peser sa valeur.",
            u"Le sage a les yeux ouverts mais l'insensé marche dans les ténèbres.",
            u"Tous les malheurs de nos pères Ne nous ont point détrompés; Nous éprouvons les misères Dont nos fils seront frappés.",
            u"C'est un don du Seigneur qu'une femme silencieuse et sans prix est la femme bien élevée.",
            u"Il n'y a pas d'homme juste sur la terre qui fasse le bien sans jamais pécher.",
            u"Pour un mort sept jours de deuil ; pour le sot et pour l'impie tous les jours de leur vie.",
            u"Ne te détourne pas d'une épouse sage et bonne, Car son charme vaut mieux que l'or.",
            u"L'étalon est l'image de l'ami moqueur : il hennit sous tout cavalier.",
            u"Le riche commet une injustice, et il frémit d'indignation ; le pauvre est maltraité, et il demande pardon.",
            u"Si un homme instruit entend une parole sage, il l'apprécie et y ajoute du sien ; qu'un débauché l'entende, elle lui déplaît, il la rejette derrière lui.",
            u"La sagesse vaut mieux que la force, mais la sagesse du pauvre est méconnue et ses paroles, personne ne les écoute.",
            u"Sagesse cachée et trésor invisible, à quoi servent-ils l'un et l'autre ? Mieux vaut un homme qui cache sa folie qu'un homme qui cache sa sagesse.",
            u"Chercher n'est pas une chose et trouver une autre, mais le gain de la recherche, c'est la recherche même.",
            u"Pleure sur un mort car lui manque la lumière ; pleure sur un sot car lui manque le bon sens ; pleure doucement sur le mort car il a trouvé le repos ; mais la vie du sot est pire que la mort.",
            u"Le sable de la mer, les gouttes de la pluie, les jours de l'éternité, qui peut les dénombrer ? La hauteur du ciel, l'étendue de la terre, la profondeur de l'abîme, qui peut les explorer ? Mais avant toute chose fut créée la Sagesse..."
            u"Sans une femme l'homme gémit et va à la dérive.",
            u"Ce qui fut, cela sera ; ce qui s'est fait se refera ; et il n'y a rien de nouveau sous le soleil",
            u"Pour tous ceux qui vivent il y a de l'espérance ; et même un chien vivant vaut mieux qu'un lion mort."
            u"N'abandonne pas un vieil ami, le nouveau ne le vaudra pas.",
            u"Mieux vaut écouter la semonce du sage qu'écouter le chant du fou.",
            u"Il y a un temps pour tout, un temps de pleurer, un temps de rire, un temps à se lamenter et un temps de danser.",
            u"Qui observe le vent ne sème point, qui regarde les nuages ne moissonne point.",
            u"Ne sois pas juste à l'excès, ni sage outre mesure. Pourquoi te rendrais-tu stupide ?",
            u"Ne dispute pas avec un beau parleur, ne mets pas de bois sur le feu.",
        ]
        proverbes = [
            u"La haine excite les querelles, l'amour couvre toutes les fautes.",
            u"Faute de vision, le peuple vit sans frein.",
            u"Celui qui est lent à la colère vaut mieux qu'un héros.",
            u"C'est ouvrir une digue qu'entamer un procès; avant qu'il ne s'engage, désiste-toi.",
            u"As-tu vu un homme pressé de parler, - Il y a plus à espérer d'un sot que de lui.",
            u"Fortune hâtive va diminuant; - qui amasse peu à peu s'enrichit."
        ]
        isaie = [
            u"Pour voir le futur, il faut regarder derrière soi.",
            u"Mieux vaut acquérir la sagesse que les perles.",
            u"De leurs épées ils forgeront des socs, - Et de leurs lances des serpes. - Une nation ne tirera plus l'épée contre une autre, - Et l'on ne s'entraînera plus à la guerre.",
            u"Quand vos péchés seraient comme l'écarlate, ils deviendront blancs comme la neige; et quand ils seraient rouges comme le vermillon, ils seront blancs comme la laine la plus blanche."
        ]
        jeremie = [
            u"Ecoutez donc ceci, peuple stupide et irréfléchi : avec leurs yeux, ils ne voient rien, avec leurs oreilles, ils n'entendent rien !",
            u"La voie des humains n'est pas en leur pouvoir, et il n'est pas donné à l'homme qui marche de diriger ses pas.",
            u"Un ami fidèle n'a pas de prix, et pas de poids pour peser sa valeur.",
            u"Pour un mort sept jours de deuil ; pour le sot et pour l'impie tous les jours de leur vie."
        ]
        job = [
            u"Le châtiment des sots est la sottise.",
            u"Tu viendras jusqu'ici, pas plus loin, - Ici s'arrêtera l'orgueil de tes flots.",
            u"Après les ténèbres, j'espère revoir la lumière.",
            u"Quand un humain expire, où donc est-il?",
            u"A l'infortune, le mépris! opinent les gens heureux; un coup de plus à qui chancelle!",
            u"Nous, né d'hier, nous ne savons rien, notre vie sur terre passe comme une ombre.",
            u"Yahvé avait donné, Yahvé a repris; - que le nom de Yahvé soit béni!",
            u"Je suis sorti nu du sein de ma mère et j'y retournerai nu."
        ]
        abdias = [
            u"Comme tu as fait il te sera fait : tes actes te retomberont sur la tête."
        ]
        psaumes = [
            u"Ceux qui sèment dans les larmes moissonneront dans la joie.",
            u"Le commencement de la sagesse, c'est la crainte de l'Eternel.",
            u"L'homme! ses jours sont comme l'herbe, - Il fleurit comme la fleur des champs. - Lorsqu'un vent passe sur elle, elle n'est plus, - Et le lieu qu'elle occupait ne la reconnaît plus.",
            u"Le Seigneur connaît les pensées des sages et sait qu'elles sont vaines.",
            u"Tu éloignes de moi amis et proches; - ma compagnie, c'est la ténèbre.",
            u"Vous les hommes, jusqu'à quand ces coeurs fermés, ce goût du rien, cette course au mensonge?",
            u"Et maintenant, ô rois! comprenez; instruisez-vous, vous qui jugez la terre.",
            u"Au bord des fleuves de Babylone - nous étions assis et pleurions, - nous souvenant de Sion.",
            u"Je tiens mon âme en paix et en silence, comme un enfant contre sa mère.",
            u"Des profondeurs je crie vers toi, Yahvé: Seigneur, écoute mon appel!",
            u"Ton épouse, une vigne fructueuse au coeur de ta maison. Tes enfants comme des plants d'olivier alentour de ta table"
        ]
        deuteronome = [
            u"Tu dois ouvrir ta main à ton frère, à celui qui est humilié et pauvre dans ton pays.",
            u"Quand tu donnes, tu dois donner de bon coeur.",
            u"Vous aimerez le Seigneur, votre Dieu de tout votre coeur, de toute votre âme, et de toutes vos forces.",
            u"Une femme ne portera pas un costume masculin, et un homme ne mettra pas un vêtement de femme: quiconque agit ainsi est en abomination à Yahvé ton Dieu.",
            u"Maudit soit celui qui méconnaît le droit de l'étranger, de l'orphelin et de la veuve!",
            u"Tu n'auras pas dans ton sac poids et poids, l'un lourd et l'autre léger.",
            u"Tu ne laboureras pas avec un boeuf et un âne ensemble."
        ]
        bible = [
            u"Dieu créa l'homme à son image.",
            u"Tu es poussière et tu retourneras en poussière.",
            u"Le châtiment des sots est la sottise."
        ]
        bdd =[
            {'auteur':"Ecclesiaste" ,       'citation':ecclesiaste  ,       'bind':"ecclesiaste"    },
            {'auteur':"Proverbes"   ,       'citation':proverbes    ,       'bind':"proverbes"      },
            {'auteur':"Isaie"       ,       'citation':isaie        ,       'bind':"isaie"          },
            {'auteur':"Jérémie"     ,       'citation':jeremie      ,       'bind':"jeremie"        },
            {'auteur':"Job"         ,       'citation':job          ,       'bind':"job"            },
            {'auteur':"Abdias"      ,       'citation':abdias       ,       'bind':"abdias"         },
            {'auteur':"Psaumes"     ,       'citation':psaumes      ,       'bind':"psaumes"        },
            {'auteur':"Deutéronome" ,       'citation':deuteronome  ,       'bind':"deuteronome"    },
            {'auteur':"Bible"       ,       'citation':bible        ,       'bind':"bible"          }
        ]
    elif( category == "simpson" ):
        # Simpson
        saison1 = [
            u"Homer : Oh, c'est pas vrai ! Y'a combien de classes dans cette satanée école ?",
            u"Marge : Très chers amis, nous avons eu notre lot de chagrin et de joie cette année encore. Les chagrins d'abord. Notre petit chat Boule de Neige est passé sous une voiture. Il s'en est allé au paradis des minous. Mais nous avons acheté un nouveau petit chat, Boule de Neige II, la vie continue. En parlant de la vie qui continue, Grand-père est toujours de ce monde plus grognon que jamais. Maggie marche toute seule à présent et Lisa est toujours aussi bonne élève. Quant à Bart, et bien... on l'aime Bart. Cette période magique de Noël nous met tous le coeur en fête.",
            u"Technicien de la clinique au laser : [En allumant le laser] Tu fais ce que tu veux, mais surtout ne te tortille pas. Tu n'as pas envie de prendre ce rayon glouton entre les yeux ou... entre les jambes, hein ?",
            u"Homer : Il me reste plus que la petite Maggie. Oh, regardez-moi ça, un petit jouet qui couine. C'est écrit « pour chiens ». Bah, elle sait pas lire.",
            u"Homer : Euh... quand tu... descendras... du ciel, avec tes dollars... par milliers. N'oublie pas... mon petit bocal.",
            u"Bart : Ouais, ça je te crois, p'pa. Faut vraiment que tu nous aimes pour tomber aussi bas.",
            u"Homer : [Costumé en Père Noël, en sortant de l'atelier] Coucou les enfants, le Père Noël est de retour. Ho ho... [Il se cogne la tête] Aïe ! Saloperie ! Ca fait mal.",
            u"Homer : Mais c'est un perdant ! C'est un minable ! C'est un... Un Simpson.",
            u"Bart : S'il se sauve on aura pas de mal à le rattraper.",
            u"Marge : [En écrivant une lettre] Chers amis de la famille Simpson, nous avons connu des joies et des peines cette année. Commençons par les peines. Notre petit chat, Boule de neige, s'est fait frapper, sans le vouloir, par un camion et est monté au ciel des p'tits minous. Mais, nous avons acheté un autre Boule de neige numéro II, faut croire que la vie continue. Parlant de la vie qui continue, Grand-père est toujours parmi nous, aussi alerte que jamais. Maggie marche maintenant toute seule. Lisa a eu des « A » dans toutes ses matières et Bart... euh... on l'aime bien notre Bart. Nous sommes tous dans l'esprit de Noël.",
            u"Technicien de la clinique au laser : [En allumant le laser] Tu peux faire tout ce que tu veux mon gars, sauf te tortiller. Tu voudrais pas que ça t'arrive dans les yeux ou ... entre les jambes.",
            u"Homer : Y reste plus que la p'tite Maggie. Oh, regarde-moi ça, une petite bébelle qui fait couic-couic. Ouais, c'est pour les chiens par exemple. Bah, de toute façon, elle ne sait pas lire.",
            u"Homer : Coureur ... euh... Danseur, Caracoleur... euh... Nixon, Comète, Cupidon, Donne-moi le ton.",
            u"Bart : Sais-tu pôpa, il faut que tu nous aime en titi pour descendre aussi bas.",
            u"Homer : [Costumé en Père Noël, en sortant de l'atelier] Salut les p'tits enfants, le Père Noël est de retour. Ho Ho... [Il se cogne la tête] Oh oh, tarvisse, oh, oh...",
            u"Homer : Ben voyons, c'est rien qu'un perdant, c'est une guenille, c'est un ... Ben, c't'un Simpson.",
            u"Bart : Pis, si il essaie de s'enfuir, il va être facile à rattraper..",
            u"Krapabelle : Ne vous en faîtes pas, surtout. Ces tests n'ont aucune influence sur vos résultats scolaires. Ils ne font qu'évaluer votre futur statut social et votre réussite matérielle... [À Bart.] S'il y en a une.",
            u"Homer : Allez vas-y maintenant et tâche de bien écouter surtout. Parce que si tu travailles bien, qui sait, peut-être qu'un jour tu réaliseras le rêve que les Simpson font depuis des générations : prouver qu'on est pas plus bête qu'un autre.",
            u"Bart : Si vous voulez la guerre, vous devez préparer la paix.",
            u"Homer : Pas de bières, pas de hot dog, pas d'esquim-opéra.",
            u"Homer : Je suis bien sûr qu'Einstein est passé par toutes les couleurs de l'arc-en-ciel avant d'inventer l'ampoule.",
            u"Apu Nahasapeemapetilon : Oui oui, je connais la marche à suivre, vous énervez pas. Chez nous le client a toujours raison, surtout s'il est armé."
        ]
        #~ saison4 = [ u"Saison 4",
            #~ u" Oh la crise... cardiaque ! Assureur : Hein hein, euh vous buvez ? Homer : Je crache pas sur un p’tit verre de Porto à Noël. Assureur : Entendu, voici votre police.",
            #~ u"Lisa : Tuer des serpents, c’est mal. Homer : T’as p’têt raison Lisa. Mais ça fait partie de notre nature humaine. Dans chaque homme, y a un tiraillage entre le bien et le mal. Et ça, ça peut pas se régler."
        #~ ]
        saison5 = [
            u"Waylon Smithers : Regardez toutes les merveilleuses choses que vous avez. Excalibur du roi Arthur, la seul photo nue existante de Mark Twain et ce très rare premier jet de la constitution dans lequel reste le mot « andouille »."
        ]
        saison6 = [
            u"Moe Szyslak : Mais Blanche, il faut que tu m'aides, j'ai un trou de 64 000 $, ils vont me couper les pouces !",
            u"Lisa : Il faut se faire une raison, Bart. Notre salut ne viendra pas d'un petit camion idiot qui sillonne la ville."
        ]
        saison7 = [
            u"Abraham Simpson : Ouais ben désolé mais il faisait quarante degrés dans la bagnole",
            u"Lisa : Devenir l'assistant de M. Burns peut donner un sacré coup de pouce à ta carrière !",
            u"Ralph : Moi, quand je serais grand, j'irais à l'université bovine."
        ]
        saison8 = [
            u"Cecil : Un verre de Bordeaux peut-être ? J'ai un Chateau LaTour de 82 et un rouge californien plutôt quelconque... Tahiti Bob : J'ai vécu en prison Cecil. Tant qu'il ne s'agit pas d'une boisson à l'orange fermentée sur un radiateur ça m'ira...",
            u"Homer : Des Extra-terrestre ?! Me mangez pas ! J'ai une femme et des gosses... Mangez-les !"
        ]
        saison9 = [
            u"Carl Carlson : Non chez Hefner, le patron de Playboy.",
            u"Un vendeur : Seulement des Klav-kalash, toilettes dans tour, tour ! Terrasse panoramique !"
        ]
        saison10 = [
            u"Troy McClure : Ouais ben désolé mais il faisait quarante degrés dans la bagnole",
            u"Max Puissant : Il y a trois façons de faire les choses : la bonne, la mauvaise et celle de Max Puissant.",
            u"Wink : Ne vous inquiétez pas, cette « lave » n'est que de l'orangeade fabriquée par notre sponsor la société orangeade Osaka."
        ]
        saison14 = [
            u"Une poupée ressemblant à Homer : J'ai pissé dans mon froc !",
            u"Un virgile : Oui, bien sûr ! Et moi je vais danser le tango avec Cendrillon !",
            u"Homer : Ah oui. Donnez-moi ça que je regarde... Quoi ! 1 000 $ ! Comment vous avez pu claquer 1 000 $ ?!",
            u"Apu Nahasapeemapetilon : La production du reality show m'oblige à ne vous vendre que les produits existants en 1895. Chocoleos, désolé, c'est sorti en 96. Papier hygiénique parfumé. Non, oubliez-ça. Urkelo's, délicieux mais déconseillé.",
            u"Homer : Et si on allait tous boire un énorme milk-shake au chocolat !"
        ]
        saison15 = [
            u"Marge : Le petit est nul au jeu de cache-cache, n'empêche qu'il nous file comme Sherlock Holmes.",
            u"Homer : Ça y est Marge, je crois que j'ai trouvé. Lee Harvey Oswald voulait voler le rubis de Jack.",
            u"Homer : Aaaaaah !! Y'a un ours qui parle qui mange mon père !",
            u"Apu Nahasapeemapetilon : Très bien... Lard fumé de porc « endurci au lard », Lard fumé de porc « tué lentement », Lard fumé « spécial voyage »... Monsieur Simpson, si vous tenez vraiment à vous tuer, je vend aussi des revolvers !"
        ]
        saison16 = [
            u"Barney Gumble : Raté les enfants ! Et maintenant, comme Road Runner qui a vu le coyote... Bip Bip !",
            u"Ray Magini : Regardez-moi tout ce fromage fondu. Ça me rappelle le tas de guimauve quand mon disque de Billy Joel avait fondu au soleil."
        ]
        saison17 = [
            u"Richard Dean Anderson : Vous aimez MacGyver !? C'était une série complètement débile ! Ooooh, je suis MacGyver, je fais une bombe avec une peau de banane et un grille-pain ! J'ai joué ce rôle seulement pour l'argent, et rien d'autre",
            u"Mason Fairbanks : Avec grand plaisir. J'ai dîné avec le prince de Galles et avec une vache du pays de Galles. Mais seule cette dernière savait mâcher en fermant la bouche."
        ]
        saison18 = [
            u"Bart : Avant j'étais un grand batteur et maintenant je ne suis plus rien ! Comme Phil Collins !"
        ]
        saison20 = [
            u"Milhouse : Il est à Denis Leary ! Euh... Je suis désolé, Bart. Je résiste pas à l'envie de faire plaisir à un adulte."
        ]
        film = [
            u"Homer : Spider Cochon, Spider Cochon, Il peut marcher au plafond. Est-ce qu'il peut faire une toile ? Biensûr que non, c'est un cochon. Prends garde ! Spider Cochon est là."
        ]
        bdd =[
            {'auteur':"Saison 1"    ,       'citation':saison1      ,       'bind':"saison1"    },
            #~ {'auteur':"Saison 4"    ,       'citation':saison4      ,       'bind':"saison4"    },
            {'auteur':"Saison 5"    ,       'citation':saison5      ,       'bind':"saison5"    },
            {'auteur':"Saison 6"    ,       'citation':saison6      ,       'bind':"saison6"    },
            {'auteur':"Saison 7"    ,       'citation':saison7      ,       'bind':"saison7"    },
            {'auteur':"Saison 8"    ,       'citation':saison8      ,       'bind':"saison8"    },
            {'auteur':"Saison 9"    ,       'citation':saison9      ,       'bind':"saison9"    },
            {'auteur':"Saison 10"   ,       'citation':saison10     ,       'bind':"saison10"   },
            {'auteur':"Saison 14"   ,       'citation':saison14     ,       'bind':"saison14"   },
            {'auteur':"Saison 15"   ,       'citation':saison15     ,       'bind':"saison15"   },
            {'auteur':"Saison 16"   ,       'citation':saison16     ,       'bind':"saison16"   },
            {'auteur':"Saison 17"   ,       'citation':saison17     ,       'bind':"saison17"   },
            {'auteur':"Saison 18"   ,       'citation':saison18     ,       'bind':"saison18"   },
            {'auteur':"Saison 20"   ,       'citation':saison20     ,       'bind':"saison20"   },
            {'auteur':"Le film"     ,       'citation':film         ,       'bind':"film"       }
        ]
    elif( category == "politic" ):
        albanel = [
            u"Mes cheveux raccourcissent au fur et à mesure que mon expérience croît. - 2009"
        ]
        alliotmarie  = [
            u"La France, c'est la Tour Eiffel et Jacques Chirac. - 2007"
        ]
        amara = [
            u"J’ai tendance à croire que Nadine Morano c’est la Castafiore (à propos de Nadine Morano). - 2007"
        ]
        arpaillange = [
            u"En 1989, sur cinquante-deux évadés, on en a repris cinquante-trois."
        ]
        arthaud = [
            u"Je ne serai peut être pas élue Présidente de la République, mais je ne serai pas la seule. - 2011"
        ]
        arthuis = [
            u"Bernard Palissy brûlait ses meubles. Bayrou brûle ses élus. C’est la stratégie de l’anéantissement. - 2008"
        ]
        bachelot = [
            u"Dans les vestiaires, nous n'avions qu'un mot : énorme ! (après la victoire des handballeurs français aux Championnats du Monde) - 2009",
            u"La moitié du nuage d’ozone qui sévit dans la région parisienne est d’importation anglaise et allemande. - 2004",
            u"Le bobsleigh, c'est comme l'amour : on hésite au début, on trouve cela très bien pendant et on regrette que cela soit déjà terminé après. - 2007"
        ]
        balkany = [
            u"Je suis l’homme le plus honnête du monde."
        ]
        barnier = [
            u"Que l'on soit pour ou contre la Turquie, on ne pourra pas changer l'endroit où elle se trouve."
        ]
        baroin = [
            u"Je ne suis pas sûr qu'on prenne de la hauteur en montant sur une table. 1995",
            u"Je suis un des rares ministres chiraco-sarko-villepino compatible. - 2006",
            u"L'UMP est une formation jeune qui n'avait pas prévu qu'un des siens deviendrait président de la République ! (Union pour la Majorité Présidentielle) - 2007",
            u"Michèle Alliot-Marie conserve toute sa légitimité à Saint-Jean-de-Luz"
        ]
        barre = [
            u"La meilleure façon de résoudre le chômage, c'est de travailler. - 1997",
            "Quand le moment est venu, l'heure est arrivée"
        ]
        bayrou = [
            u"J'ai été longtemps un jeune conformiste, et sans doute formiste était-il de trop",
            u"Je vous le promets, nous aurons d'autres victoires (le soir de sa défaite aux municipales.)",
            u"Rassembler les centristes, c’est comme conduire une brouette pleine de grenouilles : elles sautent dans tous les sens. - 2012"
        ]
        bertrand = [
            u"Le Parti socialiste est un parti sans leader. François Bayrou est un leader sans parti. Ils sont faits pour fusionner. - 2008"
        ]
        besson = [
            u"On ne peut pas s’entendre avec tous les Ministres, car tous les Ministres ne peuvent pas s’entendre. - 2008"
        ]
        borloo = [
            u"Sarkozy, c’est le seul qui a été obligé de passer par l’Élysée pour devenir Premier ministre. - 2007"
        ]
        charasse = [
            u"Cela pourrait faire un film dont le titre serait Mamère Noël est une ordure - 2004."
        ]
        chassaigne = [
            u"Dans sa forme historique, le PC est mort ; mais il a encore de l’avenir - 2011."
        ]
        chatel = [
            u"Une touche de rose, vert, rouge : c’est le retour de la gouache plurielle. - 2010"
        ]
        chevenement = [
            u"[Hollande propos des «assises de la transformation sociale de la Gauche».] Pourquoi des Assises ? La correctionnelle suffirait ! - 2007"
        ]
        bachelay = [
            u"Qu’on commette des erreurs en politique c’est possible ; qu’on les commette toutes, c’est fou !- 2011"
        ]
        bchirac = [
            u"[S'adressant à Nicolas Sarkozy] Heureusement qu’on vous a ; et, en plus, je suis sincère. - 2004",
            u"Je ne l'ai pas beaucoup côtoyé à l’Élysée, on peut ne pas prendre le même escalier (À propos de Dominique de Villepin) - 2006"
        ]
        jchirac = [
            u"J'ai décidé de dissoudre l'Assemblée Nationale. - 1997"
        ]
        clement = [
            u"Je suis peut-être nul, mais le ministre, c'est moi. - 2007"
        ]
        gcohnbendit = [
            u"Les Verts sont capables du meilleur comme du pire ; mais c’est dans le pire qu’ils sont les meilleurs. (frère de Daniel Cohn-Bendit) - 2011"
        ]
        cope = [
            u"Tu as prévu de filer les clés de l'UMP à Xavier Bertrand; tu devrais en garder un double. - 2009",
            u"Moi vivant, il n'y aura pas d'augmentation de la redevance. - 2009"
        ]
        crepeau =  [
            u"J'ai été avocat pendant 28 ans et Garde des Sceaux pendant 28 jours. Si je suis le seul ministre de la Justice à ne pas avoir commis d'erreur, c'est parce que je n'ai pas eu le temps. - 1998"
        ]
        darcos = [
            u"uand vous êtes aux affaires vous manquez de souffle ; quand vous êtes dans l’opposition vous ne manquez pas d’air. (S'adressant à des élus PS)- 2004"
        ]
        dati = [
            u"Je n’ai jamais cherché à attirer l’attention des médias."
        ]
        debre = [
            u"Je n’imagine pas un instant cette île séparée du continent. (Àpropos de la Corse) - 2004",
            u"À l'Assemblée on s'occupe des JO et on laisse les Jeux paralympiques au Sénat"
        ]
        delanoe = [
            u"Le vrai changement au PS, ce serait de gagner. 2009"
        ]
        devedjian = [
            u"On était dans un appartement avec une fuite de gaz. Chirac a craqué une allumette pour y voir clair. (A propos de la dissolution) - 1998",
            u"Les coupures de presse sont celles qui cicatrisent le plus vite. - 2006",
            u"Je suis pour un gouvernement d'ouverture, y compris aux Sarkozistes, c'est tout dire. - 2007",
            u"Il y avait tellement de gens à mon enterrement que j’ai décidé de ne pas m’y rendre. - 2011"
        ]
        dousteblazy = [
            u"Le Hamas a voulu faire une croix sur Israël. - 2006"
        ]
        duflot = [
            u"Quel est le féminin de candidat aux cantonales ? C’est suppléante. - 2011"
        ]
        estrosi = [
            u"Vous avez vu comme Monsieur Sarkozy est populaire en forêt amazonienne ? - 2007"
        ]
        fabius = [
            u"Je ne suis pas une pompom girl de DSK.",
            u"Il est plus facile de céder son siège à une femme dans l'autobus qu'à l'Assemblée nationale. - 1997",
            u"Je préfère dire voici mon projet que mon projet c'est Voici. - 2006",
            u"Mitterrand est aujourd'hui adulé, mais il a été l'homme le plus détesté de France. Ce qui laisse pas mal d'espoir pour beaucoup d'entre nous… - 2011"
        ]
        faure = [
            u"Voici que s'avance l'immobilisme et nous ne savons pas comment l'arrêter."
        ]
        fidelin= [
            u"Vu de la Chine, le port du Havre ne travaille pas. - 2011"
        ]
        fillon = [
            u"Aucune mobilisation ne règlera le problème démographique que pose la question des retraites. - 25 Juin 2010",
            u"L'intérêt général nous commande de ne pas transiger sur les principaux paramètres de la réforme. - 25 Juin 2010",
            u"Ceux qui confondent le prix de la tonne de carbone avec un baromètre des relations entre le président et le Premier ministre en seront pour leurs frais. - 6 Septembre 20009",
            u"La stratégie de Lisbonne était un beau projet, plein d'ambition, mais il faut reconnaître son échec au moment de redéfinir notre méthode. - 5 Septembre 2009"
        ]
        freche = [
            u"Des gens intelligents il y en a 5 à 6 % ; moi je fais campagne pour les cons - 2010"
        ]
        garaud = [
            u"Il ment tellement que l’on ne peut même pas croire le contraire de ce qu’il dit. (Parlant de Jacques Chirac)"
        ]
        gueant = [
            u"Je veux bien qu’on fasse un remaniement, mais on manque de stock."
        ]
        goasguen = [
            u"Une chose est sûre, ce ne sont pas nos suppléants qui vont nous pousser à nous faire vacciner contre la grippe A. - 2010"
        ]
        godfrain = [
            u"Les socialistes aiment tellement les pauvres qu'ils en fabriquent."
        ]
        goulard = [
            u"François Fillon a tellement de qualités qu’il mériterait d’être premier ministre.",
            u"Cette semaine, le gouvernement fait un sans faute : il est vrai que nous ne sommes que mardi !",
            u"Johnny Hallyday qui annonce son intention de rester français et Bernard Laporte qui entre au gouvernement, c'est une période faste pour l'intelligence française !"
        ]
        hollande = [
            u"Jack Lang avait toutes les qualités pour briguer la Présidence de la République. C'est pour cela que je l'ai chaudement encouragé à se retirer. ",
            u"Sarkozy est passé de la présidence bling-bling à la présidence couac-couac. - 2008",
            u"Mélenchon, ce qui est terrible, c’est qu’il a été Socialiste toute sa vie et que toute sa vie ça va le suivre"
        ]
        hortefeux = [
            u"[Après la tempête de neige sur l’Ile-de-France]Il n’y a pas de pagaille ; la preuve le Préfet a pu venir en trois minutes. - 2011"
        ]
        hue = [
            u"Si Bush et Thatcher avaient eu un enfant ensemble, ils l'auraient appelé Sarkozy."
        ]
        joly = [
            u"Je connais bien Dominique Strauss-Kahn, je l’ai mis en examen. - 2010",
        ]
        juppe = [
            u"Pourquoi être seulement désagréable lorsqu'on peut être parfaitement odieux ?"
        ]
        kouchner = [
            u"J’ai bien pensé à démissionner, mais je n’ai pas voulu déserter. ",
            u"La contraception doit avoir ses règles. - 1998"
        ]
        lagarde = [
            u"Pour faire face à la hausse du prix du pétrole, je conseille aux Français de faire du vélo. - 2008"
        ]
        laporte = [
            u"Je voulais voir les Antilles de vive voix. - 2008"
        ]
        lellouche = [
            u"La Royal a coulé la Marine. - 2007"
        ]
        jmlepen = [
            u"Question d'un journaliste à Jean-Marie Le Pen : «Si vous êtes élu Président, quel sera votre premier voyage à l'étranger ?» Réponse : «Montfermeil». (située dans le département de la Seine-Saint-Denis) - 2007"
        ]
        klarsfeld = [
            u"Je ne suis pas un expert du 12ème arrondissement, mais je l'ai traversé quand j'ai couru le marathon de Paris. - 2007"
        ]
        lienemann = [
            u"Mon mari était jusqu'à présent chômeur, mais je suis en train de changer de mari."
        ]
        luca = [
            u"Il n’y a pas besoin d’être de droite ou de gauche pour dire des conneries. - 2010"
        ]
        marchais = [
            u"Je n’en ai discuté avec personne, mais c’est la position de mon parti."
        ]
        mitterrand = [
            u"Quand on m’appelle M. le ministre, j’ai toujours l’impression que Jack Lang va surgir derrière moi! - 2010"
        ]
        morano = [
            u"Fadela Amara au Gouvernement, cela montre les limites du casting à la Fogiel. - 2008",
            u"Je suis sarkozyste jusqu'au bout des globules - 2009"
        ]
        nallet = [
            u"Le plan sécheresse n'est pas un arrosage."
        ]
        olin = [
            u"Je trouve qu'on a tellement de choses à se mettre dans la tête qu'il est inutile de s'encombrer le cerveau. - 2006"
        ]
        pasqua = [
            u"Mes détracteurs ont commencé à s'opposer aux charters. La police de l'air a négocié avec la SNCF, on a parlé de train de la honte. Si on décidait d'utiliser les bateaux, on évoquerait l'« Exodus ». Il ne nous reste donc, en réalité, que l'autobus ou le vélo. - 1994",
            u"Les gazelles courent plus vite que les éléphants"
        ]
        poignant  = [
            u"L'an dernier, les carottes étaient râpées, cette fois elles sont cuites. - 2005"
        ]
        raffarin = [
            u"Les veuves vivent plus longtemps que leurs conjoints. (Repris de la célèbre phrase de Georges Clemenceau : Les femmes vivent plus longtemps que les hommes, surtout les veuves.) - 2005",
            u"Ségolène, elle séduit au loin et irrite au près. - 2006",
            u"Il faut avoir conscience de la profondeur de la question du sens. - 2008",
            u"Le tour de taille n'est pas un handicap au Sénat. - 2009"
        ]
        rocard = [
            u"Le PS est mal portant; et comme je respecte les hôpitaux, je baisse la voix comme on doit le faire quand il y a un malade dans la place. - 2009"
        ]
        rohan = [
            u"Souvent les courants d’air proviennent de ce qu’il y a trop d’ouverture . - 2008"
        ]
        royal = [
            u"’est moi qui maîtrise la rareté de ma parole politique, pour dire des choses intelligentes quand j’ai besoin de les dire.",
            u"Je m’adresse à vous, à cette génération qui n’est pas encore née.",
            u"Même quand je ne dis rien, cela fait du bruit. - 2006",
            u"Je ne parlerai ni des attentats ni des incendies, je ne parlerai que de la Corse qui travaille",
            u"Qui vient sur la grande muraille, conquiert la bravitude. - 2007",
            u"Il m'a fait l'impression de l'amant qui craint la panne. (à propos de François Bayrou qui refuse que Mme Royal monte le rencontrer à son domicile parisien entre les deux tours de la présidentielle ) - 2007"
        ]
        toubon = [
            u"Même en avion, nous serons tous dans le même bateau"
        ]
        santini = [
            u"Barre, c'est mon compagnon de chambre : il dort à côté de moi à l'Assemblée.",
            u"Saint Louis rendait la justice sous un chêne. Pierre Arpaillange la rend comme un gland",
            u"Decourtray n'a rien compris au préservatif. La preuve, il le met à l'index",
            u"Alain Juppé voulait un gouvernement ramassé, il n'est pas loin de l'avoir. - 1996",
            u"Je me demande si l'on n'en a pas trop fait pour les obsèques de François Mitterrand. Je ne me souviens pas qu'on en ait fait autant pour Giscard. (Note: Giscard est toujours vivant)"
        ]
        sarkozy = [
            u"Je ne suis candidat à rien. - 2005",
            u"Travailler plus pour gagner plus. - 2007"
        ]
        seguin = [
            u"En 1974, les Français voulaient un jeune : ils ont eu Giscard. En 1995, ils voudront un vieux : ils auront Giscard",
            u"Avec Delors, les socialistes passent de Léon Blum à Léon XIII"
        ]
        strausskahn = [
            u"C’est l’union d’un postier et d’une timbrée. (à propos de l’alliance LO-LCR) - 2004"
        ]
        tapie = [
            u"J’ai menti, mais c’était de bonne foi."
        ]
        valls = [
            u"J'étais partisan du non, mais face à la montée du non, je vote oui. - 2005 "
        ]
        veil = [
            u"Il n'y a rien de plus ennuyeux qu’une réunion électorale. Un jour, je me suis endormie pendant mon propre discours."
        ]
        villepin = [
            u"Le Villepin nouveau sera gouleyant, fort en bouche et il aura de la cuisse. - 2010",
            u"C’est un combat essentiel que celui de la laïcité, il a causé, Dieu le sait, beaucoup de morts dans notre pays. - 7 Fécrier 2008",
            u"Le pétrole est une ressource inépuisable qui va se faire de plus en plus rare. - 2006",
            u"J'écoute ceux qui manifestent mais j'écoute aussi ceux qui ne manifestent pas. - 2006",
            u"Ils vont s'apercevoir que je suis assez con pour aller jusqu'au bout. - 2006"
        ]
        villier = [
            u"Si elle s’appelait République, Ségolène ne séduirait pas nos électeurs (A propos de Ségolène Royal)",
            u"Docteur Sarko et Doc Gynéco, c'est la com' et la came. (concernant le soutien du rappeur à la candidature de Nicolas Sarkozy) - 2006",
            u"Quand on va m'entendre et que l'on va me voir, ça va se voir et ça va s'entendre. - 2007"
        ]
        wauquiez = [
            u"Il n’a pas fallu trente-cinq heures à Martine Aubry pour virer sa cuti sur Georges Frêche.",
            u"Il n’a pas fallu 35 heures à Martine Aubry pour virer sa cuti sur Georges Frêche"
        ]
        yade = [
            u"Je me retrouve avec la journée des droits de l’homme sur les bras et Khadafi sur le tarmac. - 2008"
        ]
        yamgnane = [
            u"[Je suis un] Breton d'après la marée noire"
        ]
        bdd = [
            {'auteur':"Christine Albanel"           ,       'citation':albanel      ,       'bind':"albanel"    },
            {'auteur':"Michèle Alliot-Marie"        ,       'citation':alliotmarie  ,       'bind':"alliotmarie"},
            {'auteur':"Fadela Amara"                ,       'citation':amara        ,       'bind':"amara"      },
            {'auteur':"Pierre Arpaillange"          ,       'citation':arpaillange  ,       'bind':"arpaillange"},
            {'auteur':"Nathalie Arthaud"            ,       'citation':arthaud      ,       'bind':"arthaud"    },
            {'auteur':"Jean Arthuis"                ,       'citation':arthuis      ,       'bind':"arthuis"    },
            {'auteur':"Guillaume Bachelay"          ,       'citation':bachelay     ,       'bind':"bachelay"   },
            {'auteur':"Roselyne Bachelot-Narquin"   ,       'citation':bachelot     ,       'bind':"bachelot"   },
            {'auteur':"Patrick Balkany"             ,       'citation':balkany      ,       'bind':"balkany"    },
            {'auteur':"Michel Barnier"              ,       'citation':barnier      ,       'bind':"barnier"    },
            {'auteur':"François Baroin"             ,       'citation':baroin       ,       'bind':"baroin"     },
            {'auteur':"Raymond Barre"               ,       'citation':barre        ,       'bind':"barre"      },
            {'auteur':"François Bayrou"             ,       'citation':bayrou       ,       'bind':"bayrou"     },
            {'auteur':"Xavier Bertrand"             ,       'citation':bertrand     ,       'bind':"bertrand"   },
            {'auteur':"Éric Besson"                 ,       'citation':besson       ,       'bind':"besson"     },
            {'auteur':"Jean-Louis Borlo"            ,       'citation':borloo       ,       'bind':"borloo"     },
            {'auteur':"Michel Charasse"             ,       'citation':charasse     ,       'bind':"charasse"   },
            {'auteur':"André Chassaigne"            ,       'citation':chassaigne   ,       'bind':"chassaigne" },
            {'auteur':"Luc Chatel"                  ,       'citation':chatel       ,       'bind':"chatel"     },
            {'auteur':"Jean-Pierre Chevènement"     ,       'citation':chevenement  ,       'bind':"chevenement"},
            {'auteur':"Bernadette Chirac"           ,       'citation':bchirac      ,       'bind':"bchirac"    },
            {'auteur':"Jacques Chirac"              ,       'citation':jchirac      ,       'bind':"jchirac"    },
            {'auteur':"Pascal Clément"              ,       'citation':clement      ,       'bind':"clement"    },
            {'auteur':"Gabriel Cohn-Bendit"         ,       'citation':gcohnbendit  ,       'bind':"gcohnbendit"},
            {'auteur':"Jean-François Copé"          ,       'citation':cope         ,       'bind':"cope"       },
            {'auteur':"Michel Crépeau"              ,       'citation':crepeau      ,       'bind':"crepeau"    },
            {'auteur':"Xavier Darcos"               ,       'citation':darcos       ,       'bind':"darcos"     },
            {'auteur':"Rachida Dati"                ,       'citation':dati         ,       'bind':"dati"       },
            {'auteur':"Jean-Louis Debré"            ,       'citation':debre        ,       'bind':"debre"      },
            {'auteur':"Bertrand Delanoë"            ,       'citation':delanoe      ,       'bind':"delanoe"    },
            {'auteur':"Patrick Devedjian"           ,       'citation':devedjian    ,       'bind':"devedjian"  },
            {'auteur':"Cécile Duflot"               ,       'citation':duflot       ,       'bind':"duflot"     },
            {'auteur':"Philippe Douste-Blazy"       ,       'citation':dousteblazy  ,       'bind':"dousteblazy"},
            {'auteur':"Christian Estrosi"           ,       'citation':estrosi      ,       'bind':"estrosi"    },
            {'auteur':"Laurent Fabius"              ,       'citation':fabius       ,       'bind':"fabius"     },
            {'auteur':"Edgar Faure"                 ,       'citation':faure        ,       'bind':"faure"      },
            {'auteur':"Daniel Fidelin"              ,       'citation':fidelin      ,       'bind':"fidelin"    },
            {'auteur':"François fillon"             ,       'citation':fillon       ,       'bind':"fillon"     },
            {'auteur':"Georges Frêche"              ,       'citation':freche       ,       'bind':"freche"     },
            {'auteur':"Marie-France Garaud"         ,       'citation':garaud       ,       'bind':"garaud"     },
            {'auteur':"Claude Guéant"               ,       'citation':gueant       ,       'bind':"gueant"     },
            {'auteur':"Claude Goasguen"             ,       'citation':goasguen     ,       'bind':"goasguen"   },
            {'auteur':"Jacques Godfrain"            ,       'citation':godfrain     ,       'bind':"godfrain"   },
            {'auteur':"François Goulard"            ,       'citation':goulard      ,       'bind':"goulard"    },
            {'auteur':"François Hollande"           ,       'citation':hollande     ,       'bind':"hollande"   },
            {'auteur':"Brice Hortefeux"             ,       'citation':hortefeux    ,       'bind':"hortefeux"  },
            {'auteur':"Robert Hue"                  ,       'citation':hue          ,       'bind':"hue"        },
            {'auteur':"Eva Joly"                    ,       'citation':joly         ,       'bind':"joly"       },
            {'auteur':"Alain Juppé"                 ,       'citation':juppe        ,       'bind':"juppe"      },
            {'auteur':"Bernard Kouchner"            ,       'citation':kouchner     ,       'bind':"kouchner"   },
            {'auteur':"Bernard Laporte"             ,       'citation':laporte      ,       'bind':"laporte"    },
            {'auteur':"Pierre Lellouche"            ,       'citation':lellouche    ,       'bind':"lellouche"  },
            {'auteur':"Jean-Marie Le Pen"           ,       'citation':jmlepen      ,       'bind':"jmlepen"    },
            {'auteur':"Arno Klarsfeld"              ,       'citation':klarsfeld    ,       'bind':"klarsfeld"  },
            {'auteur':"Marie-Noëlle Lienemann."     ,       'citation':lienemann    ,       'bind':"lienemann"  },
            {'auteur':"Lionnel Luca"                ,       'citation':luca         ,       'bind':"luca"       },
            {'auteur':"Georges Marchais."           ,       'citation':marchais     ,       'bind':"marchais"   },
            {'auteur':"Frédéric Mitterrand"         ,       'citation':mitterrand   ,       'bind':"mitterrand" },
            {'auteur':"Nadine Morano"               ,       'citation':morano       ,       'bind':"morano"     },
            {'auteur':"Henri Nallet"                ,       'citation':nallet       ,       'bind':"nallet"     },
            {'auteur':"Henri Nallet"                ,       'citation':nallet       ,       'bind':"nallet"     },
            {'auteur':"Nelly Olin"                  ,       'citation':olin         ,       'bind':"olin"       },
            {'auteur':"Bernard Poignant"            ,       'citation':poignant     ,       'bind':"poignant"   },
            {'auteur':"Jean-Pierre Raffarin"        ,       'citation':raffarin     ,       'bind':"raffarin"   },
            {'auteur':"Michel Rocard"               ,       'citation':rocard       ,       'bind':"rocard"     },
            {'auteur':"Josselin de Rohan"           ,       'citation':rohan        ,       'bind':"rohan"      },
            {'auteur':"Ségolène Royal"              ,       'citation':royal        ,       'bind':"royal"      },
            {'auteur':"Jacques Toubon"              ,       'citation':toubon       ,       'bind':"toubon"     },
            {'auteur':"Philippe de Villiers"        ,       'citation':villier      ,       'bind':"villier"    },
            {'auteur':"André Santini"               ,       'citation':santini      ,       'bind':"santini"    },
            {'auteur':"Dominique Strauss-Kahn"      ,       'citation':strausskahn  ,       'bind':"strausskahn"},
            {'auteur':"Bernard Tapie"               ,       'citation':tapie        ,       'bind':"tapie"      },
            {'auteur':"Nicolas Sarkozy"             ,       'citation':sarkozy      ,       'bind':"sarkozy"    },
            {'auteur':"Philippe Séguin"             ,       'citation':seguin       ,       'bind':"seguin"     },
            {'auteur':"Manuel Valls"                ,       'citation':valls        ,       'bind':"valls"      },
            {'auteur':"Simone Veil"                 ,       'citation':veil         ,       'bind':"veil"       },
            {'auteur':"Dominique de Villepin"       ,       'citation':villepin     ,       'bind':"villepin"   },
            {'auteur':"Laurent Wauquiez"            ,       'citation':wauquiez     ,       'bind':"wauquiez"   },
            {'auteur':"Rama Yade"                   ,       'citation':yade         ,       'bind':"yade"       },
            {'auteur':"Kofi Yamgnane"               ,       'citation':yamgnane     ,       'bind':"yamgnane"   }
        ]
    return bdd

# MAIN
#BUGS
# Switching back and forth between modes messes things up
debug=False
#~ debug=True

# Globals
bg_color                    = "#00000000"
frame_color                 = "#00000000"
background_image_visible    = False
bg_image                    = "bg/glass.svg"
quote_font                  = "Serif Bold Italic 12"
quote_font_color            = "#00FE00"
quote2_font_color           = "#000000"
qauthor_font                = "Sans Bold 11"
qauthor_font_color          = "#FEA900"
qauthor2_font_color         = "#000000"
size                        = 300
interval                    = "hourly"
heures                      = 1
minutes                     = 0
secondes                    = 0
t0                          = MyDate( time.time )
t1                          = t0.dup()
t                           = MyDate( (heures, minutes, secondes) )
citation_type               = "celebrity"

#watch time
initialize_timer(  )
time.bind("time", refresh_quote)
