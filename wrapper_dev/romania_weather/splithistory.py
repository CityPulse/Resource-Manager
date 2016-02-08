__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

import csv
import os.path


def niceFilename(org):
    return org.replace('(', '_').replace(')', '_').replace(' ', '_').replace('/', '_').lower()

if __name__ == "__main__":
    writers = {}
    ids = {
        "Arad": "POINT(21.31 46.19)",
        "Bacau": "POINT(26.91 46.57)",
        "Baia Mare": "POINT(23.57 47.65)",
        "Barlad": "POINT(27.67 46.23)",
        "Bistrita": "POINT(24.04 45.19)",
        "Botosani": "POINT(26.67 47.75)",
        "Braila": "POINT(27.97 45.28)",
        "Brasov": "POINT(25.60 45.65)",
        "Bucuresti": "POINT(26.1 44.44)",
        "Buzau": "POINT(26.82 45.15)",
        "Calarasi": "POINT(23.85 46.48)",
        "Cluj-Napoca": "POINT(23.61 46.78)",
        "Constanta": "POINT(28.63 44.18)",
        "Craiova": "POINT(23.8 44.32)",
        "Deva": "POINT(22.9 45.88)",
        "Drobeta Turnu Severin": "POINT(22.66 44.63)",
        "Focsani": "POINT(27.18 45.69)",
        "Galati": "POINT(28.04 45.44)",
        "Iasi": "POINT(27.58 47.16)",
        "Ploiesti": "POINT(26.02 44.94)",
        "Piatra-Neamt": "POINT(26.37 46.93)",
        "Ramnicu Valcea": "POINT(24.37 45.10)",
        "Roman": "POINT(26.92 46.92)",
        "Satu Mare": "POINT(22.88 47.78)",
        "Sibiu": "POINT(24.15 45.79)",
        "Slatina": "POINT(24.36 44.42)",
        "Suceava": "POINT(26.15 47.60)",
        "Targu-Mures": "POINT(24.55 46.54)",
        "Timisoara": "POINT(21.23 45.76)",
        "Tulcea": "POINT(28.79 45.17)"
    }
    drops = {}
    for _id in ids:
        fileobj = open(os.path.join("historicdata", "weatherAW-%s.csv" % (niceFilename(_id),)), "wb")
        __id = _id.lower()
        writers[__id] = csv.writer(fileobj, delimiter=';')

    src = open(os.path.join("historicdata", "temperatureeventAW.csv"), "rb")
    src = csv.reader(src, quotechar='"', delimiter=',')

    headers = src.next()
    for w in writers:
        writers[w].writerow(headers)

    for row in src:
        _id = row[1].lower()
        if _id in writers:
            writers[_id].writerow(row)
        else:
            if _id in drops:
                drops[_id] += 1
            else:
                drops[_id] = 1
        print "AW", row

    ids_mr = {
        "ADAMCLISI": "POINT(27.96 44.09)",
        "ADJUD": "POINT(27.18 46.1)",
        "ALBA IULIA": "POINT(23.57 46.07)",
        "ALEXANDRIA": "POINT(25.33 43.97)",
        "ARAD": "POINT(21.32 46.17)",
        "BACAU": "POINT(26.92 46.58)",
        "BACLES": "POINT(23.12 44.49)",
        "BAIA MARE": "POINT(23.58 47.67)",
        "BAILE HERCULANE": "POINT(22.41 44.88)",
        "BAILESTI": "POINT(23.35 44.03)",
        "BAISOARA": "POINT(23.46 46.58)",
        "BALEA LAC": "POINT(24.61 45.60)",
        "BANLOC": "POINT(21.14 45.39)",
        "BARAOLT": "POINT(25.6 46.08)",
        "BARLAD:": "POINT(27.67 46.23)",
        "BARNOVA RADAR": "POINT(27.63 47.07)",
        "BATOS": "POINT(24.65 46.89)",
        "BECHET": "POINT(24.18 44.39)",
        "BISOCA": "POINT(26.71 45.54)",
        "BISTRITA": "POINT(24.49 47.13)",
        "BLAJ": "POINT(23.91 46.18)",
        "BOITA": "POINT(24.26 45.63)",
        "BOROD": "POINT(22.61 46.99)",
        "BOTOSANI": "POINT(26.67 47.75)",
        "BOZOVICI": "POINT(22.0 44.93)",
        "BRAILA": "POINT(27.96 45.27)",
        "BRASOV GHIMBAV": "POINT(25.51 45.66)",
        "BUCIN": "POINT(25.42 46.68)",
        "BUCURESTI AFUMATI": "POINT(26.25 44.53)",
        "BUCURESTI BANEASA": "POINT(26.08 44.49)",
        "BUCURESTI FILARET": "POINT(26.08 44.42)",
        "BUZAU": "POINT(26.82 45.15)",
        "CALAFAT": "POINT(22.94 43.99)",
        "CALARASI": "POINT(27.34 44.2)",
        "CALIMANI RETITIS": "POINT(25.24 47.09)",
        "CAMPENI BISTRA": "POINT(23.05 46.36)",
        "CAMPINA": "POINT(25.74 45.13)",
        "CAMPULUNG MUSCEL": "POINT(25.05 45.27)",
        "CARACAL": "POINT(24.35 44.11)",
        "CARANSEBES": "POINT(22.22 45.42)",
        "CEAHLAU TOACA": "POINT(25.95 46.98)",
        "CERNAVODA": "POINT(28.03 44.34)",
        "CHISINEU CRIS": "POINT(21.52 46.52)",
        "CLUJ-NAPOCA": "POINT(23.58 46.76)",
        "CONSTANTA": "POINT(28.64 44.17)",
        "CORUGEA": "POINT(28.34 44.74)",
        "COTNARI": "POINT(26.94 47.35)",
        "CRAIOVA": "POINT(23.8 44.32)",
        "CUNTU": "POINT(24.14 45.59)",
        "CURTEA DE ARGES": "POINT(24.68 45.14)",
        "DARABANI": "POINT(28.3 43.79)",
        "DEDULES": None,
        "DEDULESTI-MORARESTI": "POINT(24.53 45.01)",
        "DEJ": "POINT(23.88 47.14)",
        "DEVA": "POINT(22.9 45.88)",
        "DRAGASANI": "POINT(24.26 44.66)",
        "DROBETA TURNU SEVERIN": "POINT(22.67 44.63)",
        "DUMBRAVENI": "POINT(24.58 46.23)",
        "DUMBRAVITA DE CODRU": "POINT(22.16 46.66)",
        "FAGARAS": "POINT(24.97 45.84)",
        "FETESTI": "POINT(27.83 44.37)",
        "FOCSANI": "POINT(27.18 45.7)",
        "FUNDATA": "POINT(25.29 45.44)",
        "FUNDULEA": "POINT(26.52 44.45)",
        "GALATI": "POINT(28.04 45.42)",
        "GIURGIU": "POINT(25.97 43.9)",
        "GORGOVA": "POINT(29.17 45.18)",
        "GRIVITA": "POINT(27.65 45.72)",
        "GURA PORTITEI": "POINT(29.00 44.69)",
        "GURAHONT": "POINT(22.34 46.27)",
        "HALANGA": "POINT(22.69 44.68)",
        "HARSOVA": "POINT(27.95 44.69)",
        "HOLOD": "POINT(22.13 46.79)",
        "HUEDIN": "POINT(23.03 46.87)",
        "IASI": "POINT(27.59 47.16)",
        "IEZER": "POINT(26.34 47.99)",
        "INTORSURA BUZAULUI": "POINT(26.03 45.67)",
        "JIMBOLIA": "POINT(20.72 45.79)",
        "JOSENI": "POINT(25.5 46.7)",
        "JURILOVCA": "POINT(28.87 44.76)",
        "LACAUTI": "POINT(26.02 44.93)",
        "LUGOJ": "POINT(21.9 45.69)",
        "MAHMUDIA": "POINT(29.08 45.08)",
        "MANGALIA": "POINT(28.58 43.82)",
        "MEDGIDIA": "POINT(28.27 44.25)",
        "MIERCUREA CIUC": "POINT(25.81 46.36)",
        "MOLDOVA VECHE": "POINT(21.62 44.72)",
        "NEGRESTI VASLUI": "POINT(27.46 46.83)",
        "OBARSIA LOTRULUI": "POINT(23.63 45.44)",
        "OCNA SUGATAG": "POINT(23.93 47.78)",
        "ODORHEIUL SECUIESC": "POINT(25.29 46.3)",
        "OLTENITA": "POINT(26.64 44.09)",
        "ORADEA": "POINT(21.92 47.07)",
        "ORAVITA": "POINT(21.68 45.03)",
        "PADES APA NEAGRA": "POINT(22.86 45.0)",
        "PALTINIS": "POINT(23.93 45.66)",
        "PARANG": "POINT(23.56 45.34)",
        "PATARLAGELE": "POINT(26.36 45.32)",
        "PENTELEU": "POINT(26.41 45.60)",
        "PETROSANI": "POINT(23.37 45.42)",
        "PIATRA NEAMT": "POINT(26.37 46.93)",
        "PITESTI": "POINT(24.88 44.86)",
        "PLOIESTI": "POINT(26.02 44.94)",
        "POIANA STAMPEI": "POINT(25.14 47.32)",
        "POLOVRAGI": "POINT(23.81 45.17)",
        "PREDEAL": "POINT(25.58 45.5)",
        "RADAUTI": "POINT(25.92 47.84)",
        "RAMNICU SARAT": "POINT(27.06 45.38)",
        "RAMNICU VALCEA": "POINT(24.38 45.1)",
        "RESITA": "POINT(21.89 45.3)",
        "ROMAN": "POINT(26.92 46.92)",
        "ROSIA MONTANA": "POINT(23.13 46.31)",
        "ROSIORII DE VEDE": "POINT(24.99 44.11)",
        "SACUIENI": "POINT(22.11 47.34)",
        "SANNICOLAU MARE": "POINT(20.63 46.07)",
        "SARMASU": "POINT(24.16 46.75)",
        "SATU MARE": "POINT(22.88 47.8)",
        "SEBES ALBA": "POINT(23.57 45.96)",
        "SEMENIC": "POINT(21.96 45.15)",
        "SFANTU GHEORGHE DELTA": "POINT(29.59 44.9)",
        "SFANTU GHEORGHE MUNTE": None,
        "SIBIU": "POINT(24.15 45.79)",
        "SIGHETUL MARMATIEI": "POINT(23.89 47.93)",
        "SINAIA 1500": "POINT(24.33 46.16)",
        "SIRIA": "POINT(21.63 46.26)",
        "SLATINA": "POINT(24.37 44.42)",
        "SLOBOZIA": "POINT(27.37 44.56)",
        "STANA DE VALE": "POINT(26.08 44.41)",
        "STEFANESTI STANCA": "POINT(27.2 47.82)",
        "STEI PETRU GROZA": "POINT(22.47 46.53)",
        "STOLNICI": "POINT(24.78 44.57)",
        "SUCEAVA": "POINT(26.26 47.65)",
        "SULINA": "POINT(29.65 45.16)",
        "SUPURU DE JOS": "POINT(22.79 47.47)",
        "TARCU": None,
        "TARGOVISTE": "POINT(21.83 45.82)",
        "TARGU JIU": "POINT(23.28 45.04)",
        "TARGU LAPUS": "POINT(23.86 47.45)",
        "TARGU LOGRESTI": "POINT(23.71 44.87)",
        "TARGU MURES": "POINT(24.56 46.54)",
        "TARGU NEAMT": "POINT(26.36 47.2)",
        "TARGU OCNA": "POINT(26.62 46.28)",
        "TARGU SECUIESC": "POINT(26.14 46.0)",
        "TARNAVENI BOBOHALMA": "POINT(24.24 46.35)",
        "TEBEA": "POINT(22.73 46.17)",
        "TECUCI": "POINT(27.43 45.85)",
        "TIMISOARA": "POINT(21.23 45.76)",
        "TITU": "POINT(25.57 44.66)",
        "TOPLITA": "POINT(25.35 46.92)",
        "TULCEA": "POINT(28.79 45.17)",
        "TURDA": "POINT(23.79 46.57)",
        "TURNU MAGURELE": "POINT(24.87 43.75)",
        "URZICENI": "POINT(26.64 44.72)",
        "VARADIA DE MURES": "POINT(22.16 46.01)",
        "VARFUL OMU": "POINT(25.45 45.44)",
        "VASLUI": "POINT(27.73 46.64)",
        "VIDELE": "POINT(25.53 44.28)",
        "VLADEASA 1400": None,
        "VLADEASA 1800": "POINT(24.51 46.52)",
        "VOINEASA": "POINT(23.96 45.42)",
        "ZALAU": "POINT(23.05 47.18)",
        "ZIMNICEA": "POINT(25.37 43.65)"
    }

    src = open(os.path.join("historicdata", "temperatureeventMR.csv"), "rb")
    src = csv.reader(src, quotechar='"', delimiter=',')
    writers = {}
    drops_mr = {}
    for _id in ids_mr:
        fileobj = open(os.path.join("historicdata", "weatherMR-%s.csv" % (niceFilename(_id),)), "wb")
        writers[_id] = csv.writer(fileobj, delimiter=';')

    headers = src.next()
    for w in writers:
        writers[w].writerow(headers)

    for row in src:
        _id = row[1]
        if _id in writers:
            writers[_id].writerow(row)
        else:
            if _id in drops_mr:
                drops_mr[_id] += 1
            else:
                drops_mr[_id] = 1
        print "MR", row

    print
    print drops
    print drops_mr
    print

    # # look which ids are in both
    # nice = map(lambda x: niceFilename(x), ids)
    # nice2 = map(lambda x: niceFilename(x), ids_mr)
    # print nice
    # print nice2
    # print
    # both = filter(lambda x: x in nice2, nice)
    # print both
    # both2 = filter(lambda x: x in nice, nice2)
    # print both2
