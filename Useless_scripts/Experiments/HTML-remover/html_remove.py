#!/usr/bin/python
# -*- coding: utf-8 -*-
a = """" 

<font size=2>In appreciation of the painterly virtues of ""Après la tempête"" it must be said that this pochade demonstrates <a href=""http://www.klinkhoff.com/canadian-artist/Clarence-A-Gagnon"">Clarence Gagnon</a> at the height of his artistic powers.  According to Hélène Sicotte in her important catalogue <i>Clarence Gagnon: Dreaming the Landscape</i> for the outstanding Clarence Gagnon exhibition at the Musée National des Beaux arts du Québec and the National Gallery of Canada in 2006 and 2007, after World War I Gagnon had become disillusioned with the deteriorating quality of artist's colours being produced in Paris where he customarily ordered them and that, ""[h]e began experimenting with different painting techniques and making his own preparations.  He even ground his own pigments..."".  Sicotte notes that ""Winter in the Laurentians, Quebec"", a slightly larger work Gagnon painted up from ""Après la tempête"" was ""... the first picture executed with his own paints"".  The former is a contribution to an exhibition at New York's Salmagundi Club, a painting which won him the Trevor Prize in the club's 1923 exhibition.  I have no hesitation in suggesting that Sicotte's comments about ""Winter in the Laurentians, Quebec"" as to the ""vivacity and purity of its colours"" are equally applicable to the brilliance we appreciate in ""Après la tempête"". The original freshness of colour and vigour of brushwork of this work painted almost 90 years ago is gloriously revealed after only the lightest professional cleaning.

  

The chronology provided by Hélène Sicotte’s research for <i>Clarence Gagnon: Dreaming the Landscape</i> shows that this pochade was painted at an important and exciting stage in Gagnon's career and life when he was living in Baie-St-Paul.  A review of Sicotte's catalogue for <i>Dreaming the Landscape</i> will confirm that the paintings the master was executing at this juncture are of the finest in quality including ""The Ice Bridge, Quebec"" (no. 81), ""A Quebec Village Street, Winter"" (no. 82), "" Early Morning in March"", 1922, (no. 87), ""Heating the Oven, Winter Scene"" (no. 91), ""Village Street, Baie-Saint-Paul"" (no. 95), ""Afternoon Sun, Baie-Saint-Paul"" (no. 98), "" Horse Races in Winter"" (no. 100), ""Twilight, Baie-Saint-Paul"" (no. 102), ""Early Winter Morning in the Woods, Baie -St -Paul"" (no. 103). 



He had only recently married Lucile Rodier and his reputation as an artist had been raised to that of among the foremost artists residing in the Province of Quebec and Canada . The Province of Quebec's department of fine arts had requested that he accept to serve as Director, an offer he rejected and he similarly rejected an offer to be director of the art school at the Art Association of Montreal.  Gagnon did however accept a position to serve on a jury to select artists to represent Canada in the 1924 Wembly, an exhibition that ultimately included three paintings and seven etchings of his own.  After 11 years serving as an Associate of the Royal Canadian Academy of the Arts Gagnon was elected to full membership. 

  



<font size=3><b>Related Links...</b></font>



<a href=""http://www.klinkhoff.com/news-archive/archive"">See previous highlights and other Canadian Art News</a>"""
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()























