from flpy.excel import convert_excel, rows_to_excel

a_dict = {
  "19centuryantiques": {
    "aol3_url": "https://app.artlogic.net/19centuryantiques", 
    "old_url": "https://secure.artlogiconline.com/19centuryantiques", 
    "site_name": "19th Century Antiques"
  }, 
  "abcarte": {
    "aol3_url": "https://app.artlogic.net/abcarte", 
    "old_url": "https://secure.artlogiconline.com/abcarte", 
    "site_name": "ABC-ARTE"
  }, 
  "ac": {
    "aol3_url": "https://app.artlogic.net/ac", 
    "old_url": "https://secure.artlogiconline.com/ac", 
    "site_name": "Cutting Edge Associates LLC"
  }, 
  "adrianberg": {
    "aol3_url": "https://app.artlogic.net/adrianberg", 
    "old_url": "https://secure.artlogiconline.com/adrianberg", 
    "site_name": "Adrian Berg Estate"
  }, 
  "afroco": {
    "aol3_url": "https://app.artlogic.net/afroco", 
    "old_url": "https://secure.artlogiconline.com/afroco", 
    "site_name": "Afroco - Chris Ofili Office"
  }, 
  "afterlife": {
    "aol3_url": "https://app.artlogic.net/afterlife", 
    "old_url": "https://secure.artlogiconline.com/afterlife", 
    "site_name": "Afterlife Ltd."
  }, 
  "agnesb": {
    "aol3_url": "https://app.artlogic.net/agnesb", 
    "old_url": "https://secure.artlogiconline.com/agnesb", 
    "site_name": "Agnes b"
  }, 
  "aktis": {
    "aol3_url": "https://app.artlogic.net/aktis", 
    "old_url": "https://secure.artlogiconline.com/aktis", 
    "site_name": "Aktis Gallery (UK) Ltd"
  }, 
  "alesortuzar": {
    "aol3_url": "https://app.artlogic.net/alesortuzar", 
    "old_url": "https://secure.artlogiconline.com/alesortuzar", 
    "site_name": "Ales Ortuzar"
  }, 
  "alisonjacques": {
    "aol3_url": "https://app.artlogic.net/alisonjacques", 
    "old_url": "https://secure.artlogiconline.com/alisonjacques", 
    "site_name": "Alison Jacques Gallery"
  }, 
  "altamira": {
    "aol3_url": "https://app.artlogic.net/altamira", 
    "old_url": "https://secure.artlogiconline.com/altamira", 
    "site_name": "Altamira Fine Art"
  }, 
  "altmansiegel": {
    "aol3_url": "https://app.artlogic.net/altmansiegel", 
    "old_url": "https://secure.artlogiconline.com/altmansiegel", 
    "site_name": "Altman Siegel Gallery"
  }, 
  "ancientandmodern": {
    "aol3_url": "https://app.artlogic.net/ancientandmodern", 
    "old_url": "https://secure.artlogiconline.com/ancientandmodern", 
    "site_name": "Bruce Haines, Mayfair"
  }, 
  "andrekohn": {
    "aol3_url": "https://app.artlogic.net/andrekohn", 
    "old_url": "https://secure.artlogiconline.com/andrekohn", 
    "site_name": "Andre Kohn Fine Art"
  }, 
  "andygoldsworthy": {
    "aol3_url": "https://app.artlogic.net/andygoldsworthy", 
    "old_url": "https://secure.artlogiconline.com/andygoldsworthy", 
    "site_name": "Andy Goldsworthy"
  }, 
  "andyvalmorbida": {
    "aol3_url": "https://app.artlogic.net/andyvalmorbida", 
    "old_url": "https://secure.artlogiconline.com/andyvalmorbida", 
    "site_name": "Andy Valmorbida"
  }, 
  "annetgelink": {
    "aol3_url": "https://app.artlogic.net/annetgelink", 
    "old_url": "https://secure.artlogiconline.com/annetgelink", 
    "site_name": "Annet Gelink Gallery"
  }, 
  "antonymous": {
    "aol3_url": "https://app.artlogic.net/antonymous", 
    "old_url": "https://secure.artlogiconline.com/antonymous", 
    "site_name": "Anton Corbijn"
  }, 
  "anyagallaccio": {
    "aol3_url": "https://app.artlogic.net/anyagallaccio", 
    "old_url": "https://secure.artlogiconline.com/anyagallaccio", 
    "site_name": "Anya Gallaccio"
  }, 
  "aoldev": {
    "aol3_url": "https://app.artlogic.net/aoldev", 
    "old_url": "https://secure.artlogiconline.com/aoldev", 
    "site_name": "Artlogic Development"
  }, 
  "aolnewinstance": {
    "aol3_url": "https://app.artlogic.net/aolnewinstance", 
    "old_url": "https://secure.artlogiconline.com/aolnewinstance", 
    "site_name": "Artlogic Template"
  }, 
  "aoltest": {
    "aol3_url": "https://app.artlogic.net/aoltest", 
    "old_url": "https://secure.artlogiconline.com/aoltest", 
    "site_name": "Artlogic Online Test Site"
  }, 
  "arcimboldo": {
    "aol3_url": "https://app.artlogic.net/arcimboldo", 
    "old_url": "https://secure.artlogiconline.com/arcimboldo", 
    "site_name": "Arcimboldo"
  }, 
  "artform": {
    "aol3_url": "https://app.artlogic.net/artform", 
    "old_url": "https://secure.artlogiconline.com/artform", 
    "site_name": "Artform Sculptures Limited"
  }, 
  "arthurrogergallery": {
    "aol3_url": "https://app.artlogic.net/arthurrogergallery", 
    "old_url": "https://secure.artlogiconline.com/arthurrogergallery", 
    "site_name": "Arthur Roger Gallery"
  }, 
  "artlabafrica": {
    "aol3_url": "https://app.artlogic.net/artlabafrica", 
    "old_url": "https://secure.artlogiconline.com/artlabafrica", 
    "site_name": "ARTLabAfrica"
  }, 
  "artlogic": {
    "aol3_url": "https://app.artlogic.net/artlogic", 
    "old_url": "https://secure.artlogiconline.com/artlogic", 
    "site_name": "Artlogic"
  }, 
  "artlogiconline": {
    "aol3_url": "https://app.artlogic.net/artlogiconline", 
    "old_url": "https://secure.artlogiconline.com/artlogiconline", 
    "site_name": "Demo Gallery"
  }, 
  "artlogictraining": {
    "aol3_url": "https://app.artlogic.net/artlogictraining", 
    "old_url": "https://secure.artlogiconline.com/artlogictraining", 
    "site_name": "Clock House Gallery"
  }, 
  "artseen": {
    "aol3_url": "https://app.artlogic.net/artseen", 
    "old_url": "https://secure.artlogiconline.com/artseen", 
    "site_name": "Art Seen Limited"
  }, 
  "artwalk": {
    "aol3_url": "https://app.artlogic.net/artwalk", 
    "old_url": "https://secure.artlogiconline.com/artwalk", 
    "site_name": "Katinka Traaseth"
  }, 
  "artwise": {
    "aol3_url": "https://app.artlogic.net/artwise", 
    "old_url": "https://secure.artlogiconline.com/artwise", 
    "site_name": "Artwise Curators"
  }, 
  "aubergineart": {
    "aol3_url": "https://app.artlogic.net/aubergineart", 
    "old_url": "https://secure.artlogiconline.com/aubergineart", 
    "site_name": "Aubergine Art Ltd"
  }, 
  "avidimages": {
    "aol3_url": "https://app.artlogic.net/avidimages", 
    "old_url": "https://secure.artlogiconline.com/avidimages", 
    "site_name": "Avid Images"
  }, 
  "avran": {
    "aol3_url": "https://app.artlogic.net/avran", 
    "old_url": "https://secure.artlogiconline.com/avran", 
    "site_name": "Avran Art"
  }, 
  "ayegallery": {
    "aol3_url": "https://app.artlogic.net/ayegallery", 
    "old_url": "https://secure.artlogiconline.com/ayegallery", 
    "site_name": "Aye Gallery"
  }, 
  "ayyamgallery": {
    "aol3_url": "https://app.artlogic.net/ayyamgallery", 
    "old_url": "https://secure.artlogiconline.com/ayyamgallery", 
    "site_name": "Ayyam Gallery"
  }, 
  "azure": {
    "aol3_url": "https://app.artlogic.net/azure", 
    "old_url": "https://secure.artlogiconline.com/azure", 
    "site_name": "Azure Glory Limited"
  }, 
  "babington": {
    "aol3_url": "https://app.artlogic.net/babington", 
    "old_url": "https://secure.artlogiconline.com/babington", 
    "site_name": "The Incite Project"
  }, 
  "baertgallery": {
    "aol3_url": "https://app.artlogic.net/baertgallery", 
    "old_url": "https://secure.artlogiconline.com/baertgallery", 
    "site_name": "Baert Gallery"
  }, 
  "beetleshuxley": {
    "aol3_url": "https://app.artlogic.net/beetleshuxley", 
    "old_url": "https://secure.artlogiconline.com/beetleshuxley", 
    "site_name": "Beetles+Huxley"
  }, 
  "benbrown": {
    "aol3_url": "https://app.artlogic.net/benbrown", 
    "old_url": "https://secure.artlogiconline.com/benbrown", 
    "site_name": "Ben Brown Fine Arts"
  }, 
  "bischoffweiss": {
    "aol3_url": "https://app.artlogic.net/bischoffweiss", 
    "old_url": "https://secure.artlogiconline.com/bischoffweiss", 
    "site_name": "Bischoff Weiss"
  }, 
  "blankspace": {
    "aol3_url": "https://app.artlogic.net/blankspace", 
    "old_url": "https://secure.artlogiconline.com/blankspace", 
    "site_name": "Blank Space"
  }, 
  "bridgetriley": {
    "aol3_url": "https://app.artlogic.net/bridgetriley", 
    "old_url": "https://secure.artlogiconline.com/bridgetriley", 
    "site_name": "Bridget Riley Services"
  }, 
  "brunfineart": {
    "aol3_url": "https://app.artlogic.net/brunfineart", 
    "old_url": "https://secure.artlogiconline.com/brunfineart", 
    "site_name": "Brun Fine Art"
  }, 
  "bullseye": {
    "aol3_url": "https://app.artlogic.net/bullseye", 
    "old_url": "https://secure.artlogiconline.com/bullseye", 
    "site_name": "Bullseye Projects"
  }, 
  "c4lb": {
    "aol3_url": "https://app.artlogic.net/c4lb", 
    "old_url": "https://secure.artlogiconline.com/c4lb", 
    "site_name": "c4lb test site"
  }, 
  "cabin": {
    "aol3_url": "https://app.artlogic.net/cabin", 
    "old_url": "https://secure.artlogiconline.com/cabin", 
    "site_name": "Cabin"
  }, 
  "candicebermangallery": {
    "aol3_url": "https://app.artlogic.net/candicebermangallery", 
    "old_url": "https://secure.artlogiconline.com/candicebermangallery", 
    "site_name": "Candice Berman Fine Art Gallery (PTY) LTD"
  }, 
  "candidastevens": {
    "aol3_url": "https://app.artlogic.net/candidastevens", 
    "old_url": "https://secure.artlogiconline.com/candidastevens", 
    "site_name": "Candida Stevens Gallery"
  }, 
  "canvasgallery": {
    "aol3_url": "https://app.artlogic.net/canvasgallery", 
    "old_url": "https://secure.artlogiconline.com/canvasgallery", 
    "site_name": "Canvas Gallery"
  }, 
  "capsuleshanghai": {
    "aol3_url": "https://app.artlogic.net/capsuleshanghai", 
    "old_url": "https://secure.artlogiconline.com/capsuleshanghai", 
    "site_name": "Capsule Shanghai"
  }, 
  "carlfreedman": {
    "aol3_url": "https://app.artlogic.net/carlfreedman", 
    "old_url": "https://secure.artlogiconline.com/carlfreedman", 
    "site_name": "Carl Freedman Gallery"
  }, 
  "carrollfletcher": {
    "aol3_url": "https://app.artlogic.net/carrollfletcher", 
    "old_url": "https://secure.artlogiconline.com/carrollfletcher", 
    "site_name": "Carroll / Fletcher"
  }, 
  "carstenholler": {
    "aol3_url": "https://app.artlogic.net/carstenholler", 
    "old_url": "https://secure.artlogiconline.com/carstenholler", 
    "site_name": "Carsten H\u00f6ller"
  }, 
  "centurymark": {
    "aol3_url": "https://app.artlogic.net/centurymark", 
    "old_url": "https://secure.artlogiconline.com/centurymark", 
    "site_name": "Century Mark Co. Ltd."
  }, 
  "christies": {
    "aol3_url": "https://app.artlogic.net/christies", 
    "old_url": "https://secure.artlogiconline.com/christies", 
    "site_name": "Christies International"
  }, 
  "christiesdemo": {
    "aol3_url": "https://app.artlogic.net/christiesdemo", 
    "old_url": "https://secure.artlogiconline.com/christiesdemo", 
    "site_name": "Christies International"
  }, 
  "citco": {
    "aol3_url": "https://app.artlogic.net/citco", 
    "old_url": "https://secure.artlogiconline.com/citco", 
    "site_name": "Citco"
  }, 
  "commune": {
    "aol3_url": "https://app.artlogic.net/commune", 
    "old_url": "https://secure.artlogiconline.com/commune", 
    "site_name": "Commune LP"
  }, 
  "connaughtbrown": {
    "aol3_url": "https://app.artlogic.net/connaughtbrown", 
    "old_url": "https://secure.artlogiconline.com/connaughtbrown", 
    "site_name": "Connaught Brown"
  }, 
  "copperhousegallery": {
    "aol3_url": "https://app.artlogic.net/copperhousegallery", 
    "old_url": "https://secure.artlogiconline.com/copperhousegallery", 
    "site_name": "The Copper House Gallery"
  }, 
  "cricket": {
    "aol3_url": "https://app.artlogic.net/cricket", 
    "old_url": "https://secure.artlogiconline.com/cricket", 
    "site_name": "Cricket Fine Art"
  }, 
  "crosssteele": {
    "aol3_url": "https://app.artlogic.net/crosssteele", 
    "old_url": "https://secure.artlogiconline.com/crosssteele", 
    "site_name": "Cross Family Collection"
  }, 
  "crossstreet": {
    "aol3_url": "https://app.artlogic.net/crossstreet", 
    "old_url": "https://secure.artlogiconline.com/crossstreet", 
    "site_name": "Cross Street Gallery"
  }, 
  "cure3": {
    "aol3_url": "https://app.artlogic.net/cure3", 
    "old_url": "https://secure.artlogiconline.com/cure3", 
    "site_name": "Cure3"
  }, 
  "cynthiacorbettgallery": {
    "aol3_url": "https://app.artlogic.net/cynthiacorbettgallery", 
    "old_url": "https://secure.artlogiconline.com/cynthiacorbettgallery", 
    "site_name": "Cynthia Corbett Gallery"
  }, 
  "dacunha": {
    "aol3_url": "https://app.artlogic.net/dacunha", 
    "old_url": "https://secure.artlogiconline.com/dacunha", 
    "site_name": "Da Cunha Studio"
  }, 
  "dais": {
    "aol3_url": "https://app.artlogic.net/dais", 
    "old_url": "https://secure.artlogiconline.com/dais", 
    "site_name": "Dais Contemporary Ltd"
  }, 
  "daniellaluxembourg": {
    "aol3_url": "https://app.artlogic.net/daniellaluxembourg", 
    "old_url": "https://secure.artlogiconline.com/daniellaluxembourg", 
    "site_name": "Daniella Luxembourg"
  }, 
  "dastangallery": {
    "aol3_url": "https://app.artlogic.net/dastangallery", 
    "old_url": "https://secure.artlogiconline.com/dastangallery", 
    "site_name": "Dastan Gallery"
  }, 
  "davidroberts": {
    "aol3_url": "https://app.artlogic.net/davidroberts", 
    "old_url": "https://secure.artlogiconline.com/davidroberts", 
    "site_name": "David Roberts Art Foundation"
  }, 
  "degunzburg": {
    "aol3_url": "https://app.artlogic.net/degunzburg", 
    "old_url": "https://secure.artlogiconline.com/degunzburg", 
    "site_name": "Terry & Jean de Gunzburg Art Collection"
  }, 
  "delahuntyfineart": {
    "aol3_url": "https://app.artlogic.net/delahuntyfineart", 
    "old_url": "https://secure.artlogiconline.com/delahuntyfineart", 
    "site_name": "Delahunty Fine Art"
  }, 
  "demo": {
    "aol3_url": "https://app.artlogic.net/demo", 
    "old_url": "https://secure.artlogiconline.com/demo", 
    "site_name": "Demo Gallery"
  }, 
  "derekjohns": {
    "aol3_url": "https://app.artlogic.net/derekjohns", 
    "old_url": "https://secure.artlogiconline.com/derekjohns", 
    "site_name": "Derek Johns"
  }, 
  "dhg": {
    "aol3_url": "https://app.artlogic.net/dhg", 
    "old_url": "https://secure.artlogiconline.com/dhg", 
    "site_name": "Dennis Hotz Gallery"
  }, 
  "dmt": {
    "aol3_url": "https://app.artlogic.net/dmt", 
    "old_url": "https://secure.artlogiconline.com/dmt", 
    "site_name": "Diego Marroquin"
  }, 
  "ebandflow": {
    "aol3_url": "https://app.artlogic.net/ebandflow", 
    "old_url": "https://secure.artlogiconline.com/ebandflow", 
    "site_name": "Berloni Gallery"
  }, 
  "edelassanti": {
    "aol3_url": "https://app.artlogic.net/edelassanti", 
    "old_url": "https://secure.artlogiconline.com/edelassanti", 
    "site_name": "Edel Assanti"
  }, 
  "edouardmalingue": {
    "aol3_url": "https://app.artlogic.net/edouardmalingue", 
    "old_url": "https://secure.artlogiconline.com/edouardmalingue", 
    "site_name": "Edouard Malingue Gallery"
  }, 
  "elizabethdee": {
    "aol3_url": "https://app.artlogic.net/elizabethdee", 
    "old_url": "https://secure.artlogiconline.com/elizabethdee", 
    "site_name": "Elizabeth Dee"
  }, 
  "estherschipper": {
    "aol3_url": "https://app.artlogic.net/estherschipper", 
    "old_url": "https://secure.artlogiconline.com/estherschipper", 
    "site_name": "Esther Schipper"
  }, 
  "exit": {
    "aol3_url": "https://app.artlogic.net/exit", 
    "old_url": "https://secure.artlogiconline.com/exit", 
    "site_name": "Gallery Exit"
  }, 
  "eykynmaclean": {
    "aol3_url": "https://app.artlogic.net/eykynmaclean", 
    "old_url": "https://secure.artlogiconline.com/eykynmaclean", 
    "site_name": "Eykyn Maclean Ltd."
  }, 
  "fionabanner": {
    "aol3_url": "https://app.artlogic.net/fionabanner", 
    "old_url": "https://secure.artlogiconline.com/fionabanner", 
    "site_name": "Fiona Banner Studio"
  }, 
  "fioruccicollection": {
    "aol3_url": "https://app.artlogic.net/fioruccicollection", 
    "old_url": "https://secure.artlogiconline.com/fioruccicollection", 
    "site_name": "NICOLETTA FIORUCCI COLLECTION"
  }, 
  "flavie": {
    "aol3_url": "https://app.artlogic.net/flavie", 
    "old_url": "https://secure.artlogiconline.com/flavie", 
    "site_name": "Flavie Audi Studio"
  }, 
  "flowers": {
    "aol3_url": "https://app.artlogic.net/flowers", 
    "old_url": "https://secure.artlogiconline.com/flowers", 
    "site_name": "Flowers Gallery"
  }, 
  "forestgallery": {
    "aol3_url": "https://app.artlogic.net/forestgallery", 
    "old_url": "https://secure.artlogiconline.com/forestgallery", 
    "site_name": "Forest Gallery"
  }, 
  "frankssuss": {
    "aol3_url": "https://app.artlogic.net/frankssuss", 
    "old_url": "https://secure.artlogiconline.com/frankssuss", 
    "site_name": "Franks-Suss Collection"
  }, 
  "friesen": {
    "aol3_url": "https://app.artlogic.net/friesen", 
    "old_url": "https://secure.artlogiconline.com/friesen", 
    "site_name": "Friesen Gallery"
  }, 
  "fumi": {
    "aol3_url": "https://app.artlogic.net/fumi", 
    "old_url": "https://secure.artlogiconline.com/fumi", 
    "site_name": "Gallery FUMI"
  }, 
  "gafra": {
    "aol3_url": "https://app.artlogic.net/gafra", 
    "old_url": "https://secure.artlogiconline.com/gafra", 
    "site_name": "Gallery of African Art"
  }, 
  "galerieegp": {
    "aol3_url": "https://app.artlogic.net/galerieegp", 
    "old_url": "https://secure.artlogiconline.com/galerieegp", 
    "site_name": "Galerie E.G.P"
  }, 
  "galleryso": {
    "aol3_url": "https://app.artlogic.net/galleryso", 
    "old_url": "https://secure.artlogiconline.com/galleryso", 
    "site_name": "Gallery S O"
  }, 
  "gallevery": {
    "aol3_url": "https://app.artlogic.net/gallevery", 
    "old_url": "https://secure.artlogiconline.com/gallevery", 
    "site_name": "The Gallery of Everything"
  }, 
  "gce1test": {
    "aol3_url": "https://app.artlogic.net/gce1test", 
    "old_url": "https://secure.artlogiconline.com/gce1test", 
    "site_name": "GCE1 Test Site"
  }, 
  "ges": {
    "aol3_url": "https://app.artlogic.net/ges", 
    "old_url": "https://secure.artlogiconline.com/ges", 
    "site_name": "Gallery Elena Shchukina"
  }, 
  "gibbonsnicholas": {
    "aol3_url": "https://app.artlogic.net/gibbonsnicholas", 
    "old_url": "https://secure.artlogiconline.com/gibbonsnicholas", 
    "site_name": "Gibbons & Nicholas"
  }, 
  "goodmantaft": {
    "aol3_url": "https://app.artlogic.net/goodmantaft", 
    "old_url": "https://secure.artlogiconline.com/goodmantaft", 
    "site_name": "Goodman Taft"
  }, 
  "gps": {
    "aol3_url": "https://app.artlogic.net/gps", 
    "old_url": "https://secure.artlogiconline.com/gps", 
    "site_name": "Glasgow Print Studio"
  }, 
  "greynoise": {
    "aol3_url": "https://app.artlogic.net/greynoise", 
    "old_url": "https://secure.artlogiconline.com/greynoise", 
    "site_name": "GREY NOISE"
  }, 
  "grimm": {
    "aol3_url": "https://app.artlogic.net/grimm", 
    "old_url": "https://secure.artlogiconline.com/grimm", 
    "site_name": "GRIMM"
  }, 
  "grobgallery": {
    "aol3_url": "https://app.artlogic.net/grobgallery", 
    "old_url": "https://secure.artlogiconline.com/grobgallery", 
    "site_name": "Grob Gallery"
  }, 
  "grosvenorgallery": {
    "aol3_url": "https://app.artlogic.net/grosvenorgallery", 
    "old_url": "https://secure.artlogiconline.com/grosvenorgallery", 
    "site_name": "Grosvenor Gallery"
  }, 
  "gusfordgallery": {
    "aol3_url": "https://app.artlogic.net/gusfordgallery", 
    "old_url": "https://secure.artlogiconline.com/gusfordgallery", 
    "site_name": "GUSFORD | los angeles"
  }, 
  "gxgallery": {
    "aol3_url": "https://app.artlogic.net/gxgallery", 
    "old_url": "https://secure.artlogiconline.com/gxgallery", 
    "site_name": "GX Gallery"
  }, 
  "halesgallery": {
    "aol3_url": "https://app.artlogic.net/halesgallery", 
    "old_url": "https://secure.artlogiconline.com/halesgallery", 
    "site_name": "Hales London New York"
  }, 
  "hamiltonsdma": {
    "aol3_url": "https://app.artlogic.net/hamiltonsdma", 
    "old_url": "https://secure.artlogiconline.com/hamiltonsdma", 
    "site_name": "Hamiltons DMA"
  }, 
  "hanover": {
    "aol3_url": "https://app.artlogic.net/hanover", 
    "old_url": "https://secure.artlogiconline.com/hanover", 
    "site_name": "10 Hanover"
  }, 
  "hignellgallery": {
    "aol3_url": "https://app.artlogic.net/hignellgallery", 
    "old_url": "https://secure.artlogiconline.com/hignellgallery", 
    "site_name": "Hignell Gallery Limited"
  }, 
  "hiscox": {
    "aol3_url": "https://app.artlogic.net/hiscox", 
    "old_url": "https://secure.artlogiconline.com/hiscox", 
    "site_name": "Hiscox Collection"
  }, 
  "hixart": {
    "aol3_url": "https://app.artlogic.net/hixart", 
    "old_url": "https://secure.artlogiconline.com/hixart", 
    "site_name": "CNB Gallery"
  }, 
  "hollandmurray": {
    "aol3_url": "https://app.artlogic.net/hollandmurray", 
    "old_url": "https://secure.artlogiconline.com/hollandmurray", 
    "site_name": "Holland Murray Fine Art"
  }, 
  "hortaosorio": {
    "aol3_url": "https://app.artlogic.net/hortaosorio", 
    "old_url": "https://secure.artlogiconline.com/hortaosorio", 
    "site_name": "Horta-Osorio"
  }, 
  "hosfeltgallery": {
    "aol3_url": "https://app.artlogic.net/hosfeltgallery", 
    "old_url": "https://secure.artlogiconline.com/hosfeltgallery", 
    "site_name": "Hosfelt Gallery"
  }, 
  "hotn": {
    "aol3_url": "https://app.artlogic.net/hotn", 
    "old_url": "https://secure.artlogiconline.com/hotn", 
    "site_name": "House of the Nobleman"
  }, 
  "hov": {
    "aol3_url": "https://app.artlogic.net/hov", 
    "old_url": "https://secure.artlogiconline.com/hov", 
    "site_name": "Haunch of Venison"
  }, 
  "hurvinandersonstudio": {
    "aol3_url": "https://app.artlogic.net/hurvinandersonstudio", 
    "old_url": "https://secure.artlogiconline.com/hurvinandersonstudio", 
    "site_name": "Hurvin Anderson"
  }, 
  "ianda": {
    "aol3_url": "https://app.artlogic.net/ianda", 
    "old_url": "https://secure.artlogiconline.com/ianda", 
    "site_name": "I & A Art Ltd"
  }, 
  "ibid": {
    "aol3_url": "https://app.artlogic.net/ibid", 
    "old_url": "https://secure.artlogiconline.com/ibid", 
    "site_name": "Ibid"
  }, 
  "imlaqah": {
    "aol3_url": "https://app.artlogic.net/imlaqah", 
    "old_url": "https://secure.artlogiconline.com/imlaqah", 
    "site_name": "Imlaqah International"
  }, 
  "inglebygallery": {
    "aol3_url": "https://app.artlogic.net/inglebygallery", 
    "old_url": "https://secure.artlogiconline.com/inglebygallery", 
    "site_name": "Ingleby Gallery"
  }, 
  "inkstudio": {
    "aol3_url": "https://app.artlogic.net/inkstudio", 
    "old_url": "https://secure.artlogiconline.com/inkstudio", 
    "site_name": "Ink Studio"
  }, 
  "isaacjulien": {
    "aol3_url": "https://app.artlogic.net/isaacjulien", 
    "old_url": "https://secure.artlogiconline.com/isaacjulien", 
    "site_name": "Isaac Julien"
  }, 
  "islandpress": {
    "aol3_url": "https://app.artlogic.net/islandpress", 
    "old_url": "https://secure.artlogiconline.com/islandpress", 
    "site_name": "Island Press"
  }, 
  "ivde": {
    "aol3_url": "https://app.artlogic.net/ivde", 
    "old_url": "https://secure.artlogiconline.com/ivde", 
    "site_name": "Gallery Isabelle Van Den Eynde"
  }, 
  "jackbell": {
    "aol3_url": "https://app.artlogic.net/jackbell", 
    "old_url": "https://secure.artlogiconline.com/jackbell", 
    "site_name": "Jack Bell Gallery"
  }, 
  "jacksonfineart": {
    "aol3_url": "https://app.artlogic.net/jacksonfineart", 
    "old_url": "https://secure.artlogiconline.com/jacksonfineart", 
    "site_name": "Jackson Fine Art"
  }, 
  "janazadeh": {
    "aol3_url": "https://app.artlogic.net/janazadeh", 
    "old_url": "https://secure.artlogiconline.com/janazadeh", 
    "site_name": "Jana Zadeh"
  }, 
  "jeaninehofland": {
    "aol3_url": "https://app.artlogic.net/jeaninehofland", 
    "old_url": "https://secure.artlogiconline.com/jeaninehofland", 
    "site_name": "Jeanine Hofland"
  }, 
  "jennaburlingham": {
    "aol3_url": "https://app.artlogic.net/jennaburlingham", 
    "old_url": "https://secure.artlogiconline.com/jennaburlingham", 
    "site_name": "Jenna Burlingham Fine Art Ltd"
  }, 
  "jfa": {
    "aol3_url": "https://app.artlogic.net/jfa", 
    "old_url": "https://secure.artlogiconline.com/jfa", 
    "site_name": "Joseph Fine Art"
  }, 
  "jgh": {
    "aol3_url": "https://app.artlogic.net/jgh", 
    "old_url": "https://secure.artlogiconline.com/jgh", 
    "site_name": "Graham Honeybill Collection"
  }, 
  "joeelliottart": {
    "aol3_url": "https://app.artlogic.net/joeelliottart", 
    "old_url": "https://secure.artlogiconline.com/joeelliottart", 
    "site_name": "Kingsley Elliott"
  }, 
  "jonasstaal": {
    "aol3_url": "https://app.artlogic.net/jonasstaal", 
    "old_url": "https://secure.artlogiconline.com/jonasstaal", 
    "site_name": "Jonas Staal"
  }, 
  "jonathanclark": {
    "aol3_url": "https://app.artlogic.net/jonathanclark", 
    "old_url": "https://secure.artlogiconline.com/jonathanclark", 
    "site_name": "Jonathan Clark & Co Ltd"
  }, 
  "jonathancooperparkwalk": {
    "aol3_url": "https://app.artlogic.net/jonathancooperparkwalk", 
    "old_url": "https://secure.artlogiconline.com/jonathancooperparkwalk", 
    "site_name": "Jonathan Cooper Park Walk Gallery"
  }, 
  "josieeastwood": {
    "aol3_url": "https://app.artlogic.net/josieeastwood", 
    "old_url": "https://secure.artlogiconline.com/josieeastwood", 
    "site_name": "Josie Eastwood Fine Art"
  }, 
  "judehess": {
    "aol3_url": "https://app.artlogic.net/judehess", 
    "old_url": "https://secure.artlogiconline.com/judehess", 
    "site_name": "Jude Hess Fine Arts"
  }, 
  "juliemehretu": {
    "aol3_url": "https://app.artlogic.net/juliemehretu", 
    "old_url": "https://secure.artlogiconline.com/juliemehretu", 
    "site_name": "Julie Mehretu Studio"
  }, 
  "kaikaikiki": {
    "aol3_url": "https://app.artlogic.net/kaikaikiki", 
    "old_url": "https://secure.artlogiconline.com/kaikaikiki", 
    "site_name": "Kaikai Kiki Gallery"
  }, 
  "kamellazaarfoundation": {
    "aol3_url": "https://app.artlogic.net/kamellazaarfoundation", 
    "old_url": "https://secure.artlogiconline.com/kamellazaarfoundation", 
    "site_name": "Kamel Lazaar Foundation"
  }, 
  "kang": {
    "aol3_url": "https://app.artlogic.net/kang", 
    "old_url": "https://secure.artlogiconline.com/kang", 
    "site_name": "Kang Collection of Korean Art"
  }, 
  "karstenschubert": {
    "aol3_url": "https://app.artlogic.net/karstenschubert", 
    "old_url": "https://secure.artlogiconline.com/karstenschubert", 
    "site_name": "Karsten Schubert"
  }, 
  "kfg": {
    "aol3_url": "https://app.artlogic.net/kfg", 
    "old_url": "https://secure.artlogiconline.com/kfg", 
    "site_name": "Kevin Francis Gray Studio"
  }, 
  "kilmorack": {
    "aol3_url": "https://app.artlogic.net/kilmorack", 
    "old_url": "https://secure.artlogiconline.com/kilmorack", 
    "site_name": "Kilmorack Gallery"
  }, 
  "kirkmechar": {
    "aol3_url": "https://app.artlogic.net/kirkmechar", 
    "old_url": "https://secure.artlogiconline.com/kirkmechar", 
    "site_name": "Kirk Mechar Studio"
  }, 
  "kristiansibast": {
    "aol3_url": "https://app.artlogic.net/kristiansibast", 
    "old_url": "https://secure.artlogiconline.com/kristiansibast", 
    "site_name": "Kristian Sibast"
  }, 
  "kristinenardelli": {
    "aol3_url": "https://app.artlogic.net/kristinenardelli", 
    "old_url": "https://secure.artlogiconline.com/kristinenardelli", 
    "site_name": "Kristine Nardelli"
  }, 
  "kristinhjellegjerde": {
    "aol3_url": "https://app.artlogic.net/kristinhjellegjerde", 
    "old_url": "https://secure.artlogiconline.com/kristinhjellegjerde", 
    "site_name": "Kristin Hjellegjerde Gallery"
  }, 
  "kristofdeclercqgallery": {
    "aol3_url": "https://app.artlogic.net/kristofdeclercqgallery", 
    "old_url": "https://secure.artlogiconline.com/kristofdeclercqgallery", 
    "site_name": "LOTIKA BVBA | Kristof De Clercq gallery"
  }, 
  "lambarts": {
    "aol3_url": "https://app.artlogic.net/lambarts", 
    "old_url": "https://secure.artlogiconline.com/lambarts", 
    "site_name": "LAMB Arts"
  }, 
  "largedemo": {
    "aol3_url": "https://app.artlogic.net/largedemo", 
    "old_url": "https://secure.artlogiconline.com/largedemo", 
    "site_name": "Demo Gallery"
  }, 
  "laurabartlett": {
    "aol3_url": "https://app.artlogic.net/laurabartlett", 
    "old_url": "https://secure.artlogiconline.com/laurabartlett", 
    "site_name": "Laura Bartlett Gallery"
  }, 
  "laurelgitlen": {
    "aol3_url": "https://app.artlogic.net/laurelgitlen", 
    "old_url": "https://secure.artlogiconline.com/laurelgitlen", 
    "site_name": "Laurel Gitlen"
  }, 
  "laurentdelaye": {
    "aol3_url": "https://app.artlogic.net/laurentdelaye", 
    "old_url": "https://secure.artlogiconline.com/laurentdelaye", 
    "site_name": "Laurent Delaye Gallery"
  }, 
  "lawrieshabibi": {
    "aol3_url": "https://app.artlogic.net/lawrieshabibi", 
    "old_url": "https://secure.artlogiconline.com/lawrieshabibi", 
    "site_name": "Lawrie Shabibi"
  }, 
  "lehmannmaupin": {
    "aol3_url": "https://app.artlogic.net/lehmannmaupin", 
    "old_url": "https://secure.artlogiconline.com/lehmannmaupin", 
    "site_name": "Lehmann Maupin"
  }, 
  "leogallery": {
    "aol3_url": "https://app.artlogic.net/leogallery", 
    "old_url": "https://secure.artlogiconline.com/leogallery", 
    "site_name": "Leo Gallery"
  }, 
  "leokoenig": {
    "aol3_url": "https://app.artlogic.net/leokoenig", 
    "old_url": "https://secure.artlogiconline.com/leokoenig", 
    "site_name": "Leo Koenig Inc."
  }, 
  "lesenluminures": {
    "aol3_url": "https://app.artlogic.net/lesenluminures", 
    "old_url": "https://secure.artlogiconline.com/lesenluminures", 
    "site_name": "Les Enluminures"
  }, 
  "leslozes": {
    "aol3_url": "https://app.artlogic.net/leslozes", 
    "old_url": "https://secure.artlogiconline.com/leslozes", 
    "site_name": "JABRE Art System"
  }, 
  "lfa": {
    "aol3_url": "https://app.artlogic.net/lfa", 
    "old_url": "https://secure.artlogiconline.com/lfa", 
    "site_name": "Lane Fine Art Ltd"
  }, 
  "libbysellers": {
    "aol3_url": "https://app.artlogic.net/libbysellers", 
    "old_url": "https://secure.artlogiconline.com/libbysellers", 
    "site_name": "Gallery Libby Sellers"
  }, 
  "lindongallery": {
    "aol3_url": "https://app.artlogic.net/lindongallery", 
    "old_url": "https://secure.artlogiconline.com/lindongallery", 
    "site_name": "Lindon Gallery"
  }, 
  "lionelgallery": {
    "aol3_url": "https://app.artlogic.net/lionelgallery", 
    "old_url": "https://secure.artlogiconline.com/lionelgallery", 
    "site_name": "LionelGallery"
  }, 
  "lisabird": {
    "aol3_url": "https://app.artlogic.net/lisabird", 
    "old_url": "https://secure.artlogiconline.com/lisabird", 
    "site_name": "Galerie Lisa Kandlhofer"
  }, 
  "lisanorris": {
    "aol3_url": "https://app.artlogic.net/lisanorris", 
    "old_url": "https://secure.artlogiconline.com/lisanorris", 
    "site_name": "Lisa Norris Gallery"
  }, 
  "lisasharpe": {
    "aol3_url": "https://app.artlogic.net/lisasharpe", 
    "old_url": "https://secure.artlogiconline.com/lisasharpe", 
    "site_name": "Lisa Sharpe"
  }, 
  "livedemo": {
    "aol3_url": "https://app.artlogic.net/livedemo", 
    "old_url": "https://secure.artlogiconline.com/livedemo", 
    "site_name": "Demonstration System"
  }, 
  "lodeveans": {
    "aol3_url": "https://app.artlogic.net/lodeveans", 
    "old_url": "https://secure.artlogiconline.com/lodeveans", 
    "site_name": "Lodeveans Collection"
  }, 
  "louisaguinness": {
    "aol3_url": "https://app.artlogic.net/louisaguinness", 
    "old_url": "https://secure.artlogiconline.com/louisaguinness", 
    "site_name": "Louisa Guinness Gallery"
  }, 
  "lovaas": {
    "aol3_url": "https://app.artlogic.net/lovaas", 
    "old_url": "https://secure.artlogiconline.com/lovaas", 
    "site_name": "Lovaas Projects GmbH"
  }, 
  "luxembourgdayan": {
    "aol3_url": "https://app.artlogic.net/luxembourgdayan", 
    "old_url": "https://secure.artlogiconline.com/luxembourgdayan", 
    "site_name": "Luxembourg & Dayan Art Limited "
  }, 
  "luxembourgdayanny": {
    "aol3_url": "https://app.artlogic.net/luxembourgdayanny", 
    "old_url": "https://secure.artlogiconline.com/luxembourgdayanny", 
    "site_name": "Luxembourg & Dayan New York"
  }, 
  "luxzoo": {
    "aol3_url": "https://app.artlogic.net/luxzoo", 
    "old_url": "https://secure.artlogiconline.com/luxzoo", 
    "site_name": "Coburn Projects"
  }, 
  "m13": {
    "aol3_url": "https://app.artlogic.net/m13", 
    "old_url": "https://secure.artlogiconline.com/m13", 
    "site_name": "M13 Test Instance"
  }, 
  "makasiini": {
    "aol3_url": "https://app.artlogic.net/makasiini", 
    "old_url": "https://secure.artlogiconline.com/makasiini", 
    "site_name": "Makasiini Contemporary"
  }, 
  "marcianoartfoundation": {
    "aol3_url": "https://app.artlogic.net/marcianoartfoundation", 
    "old_url": "https://secure.artlogiconline.com/marcianoartfoundation", 
    "site_name": "Marciano Art Foundation"
  }, 
  "mariabernheim": {
    "aol3_url": "https://app.artlogic.net/mariabernheim", 
    "old_url": "https://secure.artlogiconline.com/mariabernheim", 
    "site_name": "Galerie Maria Bernheim"
  }, 
  "mariangoodman": {
    "aol3_url": "https://app.artlogic.net/mariangoodman", 
    "old_url": "https://secure.artlogiconline.com/mariangoodman", 
    "site_name": "Marian Goodman Gallery"
  }, 
  "markelfinearts": {
    "aol3_url": "https://app.artlogic.net/markelfinearts", 
    "old_url": "https://secure.artlogiconline.com/markelfinearts", 
    "site_name": "Kathryn Markel Fine Arts"
  }, 
  "masterpiecelondon": {
    "aol3_url": "https://app.artlogic.net/masterpiecelondon", 
    "old_url": "https://secure.artlogiconline.com/masterpiecelondon", 
    "site_name": "Masterpiece London"
  }, 
  "matthewmarks": {
    "aol3_url": "https://app.artlogic.net/matthewmarks", 
    "old_url": "https://secure.artlogiconline.com/matthewmarks", 
    "site_name": "Matthew Marks Gallery"
  }, 
  "maureenpaley": {
    "aol3_url": "https://app.artlogic.net/maureenpaley", 
    "old_url": "https://secure.artlogiconline.com/maureenpaley", 
    "site_name": "Maureen Paley"
  }, 
  "mayarchitecture": {
    "aol3_url": "https://app.artlogic.net/mayarchitecture", 
    "old_url": "https://secure.artlogiconline.com/mayarchitecture", 
    "site_name": "May Architecture + Interiors"
  }, 
  "mazzoleniart": {
    "aol3_url": "https://app.artlogic.net/mazzoleniart", 
    "old_url": "https://secure.artlogiconline.com/mazzoleniart", 
    "site_name": "MAZZOLENI ART"
  }, 
  "mbla": {
    "aol3_url": "https://app.artlogic.net/mbla", 
    "old_url": "https://secure.artlogiconline.com/mbla", 
    "site_name": "MBLA"
  }, 
  "meadcarney": {
    "aol3_url": "https://app.artlogic.net/meadcarney", 
    "old_url": "https://secure.artlogiconline.com/meadcarney", 
    "site_name": "MC Masters & Contemporary"
  }, 
  "meemgallery": {
    "aol3_url": "https://app.artlogic.net/meemgallery", 
    "old_url": "https://secure.artlogiconline.com/meemgallery", 
    "site_name": "Meem Gallery"
  }, 
  "metrogallery": {
    "aol3_url": "https://app.artlogic.net/metrogallery", 
    "old_url": "https://secure.artlogiconline.com/metrogallery", 
    "site_name": "Metro Gallery"
  }, 
  "michaelgaillard": {
    "aol3_url": "https://app.artlogic.net/michaelgaillard", 
    "old_url": "https://secure.artlogiconline.com/michaelgaillard", 
    "site_name": "Michael Gaillard"
  }, 
  "mikehammer": {
    "aol3_url": "https://app.artlogic.net/mikehammer", 
    "old_url": "https://secure.artlogiconline.com/mikehammer", 
    "site_name": "Mike Hammer"
  }, 
  "ministryofnomads": {
    "aol3_url": "https://app.artlogic.net/ministryofnomads", 
    "old_url": "https://secure.artlogiconline.com/ministryofnomads", 
    "site_name": "Ministry of Nomads"
  }, 
  "minjungkim": {
    "aol3_url": "https://app.artlogic.net/minjungkim", 
    "old_url": "https://secure.artlogiconline.com/minjungkim", 
    "site_name": "Studio Minjung Kim"
  }, 
  "moatti": {
    "aol3_url": "https://app.artlogic.net/moatti", 
    "old_url": "https://secure.artlogiconline.com/moatti", 
    "site_name": "Moatti Fine Art"
  }, 
  "modernart": {
    "aol3_url": "https://app.artlogic.net/modernart", 
    "old_url": "https://secure.artlogiconline.com/modernart", 
    "site_name": "Stuart Shave/Modern Art"
  }, 
  "modernism": {
    "aol3_url": "https://app.artlogic.net/modernism", 
    "old_url": "https://secure.artlogiconline.com/modernism", 
    "site_name": "Modernism"
  }, 
  "morettigallery": {
    "aol3_url": "https://app.artlogic.net/morettigallery", 
    "old_url": "https://secure.artlogiconline.com/morettigallery", 
    "site_name": "Moretti Fine Art Ltd"
  }, 
  "multiplesinc": {
    "aol3_url": "https://app.artlogic.net/multiplesinc", 
    "old_url": "https://secure.artlogiconline.com/multiplesinc", 
    "site_name": "MultiplesInc Projects"
  }, 
  "narrativeprojects": {
    "aol3_url": "https://app.artlogic.net/narrativeprojects", 
    "old_url": "https://secure.artlogiconline.com/narrativeprojects", 
    "site_name": "Narrative Projects"
  }, 
  "naw": {
    "aol3_url": "https://app.artlogic.net/naw", 
    "old_url": "https://secure.artlogiconline.com/naw", 
    "site_name": "Arianne Piper Art Advisory"
  }, 
  "nettiehorn": {
    "aol3_url": "https://app.artlogic.net/nettiehorn", 
    "old_url": "https://secure.artlogiconline.com/nettiehorn", 
    "site_name": "Nettie Horn Gallery"
  }, 
  "neugerriemschneider": {
    "aol3_url": "https://app.artlogic.net/neugerriemschneider", 
    "old_url": "https://secure.artlogiconline.com/neugerriemschneider", 
    "site_name": "neugerriemschneider GmbH"
  }, 
  "northcote": {
    "aol3_url": "https://app.artlogic.net/northcote", 
    "old_url": "https://secure.artlogiconline.com/northcote", 
    "site_name": "Northcote Gallery"
  }, 
  "notvitalstudio": {
    "aol3_url": "https://app.artlogic.net/notvitalstudio", 
    "old_url": "https://secure.artlogiconline.com/notvitalstudio", 
    "site_name": "Not Vital Studio"
  }, 
  "offerwaterman": {
    "aol3_url": "https://app.artlogic.net/offerwaterman", 
    "old_url": "https://secure.artlogiconline.com/offerwaterman", 
    "site_name": "Offer Waterman"
  }, 
  "ohwow": {
    "aol3_url": "https://app.artlogic.net/ohwow", 
    "old_url": "https://secure.artlogiconline.com/ohwow", 
    "site_name": "MORAN BONDAROFF"
  }, 
  "olyvia": {
    "aol3_url": "https://app.artlogic.net/olyvia", 
    "old_url": "https://secure.artlogiconline.com/olyvia", 
    "site_name": "Willstone Management"
  }, 
  "omg": {
    "aol3_url": "https://app.artlogic.net/omg", 
    "old_url": "https://secure.artlogiconline.com/omg", 
    "site_name": "Olivier Malingue Gallery"
  }, 
  "omr": {
    "aol3_url": "https://app.artlogic.net/omr", 
    "old_url": "https://secure.artlogiconline.com/omr", 
    "site_name": "Galeria OMR"
  }, 
  "oraora": {
    "aol3_url": "https://app.artlogic.net/oraora", 
    "old_url": "https://secure.artlogiconline.com/oraora", 
    "site_name": "Ora-Ora"
  }, 
  "ordovas": {
    "aol3_url": "https://app.artlogic.net/ordovas", 
    "old_url": "https://secure.artlogiconline.com/ordovas", 
    "site_name": "Ordovas Ltd"
  }, 
  "pag": {
    "aol3_url": "https://app.artlogic.net/pag", 
    "old_url": "https://secure.artlogiconline.com/pag", 
    "site_name": "Pertwee Anderson & Gold"
  }, 
  "parafin": {
    "aol3_url": "https://app.artlogic.net/parafin", 
    "old_url": "https://secure.artlogiconline.com/parafin", 
    "site_name": "Parafin"
  }, 
  "paulstolper": {
    "aol3_url": "https://app.artlogic.net/paulstolper", 
    "old_url": "https://secure.artlogiconline.com/paulstolper", 
    "site_name": "Paul Stolper Gallery"
  }, 
  "pdc": {
    "aol3_url": "https://app.artlogic.net/pdc", 
    "old_url": "https://secure.artlogiconline.com/pdc", 
    "site_name": "Private Collection, London"
  }, 
  "peterdoig": {
    "aol3_url": "https://app.artlogic.net/peterdoig", 
    "old_url": "https://secure.artlogiconline.com/peterdoig", 
    "site_name": "Peter Doig Studio"
  }, 
  "pianonobile": {
    "aol3_url": "https://app.artlogic.net/pianonobile", 
    "old_url": "https://secure.artlogiconline.com/pianonobile", 
    "site_name": "Piano Nobile"
  }, 
  "pifo": {
    "aol3_url": "https://app.artlogic.net/pifo", 
    "old_url": "https://secure.artlogiconline.com/pifo", 
    "site_name": "PIFO Gallery"
  }, 
  "pilarcorrias": {
    "aol3_url": "https://app.artlogic.net/pilarcorrias", 
    "old_url": "https://secure.artlogiconline.com/pilarcorrias", 
    "site_name": "Pilar Corrias"
  }, 
  "pkg": {
    "aol3_url": "https://app.artlogic.net/pkg", 
    "old_url": "https://secure.artlogiconline.com/pkg", 
    "site_name": "Paul Kasmin Gallery"
  }, 
  "plateaux": {
    "aol3_url": "https://app.artlogic.net/plateaux", 
    "old_url": "https://secure.artlogiconline.com/plateaux", 
    "site_name": "Plateaux Gallery"
  }, 
  "plusonegallery": {
    "aol3_url": "https://app.artlogic.net/plusonegallery", 
    "old_url": "https://secure.artlogiconline.com/plusonegallery", 
    "site_name": "Plus One Gallery"
  }, 
  "porfirius": {
    "aol3_url": "https://app.artlogic.net/porfirius", 
    "old_url": "https://secure.artlogiconline.com/porfirius", 
    "site_name": "Porfirius Kunstkammer"
  }, 
  "porthminstergallery": {
    "aol3_url": "https://app.artlogic.net/porthminstergallery", 
    "old_url": "https://secure.artlogiconline.com/porthminstergallery", 
    "site_name": "Porthminster Gallery"
  }, 
  "proyectarte": {
    "aol3_url": "https://app.artlogic.net/proyectarte", 
    "old_url": "https://secure.artlogiconline.com/proyectarte", 
    "site_name": "Proyect Arte"
  }, 
  "rademakersgallery": {
    "aol3_url": "https://app.artlogic.net/rademakersgallery", 
    "old_url": "https://secure.artlogiconline.com/rademakersgallery", 
    "site_name": "Rademakers Gallery"
  }, 
  "ramiken": {
    "aol3_url": "https://app.artlogic.net/ramiken", 
    "old_url": "https://secure.artlogiconline.com/ramiken", 
    "site_name": "Ramiken Crucible"
  }, 
  "ramikim": {
    "aol3_url": "https://app.artlogic.net/ramikim", 
    "old_url": "https://secure.artlogiconline.com/ramikim", 
    "site_name": "Rami Kim International"
  }, 
  "rashidalkhalifa": {
    "aol3_url": "https://app.artlogic.net/rashidalkhalifa", 
    "old_url": "https://secure.artlogiconline.com/rashidalkhalifa", 
    "site_name": "Rashid Al Khalifa"
  }, 
  "rcfa": {
    "aol3_url": "https://app.artlogic.net/rcfa", 
    "old_url": "https://secure.artlogiconline.com/rcfa", 
    "site_name": "Rollo Campbell Fine Art"
  }, 
  "rebeccahossack": {
    "aol3_url": "https://app.artlogic.net/rebeccahossack", 
    "old_url": "https://secure.artlogiconline.com/rebeccahossack", 
    "site_name": "Rebecca Hossack Art Gallery"
  }, 
  "regina": {
    "aol3_url": "https://app.artlogic.net/regina", 
    "old_url": "https://secure.artlogiconline.com/regina", 
    "site_name": "Regina Gallery"
  }, 
  "rh": {
    "aol3_url": "https://app.artlogic.net/rh", 
    "old_url": "https://secure.artlogiconline.com/rh", 
    "site_name": "Studio Raphael Hefti"
  }, 
  "richardsaltoun": {
    "aol3_url": "https://app.artlogic.net/richardsaltoun", 
    "old_url": "https://secure.artlogiconline.com/richardsaltoun", 
    "site_name": "Richard Saltoun"
  }, 
  "rocket": {
    "aol3_url": "https://app.artlogic.net/rocket", 
    "old_url": "https://secure.artlogiconline.com/rocket", 
    "site_name": "Rocket Gallery"
  }, 
  "rodbarton": {
    "aol3_url": "https://app.artlogic.net/rodbarton", 
    "old_url": "https://secure.artlogiconline.com/rodbarton", 
    "site_name": "Rod Barton"
  }, 
  "rodeo": {
    "aol3_url": "https://app.artlogic.net/rodeo", 
    "old_url": "https://secure.artlogiconline.com/rodeo", 
    "site_name": "RODEO"
  }, 
  "rodolphejanssen": {
    "aol3_url": "https://app.artlogic.net/rodolphejanssen", 
    "old_url": "https://secure.artlogiconline.com/rodolphejanssen", 
    "site_name": "Galerie Rodolphe Janssen"
  }, 
  "ronaldandsharoncohen": {
    "aol3_url": "https://app.artlogic.net/ronaldandsharoncohen", 
    "old_url": "https://secure.artlogiconline.com/ronaldandsharoncohen", 
    "site_name": "Sir Ronald and Lady Cohen"
  }, 
  "ronewaart": {
    "aol3_url": "https://app.artlogic.net/ronewaart", 
    "old_url": "https://secure.artlogiconline.com/ronewaart", 
    "site_name": "Ronewa Art Gallery"
  }, 
  "ronmandos": {
    "aol3_url": "https://app.artlogic.net/ronmandos", 
    "old_url": "https://secure.artlogiconline.com/ronmandos", 
    "site_name": "Galerie Ron Mandos"
  }, 
  "rosenbaumcontemporary": {
    "aol3_url": "https://app.artlogic.net/rosenbaumcontemporary", 
    "old_url": "https://secure.artlogiconline.com/rosenbaumcontemporary", 
    "site_name": "Rosenbaum Contemporary"
  }, 
  "rosenfeldporcini": {
    "aol3_url": "https://app.artlogic.net/rosenfeldporcini", 
    "old_url": "https://secure.artlogiconline.com/rosenfeldporcini", 
    "site_name": "Rosenfeld Porcini"
  }, 
  "rossnewman": {
    "aol3_url": "https://app.artlogic.net/rossnewman", 
    "old_url": "https://secure.artlogiconline.com/rossnewman", 
    "site_name": "Ross Newman"
  }, 
  "rv": {
    "aol3_url": "https://app.artlogic.net/rv", 
    "old_url": "https://secure.artlogiconline.com/rv", 
    "site_name": "Robilant+Voena"
  }, 
  "rwstudio": {
    "aol3_url": "https://app.artlogic.net/rwstudio", 
    "old_url": "https://secure.artlogiconline.com/rwstudio", 
    "site_name": "Rebecca Warren Studio"
  }, 
  "sacbangkok": {
    "aol3_url": "https://app.artlogic.net/sacbangkok", 
    "old_url": "https://secure.artlogiconline.com/sacbangkok", 
    "site_name": "S.A.C Subhashok The Arts Centre"
  }, 
  "sacramons": {
    "aol3_url": "https://app.artlogic.net/sacramons", 
    "old_url": "https://secure.artlogiconline.com/sacramons", 
    "site_name": "Sacra Mons Art & Collection Management"
  }, 
  "saparcontemporary": {
    "aol3_url": "https://app.artlogic.net/saparcontemporary", 
    "old_url": "https://secure.artlogiconline.com/saparcontemporary", 
    "site_name": "Sapar Contemporary"
  }, 
  "sbg": {
    "aol3_url": "https://app.artlogic.net/sbg", 
    "old_url": "https://secure.artlogiconline.com/sbg", 
    "site_name": "Stephen Bulger Gallery"
  }, 
  "schoeni": {
    "aol3_url": "https://app.artlogic.net/schoeni", 
    "old_url": "https://secure.artlogiconline.com/schoeni", 
    "site_name": "Schoeni Art Consultancy"
  }, 
  "shiraga": {
    "aol3_url": "https://app.artlogic.net/shiraga", 
    "old_url": "https://secure.artlogiconline.com/shiraga", 
    "site_name": "Shiraga"
  }, 
  "shootgallery": {
    "aol3_url": "https://app.artlogic.net/shootgallery", 
    "old_url": "https://secure.artlogiconline.com/shootgallery", 
    "site_name": "Shoot Gallery"
  }, 
  "simmons": {
    "aol3_url": "https://app.artlogic.net/simmons", 
    "old_url": "https://secure.artlogiconline.com/simmons", 
    "site_name": "Simmons & Simmons"
  }, 
  "skarstedt": {
    "aol3_url": "https://app.artlogic.net/skarstedt", 
    "old_url": "https://secure.artlogiconline.com/skarstedt", 
    "site_name": "Skarstedt"
  }, 
  "slg": {
    "aol3_url": "https://app.artlogic.net/slg", 
    "old_url": "https://secure.artlogiconline.com/slg", 
    "site_name": " Simon Lee Gallery"
  }, 
  "sophiacontemporary": {
    "aol3_url": "https://app.artlogic.net/sophiacontemporary", 
    "old_url": "https://secure.artlogiconline.com/sophiacontemporary", 
    "site_name": "Sophia Contemporary Gallery"
  }, 
  "sothebys": {
    "aol3_url": "https://app.artlogic.net/sothebys", 
    "old_url": "https://secure.artlogiconline.com/sothebys", 
    "site_name": "Sothebys Diamonds"
  }, 
  "spencertunick": {
    "aol3_url": "https://app.artlogic.net/spencertunick", 
    "old_url": "https://secure.artlogiconline.com/spencertunick", 
    "site_name": "Spencer Tunick"
  }, 
  "stairsainty": {
    "aol3_url": "https://app.artlogic.net/stairsainty", 
    "old_url": "https://secure.artlogiconline.com/stairsainty", 
    "site_name": "Stair Sainty Gallery"
  }, 
  "star": {
    "aol3_url": "https://app.artlogic.net/star", 
    "old_url": "https://secure.artlogiconline.com/star", 
    "site_name": "Star Diamond"
  }, 
  "stellar": {
    "aol3_url": "https://app.artlogic.net/stellar", 
    "old_url": "https://secure.artlogiconline.com/stellar", 
    "site_name": "Stellar International Art Foundation"
  }, 
  "sternarts": {
    "aol3_url": "https://app.artlogic.net/sternarts", 
    "old_url": "https://secure.artlogiconline.com/sternarts", 
    "site_name": "SternArts Ltd."
  }, 
  "sullivanstrumpf": {
    "aol3_url": "https://app.artlogic.net/sullivanstrumpf", 
    "old_url": "https://secure.artlogiconline.com/sullivanstrumpf", 
    "site_name": "Sullivan+Strumpf"
  }, 
  "susaninglett": {
    "aol3_url": "https://app.artlogic.net/susaninglett", 
    "old_url": "https://secure.artlogiconline.com/susaninglett", 
    "site_name": "Susan Inglett Gallery"
  }, 
  "svr": {
    "aol3_url": "https://app.artlogic.net/svr", 
    "old_url": "https://secure.artlogiconline.com/svr", 
    "site_name": "Stefan von Ratibor"
  }, 
  "symbolic": {
    "aol3_url": "https://app.artlogic.net/symbolic", 
    "old_url": "https://secure.artlogiconline.com/symbolic", 
    "site_name": "Symbolic London"
  }, 
  "tanyaleighton": {
    "aol3_url": "https://app.artlogic.net/tanyaleighton", 
    "old_url": "https://secure.artlogiconline.com/tanyaleighton", 
    "site_name": "Tanya Leighton"
  }, 
  "taymourgrahne": {
    "aol3_url": "https://app.artlogic.net/taymourgrahne", 
    "old_url": "https://secure.artlogiconline.com/taymourgrahne", 
    "site_name": "Taymour Grahne Gallery"
  }, 
  "tbdxles": {
    "aol3_url": "https://app.artlogic.net/tbdxles", 
    "old_url": "https://secure.artlogiconline.com/tbdxles", 
    "site_name": "TBD Art Ltd"
  }, 
  "thedotproject": {
    "aol3_url": "https://app.artlogic.net/thedotproject", 
    "old_url": "https://secure.artlogiconline.com/thedotproject", 
    "site_name": "The Dot Project"
  }, 
  "thierrybigaignon": {
    "aol3_url": "https://app.artlogic.net/thierrybigaignon", 
    "old_url": "https://secure.artlogiconline.com/thierrybigaignon", 
    "site_name": "Galerie Thierry Bigaignon"
  }, 
  "thomasdane": {
    "aol3_url": "https://app.artlogic.net/thomasdane", 
    "old_url": "https://secure.artlogiconline.com/thomasdane", 
    "site_name": "THOMAS DANE GALLERY"
  }, 
  "thomasdanelimited": {
    "aol3_url": "https://app.artlogic.net/thomasdanelimited", 
    "old_url": "https://secure.artlogiconline.com/thomasdanelimited", 
    "site_name": "Thomas Dane Limited"
  }, 
  "timothytaylor": {
    "aol3_url": "https://app.artlogic.net/timothytaylor", 
    "old_url": "https://secure.artlogiconline.com/timothytaylor", 
    "site_name": "Timothy Taylor"
  }, 
  "timothytaylor16x34": {
    "aol3_url": "https://app.artlogic.net/timothytaylor16x34", 
    "old_url": "https://secure.artlogiconline.com/timothytaylor16x34", 
    "site_name": "Timothy Taylor 16x34"
  }, 
  "tobyziegler": {
    "aol3_url": "https://app.artlogic.net/tobyziegler", 
    "old_url": "https://secure.artlogiconline.com/tobyziegler", 
    "site_name": "Toby Ziegler Studio"
  }, 
  "tomdean": {
    "aol3_url": "https://app.artlogic.net/tomdean", 
    "old_url": "https://secure.artlogiconline.com/tomdean", 
    "site_name": "Thompson Dean"
  }, 
  "tomfordcollection": {
    "aol3_url": "https://app.artlogic.net/tomfordcollection", 
    "old_url": "https://secure.artlogiconline.com/tomfordcollection", 
    "site_name": "Tom Ford"
  }, 
  "triangle": {
    "aol3_url": "https://app.artlogic.net/triangle", 
    "old_url": "https://secure.artlogiconline.com/triangle", 
    "site_name": "Triangle"
  }, 
  "tristanhoaregallery": {
    "aol3_url": "https://app.artlogic.net/tristanhoaregallery", 
    "old_url": "https://secure.artlogiconline.com/tristanhoaregallery", 
    "site_name": "Tristan Hoare"
  }, 
  "tyburngallery": {
    "aol3_url": "https://app.artlogic.net/tyburngallery", 
    "old_url": "https://secure.artlogiconline.com/tyburngallery", 
    "site_name": "Tyburn Gallery"
  }, 
  "uandi": {
    "aol3_url": "https://app.artlogic.net/uandi", 
    "old_url": "https://secure.artlogiconline.com/uandi", 
    "site_name": "Development Securities"
  }, 
  "ullensfoundation": {
    "aol3_url": "https://app.artlogic.net/ullensfoundation", 
    "old_url": "https://secure.artlogiconline.com/ullensfoundation", 
    "site_name": "Fondation Guy et Myriam Ullens"
  }, 
  "unitlondon": {
    "aol3_url": "https://app.artlogic.net/unitlondon", 
    "old_url": "https://secure.artlogiconline.com/unitlondon", 
    "site_name": "Unit London"
  }, 
  "ursfischer": {
    "aol3_url": "https://app.artlogic.net/ursfischer", 
    "old_url": "https://secure.artlogiconline.com/ursfischer", 
    "site_name": "Urs Fischer LLC"
  }, 
  "vandermeij": {
    "aol3_url": "https://app.artlogic.net/vandermeij", 
    "old_url": "https://secure.artlogiconline.com/vandermeij", 
    "site_name": "Van der Meij Fine Arts C.V."
  }, 
  "vartai": {
    "aol3_url": "https://app.artlogic.net/vartai", 
    "old_url": "https://secure.artlogiconline.com/vartai", 
    "site_name": "Galerija Vartai"
  }, 
  "venusoverlosangeles": {
    "aol3_url": "https://app.artlogic.net/venusoverlosangeles", 
    "old_url": "https://secure.artlogiconline.com/venusoverlosangeles", 
    "site_name": "Venus Over Los Angeles"
  }, 
  "victoriamiro": {
    "aol3_url": "https://app.artlogic.net/victoriamiro", 
    "old_url": "https://secure.artlogiconline.com/victoriamiro", 
    "site_name": "Victoria Miro"
  }, 
  "vigogallery": {
    "aol3_url": "https://app.artlogic.net/vigogallery", 
    "old_url": "https://secure.artlogiconline.com/vigogallery", 
    "site_name": "Vigo Gallery"
  }, 
  "villalenafoundation": {
    "aol3_url": "https://app.artlogic.net/villalenafoundation", 
    "old_url": "https://secure.artlogiconline.com/villalenafoundation", 
    "site_name": "Villa Lena Foundation"
  }, 
  "vilmagold": {
    "aol3_url": "https://app.artlogic.net/vilmagold", 
    "old_url": "https://secure.artlogiconline.com/vilmagold", 
    "site_name": "Vilma Gold"
  }, 
  "vinylfactory": {
    "aol3_url": "https://app.artlogic.net/vinylfactory", 
    "old_url": "https://secure.artlogiconline.com/vinylfactory", 
    "site_name": "The Vinyl Factory"
  }, 
  "vladey": {
    "aol3_url": "https://app.artlogic.net/vladey", 
    "old_url": "https://secure.artlogiconline.com/vladey", 
    "site_name": "VLADEY"
  }, 
  "vonbartha": {
    "aol3_url": "https://app.artlogic.net/vonbartha", 
    "old_url": "https://secure.artlogiconline.com/vonbartha", 
    "site_name": "VON BARTHA"
  }, 
  "whiterainbow": {
    "aol3_url": "https://app.artlogic.net/whiterainbow", 
    "old_url": "https://secure.artlogiconline.com/whiterainbow", 
    "site_name": "White Rainbow"
  }, 
  "whitneyferrare": {
    "aol3_url": "https://app.artlogic.net/whitneyferrare", 
    "old_url": "https://secure.artlogiconline.com/whitneyferrare", 
    "site_name": "Whitney Ferrare"
  }, 
  "workplace": {
    "aol3_url": "https://app.artlogic.net/workplace", 
    "old_url": "https://secure.artlogiconline.com/workplace", 
    "site_name": "Workplace Gallery"
  }, 
  "wykehamgallery": {
    "aol3_url": "https://app.artlogic.net/wykehamgallery", 
    "old_url": "https://secure.artlogiconline.com/wykehamgallery", 
    "site_name": "Wykeham Gallery"
  }, 
  "xva": {
    "aol3_url": "https://app.artlogic.net/xva", 
    "old_url": "https://secure.artlogiconline.com/xva", 
    "site_name": "XVA Gallery"
  }, 
  "yaelbartana": {
    "aol3_url": "https://app.artlogic.net/yaelbartana", 
    "old_url": "https://secure.artlogiconline.com/yaelbartana", 
    "site_name": "Yael Bartana"
  }, 
  "zuleika": {
    "aol3_url": "https://app.artlogic.net/zuleika", 
    "old_url": "https://secure.artlogiconline.com/zuleika", 
    "site_name": "Zuleika Gallery"
  }
}

# spread_sheet = []

# for account, settings in dict.items():
#     row = {}
#     row['account'] = account
#     for setting, value in settings.items():
#         row[setting] = value
#     spread_sheet.append(row)

# if spread_sheet:
#     rows_to_excel('./WowItWorks.xls', spread_sheet, ['account', 'aol3_url','site_name','old_url'])


a_list = []

for account, keys in a_dict.items():
  rows = {}
  rows['Gallery Name'] = account
  for key, value in keys.items():
    rows[key] = value
  a_list.append(rows)


rows_to_excel('./Yessss.xls', a_list, ['Gallery Name', 'aol3_url', 'site_name', 'old_url'])




















