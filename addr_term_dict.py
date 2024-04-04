province_lst = ["on", "ab", "bc", "ns", "nb", "pe", "qc", "sk", "mb", "nt"]

# Everything in value list will be standardized as key
to_non_stand_prov = {
    "ab": ["alberta"],
    "bc": ["british columbia", "b.c.", "b. c."],
    "mb": ["manitoba"],
    "nb": ["new brunswick", "n.b."],
    "ns": ["nova scotia", "n.s.", "n. s."],
    "nt": ["northwest territories", "n.t.", "nwt"],
    "nu": ["nunavut"],
    "on": ["ontario"],
    "pe": ["prince edward island", "pei", "p. e. i.", "p.e.i"],
    "qc": ["quebec"],
    "sk": ["saskatchewan"],
    "yt": ["yukon", "the yukon", "yukon territory"],
    "nl": ["newfoundland and labrador", "n. l.", "n.l."],
}


to_non_stand_street_dir = {
    "e": ["east", "e."],
    "n": ["north", "n.", "nrt", "nrth", "northern"],
    "ne": [
        "northeast",
        "north east",
        "northe",
        "north e",
        "neast",
        "n east",
        "ne",
        "n e",
        "nrteast",
        "nrt east",
        "nrte",
        "nrt e",
        "nrtheast",
        "nrth east",
        "nrthe",
        "nrth e",
        "ntheast",
        "nth east",
        "nthe",
        "nth e",
        "norheast",
        "norh east",
        "norhe",
        "norh e",
        "norteast",
        "nort east",
        "norte",
        "nort e",
    ],
    "nw": [
        "northwest",
        "north west",
        "northw",
        "north w",
        "northwst",
        "north wst",
        "nwest",
        "n west",
        "n w",
        "nwst",
        "n wst",
        "nrtwest",
        "nrt west",
        "nrtw",
        "nrt w",
        "nrtwst",
        "nrt wst",
        "nrthwest",
        "nrth west",
        "nrthw",
        "nrth w",
        "nrthwst",
        "nrth wst",
        "nthwest",
        "nth west",
        "nthw",
        "nth w",
        "nthwst",
        "nth wst",
        "norhwest",
        "norh west",
        "norhw",
        "norh w",
        "norhwst",
        "norh wst",
        "nortwest",
        "nort west",
        "nortw",
        "nort w",
        "nortwst",
        "nort wst",
    ],
    "s": ["south", "so", "sth"],
    "se": [
        "southeast",
        "south east",
        "southe",
        "south e",
        "seast",
        "s east",
        "s e",
        "soeast",
        "so east",
        "so e",
        "stheast",
        "sth east",
        "sthe",
        "sth e",
    ],
    "sw": [
        "southwest",
        "south west",
        "southw",
        "south w",
        "southwst",
        "south wst",
        "swest",
        "s west",
        "s w",
        "swst",
        "s wst",
        "sowest",
        "so west",
        "so w",
        "sowst",
        "so wst",
        "sthwest",
        "sth west",
        "sthw",
        "sth w",
        "sthwst",
        "sth wst",
    ],
    "w": ["west", "wst"],
}

to_non_stand_num_term = {
    "unit": [
        "suite",
        "apt",
        "apartment",
        "ste",
    ],  # unit is special case stuff like 123-43 king should eval to unit 123 43 king
    "po box": [
        "post office box",
        "p.o. box",
        "p.o box",
        "pobox",
        "postbox",
        "post box",
        "post box",
        "p o box",
        "p office box",
        "pb",
        "pob",
        "p o b",
        "post mail box",
        "post mail box",
        "pmb",
        "box",
        "box",
        "box",
    ],
    "ph" : [
        "penthouse",
        "pent house",
        "penth",
        "penthse",
        "pHouse",
        "pent.",
    ],
    "rr" : ["rr#", "rural road", "r road", "country road", "side road"]
}


