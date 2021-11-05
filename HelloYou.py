import random

def C2c():
    print("Een paar weken later kom je aan in Rotterdam. Je wilt hier een leven starten hoe begin je?")
    print("A: Ga werken op een vissers boot")
    print("B: Begin een Koreaanse snoep winkel")
    inp =input()
    if inp == "A":
        print("Na 2 jaar ga je vier dagen per week de zee op met jee eigen vissersboot, Je woont in een koophuis samen met 4 vrienden. Het leven is goed.")
    if inp == "B":
        print("Na 2 jaar ben je een van de meer succesvolle snoepwinkels in Rotterdam. Je woont met je vriend en een hond in een koophuis in de binnenstad.")

def C1c():
    print("Je bent op een vliegveld en ziet een klein vliegtuigje staan, je gaat er heen om te kijken of het los is, iemand ziet je en vraagt wat je doet, wat doe je?")
    print("A: Zeg dat je op vakantie wilt naar Nederland.")
    print("B: Begin wild te schreeuwen en weg te rennen.")
    inp =input()
    if inp == "A":
        print("De persoon zegt dat hij een nicht heeft wonen in Nederland die hij graag nog een keer wil bezoeken. Hij wilt je dus graag naar Nederland brengen.")
        C2c()
    if inp == "B":
        print("Je begint wild te schreeuwen en rennen, iedereen kijkt je raar aan. Nadat je weg rent hoor je politie aan komen. Zonder de denken ren je weg, maar ze weten je te arresteren. Je word teruggestuurd naar Noord Korea. Je straf is de dood.")
        end()

def C2b():
    print("Je vind na twee dagen iemand die je verder naar Duitsland wilt mee nemen. Via daar kom je makkelijk in Nederland. Uiteindelijk kom je aan in 's-Hertogenbosch. Je wilt hier een leven starten, wat ga je doen?")
    print("A: Zoek een fabriek baan")
    print("B: Begin een marktkraam")
    inp =input()
    if inp == "A":
        print("2 jaar later heb je een redelijke baan bij een Verkade fabriek. Je woont in een huurhuis samen met je vriendin. Het leven is goed.")
        end()
    if inp == "B":
        print("2 jaar later sta je elke dag op de markt producten voor honden te verkopen, je woont samen met drie honden en een kat in een huurhuis in de binnenstad. Het leven is goed.")
        end()

def C1b():
    print("Je vind al snel een groep vrienden die naar Kazachstan aan het reizen zijn die je mee willen nemen. Ze zetten je dichtbij de grens van Rusland af, wat doe je?")
    print("	A: Ga verder liften.")
    print("B: Steek het bos door naar een veiligere drukkere weg.")
    inp =input()
    if inp == "A":
        C2b()
    if inp == "B":
        print("Je raakt verdwaalt in het bos en moet zien te overleven. Gelukkig heb je vroeger op school survival skills geleerd. Na een week ben je nog steeds verdwaalt, maar eigenlijk vind je het wel rustgevend. Je besluit de rest van je leven een rustgevend maar eenzaam leven te leiden in het bos.")
        end()


def C2a():
    print("Ze snapt waarom en heeft medelijden, ze neemt je mee naar Nederland. Uiteindelijk kom je aan in de stad Groningen, je wilt hier een leven starten, wat ga je doen? ")
    print("A: Zoek werk op het land")
    print("B: probeer een studie te zoeken in de stad")
    inp =input()
    if inp == "A":
        print("2 jaar later woon je in een schattig huisje in een dorp, je werkt 5 dagen in de tulpen en op zondag ga je tennissen met je dorps vrienden. Het leven is goed. ")
        end()
    if inp == "B":
        print("2 jaar later is het helaas niet gelukt om een studie te doen, maar je bijbaantje is gegroeid tot een redelijke baan in de supermarkt. Je woont in een appartement samen met je vriend. Het leven is goed.")
        end()


def C1a():
    print("Je bent bij een transport bedrijf en je vind aan vrachtwagen die naar Nederland gaat, je verstopt je achterin. Na een paar dagen checkt de chauffeuse haar vracht, ze ziet je, wat doe je?")
    print("A: Leg uit waarom je aan het versteken bent.")
    print("B: Begin met vechten en probeer haar vrachtwagen te stelen.")
    inp =input()
    if inp == "A":
        C2a()
    if inp == "B":
        print("Je springt op haar af, maar ze ontwijkt je. Je ligt midden op de weg en je word overgereden.")
        end()


