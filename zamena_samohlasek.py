def vymena_samohlasek(text):
    kratke_samohlasky = [“a”,"e","ě","o","u","y"]                #samohlasky bez i
    dlouhe_samohlasky = ["á","é","ó","ů","ú","ý"]                #samohlasky bez í
 
    for kl_sam in kratke_samohlasky:                             #pro vsechny krate samohlasky
        while text.find(kl_sam) >= 0:                            #dokud se tam vyskytuje
            pozice_sam = text.find(kl_sam)
            text = text[:pozice_sam] + "i" + text[pozice_sam+1:] #ji vymenim za i
        

    for kl_sam in dlouhe_samohlasky:                             #pro vsechny dlouhe samohlasky
        while text.find(kl_sam) >= 0:                            #dokud se tam vyskytuje
            pozice_sam = text.find(kl_sam)
            text = text[:pozice_sam] + "í" + text[pozice_sam+1:] #ji vymenim za í

    return text 