to_non_stand_street_type = {
    "alley": ["aly", "ally"],
    "alwy": ["alleyway", "allyway", "allwy"],
    "anx": ["annex", "anex", "annx"],
    "arc": ["arcade"],
    "ave": ["avenue", "av", "aven", "avenu", "avn", "avnue"],
    "bayou": ["bayoo"],
    "bch": ["beach"],
    "bldg": ["building", "bdg", "bld", "blg"],
    "blf": ["bluf", "bluff"],
    "blfs": ["bluffs"],
    "blk": ["block"],
    "blvd": ["boulevard", "boul", "boulv"],
    "bnd": ["bend"],
    "bnglw": ["bungalow", "bongalow", "bunglow", "bungalo", "bngw"],
    "bot": ["bottom", "bottm", "btm"],
    "br": ["branch", "brnch"],
    "brg": ["bridge", "brdge"],
    "brgs": ["burgs"],
    "brk": ["brook", "break"],
    "brks": ["brooks"],
    "bsmt": ["basement", "bsm", "bsmnt", "basement", "bsment"],
    "byps": ["bypass", "bypa", "bps", "byp"],
    "cabin": ["cabn"],
    "circ": ["circle", "cir", "circel", "circles"],
    "clf": ["cliff"],
    "clfs": ["cliffs"],
    "cmn": ["common"],
    "cmns": ["commons"],
    "cmp" : ["camp"],
    "cnyn" : ["canyon", "cyn"],
    "cor" : ["corner"],
    "cors" : ["corners"],
    "cpe": ["cape"],
    "cresc": ["crescent", "crs", "crecent"],
    "crk": ["creek"],
    "crossing": ["xing", "crssing"],
    "crossroad" : ["cross road", "xroad"],
    "cswy": ["causeway", "cause way"],
    "ct" : ["court"],
    "ctyd" : ["court yard", "courtyard"],
    "ctr": ["center", "centre", "cent", "centr", "cnter", "cntr"],
    "curv" : ["curve"],
    "cv" : ["cove"],
    "cvs" : ["coves"],
    "dl" : ["dale"],
    "dm" : ["dam"],
    "div" : ["divide"],
    "dr": ["drive", "drv", "driv"],
    "drs" : ["drives"],
    "dupl": ["duplex", "dup"],
    "dvwy": ["driveway", "dway", "drive way"],
    "est": ["estate"],
    "ests" : ["estates"],
    "exp": ["express", "expressway", "express way", "expwy", "expw", "expr"],
    "fcty": ["fty", "fy"],
    "fl": [
        "floor",
        "flr",
        "f",
        "level",
        "lev",
        "levl",
        "lvel",
        "lvl",
        "platform",
        "pf",
        "storey",
    ],
    "fld": ["field"],
    "flds" : ["fields"],
    "fls" : ["falls"],
    "flt": ["flat"],
    "frd": ["ford"],
    "frds" : ["fords"],
    "frg" : ["forge", "forg"],
    "frgs" : ["forges"],
    "frk": ["fork"],
    "frst": ["forest"],
    "fry": ["ferry", "frry"],
    "fwy": ["freeway", "free way", "freewy"],
    "gdfl": [
        "ground floor",
        "gdfl",
        "gd fl",
        "gd/fl",
        "gd / fl",
        "gf",
        "ground level",
        "gd lvl",
        "g lvl",
        "g level",
        "gd level",
        "ground lvl",
        "lobby",
        "main floor",
    ],
    "gpo": ["general post office box", "gpo box"],
    "grdn": ["garden", "gardn"],
    "grn" : ["green"],
    "grns" : ["greens"],
    "grv": ["grove", "grov"],
    "grvs": ["groves"],
    "gym": ["gymnasium"],
    "hbr" : ["harbour", "hrbor"],
    "hbrs" : ["harbours"],
    "hl": ["hill"],
    "hls" : ["hills"],
    "hllw": ["hollow", "holw"],
    "hotl": ["hotel", "hot", "htel"],
    "hs": ["high school", "h s"],
    "hsp": ["hospital", "hos", "hosp", "hospice", "hosptl", "hsptl"],
    "hts": ["heights"],
    "hvn": ["haven"],
    "hwy": ["highway", "highwy"],
    "jct": ["junction", "jction", "juncton"],
    "jcts": ["junctions"],
    "ky" : ["key"],
    "kys" : ["keys"],
    "knl" : ["knoll"],
    "knls" : ["knolls"],
    "lck": ["lock"],
    "lcks": ["locks"],
    "ldg": ["lodge", "lodg", "ldge"],
    "lgt": ["light"],
    "lk" : ["lake"],
    "lks" : ["lakes"],
    "ln": ["lane"],
    "lp": ["loop"],
    "lwr": ["lower", "lowr"],
    "mdw": ["meadow"],
    "mdws" : ["meadows"],
    "ml" : ["mill"],
    "mls" : ["mills"],
    "mnr": ["manor"],
    "mnrs" : ["manors"],
    "msn" : ["mission"],
    "mt": ["mount"],
    "mtn": ["mountain"],
    "mtns": ["mountains"],
    "mtwy": ["motorway", "motor way"],
    "nck" : ["neck"],
    "orch": ["orchard", "orchrd"],
    "ovl": ["oval"],
    "ovlk" : ["overlook", "over look"],
    "opas" :  ["overpass","over pass"],
    "pkwy": ["parkway", "parkwy", "pkway", "prkwy", "prkway", "park way"],
    "pl": ["place", "pla", "plc", "plac"],
    "plz": ["plaza", "plza"],
    "prk": ["park"],
    "prt": ["port"],
    "psge" : ["passage"],
    "pt": ["point"],
    "pts": ["points"],
    "pth": ["path"],
    "pthwy": ["phwy","pway","pthway","pathway","ptway","ptwy", "pathwy"],
    "rd": ["road"],
    "rds" : ["roads"],
    "rdg": ["ridge", "rdge"],
    "rnch": ["ranch"],
    "rte": ["route"],
    "rvr": ["river", "riv", "rivr"],
    "skwy": ["skyway", "sky way"],
    "smt": ["summit"],
    "spg": ["spring", "sprng", "spng"],
    "spgs": ["springs"],
    "sq": ["square", "sqr"],
    "st" : ["str","stre","stree","strt", "street", "streets"],
    "stn": ["station", "statn", "sta"],
    "tce": ["terrace", "ter", "tr", "terr", "terace", "terrac", "terrasse", "tsse"],
    "tpke": ["turnpike", "trnpk", "turnpk"],
    "trfy": ["trafficway"],
    "trl": ["trail"],
    "trwy": ["throughway", "through way"],
    "twr": ["tower", "towers"],
    "u": ["university", "uni", "univ", "univers", "unvrsty"],
    "un": ["union"],
    "upas": ["underpass"],
    "upr": ["upper", "uppr", "up"],
    "vdct": ["viaduct", "viadct"],
    "vis": ["vista", "vst", "vsta", "vist"],
    "vl": ["ville"],
    "vlg": ["village", "vge", "vllg"],
    "vly": ["valley", "vallys", "vlly"],
    "vlys": ["valleys"],
    "wl" : ["wells"],
    "wy": ["way"],
}

