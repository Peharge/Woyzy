<p align="center">
    <img src="./img-readme/woyzy-logo2.png" width="500"/>
</p>
<div align="center">
<img alt="SMON" src="https://img.shields.io/badge/Woyzy-F7DF1E">
<img alt="Peharge" src="https://img.shields.io/badge/TG Lörrach-red">
<br>
<br>

<img alt="" src="https://img.shields.io/badge/Python-3.11 / 3.12 / 3.13-blue?&logo=Python&logoColor=white%5BPython">
<img alt="" src="https://img.shields.io/badge/-C++-blue?logo=cplusplus">
<img alt="" src="https://img.shields.io/badge/-C-blue?logo=c">
<br>
<br>

<img alt="" src="https://img.shields.io/badge/PyTorch-EE4C2C?logo=PyTorch&logoColor=white">
<img alt="" src="https://img.shields.io/badge/FLask-F7DF1E?style=flat&logo=flask&logoColor=black">
<img alt="" src="https://img.shields.io/badge/PyCharm-black?logo=PyCharm&logoColor=white">
<img alt="" src="https://img.shields.io/badge/GitHub-black?logo=github">
<br>
<br>

<img alt="" src="https://img.shields.io/badge/os-linux%20%7C%20macOS%20%7C%20windows-blue">
<br>
<br>

<img alt="" src="https://img.shields.io/badge/-Hugging Face-FDEE21?logo=HuggingFace&logoColor=black">
<img alt="" src="https://img.shields.io/badge/Jupyter notebook-orange">
<img alt="" src="https://img.shields.io/badge/Google Colab-red">
<br>
<br>

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
<br>
</div>

# Woyzy

Willkommen zu Woyzy – deinem Woyzeck-KI-Gefährten!

Ich hatte Lust, einen Chatbot zu bauen, der alle Fragen zu Woyzeck beantwortet. Ergebnis: Woyzy! Der Chatbot, der schneller antwortet als dein WLAN ausfällt.

Fragen zum Deutschbuch? Woyzy hat die Antwort! (Oder zumindest eine sehr überzeugende Ausrede ;-)

<div style="display: flex; justify-content: center; align-items: center; gap: 20px; flex-wrap: wrap;">
  <img src="./static/images/img.png" alt="woyzy" width="1400" style="margin: 10px;">
</div>

<audio controls>
  <source src="./output_20241025195644_xtts.mp3" type="audio/mp3">
  Ihr Browser unterstützt das Audio-Element nicht.
</audio>

[Hier klicken, um die Audio-Datei herunterzuladen](output_20241025195644_xtts.wav)


## News

