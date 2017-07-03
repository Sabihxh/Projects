string = """ FAILED: no rec_id for filename  The Leader 1984.jpg
                            FAILED: no rec_id for filename Arrows 2009.jpg
                            FAILED: no rec_id for filename Black Out.jpg
                            FAILED: no rec_id for filename City Spray 2009.jpg
                            FAILED: no rec_id for filename Door Rider.jpg
                            FAILED: no rec_id for filename Frazzled 2009.jpg
                            FAILED: no rec_id for filename Glitter 2009.jpg
                            FAILED: no rec_id for filename Gold Rush 2009.jpg
                            FAILED: no rec_id for filename Horse & Rider.jpg
                            FAILED: no rec_id for filename images_renamed.py
                            FAILED: no rec_id for filename NoodleInc.jpg
                            FAILED: no rec_id for filename Pretty One 2009.jpg
                            FAILED: no rec_id for filename PurpleShadow ps.jpg
                            FAILED: no rec_id for filename PurpleShadow.jpg
                            FAILED: no rec_id for filename Red Shadow Head.jpg
                            FAILED: no rec_id for filename Rocket Man 2011.jpg
                            FAILED: no rec_id for filename Rodeo edition.jpg
                            FAILED: no rec_id for filename Round Head 2009.jpg
                            FAILED: no rec_id for filename Spray 2009.jpg
                            FAILED: no rec_id for filename Spray Train.jpg
                            FAILED: no rec_id for filename SprayTime.jpg
                            FAILED: no rec_id for filename Standing Shadow.jpg
                            FAILED: no rec_id for filename Standing Shadow1.jpg
                            FAILED: no rec_id for filename Stop sign LE.jpg
                            FAILED: no rec_id for filename Tall Shadow 2009.jpg
                            FAILED: no rec_id for filename Tall Spray 2009.jpg
                            FAILED: no rec_id for filename Thinkable.jpg
                            FAILED: no rec_id for filename Venus 2009.jpg
                            FAILED: no rec_id for filename Walking Head 1984.jpg
                            FAILED: no rec_id for filename Wash Spray 2009.jpg
                            FAILED: no rec_id for filename Washer 2009.jpg
                            FAILED: no rec_id for filename WHRHXXLS1005.jpg
                            FAILED: no rec_id for filename Winkler 2009.jpg
                            FAILED: no rec_id for filename X-Men 2009.jpg
                            """
a_list = string.split('\n')
final_list = []
for item in a_list:

    print item.replace('FAILED: no rec_id for filename', '').strip()