to_non_std = {
    "st": ["saint", "st."],
    "1st" : ["first"],
    "2nd" : ["second"],
    "3rd" : ["third"],
    "4th" : ["fourth"],
    "5th" : ["fifth"],
    "6th" : ["sixth"],
    "7th" : ["seventh"],
    "8th" : ["eighth"],
    "9th" : ["ninth"],
}


to_stand_street_type = {i: k for k, v in to_non_stand_street_type.items() for i in v}
to_stand_street_dir = {i: k for k, v in to_non_stand_street_dir.items() for i in v}
to_std = {i : k for k,v in to_non_std.items() for i in v}


{
    # house","hse","hous","hs","ho
    # reserve","rsve","rsrv","rsv
    # tower","twr
    # townhouse","tnhs
    # trailer","trlr
    # villa","vlla","vl
    # center","c","ctr
    # central","c","cn","ctrl","cntrl
    # centre","c","ctr
    # block","blk","bl","blck
    # quadrant","qd","quad
    # section","sec","sect","sxn
    # township","twp","tshp
    # acres","acrs
    # access","accs
    # amble","ambl
    # anchorage","ancg
    # approach","app","apch","appr
    # arterial","artl
    # artery","art","arty
    # back","bk
    # bank","bnk
    # basin","basn","bsn
    # bayou","byu","bayoo
    # belt","blt
    # block","blk","blck
    # bottom","bot","bottm","btm","bttm
    # bottoms","bttms","btms","bottms
    # boundary","bdy
    # bowl","bl
    # brace","br","brce
    # "brk" : ["break"]
    # bridge","bdge","br","brdg","bri","brg
    # broadway","bdwy","bway","bwy","brdway
    # brook","brk
    # brooks","brks
    # brow","brw
    # butte","btte","bte
    # bypass","bypa","byps","bps","byp
    # byway","bywy
    # canyon","cyn","cnyn
    # caravan","cvan","cvn","c van
    # causeway","csway","cswy","causewy","caus","cause","cway
    # center","centre","cetr","cntr","ctr","c","cen
    # centers","ctrs
    # centreway","cnwy
    # chase","ch","chas
    # circuit","crct","circ","cct","cirt","ci","circt
    # circus","crcs","crc
    # claim","clm
    # cliff","clf
    # cliffs","clfs
    # close","cl","cls","clse
    # cluster","clr","clstr
    # colonnade","clde","clnde
    # common","cmmn","comm","cmn
    # commons","cmmns","cmns","comms
    # concord","cncd","cncrd
    # concession","conc
    # concourse","con","concs","concse","cnc
    # connection","cntn","cxn
    # connector","conr","cnctr","cntr
    # copse","cps
    # corner","cnr","crn","cor
    # corners","cnrs","crns","cors
    # corseo","cseo
    # corso","cso
    # course","crse
    # court","ct","crt
    # courts","crts","cts
    # courtyard","cyd","ctyd
    # creek","cr","crk
    # crest","crst","cst
    # crief","crf
    # croft","cft
    # cross","cs","crss
    # crossing","crsg","xing","csg","x ing","x-ing
    # crossroad","crd","cross road","xroad","x-road","x road","xrd","x-rd","x rd
    # crossroads","cross roads","xrds
    # crossway","cowy","crwy","xway","xwy","x-way","x way","x-wy","xwy
    # cruiseway","cuwy","crwy
    # cul
    # cul de sac","cul-de-sac","culdesac","cds","cusac","csac
    # curve","cve","crv","crve","curv
    # cutting","cttg","ctg","cutt
    # dale","dle
    # dell
    # dene
    # deviation","devn
    # dip
    # distributor","dstr
    # diversion","divers
    # down","dn
    # drove","drov
    # easement","esmt
    # edge","edg
    # elbow","elb
    # elm
    # end
    # entrance","ent","entr
    # esplanade","esp","espl
    # estate","est
    # estates","ests
    # exit
    # expressway","exp","expwy","expway","expy
    # extension","ex","ext","extn","exten
    # extensions","exts
    # fairway","fawy","fy
    # fall","fl
    # falls","fls
    # fare
    # farm","frm
    # farms","frms
    # fern
    # ferry","fry","fy
    # field","fld","fd
    # fields","flds","fds
    # fireline","fline","fire line","flne
    # firetrack","ftrk","fire track
    # firetrail","fit","fitr","fire trail
    # flat","fl","flt
    # follow","folw
    # footway","ftwy","foot way
    # ford","frd
    # foreshore","fshr","fore shore
    # formation","form","fmtn
    # freeway","frwy","fw","fwy","fway
    # front","frnt
    # frontage","frtg","fr
    # gap","gp
    # garden","gdn","grd","grdn
    # gardens","gdns","grds","grdns
    # gate","ga","gte
    # gates","gtes
    # gateway","gwy","gway","gtwy","gtway
    # glade","gl","gld","glde
    # glen","gln
    # grange","gra
    # green","grn","gn
    # ground","grnd
    # grounds","grnds
    # grove","gr","grv","grve","gro
    # gulch","glch
    # gully","gly
    # hanger","hngr
    # harbor","harbour","hbr","hrbr
    # harbors","hbrs
    # haven","hvn
    # head","hd
    # heads","hds
    # heath","hth
    # hill","hl
    # hills","hls
    # hollow","hllw
    # impasse","imp
    # inlet","inlt
    # interchange","intg","intchg","inter change
    # intersection","intn","inter section","intsctn
    # island","is","id","i","isl","isld
    # islands","iss","ids","islds
    # isle
    # junction","jct","jnc","jnct","jctn","jtn","junct","j
    # junctions","jcts
    # key","ky
    # keys","kys
    # knob
    # knoll","knol","knl
    # knolls","knls
    # ladder","ladr
    # lagoon","lagn","lgn","lagon
    # land
    # landing","ldg","lndg","landng
    # laneway","lnwy
    # lees
    # light","lgt","lt
    # limits","lmts
    # line","ln
    # link","lnk","lk
    # little","ltl","lttl","littl","litl","lit","lt
    # loaf","lf
    # lookout","lkt","look out
    # loop","lp
    # loops","lps
    # lot","lt
    # lynne","lynn
    # mall","ml
    # manor","mnr
    # maze
    # meadow","mdw
    # meadows","mdws
    # mead","md
    # meander","mndr","mdr","mr
    # mew","mw
    # mews","mws
    # mile","mi
    # mill","ml
    # mills","mls
    # moor
    # motorway","mway","mwy","mtwy
    # neaves","nvs
    # nook","nk
    # oaks
    # outlet","otlt
    # outlook","out","otlk
    # oval
    # overbridge","ovrb","over bridge
    # paddock","padk
    # palms","plms
    # parade","pde","prd","prde
    # parklands","pkld","pklds","parkland","park lands","park land
    # part","prt
    # pass","ps
    # passage","psge","pass
    # path","pth
    # pathway","phwy","pway","pthway","pthwy","ptway","ptwy
    # peninsula","psla
    # piazza","piaz","pzza
    # pike","pk
    # pine","pne","pn
    # pines","pns","pnes
    # port","pt","prt
    # plain","pln","pl
    # plains","plns","pls
    # plateau","plat","plt
    # plaza","plz","plza","pz
    # prarie","pr
    # pocket","pkt","pokt","pckt
    # point","piont","pnt","pt
    # pointe","pte","pnte
    # port","prt
    # ports","prts
    # prairie","pr
    # priors","prrs
    # private","pvt
    # promenade","prom","prm
    # pursuit","pur
    # quad","qd
    # quadrangle","qdgl
    # quadrant","qdrt","qd
    # quay","quy","qy
    # quays","quys","qys
    # radial","radl
    # ramble","ra","rmbl
    # ramp","rmp
    # ranae","ran
    # ranch","rnch
    # rapid","rpd
    # rapids","rpds
    # range","rng","rnge","rang
    # reach","rch
    # reef
    # reserve","res","resrv","resv","rsrv","rserv","rserve","rsrve
    # rest","rst
    # retreat","rt","rtt
    # return","rtn
    # ridge","rdge","rdg
    # ridges","rdgs
    # ridgeway","rgwy","rdgwy","ridge way
    # right of way","rowy","rightofway","rofw","row","r o w","r of w
    # ring
    # rise","ri
    # riverway","rvwy
    # riviera","rvra
    # roadside","rdsd","road side
    # roadway","rdwy","rdw","rdy
    # rocks","rks
    # ronde","rnde
    # rosebowl","rsbl","rose bowl
    # rotary","rty
    # round","rnd
    # roundabout
    # route","rt","rte
    # row","rw
    # run","rn
    # saint","st
    # sainte","ste
    # san","s
    # santa","sta
    # shoal","shl
    # shoals","shls
    # shore","shor","shr
    # shores","shors","shrs
    # shunt","shun","shnt
    # siding","sdng","sdg
    # skyway","skwy
    # slip
    # sound","snd
    # space","spc
    # spring","spg","sprng
    # spur","spr
    # square","sq","sqr
    # squares","sqs
    # stairs","strs
    # stairway","stwy","strwy","stair way","st.wy","st wy
    # steps","stps
    # strand","stra","strnd","strd
    # strands","strnds","strds
    # strip","strp
    # subdivision","subdiv
    # subway","sbwy
    # summit","smt","sumt
    # tarn","tn
    # thicket","thick
    # thoroughfare","thor","throughfare","thorough fare","thfr
    # thoroughway","thwy
    # throughway","thru","thro","thruway","trwy
    # tollway","tlwy","twy
    # top
    # tor
    # tower","twr
    # towers","twrs
    # townline","tline
    # trace","trce
    # track","tr","trk","trak
    # trafficway","trfy
    # trail","tr","trl
    # trailer","trlr
    # tram
    # tramway","tmwy
    # trees","trs
    # trunkway","tkwy
    # tunnel","tun","tunl
    # turnabout","trnabt
    # turn","tn","trn
    # turnpike","tpk","tpke
    # underpass","upas","upass","ups",""under pass"
    # union","un
    # unions","uns
    # vale","va","vl
    # valley","vlly","vly","vy
    # valleys","vlys","vllys
    # vennel
    # viaduct","via","viad","vdct","viadct
    # view","vw
    # views","vws
    # vista","vst","vsta","vis
    # vue
    # walk","wlk","wk
    # walkway","wkwy","wky","wlkwy
    # waters","wtrs
    # well","wl
    # wells","wls
    # wharf","whrf","whf
    # woods","wds
    # wynd","wyn
    # yard","yd","yrd
    # cape","cpe","cp
    # city","cty
    # creek","cr","crk
    # county","co","cty
    # downs","downes","dwns
    # flats","flts
    # forest","frst","fst
    # fort","ft
    # fords","frds
    # fork","frk
    # forks","frks
    # forge","frg
    # forges","frgs
    # glens","glns
    # great","grt","gt
    # greater","grtr","gtr
    # greens","grns
    # groves","grvs
    # heights","hghts","hgts","hieghts","ht","hts","hgths
    # international","intl","int'l
    # lake","lk
    # lakes","lks
    # little","ltl","lttl","littl","litl
    # lock","lck
    # locks","lcks
    # lower","low","lwr","lr
    # medical","med
    # memorial","mem
    # middle","mid","midl
    # military","mil
    # mount","mt","mnt
    # mountain","mtn
    # mountains","mtns
    # municipal","mun","mpal
    # national","natl","nat'l
    # neck","nck
    # orchard","orch
    # paradise","pde","pdse
    # port","pt","prt
    # park","pk","prk
    # rear of","r / o","r o
    # river","riv","rvr","rivr
    # slope","slpe","slp
    # springs","spgs","sprngs
    # stream","strm","stm
    # triangle","tri
    # upper","up","upr","uppr
    # village","vlg","vlge","vilg","vilge
    # ville","vl
    # villages","vlgs
    # wood","wd
    # woods","wds
    # front","f","frnt
    # left","l
    # right","r
    # rear","r
    # abbey","abby
    # access","accs","acc
    # acres","acrs
    # alley","aly","ally","alee","al
    # alleyway","alwy","allyway","allwy
    # amble","ambl
    # anchorage","ancg
    # annex","anx
    # apartments","apts","appartments
    # approach","app","apch","appr
    # arcade","arc
    # arterial","artl
    # artery","art","arty
    # avenue","av","ave","aven","avenu","avn","avnu","avnue
    # avenues","avs","aves","avens","avenus","avns","avnus","avnues
    # autoroute","aut
    # back","bk
    # bank","bnk
    # basin","basn","bsn
    # bay","by
    # bayou","byu","bayoo
    # belt","blt
    # block","blk","blck
    # boardwalk","bwk","bwlk","board walk
    # boulevard","blvd","bd","bde","blv","bl","blvde","blvrd","boulavard","boul","boulv","bvd","boulevarde
    # bottom","bot","bottm","btm","bttm
    # bottoms","bttms","btms","bottms
    # boundary","bdy
    # bowl","bl
    # brace","br","brce
    # brae","br
    # break","brk
    # bridge","bdge","br","brdg","bri","brg
    # broadway","bdwy","bway","bwy","brdway
    # brow","brw
    # burrow","burw
    # butte","btte","bte
    # bypass","bypa","byps","bps","byp
    # byway","bywy
    # camp","cp
    # cape","cpe","cp
    # canyon","cyn","cnyn
    # caravan","cvan","cvn","c van
    # causeway","csway","cswy","causewy","caus","cause","cway
    # center","centre","cetr","cntr","ctr","c","cen
    # centers","ctrs
    # centreway","cnwy
    # chase","ch","chas
    # circle","cir","circel
    # circles","cirs
    # circlet","clt
    # circuit","crct","circ","cct","cirt","ci","circt
    # circus","crcs","crc
    # claim","clm
    # cliff","clf
    # cliffs","clfs
    # close","cl","cls","clse
    # cluster","clr","clstr
    # colonnade","clde","clnde
    # common","cmmn","comm","cmn","com","cm
    # commons","cmmns","cmns","comms
    # concord","cncd","cncrd
    # concession","conc
    # concourse","con","concs","concse","cnc
    # connection","cntn","cxn
    # connector","conr","cnctr","cntr
    # copse","cps
    # corner","cnr","crn","cor
    # corners","cnrs","crns","cors
    # corseo","cseo
    # corso","cso
    # county highway","ch","c.h.","c.h","c h","c.hw","c hw","co.hw","co hw","cty.hw","cty hw","c.hgwy","c hgwy","co.hgwy","co hgwy","cty.hgwy","cty hgwy","c.hway","c hway","co.hway","co hway","cty.hway","cty hway","c.hwy","c hwy","co.hwy","co hwy","cty.hwy","cty hwy","c.hi","c hi","co.hi","co hi","cty.hi","cty hi
    # county road","cr","c.r.","c.r","c r","co.r","co r","c.rd","c rd","co.rd","co rd","cty.r","cty r","cty.rd","cty rd
    # county route","cr","c.r.","c.r","c r","co.r","co r","c.rt","c rt","co.rt","co rt","cty.r","cty r","cty.rt","cty rt","c.rte","c rte","co.rte","co rte","cty.rte","cty rte","county touring route
    # course","crse
    # creek","cr","crk
    # crescent","cr","cres","crs","crecent
    # crest","crst","cst
    # crief","crf
    # croft","cft
    # cross","cs","crss
    # crossing","crsg","xing","csg","x ing","x-ing
    # crossroad","crd","cross road","xroad","x-road","x road","xrd","x-rd","x rd
    # crossroads","cross roads","xrds
    # crossway","cowy","crwy","xway","xwy","x-way","x way","x-wy","xwy
    # cruiseway","cuwy","crwy
    # cul
    # cul de sac","cul-de-sac","culdesac","cds","cusac","csac
    # curve","cve","crv","crve","curv
    # cutting","cttg","ctg","cutt
    # dale","dle
    # dell
    # dene
    # deviation","devn
    # dip
    # distributor","dstr
    # diversion","divers
    # down","dn
    # downs","dns","dwns
    # drive","dr","drv","dv","dve","d
    # driveway","drwy","dvwy","dwy","dway","drvwy
    # drove","drov
    # easement","esmt
    # edge","edg
    # elbow","elb
    # elm
    # end
    # entrance","ent","entr
    # esplanade","esp","espl
    # estate","est
    # estates","ests
    # exit
    # expressway","exp","expwy","expway","expy","exwy
    # extension","ex","ext","extn","exten
    # extensions","exts
    # fairway","fawy","fy
    # fall","fl
    # falls","fls
    # fare
    # farm","frm
    # farms","frms
    # fern
    # ferry","fry","fy
    # field","fld","fd
    # fields","flds","fds
    # fireline","fline","fire line","flne
    # firetrack","ftrk","fire track
    # firetrail","fit","fitr","fire trail
    # flat","fl","flt
    # flats","flts
    # follow","folw
    # footway","ftwy","foot way
    # ford","frd
    # foreshore","fshr","fore shore
    # formation","form","fmtn
    # freeway","frwy","fw","fwy","fway
    # front","frnt
    # frontage","frtg","fr
    # gap","gp
    # garden","gdn","grd","grdn
    # gardens","gdns","grds","grdns
    # gate","ga","gte
    # gates","gtes
    # gateway","gwy","gway","gtwy","gtway
    # glade","gl","gld","glde
    # glen","gln
    # grand boulevard","gbd","grbd","grdbd","gdbd","g bd","gr bd","grd bd","gd bd","g blvd","gr blvd","grd blvd","gd blvd","g bde","gr bde","grd bde","gd bde","g blvrd","gr blvrd","grd blvrd","gd blvrd","g boul","gr boul","grd boul","gd boul","g bvd","gr bvd","grd bvd","gd bvd","g bld","gr bld","grd bld","gd bld
    # grange","gra
    # green","grn","gn","gren
    # greenway","grwy
    # ground","grnd
    # grounds","grnds
    # grove","gr","grv","grve","gro
    # gulch","glch
    # gully","gly
    # hanger","hngr
    # harbor","harbour","hbr","hrbr
    # harbors","hbrs
    # haven","hvn","havn
    # head","hd
    # heads","hds
    # heath","hth","heth
    # heights","hghts","hgts","hieghts","ht","hts","hgths
    # highlands","hghlds","hlds","hglds
    # highroad","hrd","high road","hird","hi.rd","hi rd
    # highway","hgwy","hw","hway","hwy","hi","hwye","hywy
    # hill","hl
    # hills","hls","hils
    # hollow","hllw","holw
    # hub
    # impasse","imp
    # inlet","inlt
    # interchange","intg","intchg","inter change
    # intersection","intn","inter section","intsctn
    # interstate","inter state","i","ih","i h
    # island","is","id","i","isl","isld
    # islands","iss","ids","islds
    # isle
    # junction","jct","jnc","jnct","jctn","jtn","junct","j
    # junctions","jcts
    # key","ky
    # keys","kys
    # knob
    # knoll","knol","knl
    # knolls","knls
    # ladder","ladr
    # lagoon","lagn","lgn","lagon
    # land
    # landing","ldg","lndg","landng
    # laneway","lnwy
    # lees
    # light","lgt","lt
    # limits","lmts
    # line","ln
    # link","lnk","lk
    # little","ltl","lttl","littl","litl","lit","lt
    # loaf","lf
    # lookout","lkt","look out
    # loop","lp
    # loops","lps
    # lot","lt
    # lynne","lynn
    # mall","ml
    # manor","mnr
    # maze
    # meadow","mdw
    # meadows","mdws","mead
    # mead","md
    # meander","mndr","mdr","mr
    # mew","mw
    # mews","mws
    # mile","mi
    # mill","ml
    # mills","mls
    # moor
    # motorway","mway","mwy","mtwy
    # mount","mt
    # neaves","nvs
    # nook","nk
    # number","#","nbr","num","no","nmbr","nr
    # oaks
    # outlet","otlt
    # outlook","out","otlk
    # oval
    # overbridge","ovrb","over bridge    # paddock","padk
    # palms","plms
    # parade","pde","prd","prde","pard
    # park","pk","prk
    # parklands","pkld","pklds","parkland","park lands","park land
    # parkway","pkwy","parkwy","pky","pkway","prkwy","prkway","pkw","pwy","prkw
    # parkways","pkwys
    # part","prt
    # pass","ps
    # passage","psge","pass","pasg
    # path","pth
    # pathway","phwy","pway","pthway","pthwy","ptway","ptwy
    # peninsula","psla
    # piazza","piaz","pzza
    # pier
    # pike","pk","pke
    # pine","pne","pn
    # pines","pns","pnes
    # pond
    # plain","pln","pl
    # plains","plns","pls
    # plateau","plat","plt
    # plaza","plz","plza","pz
    # prarie","pr
    # pocket","pkt","pokt","pckt
    # point","piont","pnt","pt
    # pointe","pte","pnte
    # port","prt
    # ports","prts
    # prairie","pr
    # priors","prrs
    # private","pvt
    # promenade","prom","prm
    # pursuit","pur
    # quad","qd
    # quadrangle","qdgl
    # quadrant","qdrt","qd
    # quay","quy","qy
    # quays","quys","qys
    # radial","radl
    # ramble","ra","rmbl
    # ramp","rmp
    # ranae","ran
    # ranch","rnch
    # rapid","rpd
    # rapids","rpds
    # range","rng","rnge","rang
    # range road","rge rd","range rd","rr
    # reach","rch
    # reef
    # reserve","res","resrv","resv","rsrv","rserv","rserve","rsrve
    # rest","rst
    # retreat","rt","rtt
    # return","rtn
    # ride
    # ridge","rdge","rdg
    # ridges","rdgs
    # ridgeway","rgwy","rdgwy","ridge way
    # right of way","rowy","rightofway","rofw","row","r o w","r of w
    # ring
    # rise","ri
    # riverway","rvwy
    # riviera","rvra
    # road","rd","ro","r","roa","raod
    # roads","raods","rds
    # roadside","rdsd","road side
    # roadway","rdwy","rdw","rdy
    # rocks","rks
    # ronde","rnde
    # rosebowl","rsbl","rose bowl
    # rotary","rty
    # round","rnd
    # roundabout
    # route","rt","rte
    # row","rw
    # run","rn
    # rural route","rr","r.r","r r
    # service road","svc rd","svc road","service rd","sv rd","svrd
    # serviceway","swy","svwy","svcwy
    # shoal","shl
    # shoals","shls
    # shore","shor","shr
    # shores","shors","shrs
    # shunt","shun","shnt
    # siding","sdng","sdg
    # skyway","skwy
    # slip
    # slope","slpe","slp
    # sound","snd
    # space","spc
    # spring","spg","sprng","sprn
    # springs","spgs","sprngs","spns
    # spur","spr
    # stairs","strs
    # stairway","stwy","strwy","stair way","st.wy","st wy","str.way","str way
    # state highway","s.highway","s highway","st.highway","st highway","sh","s.h.","s.h","s h","st.h","st h","s.hw","s hw","st.hw","st hw","s.hwy","s hwy","shwy","s.hgwy","s hgwy","st.hgwy","st hgwy","s.hway","s hway","st.hway","st hway","s.hwy","s hwy","st.hwy","st hwy","s.hi","s hi","st.hi","st hi","statehighway
    # state road","sr","stateroad","s.r.","s.r","s r","s.road","s road","st.road","st road","staterd","srd","s.rd","s rd","state rd","strd","st.rd","st rd
    # state route","sr","stateroute","s.r.","s.r","s r","s.route","s route","st.route","st route","statert","srt","s.rt","s rt","srte","s.rte","s rte","state rt","state rte","strt","strte","st.rt","st rt","st.rte","st rte
    # steps","stps
    # strand","stra","strnd","strd
    # strands","strnds","strds
    # stravenue","stra","strav
    # street","st","str","stre","stree","strt
    # streets","sts
    # strip","strp
    # subdivision","subdiv
    # subway","sbwy
    # summit","smt","sumt
    # tarn","tn
    # terrace","tce","ter","tr","terr","terace","terrac","terrasse","tsse
    # thicket","thick
    # thoroughfare","thor","throughfare","thorough fare","thfr
    # thoroughway","thwy
    # throughway","thru","thro","thruway","trwy","thwy
    # tollway","tlwy","twy
    # top
    # tor
    # township highway","th","t.h.","t.h","t h","twp.h","twp h","tshp.h","tshp h","t.hw","t hw","twp.hw","twp hw","tshp.hw","tshp hw","t.hgwy","t hgwy","twp.hgwy","twp hgwy","tshp.hgwy","tshp hgwy","t.hway","t hway","twp.hway","twp hway","tshp.hway","tshp hway","t.hwy","t hwy","twp.hwy","twp hwy","tshp.hwy","tshp hwy","t.hi","t hi","twp.hi","twp hi","tshp.hi","tshp hi
    # township road","tr","t.r.","t.r","t r","t rd","t.rd","trd","twpr","twp.r","twp r","twp.rd","twp rd","tshp.r","tshp r","tshp.rd","tshp rd","township rd","tp rd
    # township route","tr","t.r.","t.r","t r","t rt","t.rt","trt","t.rte","t rte","twpr","twp.r","twp r","twp.rt","twp rt","twp.rte","twp rte","tshp.r","tshp r","tshp.rt","tshp rt","tshp.rte","tshp rte
    # tower","twr
    # towers","twrs
    # townline","tline
    # trace","trce","trc
    # track","tr","trk","trak
    # trafficway","trfy
    # trail","tr","trl
    # trailer","trlr
    # tram
    # tramway","tmwy
    # trees","trs
    # triangle","tri
    # truck trail","trktrl
    # trunkway","tkwy
    # tunnel","tun","tunl
    # turnabout","trnabt
    # turn","tn","trn
    # turnpike","tpk","tpke
    # underpass","upas","upass","ups","under pass
    # union","un
    # unions","uns
    # us highway","us hwy","u s hwy
    # us route","us rte","u s rte
    # vale","va","vl
    # valley","vlly","vly","vy
    # valleys","vlys","vllys
    # vennel
    # viaduct","via","viad","vdct","viadct
    # view","vw
    # views","vws
    # villa","vla
    # village","vlge
    # villas","vlas
    # vista","vst","vsta","vis
    # vue
    # wade
    # walk","wlk","wk
    # walkway","wkwy","wky","wlkwy
    # waters","wtrs
    # way","wy
    # ways","wys
    # well","wl
    # wells","wls
    # wharf","whrf","whf
    # wynd","wyn
    # yard","yd","yrd
}


cols = ["Address", "Tags"]

street_type = list(to_non_stand_street_type.keys())
street_dir = list(to_non_stand_street_dir.keys())