def China():
    print("Je bent in China, als er iemand achter komt dat je uit Noord Korea komt dan word je opgepakt en teruggestuurd, je hebt gehoord dat Nederland een mooi land is voor vluchtelingen dus je wilt daar graag heen, wat ga je doen?")
    print("A: Probeer mee te versteken met een vrachtwagen")
    print("B: Probeer te liften")
    print("C: Steel een vliegtuig")
    inp =input()
    if inp == "A":
        C1a()
    if inp == "B":
        C1b()
    if inp == "C":
        C1c()


def B4g():
    print("Ze sturen je weg, probeer je het nog een keer?")
    print("A: Ja")
    print("B: Nee")
    inp =input()
    if inp == "A":
        if random.randint(0,100) < 21:
            print("Ze zijn er helemaal klaar mee en pakken je op")
            B4a()
        else:
            B4g()
    if inp == "B":
        B3c()

def B4f():
    print("Je ziet wat mensen even bij hun koffer weglopen, je pakt al hun spullen eruit en gooit het in een prullenbak. Je gaat in de koffer zitten, je weet dat je zo door een scanner gaat, wat doe je?")
    print("A: doe alsof je een hoop kleding bent.")
    print("B: wikkel jezelf in 2 rollen aluminium folie die je toevallig bij je hebt.")
    print("C. Consumeer de drugs die je gevonden hebt in een geheime laag in de koffer.")
    inp =input()
    if inp == "A":
        print("Je doet zo hard mogelijk je best om een hoop kleding te zijn, helaas ziet de scanner toch wel dat je geen hoop kleding bent. Iemand doet de koffer open en trekt je eruit. Een grote chagrijnige bewaker besluit om je op je achterhoofd met een wapen stok te slaan. Je word een week later wakker in het ziekenhuis, je leeft de rest van je leven in een tehuis voor invaliden.")
        end()
    if inp == "B":
        B5d()
    if inp == "C":
        print("Je ziet allemaal leuke kleurtjes en even later word alles wazig. Je word de volgende dag wakker in China.")
        China()

def B5d():
    print("De scanner merkt dat er iets mis is, iemand doet de koffer open en schrikt van je, wat doe je?")
    print("A: Doe alsof je een alienmummie bent")
    print("B: Ren weg")
    inp =input()
    if inp == "A":
        print("Iedereen is doodsbang voor je en rent weg, je loopt zo door naar het vliegtuig. Je land dezelfde dag nog in China.")
        China()
    if inp == "B":
        print("Je rent weg, maar een bewaker taserd je. Helaas is het wapen defect en blijft je voor een uur lang tasen. Je overlijd aan shock.")
        end()

def B5c():
    print("Hij vertelt je dat je doormoet zetten en moet gaan voor wat je wilt. Je voelt je geïnspireerd en je gaat er voor! Wat doe je?")
    print("A: forceer jezelf naar een vliegtuig.")
    print("B: Denk nog even goed na wat je gaat doen.")
    inp =input()
    if inp == "A":
        print("Je rent door de douane heen en je word gelijk getaserd en valt op de grond, na een paar schoppen tegen je hoofd val je bewusteloos en je word niet meer wakker.")
        end()
    if inp == "B":
        B3c()


def B4e():
    print("Je ziet iemand zijn tas neerzetten en even naar de wc lopen, je probeert zo snel en discreet mogelijk door de tas te gaan op zoek naar een paspoort en ticket. Gelukkig vind je ze! Je gaat naar de douane en laat het zien. Bij het checken van de paspoort word je weggestuurd, omdat het persoon op het paspoort een ander geslacht had dan jouw. Als je terug loopt zie je een oude net geklede man die moeite heeft met zijn veters strikken, wat doe je?")
    print("A: Help de man")
    print("B: beroof de man")
    print("C: vraag hem voor emotionele support")
    inp =input()
    if inp == "A":
        print("Je helpt de man en hij bedankt je. Hij stelt zich voor als Wen Wei Po. De oom van Kim Jong-un! Je vertelt wat je hier doet en besluit je mee te nemen, je hoeft nergens een paspoort of ticket te laten zien en een paar uur later land je in China. Jullie gaan daarna jullie eigen weg.")
        China()    
    if inp == "B":
        print("Terwijl hij zijn veters aan het strikken is steel je zijn portemonnee, je rent ermee weg, terwijl achter je iets word geschreeuwd. Even later word je getackeld door wat soldaten.")
        B4a()
    if inp == "C":
        B5c()


