import re

def pl_slo(input_pl):
        word_pl = input_pl.lower()


        word_pl = word_pl.replace("cz", "č#").replace("sz", "š#").replace("ż", "ž#")
        word_pl = word_pl.replace("rz", "r#").replace("j", "j#")
        word_pl = re.sub("r#([aou])", "rj\\1", word_pl)
        word_pl = word_pl.replace("#y", "i").replace("#ę", "e").replace("#ą", "e").replace("#", "")
        word_pl = word_pl.replace("ci", "ti").replace("dzi", "di")
        word_pl = word_pl.replace("ia", "ja").replace("ie", "e")
        word_pl = word_pl.replace("io", "jo").replace("iu", "ju")
        word_pl = word_pl.replace("ią", "e").replace("ię", "e")
        word_pl = re.sub("[ąę]", "u", word_pl)

        word_pl = word_pl.replace("l", "lj").replace("ł", "l")
        word_pl = word_pl.replace("x", "ks").replace("ch", "h").replace("w", "v")
        word_pl = word_pl.replace("ć", "t").replace("dź", "d")
        word_pl = word_pl.replace("ś", "s").replace("ź", "z")
        word_pl = word_pl.replace("ń", "nj").replace("njs", "ns").replace("jj", "j")
        word_pl = word_pl.replace("ó", "o").replace("y", "i")

        return word_pl



def reverse_flavorize(word, pos, feats, src_lang):
    print(word)
    if src_lang == "pl": return pl_slo(word)
    
    
    
    
    
    else: return word