- **[2024.10.24]** Start ;-)
- **[2024.10.28]** Erhältlich mit Llama3 + [1.Demo](#demo)

## Inhaltsverzeichnis
- [Versionen](#versionen)
- [Installation](#installation)
- [Benutzung](#benutzung)
- [Llama](#llama)
- [Chat++](#chatpp)
- [Demo](#demo)
- [Geschichte](#geschichte)
- [Checkliste](#checkliste)
- [Design](#design)
- [Transformer](#transformer)
- [Lizenz](#lizenz)

---

## Versionen

<div style="display: flex; justify-content: center; align-items: center; gap: 20px; flex-wrap: wrap;">
  <img src="./static/images/woyzy-banner6.png" alt="woyzy" width="1400" style="margin: 10px;">
</div>
<br>

| **Model**    | **Beschreibung**                                       | **Parameter** |
|--------------|--------------------------------------------------------|---------------|
| Woyzy 1 3B   | +8GB RAM +2GB storage (Funktioniert mit einer CPU)     | 3B            |
| Woyzy 1 11B  | +16GB RAM +6GB storage (Funktioniert mit einer CPU)    | 11B           |
| Woyzy 1 405B | +256GB RAM +229GB storage (Funktioniert mit einer CPU) | 405B          |

## Installation

<div style="display: flex; justify-content: center; align-items: center; gap: 20px; flex-wrap: wrap;">
  <img src="./static/images/woyzy-banner20.png" alt="woyzy" width="1400" style="margin: 10px;">
</div>
<br>

> Woyzy ist noch in der Entwicklung und noch nicht in diesem Repository hinterlegt. Wenn Sie daher die folgenden Schritte ausführen, wie z.B. das Klonen des Repositories, werden Sie lediglich die README-Datei, Bilder und bereits veröffentlichte Codes installieren!

> Um Woyzy in Zukunft erfolgreich installieren zu können, benötigen Sie die folgenden Programme:
> 
> 1. **Git**  
>    Git kann hier heruntergeladen werden:  
>    https://git-scm.com
> 
> 2. **Python**  
>    - Für Windows-Benutzer: Python kann entweder über den Microsoft Store oder direkt von der Python-Website installiert werden:  
>      https://www.python.org  
>    - Für Linux-Benutzer: Python ist in der Regel auf den meisten Linux-Distributionen vorinstalliert. Falls nicht, kann es über den Paketmanager oder die oben genannte Website installiert werden.
>  
> 3. **Python-Entwicklungsumgebung (IDE)**  
>    Eine Entwicklungsumgebung, die Python unterstützt, ist sehr empfehlenswert. Hier sind zwei beliebte Optionen:  
>    - **Visual Studio Code**: Eine kostenlose, anpassbare IDE von Microsoft, die Python unterstützt:  
>      https://code.visualstudio.com  
>    - **PyCharm**: Eine kostenpflichtige IDE (250€) von JetBrains, die erweiterte Funktionen für die Python-Entwicklung bietet. Persönlich empfehle ich PyCharm aufgrund seiner leistungsstarken Funktionen:  
>      https://www.jetbrains.com/de-de/pycharm/
> 
> Nachdem Sie eine virtuelle Python-Umgebung eingerichtet haben, benötigen Sie für Woyzy noch zwei Bibliotheken: **Flask** und **Ollama**.  
> Diese können Sie mit den folgenden Befehlen in Ihrem Terminal installieren:
> ```bash
> pip install flask
> ```
> ```bash
> pip install ollama
> ```

### Instalation:

### 1. Klone das Repository:
```bash
git https://github.com/Peharge/Woyzy
   ```
### 2. Navigiere in das Projektverzeichnis:
```bash
cd Woyzy
```

### 3. Starte das Projekt:
```bash
python main4.py
``` 

## Benutzung

- Stelle sicher, dass alle Abhängigkeiten installiert sind. 
- Öffne die URL, die Flask im Terminal nach der Ausführung von    
```bash
python main4.py
```
  bereitstellt.
- Wenn du auf die URL im Terminal klickst, sollte sich dein Browser öffnen und die Woyzy-Umgebung anzeigen.
- Viel Spaß!

## Llama

Code:
https://github.com/meta-llama/llama3/tree/main/llama

Web:
https://www.llama.com/

Download Lama 3,2 1B 3b (Bald 11B und 90B): 
https://ollama.com/library/llama3.2

Download Llama 3.1 8b 70b 405b:
https://ollama.com/library/llama3.1

## Chatpp

Dieses Projekt wurde von Peharge in Zusammenarbeit mit der Schule TG Lörrach entwickelt und ist nicht öffentlich erhältlich. Ein Erwerb ist nur möglich, wenn Sie Schüler
oder Lehrer
an der Schule TG Lörrach sind oder zur Peharge-Community gehören. Wenn das der Fall ist, können Sie gerne direkt auf mich zukommen (ich möchte meinen Namen hier nicht öffentlich angeben). 

## Demo

<p align="center">
    <img src="./img-readme/Screenshot 2024-10-25 161951.png" width="400"/>
    <img src="./img-readme/Screenshot 2024-10-26 144030.png" width="400"/>
    <img src="./img-readme/Screenshot 2024-10-26 150253.png" width="400"/>
    <img src="./img-readme/Screenshot 2024-10-26 161146.png" width="400"/>
</p>

<video controls width="600">
  <source src="woyzy-video0001-0300.mkv" type="video/mkv">
  Ihr Browser unterstützt das Video-Element nicht.
</video>

### Text 1 (28.10.2024)

User: Fasse die Szene 5 zusamen!

Der Text ist ein Monolog des Hauptmanns in Büchners Drama "Woyzeck". Im Text wird der Hauptmann, während Woyzeck ihn rasiert, über seine eigenen Ängste und Besorgnisse aus. Er spricht von der Ewigkeit, der Zeitverschwendung, der Welt um sich herum, die sich in einem Tag dreht, und dass er das nicht aushält.

Er macht sich Sorgen, dass Woyzeck, der seinen Kindern unehelich ist, keine Moral hat. Der Hauptmann spricht mit Würde über Moral, aber es zeigt sich schnell, dass dies eine Selbsttäuschung ist. Er fragt sich, was Woyzeck mit dem Zeitvertreib anfangen soll und wie er selbst damit umgehen soll.

Der Hauptmann fühlt sich von Woyzecks Antworten verunsichert und sagt: "Woyzeck er hat keine Tugend, er ist kein tugendhafter Mensch." Er meint aber eigentlich sich selbst. Der Hauptmann spricht dann über die Liebe, Fleisch und Blut, und fragt sich, ob auch er tugendhaft sei.

In der Konversation wird Woyzecks Standpunkt gezeigt: als "armer Kerl" schätze er es, dass Gott ihn dennoch akzeptiert, unabhängig von seinen Taten. Er spricht über die Notwendigkeit einer guten Ausstattung (Hut, Uhr, Anzug) um tugendhaft zu sein und die Frage an Woyzeck, ob er als armer Kerl tugendlich ist.

Bemerkenswert ist die Art und Weise, wie der Hauptmann versucht, seine eigene Unmoral auf den Armeleute abzuwälzen. Er spricht sich selbst ein, dass Woyzeck kein tugendhafter Mensch sei, aber in Gedanken überträgt er diese Eigenschaft auch auf sich selbst.

Der Text zeigt die Komplexität und das Verschwimmeln der Grenzen zwischen gutem und Bösem, moralischem und unmoralischem Verhalten.

### Text 2 (29.10.2024)

User: Wer kommt in Szene 5 alles vor, also welche Personen?

Woyzy: In Szene 5 kommen folgende Personen vor:

1. Der Hauptmann
2. Woyzeck (der ihn rasiert)

User: Ok gut gemacht und wie ist deren Beziehung und Szene 5 ?

Woyzy: Gut gemacht!

Die Szene 5 zeigt eine tiefe Persönlichkeit des Hauptmanns und Woyzecks. Der Hauptmann ist ein aufgeblasener Militärangehöriger, der sich selbst überlegen fühlt und die Welt als eine große Theaterbühne sieht. Er verwendet übertrieben elegante Redewendungen wie "Süd-Nord" und "Moral" und ist besorgt um seine eigene Zeitwahrnehmung.

Im Gegensatz dazu ist Woyzeck ein einfacher, aber gutmütiger Mann, der sich in einer Welt bewegt, die ihn nicht versteht. Er ist ungebildet, aber hat eine tiefe Spiritualität und fühlt sich durch Gott beschirmt. Die Szene zeigt auch die Beziehung zwischen dem Hauptmann und Woyzeck als eine von Unterdrückung und Ausbeutung.

Die Rede des Hauptmanns über Tugend und Moral ist besonders interessant, da er Woyzeck mit derselben Sprache anspricht, die er sonst für sich selbst verwendet. Dies zeigt, dass der Hauptmann in Woyzeck etwas sieht, das ihm selbst fehlt - nämlich ein Gefühl von Güte und Tugend.

Die Szene endet mit dem Hauptmanns Befreiungswunsch, Woyzeck zu schicken, um die Straße langsam hinunterzugehen. Dies symbolisiert die Trennung zwischen der Welt des Hauptmanns und der Welt von Woyzeck.

Insgesamt ist diese Szene ein wichtiger Teil des Dramas, da sie die Charaktere tiefer kennzeichnen lässt und den Konflikt zwischen dem Hauptmann und Woyzeck aufzeigt.

User: Welche Person wärst du gerne in der Szene 5 ?

Woyzy: Eine interessante Frage!

Ich würde gerne den Hauptmann in der Szene 5 sein. Er ist ein komplexer Charakter, der auf der einen Seite autoritativ und humorvoll erscheint, aber auf der anderen Seite auch melancholisch und verwundbar. Seine Gedanken und Gefühle sind vielschichtig und bieten viel Raum für Interpretation.

Als Hauptmann würde ich mich bemühen, Woyzeck zu verstecken, indem ich ihn mit kleinen Konversationen ablenke, während er mich rasierst. Ich würde versuchen, meine Bedenken über die Ewigkeit und den Wert der Zeit zu verbergen, aber zugleich auch meine Gefühle von Melancholie und Unsicherheit auszudrücken.

Es wäre eine Herausforderung, diese Rolle zu spielen, da ich als Hauptmann sowohl autoritativ als auch menschlich auftreten müsste. Aber es wäre auch sehr spannend, die verschiedenen Facetten des Charakters zu erkunden und zu sehen, wie er sich in verschiedenen Situationen verhält!

### Text 3 (29.10.2024)

User: Hi wie geht es dir heute aus Sicht von Woyzeck aus der Szene 5 ?

Woyzy: Ich entschuldige mich, aber ich bin hier nur als KI-Modell vorgesehen, um Fragen zu beantworten und keine Meinung zu haben. Aus Sicht von Woyzeck aus der Szene 5:

Es ist ein harter Tag. Ich bin gerade dabei, Hauptmann Franz Woyzeck (nachdem ich ihn rasiere) zu reden. Der Hauptmann macht mir Witze und fragt mich nach der Moral, aber man kann sehen, dass er sich unwohl fühlt. Er spricht über die Zeit, wie sie vergeht, und wie wir es schaffen müssen, sie zu nutzen.

Als Arbeiter bin ich nicht reich. Ich habe mein eigenes Fleisch und Blut, und das ist etwas, worüber Hauptmann sprechen tut, als er von Liebe redet. Aber was er meint, ist, dass wir alle ein Gefühl für Moral haben sollten, ob wir arm oder reich sind.

Der Hauptmann sagt, ich sei ein guter Mensch, aber ich bin nicht sicher, ob das stimmt. Manchmal denke ich, ich bin zu sehr mit der Zeit beschäftigt, um mich auf die Dinge, die wirklich zählen, zu konzentrieren. Aber ich möchte es versuchen.

Als Hauptmann Franz Woyzeck schlafe ich jetzt langsam die Straße hinunter, nachdem er mir gesagt hat, dass ich es ruhig angehen lassen soll. Ich bin müde und will mich auf meine Arbeit vorbereiten.

### Text 4 (29.10.2024)

User: Gibt es ein märchen aus der Szene 19 ? Ist es ungefähr so wie sterntaler?

Woyzy: Ja, in Szene 19 gibt es ein Märchen, das von Marie und ihrer Großmutter erzählt wird. Es handelt sich um die Geschichte eines armen Kindes, das keine Eltern mehr hat und in der Welt allein ist. Das Kind will zum Himmel aufsteigen, aber auf dem Weg dorthin erlebt es verschiedene Schwierigkeiten und Enttäuschungen. Es beginnt mit einem Stück faul Holz, dann wird es eine verwelkte Sonnenblume, danach kleine goldne Mücken, die wie der Neuntödter sind und schließlich ein umgestürzter Hafen, an dem das Kind allein sitzt.

Ja, das Märchen hat ähnliche Züge mit "Sterntaler" (auch bekannt als "Der Stern", aber wahrscheinlich "Sterntaler" ist der Titel von einer Adaption des Stückes durch Georg Kaiser), in dem ein armer Jäger seine einzige Tochter verliert und sie schließlich als Sterne am Himmel wieder sieht.

### Text 5 (28.10.2024)

User: Fasse die Szene 5 zusamen!

Woyzy: Der Text ist ein Dialog zwischen dem Hauptmann und Woyzeck, einem armen Kerl, der ihm das Haar rasieren soll. Der Hauptmann spricht über die Ewigkeit, Beschäftigung und Moral, während Woyzeck sich still und verhalten gibt.

Der Hauptmann drückt seine Besorgnis über die Ewigkeit aus und fragt Woyzeck, wie er diese Zeit nutzen könnte. Er meint, dass es wichtig sei, etwas zu tun, um die Langeweile zu vertreiben. Woyzeck reagiert aber nicht auf diese Fragen und gibt stattdessen kurze Antworten.

Der Hauptmann wird dann melancholisch, wenn er an die Liebe denkt, und spricht über seine eigene Leidenschaft für eine Frau. Er sagt, dass er ein tugendhafter Mensch ist, aber Woyzeck hat keine Tugend. Der Hauptmann meint, dass es wichtig sei, sich selbst zu reden und zu sagen: "Ich bin ein tugendhafter Mensch".

Der Text endet mit dem Hauptmann, der Woyzeck ermahnt, langsamer zu gehen und nicht so sehr besorgt auszusehen.

Die Interpretation des Textes kann auf verschiedene Weise erfolgen. Einerseits handelt es sich um einen Dialog zwischen zwei Charakteren, bei dem die Perspektiven auf das Leben, die Moral und die Zeit unterschiedlich sind. Der Hauptmann repräsentiert eine höhere soziale Stufe und drückt seine Sorge über die Ewigkeit und die Notwendigkeit, etwas zu tun, um die Langeweile zu vertreiben aus. Woyzeck hingegen ist ein armer Kerl, der sich still und verhalten gibt.

Andererseits kann man den Text auch als eine Kritik an der Gesellschaft sehen. Der Hauptmann repräsentiert das Establishment und seine Sorgen über die Ewigkeit und die Moral sind eigentlich Sorgen um sein eigenes Überleben in dieser Welt. Woyzeck hingegen ist ein Symbol für die Armut und die Ausgrenzung, die oft im Leben von Menschen vorkommt.

Die Sprache des Textes ist auch interessant. Der Hauptmann spricht in einer höflichen und respektvollen Weise über Woyzeck, aber es ist klar, dass er ihn herabwürdigt. Die Verwendung von Ausdrücken wie "ein guter Mensch" oder "eine tugendhafter Mensch" unterstreicht die Diskrepanz zwischen der Perspektive des Hauptmanns und der Wirklichkeit.

Insgesamt handelt es sich um einen interessanten Text, der auf verschiedene Weise interpretiert werden kann.

### Text 6 (28.10.2024)

User: Fasse Szene 5 zusamen!

Woyzy: Der Text ist ein Dialog zwischen dem Hauptmann und Woyzeck, einem einfachen Mann, der ihn rasiert. Der Hauptmann wird von seiner eigenen Existenzangst eingenommen und spricht über die Ewigkeit, die Beschäftigung und die Zeitverschwendung. Er meint dabei, dass das Leben wie ein Mühlrad ist, und fragt sich, was man mit dem Zeitpunkt anfangen soll, der einem entgeht.

Der Hauptmann gibt sich als fromm und moralisch aus, aber in Wirklichkeit scheint er unsicher zu sein. Er fragt Woyzeck über die Moral, obwohl er selbst nicht genau weiß, was sie bedeuten soll. Als Woyzeck antwortet, dass Gott das Kind ohne den Segen der Kirche nicht drum schlägt, macht dies den Hauptmann verwirrt.

Der Hauptmann spricht auch über seine eigene Liebe und meint, dass er Fleisch und Blut hat wie jeder andere Mensch. Er fragt sich jedoch, ob Woyzeck tugendhaft ist oder nicht. Woyzeck antwortet, dass man nicht tugendhaft sein muss, wenn man ein armer Kerl ist.

Der Hauptmann wirft Woyzeck vor, zu viel zu denken und immer verhetzt auszusehen. Er ermutigt ihn, langsam die Straße hinunterzuwalken, aber im Gegensatz dazu drängt er sich selbst zum Handeln.

Insgesamt geht es in diesem Dialog um das Thema der Existenzangst, Unsicherheit und die Suche nach Sinn. Der Hauptmann ist ein Beispiel für einen Menschen, der sich von seinem eigenen Ich eingenommen hat und versucht, die Welt mit seinen eigenen Maßstäben zu beurteilen.

### Text 7 (28.10.2024)

User: Wer kommt in Szene 5 alles vor, also welche Personen?

Woyzy: In Szene 5 kommen folgende Personen vor:

1. Der Hauptmann
2. Woyzeck (der ihn rasiert)

User: Ok gut gemacht und wie ist deren Beziehung und Szene 5 ?

Woyzy: Gut gemacht!

Die Szene 5 zeigt eine tiefe Persönlichkeit des Hauptmanns und Woyzecks. Der Hauptmann ist ein aufgeblasener Militärangehöriger, der sich selbst überlegen fühlt und die Welt als eine große Theaterbühne sieht. Er verwendet übertrieben elegante Redewendungen wie "Süd-Nord" und "Moral" und ist besorgt um seine eigene Zeitwahrnehmung.

Im Gegensatz dazu ist Woyzeck ein einfacher, aber gutmütiger Mann, der sich in einer Welt bewegt, die ihn nicht versteht. Er ist ungebildet, aber hat eine tiefe Spiritualität und fühlt sich durch Gott beschirmt. Die Szene zeigt auch die Beziehung zwischen dem Hauptmann und Woyzeck als eine von Unterdrückung und Ausbeutung.

Die Rede des Hauptmanns über Tugend und Moral ist besonders interessant, da er Woyzeck mit derselben Sprache anspricht, die er sonst für sich selbst verwendet. Dies zeigt, dass der Hauptmann in Woyzeck etwas sieht, das ihm selbst fehlt - nämlich ein Gefühl von Güte und Tugend.

Die Szene endet mit dem Hauptmanns Befreiungswunsch, Woyzeck zu schicken, um die Straße langsam hinunterzugehen. Dies symbolisiert die Trennung zwischen der Welt des Hauptmanns und der Welt von Woyzeck.

Insgesamt ist diese Szene ein wichtiger Teil des Dramas, da sie die Charaktere tiefer kennzeichnen lässt und den Konflikt zwischen dem Hauptmann und Woyzeck aufzeigt.

User: Welche Person wärst du gerne in der Szene 5 ?

Woyzy: Eine interessante Frage!

Ich würde gerne den Hauptmann in der Szene 5 sein. Er ist ein komplexer Charakter, der auf der einen Seite autoritativ und humorvoll erscheint, aber auf der anderen Seite auch melancholisch und verwundbar. Seine Gedanken und Gefühle sind vielschichtig und bieten viel Raum für Interpretation.

Als Hauptmann würde ich mich bemühen, Woyzeck zu verstecken, indem ich ihn mit kleinen Konversationen ablenke, während er mich rasierst. Ich würde versuchen, meine Bedenken über die Ewigkeit und den Wert der Zeit zu verbergen, aber zugleich auch meine Gefühle von Melancholie und Unsicherheit auszudrücken.

Es wäre eine Herausforderung, diese Rolle zu spielen, da ich als Hauptmann sowohl autoritativ als auch menschlich auftreten müsste. Aber es wäre auch sehr spannend, die verschiedenen Facetten des Charakters zu erkunden und zu sehen, wie er sich in verschiedenen Situationen verhält!

### Text 8 (28.10.2024)

User: Fasse scene Szene 19 zusammen

Woyzy: Der Text ist eine Szene aus dem Theaterstück "Woyzeck" von Georg Büchner. Hier ist meine Interpretation:

Die Szene spielt im Wohnzimmer einer Frau namens Marie, die mit ihrem Kind am Fenster sitzt. Sie beobachtet den Zapfenstreich, einem militärischen Ritual, das vorbei geht. Marie und ihre Nachbarin Margreth unterhalten sich über die Soldaten, von denen sie sagt, dass sie "schöne Burschen" sind. Marie singt ein Lied über Soldaten und gibt Auskunft darüber, wie es in ihrem Leben aussieht.

Dann kommt Woyzeck, Maries Geliebter, herein und spricht geheimnisvoll mit ihr. Er erzählt von einem Rauch, der aus dem Land kommt, was Marie besorgt macht. Woyzeck muss fort und Marie bleibt allein zurück.

Die Szene springt dann zu zwei Personen, die draußen sind und über den Ton des Wassers sprechen, das sie hören können. Sie unterhalten sich über den Tod und den Klang der Glocken, die wie gesprungne Glocken klingen.

Schließlich ist Woyzeck wieder am Teich und wirft sein Messer hinein. Er geht in den Teich und wirft weit hinein. Die Szene endet mit einer Selbstreflexion von Woyzeck über seinen Zustand und seine Bedürfnisse.

Themen und Motive:

* Die Beobachtung des Alltäglichen: Marie beobachtet den Zapfenstreich, während Woyzeck sich auf die Ereignisse im Land konzentriert.
* Die Unbeständigkeit des Lebens: Woyzeck wird von seinen Gedanken übermannt und Marie ist besorgt um ihren Zustand.
* Die Beziehung zwischen Woyzeck und Marie: Sie sind eng miteinander verbunden, aber ihre Beziehung ist auch gefährdet durch die Unsicherheit der Situation.
* Die Bedeutung des Teichs: Der Teich wird als Ort der Selbstreflexion und der Beruhigung gesehen. Es ist ein Ort, an dem Woyzeck seine Gedanken und Probleme beiseitelegen kann.

Stil und Sprache:

* Die Sprache ist einfach und direkten Charakters.
* Der Text ist stark von der Dichtung beeinflusst.
* Die Szene springt zwischen verschiedenen Ebenen und Perspektiven, was die Illusion eines Kontinuierlichen Geschehens schafft.

Es ist wichtig zu beachten, dass "Woyzeck" ein Theaterstück ist und daher nicht als realistische Darstellung von Ereignissen angesehen werden sollte. Die Szene ist eher eine Interpretation der Situationen und Emotionen der Charaktere.

### Text 9 (28.10.2024)

User: Fasse Szene 3 zusamen!

Woyzy: Der Text ist ein Exzerpt aus dem Theaterstück "Woyzeck" von Georg Büchner und zeigt eine Szene, in der Woyzeck und seine Frau Marie in einer Budenszene anwesend sind. Die Szene wird von einem Marktbeschreier moderiert, der Woyzecks Frau als einen Tier mit schwarzen Haaren und Augen beschreibt.

Der Marktbeschreier beginnt, die Teilnehmer des Publikums zu verspotten und ihnen vorzuführen, wie "sich die Kreatur" sieht, wie Gott sie gemacht hat. Er unterstreicht, dass es sich dabei um ein Tier handelt, das Mitglied von allen gelehrten Gesellschaften ist und sogar als Professor an mehreren Universitäten tätig ist.

Der Marktbeschreier beschimpft auch die Zuschauer, indem er sagt, dass sie nicht verstehen können, was Vernunft ist. Er behauptet, dass Woyzecks Frau eine Person ist, aber gleichzeitig ein Tier, und stellt fest, dass niemand es versteht, warum.

In der Szene ist auch ein Unteroffizier vorhanden, der während der Diskussion seine Uhr herausnimmt und die Zeit ansagt. Marie klettert auf einen Platz und will sich die Uhr ansehen, wobei der Unteroffizier ihr hilft.

Der Text spiegelt eine Kritik an der Gesellschaft wider, indem er die Ungerechtigkeiten und das Despotismus in der Gesellschaft anprangert. Die Szene zeigt auch Woyzecks Stimmung und seine Frustration, als er sich gegen die Machthaber auflehnt.

Analytische Aspekte:

* Die Szene zeigt eine Kritik an der Gesellschaft, indem sie die Ungerechtigkeiten und das Despotismus in der Gesellschaft anprangert.
* Der Marktbeschreier wird als eine Art von Prophet oder einer Stimme der Wahrheit dargestellt, der die Wahrheit über die Gesellschaft preisgibt.
* Die Szene zeigt auch Woyzecks Stimmung und seine Frustration, als er sich gegen die Machthaber auflehnt.
* Der Text verwendet eine Vielzahl von Metaphern und Vergleichen, um die menschliche Natur und die Gesellschaft zu beschreiben.

Literarische Aspekte:

* Der Text ist ein Beispiel für den expressionistischen Stil, der in der Literatur des 20. Jahrhunderts verwendet wurde.
* Die Szene zeigt eine starke Kritik an der Gesellschaft und ist daher als eine Art von sozialer Satire zu sehen.
* Der Marktbeschreier wird als eine Art von Autorität dargestellt, die die Zuschauer auf ihre Ungerechtigkeiten hinweist.

Hinweis: Das Theaterstück "Woyzeck" wurde von Georg Büchner 1827/28 geschrieben, aber es blieb bis zum Jahr 1912 unveröffentlicht. Es ist daher ein wichtiger Teil der deutschen Literatur des 19. und 20. Jahrhunderts.

## Geschichte

<div align="center">
  <img src="./static/images/woyzy-banner21.jpg" alt="woyzy" width="400" style="margin: 10px;">
</div>
<br>

...

## Checkliste

Hier ist die To-Do-Liste für die wichtigsten Tools und Aufgaben im Projekt:

## Aufgaben

| **Task** | **Beschreibung** | **Status** |
|----------|------------------|------------|
| Task 1   |                  | ❌          |


Nicht erledigt ❌ | Erledigt (min. 1 Monat) ✔️ | Verbesserungen nötig 🔧 | In Bearbeitung 🔄 | Verbesserungen erforderlich ⚠️

## Design

...

## Transformer

### 1. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2018)
**Authors:** Jacob Devlin, Ming-Wei Chang, Kenton Lee ...<br>
**Link:** [arXiv:1810.04805v2](https://arxiv.org/abs/1810.04805v2)  <br>
**Abstract:** We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications.
BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).

### 2. Evaluating Large Language Models Trained on Code (2021)
**Authors:** Mark Chen, Jerry Tworek, Heewoo Jun ...<br>
**Link:** [arXiv:2107.03374](https://arxiv.org/abs/2107.03374)  <br>
**Abstract:** We introduce Codex, a GPT language model fine-tuned on publicly available code from GitHub, and study its Python code-writing capabilities. A distinct production version of Codex powers GitHub Copilot. On HumanEval, a new evaluation set we release to measure functional correctness for synthesizing programs from docstrings, our model solves 28.8% of the problems, while GPT-3 solves 0% and GPT-J solves 11.4%. Furthermore, we find that repeated sampling from the model is a surprisingly effective strategy for producing working solutions to difficult prompts. Using this method, we solve 70.2% of our problems with 100 samples per problem. Careful investigation of our model reveals its limitations, including difficulty with docstrings describing long chains of operations and with binding operations to variables. Finally, we discuss the potential broader impacts of deploying powerful code generation technologies, covering safety, security, and economics.

### 3. Training language models to follow instructions with human feedback (2022)
**Authors:** Long Ouyang, Jeff Wu, Xu Jiang ...<br>
**Link:** [arXiv:2203.02155](https://arxiv.org/abs/2203.02155)  <br>
**Abstract:** Making language models bigger does not inherently make them better at following a user's intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In other words, these models are not aligned with their users. In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning. We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. We call the resulting models InstructGPT. In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters. Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets. Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.

### 4. Aligning Books and Movies: Towards Story-like Visual Explanations by Watching Movies and Reading Books (2015)
**Authors:** Yukun Zhu, Ryan Kiros, Richard Zemel ...<br>
**Link:** [arXiv:1506.06724](https://arxiv.org/abs/1506.06724)  <br>
**Abstract:** This work presents a Neural Architecture Search (NAS) method using reinforcement learning to automatically generate neural network architectures. NAS demonstrates the ability to discover novel architectures that outperform human-designed models on standard benchmarks.

### 5. Language Models are Few-Shot Learners (2020)
**Authors:** Tom B. Brown, Benjamin Mann, Nick Ryder ...<br>
**Link:** [arXiv:2005.14165v4](https://arxiv.org/abs/2005.14165v4)  <br>
**Abstract:** Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches. Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same time, we also identify some datasets where GPT-3's few-shot learning still struggles, as well as some datasets where GPT-3 faces methodological issues related to training on large web corpora. Finally, we find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans. We discuss broader societal impacts of this finding and of GPT-3 in general.

### 6. Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models (2023)
**Authors:** Chenfei Wu, Shengming Yin, Weizhen Qi ...<br>
**Link:** [arXiv:2303.04671](https://arxiv.org/abs/2303.04671)  <br>
**Abstract:** ChatGPT is attracting a cross-field interest as it provides a language interface with remarkable conversational competency and reasoning capabilities across many domains. However, since ChatGPT is trained with languages, it is currently not capable of processing or generating images from the visual world. At the same time, Visual Foundation Models, such as Visual Transformers or Stable Diffusion, although showing great visual understanding and generation capabilities, they are only experts on specific tasks with one-round fixed inputs and outputs. To this end, We build a system called \textbf{Visual ChatGPT}, incorporating different Visual Foundation Models, to enable the user to interact with ChatGPT by 1) sending and receiving not only languages but also images 2) providing complex visual questions or visual editing instructions that require the collaboration of multiple AI models with multi-steps. 3) providing feedback and asking for corrected results. We design a series of prompts to inject the visual model information into ChatGPT, considering models of multiple inputs/outputs and models that require visual feedback. Experiments show that Visual ChatGPT opens the door to investigating the visual roles of ChatGPT with the help of Visual Foundation Models.

### 7. On the Opportunities and Risks of Foundation Models (2022)
**Authors:** Rishi Bommasani, Drew A. Hudson, Ehsan Adeli, Russ Altman ...<br>
**Link:** [arXiv:2108.07258](https://arxiv.org/abs/2108.07258)  <br>
**Abstract:** AI is undergoing a paradigm shift with the rise of models (e.g., BERT, DALL-E, GPT-3) that are trained on broad data at scale and are adaptable to a wide range of downstream tasks. We call these models foundation models to underscore their critically central yet incomplete character. This report provides a thorough account of the opportunities and risks of foundation models, ranging from their capabilities (e.g., language, vision, robotics, reasoning, human interaction) and technical principles(e.g., model architectures, training procedures, data, systems, security, evaluation, theory) to their applications (e.g., law, healthcare, education) and societal impact (e.g., inequity, misuse, economic and environmental impact, legal and ethical considerations). Though foundation models are based on standard deep learning and transfer learning, their scale results in new emergent capabilities,and their effectiveness across so many tasks incentivizes homogenization. Homogenization provides powerful leverage but demands caution, as the defects of the foundation model are inherited by all the adapted models downstream. Despite the impending widespread deployment of foundation models, we currently lack a clear understanding of how they work, when they fail, and what they are even capable of due to their emergent properties. To tackle these questions, we believe much of the critical research on foundation models will require deep interdisciplinary collaboration commensurate with their fundamentally sociotechnical nature.

### 8. Training language models to follow instructions with human feedback (2022)
**Authors:** Long Ouyang, Jeff Wu, Xu Jiang ...<br>
**Link:** [arXiv:2203.02155](https://arxiv.org/abs/2203.02155) <br> 
**Abstract:** Making language models bigger does not inherently make them better at following a user's intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In other words, these models are not aligned with their users. In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning. We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. We call the resulting models InstructGPT. In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters. Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets. Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.

### 9. BioGPT: Generative Pre-trained Transformer for Biomedical Text Generation and Mining (2022)
**Authors:** Renqian Luo, Liai Sun, Yingce Xia ...<br>
**Link:** [arXiv:2210.10341](https://arxiv.org/abs/2210.10341)  <br>
**Abstract:** Pre-trained language models have attracted increasing attention in the biomedical domain, inspired by their great success in the general natural language domain. Among the two main branches of pre-trained language models in the general language domain, i.e., BERT (and its variants) and GPT (and its variants), the first one has been extensively studied in the biomedical domain, such as BioBERT and PubMedBERT. While they have achieved great success on a variety of discriminative downstream biomedical tasks, the lack of generation ability constrains their application scope. In this paper, we propose BioGPT, a domain-specific generative Transformer language model pre-trained on large scale biomedical literature. We evaluate BioGPT on six biomedical NLP tasks and demonstrate that our model outperforms previous models on most tasks. Especially, we get 44.98%, 38.42% and 40.76% F1 score on BC5CDR, KD-DTI and DDI end-to-end relation extraction tasks respectively, and 78.2% accuracy on PubMedQA, creating a new record. Our case study on text generation further demonstrates the advantage of BioGPT on biomedical literature to generate fluent descriptions for biomedical terms.

### 10. Release Strategies and the Social Impacts of Language Models (2019)
**Authors:** Irene Solaiman, Miles Brundage, Jack Clark ...<br>
**Link:** [arXiv:1908.09203](https://arxiv.org/abs/1908.09203)  <br>
**Abstract:** Large language models have a range of beneficial uses: they can assist in prose, poetry, and programming; analyze dataset biases; and more. However, their flexibility and generative capabilities also raise misuse concerns. This report discusses OpenAI's work related to the release of its GPT-2 language model. It discusses staged release, which allows time between model releases to conduct risk and benefit analyses as model sizes increased. It also discusses ongoing partnership-based research and provides recommendations for better coordination and responsible publication in AI.

### 11. WebGPT: Browser-assisted question-answering with human feedback (2022)
**Authors:**Reiichiro Nakano, Jacob Hilton, Suchir Balaji ...<br>
**Link:** [arXiv:2112.09332](https://arxiv.org/abs/2112.09332)  <br>
**Abstract:** We fine-tune GPT-3 to answer long-form questions using a text-based web-browsing environment, which allows the model to search and navigate the web. By setting up the task so that it can be performed by humans, we are able to train models on the task using imitation learning, and then optimize answer quality with human feedback. To make human evaluation of factual accuracy easier, models must collect references while browsing in support of their answers. We train and evaluate our models on ELI5, a dataset of questions asked by Reddit users. Our best model is obtained by fine-tuning GPT-3 using behavior cloning, and then performing rejection sampling against a reward model trained to predict human preferences. This model's answers are preferred by humans 56% of the time to those of our human demonstrators, and 69% of the time to the highest-voted answer from Reddit.

### 12. GPT-4 Technical Report (2023)
**Authors:** OpenAI, Josh Achiam, Steven Adler ...<br>
**Link:** [arXiv:2303.08774](https://arxiv.org/abs/2303.08774)  <br>
**Abstract:** We report the development of GPT-4, a large-scale, multimodal model which can accept image and text inputs and produce text outputs. While less capable than humans in many real-world scenarios, GPT-4 exhibits human-level performance on various professional and academic benchmarks, including passing a simulated bar exam with a score around the top 10% of test takers. GPT-4 is a Transformer-based model pre-trained to predict the next token in a document. The post-training alignment process results in improved performance on measures of factuality and adherence to desired behavior. A core component of this project was developing infrastructure and optimization methods that behave predictably across a wide range of scales. This allowed us to accurately predict some aspects of GPT-4's performance based on models trained with no more than 1/1,000th the compute of GPT-4.

### 13. Sparks of Artificial General Intelligence: Early experiments with GPT-4 (2023)
**Authors:** Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan ...<br>
**Link:** [arXiv:2303.12712](https://arxiv.org/abs/2303.12712)  <br>
**Abstract:** Artificial intelligence (AI) researchers have been developing and refining large language models (LLMs) that exhibit remarkable capabilities across a variety of domains and tasks, challenging our understanding of learning and cognition. The latest model developed by OpenAI, GPT-4, was trained using an unprecedented scale of compute and data. In this paper, we report on our investigation of an early version of GPT-4, when it was still in active development by OpenAI. We contend that (this early version of) GPT-4 is part of a new cohort of LLMs (along with ChatGPT and Google's PaLM for example) that exhibit more general intelligence than previous AI models. We discuss the rising capabilities and implications of these models. We demonstrate that, beyond its mastery of language, GPT-4 can solve novel and difficult tasks that span mathematics, coding, vision, medicine, law, psychology and more, without needing any special prompting. Moreover, in all of these tasks, GPT-4's performance is strikingly close to human-level performance, and often vastly surpasses prior models such as ChatGPT. Given the breadth and depth of GPT-4's capabilities, we believe that it could reasonably be viewed as an early (yet still incomplete) version of an artificial general intelligence (AGI) system. In our exploration of GPT-4, we put special emphasis on discovering its limitations, and we discuss the challenges ahead for advancing towards deeper and more comprehensive versions of AGI, including the possible need for pursuing a new paradigm that moves beyond next-word prediction. We conclude with reflections on societal influences of the recent technological leap and future research directions.<br>

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert – siehe die [LICENSE](LICENSE) Datei für Details.
