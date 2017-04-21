""" Enter all columns in string_to_list function, then copy and paste the returned list in _helper_filter_data function."""

def string_to_list(a_str):
    a_list = a_str.split()
    return a_list

a = string_to_list("WorkID  DateSaved   User    InventoryNumber ArtistID    StatusID    LocationID  OwnerID MediaID TypeID  PictureFile AspectRatio YearE   YearF   TitleE  TitleF  WebNotesE   WebNotesF   WebMemoE    WebMemoF    OtherMediaE OtherMediaF MediaSize   Depth   Width   Height  Notes   LiteratureE LiteratureF ProvenanceE ProvenanceF ExhibitionE ExhibitionF DateReceived    OriginalCost    AdditionalCost  ConfidentialNotes   CostNotes   LastTransactionID   LastTransactionDate Price   PriceSold   DateSold    Invoice SoldTo  SellNotes   OnArtistsPage   ShowPrice   HideSoldOnWeb   OnExhibition1   OnExhibition2   OnExhibition3   OnExhibition4   OnExhibition5   OnExhibition6   OnExhibition7   OnExhibition8   OnExhibition9   OnExhibition10  Exh1SortKey1    Exh1SortKey2    Exh1SortKey3    Exh1SortKey4    Exh1SortKey5    Exh1SortKey6    Exh1SortKey7    Exh1SortKey8    Exh1SortKey9    Exh1SortKey10   ArtistPageSortKey   ReservedUntil   ReservedBy  HighlightDate   ShowOnHomepage  ShowOnArchive   NewAquisition   NewAquisitionDate   ExhID1  ExhID2  ExhID3  ExhID4  ExhID5  ExhID6  ExhID7  ExhID8  ExhID9  ExhID10 RelatedWID  Verso   HighlightLinkE  HighlightLinkF  BlockFromWebsite    SB  Consignee   Images  Caption1E   Caption2E   Caption3E   Caption1F   Caption2F   Caption3F   Location    KeyWords    Signed  Dated   Circa   Year    KeyWordsF")
# print a
# print len(a)


def _helper_filter_data(self, row):
    #Put all the column names which you think can contains mix data
    columns = ['WorkID', 'DateSaved', 'User', 'InventoryNumber', 'ArtistID', 'StatusID', 'LocationID', 'OwnerID', 'MediaID', 'TypeID', 'PictureFile', 'AspectRatio', 'YearE', 'YearF', 'TitleE', 'TitleF', 'WebNotesE', 'WebNotesF', 'WebMemoE', 'WebMemoF', 'OtherMediaE', 'OtherMediaF', 'MediaSize', 'Depth', 'Width', 'Height', 'Notes', 'LiteratureE', 'LiteratureF', 'ProvenanceE', 'ProvenanceF', 'ExhibitionE', 'ExhibitionF', 'DateReceived', 'OriginalCost', 'AdditionalCost', 'ConfidentialNotes', 'CostNotes', 'LastTransactionID', 'LastTransactionDate', 'Price', 'PriceSold', 'DateSold', 'Invoice', 'SoldTo', 'SellNotes', 'OnArtistsPage', 'ShowPrice', 'HideSoldOnWeb', 'OnExhibition1', 'OnExhibition2', 'OnExhibition3', 'OnExhibition4', 'OnExhibition5', 'OnExhibition6', 'OnExhibition7', 'OnExhibition8', 'OnExhibition9', 'OnExhibition10', 'Exh1SortKey1', 'Exh1SortKey2', 'Exh1SortKey3', 'Exh1SortKey4', 'Exh1SortKey5', 'Exh1SortKey6', 'Exh1SortKey7', 'Exh1SortKey8', 'Exh1SortKey9', 'Exh1SortKey10', 'ArtistPageSortKey', 'ReservedUntil', 'ReservedBy', 'HighlightDate', 'ShowOnHomepage', 'ShowOnArchive', 'NewAquisition', 'NewAquisitionDate', 'ExhID1', 'ExhID2', 'ExhID3', 'ExhID4', 'ExhID5', 'ExhID6', 'ExhID7', 'ExhID8', 'ExhID9', 'ExhID10', 'RelatedWID', 'Verso', 'HighlightLinkE', 'HighlightLinkF', 'BlockFromWebsite', 'SB', 'Consignee', 'Images', 'Caption1E', 'Caption2E', 'Caption3E', 'Caption1F', 'Caption2F', 'Caption3F', 'Location', 'KeyWords', 'Signed', 'Dated', 'Circa', 'Year', 'KeyWordsF']
    result = {'emails': [], 'phones': [], 'websites' :[]}
    website_ends = ['.com', '.ca', '.net', '.org', '.uk', '.fr', '.tv', 'in', '.edu', '.mx', '.ch']
    for column in columns:
        value = self._prep_text_field(row, column)

        try:
            value_extension = value.rsplit('.', 1)[1]
        except Exception, e:
            value_extension = ''

        if value and value != '':
            if '@' in value:
                result['emails'].append(value)

            elif value_extension and '.%s'%value_extension in website_ends:
                result['websites'].append(value)

            elif 'www' in value or 'http' in value:
                result['websites'].append(value)

            elif len([x for x in value if x.isdigit()]) >= 8:
                result['phones'].append(value)
    return result

def _working(value):
    result = {'emails': [], 'phones': [], 'websites' :[]}
    website_ends = ['.com', '.ca', '.net', '.org', '.uk', '.fr', '.tv', 'in', '.edu', '.mx', '.ch']

    try:
        value_extension = value.rsplit('.', 1)[1]

    except Exception, e:
        value_extension = ''

    if value and value != '':
        if '@' in value:
            result['emails'].append(value)

        elif value_extension and '.%s'%value_extension in website_ends:
            result['websites'].append(value)

        elif 'www' in value or 'http' in value:
            result['websites'].append(value)

        elif len([x for x in value if x.isdigit()]) >= 8:
            result['phones'].append(value)
    return result

print _working("fuebfe898488unvbv45749859489h.org")