def B3c():
    print("Je bent op het vliegveld. Hoe ga je illegaal met een vliegtuig mee?")
    print("A: Steel een paspoort en ticket")
    print("B: Smokkel mee in iemands koffer.")
    print("C: Loop gewoon naar binnen.")
    inp =input()
    if inp == "A":
        B4e()
    if inp == "B":
        B4f()
    if inp == "C":
        B4g()


def B4d():
    print("Hij is een beetje verbaasd en vertelt je waar je de passagiers verdieping kan vinden, waar ga je heen? ")
    print("A: Ga naar de verdieping met voertuigen.")
    print("B: ga naar de passagiers verdieping.")
    print("Ga terug naar waar je zat.")
    inp =input()
    if inp == "A":
        B5a()
    if inp == "B":
        print("Je gaat naar de passagiers verdieping en weet de ticket controle te vermijden. Je komt even later aan in China.")
        China()
    if inp == "C":
        print("Het schip komt aan en je weet ongezien naar buiten te gaan, je bevind je nu in China.")
        China()
def B6b():
    print("Je bent in de bewaker ruimte en ziet een computer, wat doe je?")
    print("A: Wacht tot het schip aankomt.")
    print("B: probeer de volgende cours te veranderen naar een land waar je niet gezocht word.")
    inp =input()
    if inp == "A":
        print("Het schip komt uiteindelijk aan in China, je gaat naar buiten en doet je normale kleding weer aan.")
        China()
    if inp == "B":
        print("Je probeert de cours naar Nederland te veranderen en een dag later vertrekt het schip. Je verbergt je in een kombuis en komt alleen naar buiten om eten en drinken te halen.")
        C2c()


def B5b():
    print("Je doet de kleding van de bewaker aan en je pakt zijn sleutels af, wat doe je?")
    print("A: Ga naar de passagiers ruimte en wacht tot het schip aankomt.")
    print("B: Ga naar de bewaker ruimte en wacht tot het schip aan komt.")
    inp =input()
    if inp == "A":
        print("Het schip komt uiteindelijk aan in China, je gaat naar buiten en doet je normale kleding weer aan.")
        China()
    if inp == "B":
        B6b()
def B4c():
    print("Je raakt de bewaker recht op zijn achterhoofd, hij valt knock-out, wat doe je?")
    print("A: Ga naar de verdieping met voertuigen.")
    print("B: Ga naar de kantine voor een lekkere snack.")
    print("C: Doe de kleding van de bewaker aan.")
    inp =input()
    if inp == "A":
        B5a()
    if inp == "B":
        print("Je gaat naar de kantine en vind een drie chocolade taarten, na een stukje realiseer je pas hoe veel honger je hebt, je neemt nog wat. Even later realiseer je dat je ze alle drie hebt opgegeten. Je word ziek en begint over te geven, even later kom je aan in China en word je naar het ziekenhuis gebracht. De volgende dag ben je weer beter, maar inmiddels hebben ze gecheckt wie je bent en je word terug naar Noord-Korea gestuurd. Je bent weer thuis, wat doe je?")
        X1a()
    if inp == "C":
        B5b()

def B6a():
    print("Je vind een open auto en zodra het schip aankomt rij je naar buiten, je bevind je nu in China met een auto, maar de benzine is bijna op wat doe je?")
    print("A: Zoek iemand om het aan te verkopen.")
    print("B: Laat de auto achter.")
    inp =input()
    if inp == "A":
        print("Je verkoopt de auto voor 95000 Chinese renminbi, maar je komt er later achter dat het duidelijk nep geld is, je hebt er niks aan.")
        China()
    if inp == "B":
        print("Je laat de auto achter op een parkeer terrein.")
        China()


def B5a():
    print("Je bent nu in het ruim met auto’s, wat doe je?")
    print("A: Zoek naar een open auto.")
    print("B: verstop jezelf achterin een pick-up truck.")
    print("C: Ga naar de kantine voor een lekkere snack.")
    inp =input()
    if inp == "A":
        B6a()
    if inp == "B":
        print("Zodra het schip aankomt rijd de auto naar buiten en je springt er later vanaf, je bent nu in China.")
        China()    
    if inp == "C":
        print("Je gaat naar de kantine en vind drie chocolade taarten, na een stukje realiseer je pas hoe veel honger je hebt, je neemt nog wat. Even later realiseer je dat je ze alle drie hebt opgegeten. Je word ziek en begint over te geven, even later kom je aan in China en word je naar het ziekenhuis gebracht. De volgende dag ben je weer beter, maar inmiddels hebben ze gecheckt wie je bent en je word terug naar Noord-Korea gestuurd. Je bent weer thuis, wat doe je?")
        X1a()

def B4b():
    print("De bewaker ziet je niet en loopt door, wat doe je?")
    print("A: Blijf zitten.")
    print("B: Ga naar de verdieping met voertuigen.")
    print("C: Ga naar de kantine voor een lekkere snack.")
    inp =input()
    if inp == "A":
        print("Het schip komt aan en je weet ongezien naar buiten te gaan, je bevind je nu in China.")
        China()
    if inp == "B":
        B5a()
    if inp == "C":
        print("Je gaat naar de kantine en vind drie chocolade taarten, na een stukje realiseer je pas hoe veel honger je hebt, je neemt nog wat. Even later realiseer je dat je ze alle drie hebt opgegeten. Je word ziek en begint over te geven, even later kom je aan in China en word je naar het ziekenhuis gebracht. De volgende dag ben je weer beter, maar inmiddels hebben ze gecheckt wie je bent en je word terug naar Noord-Korea gestuurd. Je bent weer thuis, wat doe je?")
        X1a()


def B3b():
    print("Het lukt om jezelf op het schip te versteken, maar er is een bewaker die het ruim aan het controleren is, wat doe je?")
    print("A: Blijf zo stil mogelijk zitten.")
    print("B: Gooi een steen naar zijn hoofd.")
    print("C: Loop naar hem toe en zeg dat je de weg kwijt bent.")
    inp =input()
    if inp == "A":
        B4b()
    if inp == "B":
        B4c()
    if inp == "C":
        B4d()


def B4a():
    print("Ze brengen je naar de gevangenis, wat doe je?")
    print("A: Probeer vrienden te maken.")
    print("B: Wacht tot je straf om is.")
    print("C: Probeer te ontsnappen.")
    inp =input()
    if inp == "A":
        print("Het lukt je om vrienden te maken en je ontsnapt 2 weken later naar China. Iedereen gaat zijn eigen weg.")
        China()
    if inp == "B":
        print("Je zit voor de rest van je leven in de gevangenis.")
        end()
    if inp == "C":
        print("Je weet een schroevendraaier te vinden en je gaat de ventilatie schacht in, maar je valt erdoorheen, precies in de kantine van de bewakers. Je word de volgende dag geëxecuteerd.")
        end()



def B3a():
    print("Je loopt zo stiekem mogelijk bij de grens, maar er word een groot licht op je geschenen. Wat doe je?")
    print("A: Je rent zo snel mogelijk naar de grens.")
    print("B: Je geeft je over.")
    print("C: je verstopt je in wat bosjes.")
    inp =input()
    if inp == "A":
        print("Je word voor de grens geraakt door een kogel en overlijd.")
        end()
    if inp == "B":
        B4a()
    if inp == "C":
        print("Even later word je gepakt door een hond en je word geëxecuteerd.")
        end()


def B2a():
    print("Je gaat weg, waar ga je heen en hoe?")
    print("A: Je gaat lopend de grens over naar Zuid korea.")
    print("B: Je gaat als verstekeling met een vrachtschip mee.")
    print("C: Je gaat illegaal met het vliegtuig.")
    inp =input()
    if inp == "A":
        B3a()
    if inp == "B":
        B3b()
    if inp == "C":
        B3c()


def X1a():
    print("Wat ga je doen?")
    print("A: Blijf in Noord Korea")
    print("B: Ga weg")
    inp = input()
    if inp == "A":
        if random.randint(0,100) < 21:
            print("Een maand later overlijd je wegens politie geweld, omdat je onbewust bij een groep protestanten stond.")
            end()
        else:
            print("Na een maand ga je opnieuw nadenken.")
            X1a()
    if inp == "B":
        B2a()

print("Je heet Kim Seo-yeon, je bent 32 jaar en je woont in Noord Korea. Recent heb je stiekem op tijdens je werk op de enigste computer met internet gekeken. Je bent erachter gekomen hoeveel beter mensen het in het buitenland hebben. Je wilt weg.")

X1a()

def end():
    print("Dit is het einde!")
    print("Wil je opnieuw?")
    print("typ: ja of nee")
    inp = input()
    if inp == "ja":
        X1a()
    if inp == "nee":
        print("Doei.")
