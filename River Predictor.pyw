import os
import time
import webbrowser
import urllib
from urllib import urlopen
import numpy
from datetime import datetime  
from datetime import timedelta 
from datetime import date
import matplotlib
import matplotlib.pyplot as plt
from random import *
import sys
import shutil

#Traceback (most recent call last):
#  File "C:\Users\iaman\Documents\RainBot\Conwy.pyw", line 149, in <module>
#    main()
#  File "C:\Users\iaman\Documents\RainBot\Conwy.pyw", line 54, in main
#    if time[1]==":":
#IndexError: string index out of range

#(CentreX+j*jfactor*ScaleX)**2 + (i*ifactor*ScaleY)**2 <(RadiusL)**2 and (CentreX+j*jfactor*ScaleX)**2 + (i*ifactor*ScaleY)**2 >(RadiusS)**2 and 0.7*j+i<=130*PixelsY/300:
                
#Traceback (most recent call last):
#  File "C:\Users\Dr Blue\Documents\RainBot\ConwyCode.pyw", line 676, in <module>
#    main()
#  File "C:\Users\Dr Blue\Documents\RainBot\ConwyCode.pyw", line 145, in main
#    CodeyStuff("http://rainchasers.com/river/hindburn/millbeck-wray","https://www.myweather2.com/City-Town/United-Kingdom/Lancashire/Lowgill/14-Day-Forecast.aspx",'HindburnData.txt','HindburnVariables.txt','HindburnAll.pdf')
#  File "C:\Users\Dr Blue\Documents\RainBot\ConwyCode.pyw", line 282, in CodeyStuff
#    if time[1]==":":
#IndexError: string index out of range



def main():
    loopsetter=0
    while loopsetter<5000:

        #North Wales
        #Conwy
        CodeyStuff("http://rainchasers.com/river/conwy/a5-penmachno-bridge","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Ysbyty-Ifan/14-Day-Forecast.aspx",'ConwyData.txt','ConwyVariables.txt','ConwyAll.pdf')
        shutil.copy("C:\Users\Dr Blue\Documents\RainBot\ConwyAll.pdf", "C:\Users\Dr Blue\Dropbox\North Wales\ConwyAll.pdf")
        #dee
        CodeyStuff("http://rainchasers.com/river/dee/horseshoe-falls-llangollen","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Ysbyty-Ifan/14-Day-Forecast.aspx",'DeeData.txt','DeeVariables.txt','DeeAll.pdf')
        #dart
        CodeyStuff("http://rainchasers.com/river/dart/loop","https://www.myweather2.com/City-Town/United-Kingdom/Devon/Dartmeet/14-Day-Forecast.aspx",'DartData.txt','DartVariables.txt','DartAll.pdf')
        #winion
        CodeyStuff("http://rainchasers.com/river/wnion/dolddeuli-bridge-bontnewydd","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Mawddach/14-Day-Forecast.aspx",'WnionData.txt','WnionVariables.txt','WnionAll.pdf')
        #llugwy
        CodeyStuff("http://rainchasers.com/river/llugwy/plas-y-brenin-ugly-house","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Capel-Curig/14-Day-Forecast.aspx",'LlugwyData.txt','LlugwyVariables.txt','LlugwyAll.pdf')
        #lledr
        CodeyStuff("http://rainchasers.com/river/lledr/pont-y-pant-beaver-pool","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Dolwyddelan/14-Day-Forecast.aspx",'LledrData.txt','LledrVariables.txt','LledrAll.pdf')
        #seiont
        CodeyStuff("http://rainchasers.com/river/seiont/pont-rhythallt-pylons-caernarfon","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Llanberis/14-Day-Forecast.aspx",'SeiontData.txt','SeiontVariables.txt','SeiontAll.pdf')
        #dwyfor
        CodeyStuff("http://rainchasers.com/river/dwyfor/dolbenmaen-llanystumdwy","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Dolbenmaen/14-Day-Forecast.aspx",'DwyforData.txt','DwyforVariables.txt','DwyforAll.pdf')
        #gain
        CodeyStuff("http://rainchasers.com/river/gain/cattle-grid-pistyll-y-cain","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Bronaber/14-Day-Forecast.aspx",'GainData.txt','GainVariables.txt','GainAll.pdf')
        #glaslyn
        CodeyStuff("http://rainchasers.com/river/seiont/pont-rhythallt-pylons-caernarfon","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Llanberis/14-Day-Forecast.aspx",'GlaslynData.txt','GlaslynVariables.txt','GlaslynAll.pdf')
        #gwyrfai
        CodeyStuff("http://rainchasers.com/river/gwyrfai/waunfawr-bridge-bontnewydd","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Waunfawr/14-Day-Forecast.aspx",'GwyrfaiData.txt','GwyrfaiVariables.txt','GwyrfaiAll.pdf')
        #mawddach
        CodeyStuff("http://rainchasers.com/river/mawddach/pont-abergeirw-ptf","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Bronaber/14-Day-Forecast.aspx",'MawddachData.txt','MawddachVariables.txt','MawddachAll.pdf')
        #aled
        CodeyStuff("http://rainchasers.com/river/aled/llansannan-elwy-confluence","https://www.myweather2.com/City-Town/United-Kingdom/Denbighshire/Llansannan/14-Day-Forecast.aspx",'AledData.txt','AledVariables.txt','AledAll.pdf')
        #alyn
        CodeyStuff("http://rainchasers.com/river/alyn/hope-rosset","https://www.myweather2.com/City-Town/United-Kingdom/Wrexham/Wrexham/14-Day-Forecast.aspx",'AlynData.txt','AlynVariables.txt','AlynAll.pdf')
        #colwyn
        CodeyStuff("http://rainchasers.com/river/colwyn/hafod-ruffydd-isaf-beddgelert","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Beddgelert/14-Day-Forecast.aspx",'ColwynData.txt','ColwynVariables.txt','ColwynAll.pdf')
        #ceirw
        CodeyStuff("http://rainchasers.com/river/ceirw/ystrad-bach-bridge-maerdy","https://www.myweather2.com/City-Town/United-Kingdom/Denbighshire/Glasfryn/14-Day-Forecast.aspx",'CeirwData.txt','CeirwVariables.txt','CeirwAll.pdf')
        #cledwen
        CodeyStuff("http://rainchasers.com/river/cledwen/gwytherin-llanfair-talhaiarn","https://www.myweather2.com/City-Town/United-Kingdom/Denbighshire/Gwytherin/14-Day-Forecast.aspx",'CledwenData.txt','CledwenVariables.txt','CledwenAll.pdf')
        #clywedog
        CodeyStuff("http://rainchasers.com/river/ceirw/ystrad-bach-bridge-maerdy","https://www.myweather2.com/City-Town/United-Kingdom/Denbighshire/Glasfryn/14-Day-Forecast.aspx",'ClywedogData.txt','ClywedogVariables.txt','ClywedogAll.pdf')

        #South Wales
        #ogmore
        CodeyStuff("http://rainchasers.com/river/ogwr-fawr-ogmore/ogmore-vale-merthyr-mawr","https://www.myweather2.com/City-Town/United-Kingdom/PenyBont-ar-Ogwr-Bridgend/Abergarw/14-Day-Forecast.aspx",'OgmoreData.txt','OgmoreVariables.txt','OgmoreAll.pdf')
        #tywi
        CodeyStuff("http://rainchasers.com/river/tywi/llyn-brianne-junction-pool","https://www.myweather2.com/City-Town/United-Kingdom/Carmarthenshire/Cilycwm/14-Day-Forecast.aspx",'TywiData.txt','TywiVariables.txt','TywiAll.pdf')
        #mellte
        CodeyStuff("http://rainchasers.com/river/mellte/sgwd-clun-gwyn-falls-dinas-rock","https://www.myweather2.com/City-Town/United-Kingdom/Powys/Ystradfellte/14-Day-Forecast.aspx",'MellteData.txt','MellteVariables.txt','MellteAll.pdf')
        #tawe
        CodeyStuff("http://rainchasers.com/river/tawe/glyntawe-abercraf","https://www.myweather2.com/City-Town/United-Kingdom/Powys/Penwyllt/14-Day-Forecast.aspx",'TaweData.txt','TaweVariables.txt','TaweAll.pdf')
        #usk
        CodeyStuff("http://rainchasers.com/river/usk/talybont-usk-llangynidr","https://www.myweather2.com/City-Town/United-Kingdom/Powys/Brecon-Beacons/14-Day-Forecast.aspx",'UskData.txt','UskVariables.txt','UskAll.pdf')
        #Gwaun
        CodeyStuff("http://rainchasers.com/river/gwaun/pontfaen-fishguard","https://www.myweather2.com/City-Town/United-Kingdom/Pembrokeshire/Pontfaen/14-Day-Forecast.aspx",'GwaunData.txt','GwaunVariables.txt','GwaunAll.pdf')
        #Cleddau
        CodeyStuff("http://rainchasers.com/river/cleddau-eastern/llangolman-llangwm-ford","https://www.myweather2.com/City-Town/United-Kingdom/Pembrokeshire/Mynachlogddu/14-Day-Forecast.aspx",'CleddauData.txt','CleddauVariables.txt','CleddauAll.pdf')#
        #Gwili
        CodeyStuff("http://rainchasers.com/river/gwili-caermarthen/cynwyl-elfed-carmarthen","https://www.myweather2.com/City-Town/United-Kingdom/Carmarthenshire/Llanpumsaint/14-Day-Forecast.aspx",'GwiliData.txt','GwiliVariables.txt','GwiliAll.pdf')
        #clydach
        CodeyStuff("http://rainchasers.com/river/upper-clydach/rhyd-y-fro-pontardawe","https://www.myweather2.com/City-Town/United-Kingdom/PenyBont-ar-Ogwr-Bridgend/Bryncoch/14-Day-Forecast.aspx",'ClydachData.txt','ClydachVariables.txt','ClydachAll.pdf')
        #Swadde
        CodeyStuff("http://rainchasers.com/river/sawdde/llwynfron-cefn-coed-common","https://www.myweather2.com/City-Town/United-Kingdom/Carmarthenshire/Twynllanan/14-Day-Forecast.aspx",'SwaddeData.txt','SwaddeVariables.txt','SwaddeAll.pdf')
        #Afan
        CodeyStuff("http://rainchasers.com/river/afan/blaengwynfi-cymmer-pontrhydyfen","https://www.myweather2.com/City-Town/United-Kingdom/Neath-Port-Talbot/Glyncorrwg/14-Day-Forecast.aspx",'AfanData.txt','AfanVariables.txt','AfanAll.pdf')
        #Rhondda
        #CodeyStuff("http://rainchasers.com/river/rhondda-fawr/blaencwm-porth","https://www.myweather2.com/City-Town/United-Kingdom/Neath-Port-Talbot/Tynewydd/14-Day-Forecast.aspx",'RhonddaData.txt','RhonddaVariables.txt','RhonddaAll.pdf')
        #Corrwg
        CodeyStuff("http://rainchasers.com/river/corrwg/glyncorrwg-cymer","https://www.myweather2.com/City-Town/United-Kingdom/Neath-Port-Talbot/Glyncorrwg/14-Day-Forecast.aspx",'CorrwgData.txt','CorrwgVariables.txt','CorrwgAll.pdf')
        #NeddFechan
        CodeyStuff("http://rainchasers.com/river/nedd-fechan/pont-melin-fach-pontneddfechan","Ystradfellte",'NeddFechanData.txt','NeddFechanVariables.txt','NeddFechanAll.pdf')
        #Rhymney
        CodeyStuff("http://rainchasers.com/river/rhymney/pontlottyn-llanbradach","https://www.myweather2.com/City-Town/United-Kingdom/Blaenau-Gwent/Pontlottyn/14-Day-Forecast.aspx",'RhymneyData.txt','RhymneyVariables.txt','RhymneyAll.pdf')
        #GrwyneFawr
        CodeyStuff("http://rainchasers.com/river/grwyne-fawr/lower-cwm-bridge-glangrwyney","https://www.myweather2.com/City-Town/United-Kingdom/Gwynedd/Llanbedrog/14-Day-Forecast.aspx",'GrwyneFawrData.txt','GrwyneFawrVariables.txt','GrwyneFawrAll.pdf')
        #Lwyd
        CodeyStuff("http://rainchasers.com/river/lwyd/pontypool-caerleon","https://www.myweather2.com/City-Town/United-Kingdom/Torfaen/Abersychan/14-Day-Forecast.aspx",'LwydData.txt','LwydVariables.txt','LwydAll.pdf')

        #Lake District
        #LuneHalton
        CodeyStuff("http://rainchasers.com/river/lune/halton-rapids","https://www.myweather2.com/City-Town/United-Kingdom/Lancashire/Hornby/14-Day-Forecast.aspx",'LuneHaltonData.txt','LuneHaltonVariables.txt','LuneHaltonAll.pdf')
        #LuneLowgill
        CodeyStuff("http://rainchasers.com/river/lune/lowgill-rawthey-confluence","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Tebay/14-Day-Forecast.aspx",'LuneLowgillData.txt','LuneLowgillVariables.txt','LuneLowgillAll.pdf')
        #Leven
        CodeyStuff("http://rainchasers.com/river/leven/newby-bridge-low-wood","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Windermere/14-Day-Forecast.aspx",'LevenData.txt','LevenVariables.txt','LevenAll.pdf')
        #Crake
        CodeyStuff("http://rainchasers.com/river/crake/blawith-common-spark-bridge","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Coniston/14-Day-Forecast.aspx",'CrakeData.txt','CrakeVariables.txt','CrakeAll.pdf')
        #Duddon
        CodeyStuff("http://rainchasers.com/river/duddon/birk-s-bridge-hall-dunnerdale","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Cockley-Beck/14-Day-Forecast.aspx",'DuddonData.txt','DuddonVariables.txt','DuddonAll.pdf')
        #Esk
        CodeyStuff("http://rainchasers.com/river/esk-lakes/brotherikeld-forge-bridge","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Cockley-Beck/14-Day-Forecast.aspx",'EskData.txt','EskVariables.txt','EskAll.pdf')
        #Kent
        CodeyStuff("http://rainchasers.com/river/kent/scroggs-weir-park-head","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Burneside/14-Day-Forecast.aspx",'KentData.txt','KentVariables.txt','KentAll.pdf')
        #Calder
        CodeyStuff("http://rainchasers.com/river/calder/thornholme-farm-calder-bridge","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Calder-Bridge/14-Day-Forecast.aspx",'CalderData.txt','CalderVariables.txt','CalderAll.pdf')
        #Ehen
        CodeyStuff("http://rainchasers.com/river/ehen/wath-brow-bridge-low","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Ennerdale-Bridge/14-Day-Forecast.aspx",'EhenData.txt','EhenVariables.txt','EhenAll.pdf')
        #Sprint
        CodeyStuff("http://rainchasers.com/river/sprint/public-toilet-sprint-bridge","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Sadgill/14-Day-Forecast.aspx",'SprintData.txt','SprintVariables.txt','SprintAll.pdf')
        #Mint
        CodeyStuff("http://rainchasers.com/river/mint/patton-bridge-mint-bridge","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Patton-Bridge/14-Day-Forecast.aspx",'MintData.txt','MintVariables.txt','MintAll.pdf')
        #Brathay
        CodeyStuff("http://rainchasers.com/river/brathay/elterwater-ambleside","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Chapel-Stile/14-Day-Forecast.aspx",'BrathayData.txt','BrathayVariables.txt','BrathayAll.pdf')
        #Rothay
        CodeyStuff("http://rainchasers.com/river/rothay/grassmere-lake-windermere","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Grasmere/14-Day-Forecast.aspx",'RothayData.txt','RothayVariables.txt','RothayAll.pdf')
        #Cocker
        CodeyStuff("http://rainchasers.com/river/cocker/southwaite-bridge-cockermouth","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Low-Lorton/14-Day-Forecast.aspx",'CockerData.txt','CockerVariables.txt','CockerAll.pdf')
        #Greta
        CodeyStuff("http://rainchasers.com/river/greta-keswick/threlkeld-keswick","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Threlkeld/14-Day-Forecast.aspx",'GretaData.txt','GretaVariables.txt','GretaAll.pdf')
        #Caldew
        CodeyStuff("http://rainchasers.com/river/caldew/grainsgill-beck-mosedale","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Mosedale/14-Day-Forecast.aspx",'CaldewData.txt','CaldewVariables.txt','CaldewAll.pdf')
        #Eamont
        CodeyStuff("http://rainchasers.com/river/eamont/waterfoot-brougham-castle","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Glenridding/14-Day-Forecast.aspx",'EamontData.txt','EamontVariables.txt','EamontAll.pdf')
        #Lowther
        CodeyStuff("http://rainchasers.com/river/lowther/crookwath-bridge-brougham-castle","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Bampton/14-Day-Forecast.aspx",'LowtherData.txt','LowtherVariables.txt','LowtherAll.pdf')
        #Wyre
        CodeyStuff("http://rainchasers.com/river/wyre/tarnbrook-abbeystead","https://www.myweather2.com/City-Town/United-Kingdom/Lancashire/Tarnbrook/14-Day-Forecast.aspx",'WyreData.txt','WyreVariables.txt','WyreAll.pdf')
        #Roeburn
        CodeyStuff("http://rainchasers.com/river/roeburn/barkin-bridge-wray","https://www.myweather2.com/City-Town/United-Kingdom/Lancashire/Wray-Lancashire/14-Day-Forecast.aspx",'RoeburnData.txt','RoeburnVariables.txt','RoeburnAll.pdf')
        #Hindburn
        CodeyStuff("http://rainchasers.com/river/hindburn/millbeck-wray","https://www.myweather2.com/City-Town/United-Kingdom/Lancashire/Lowgill/14-Day-Forecast.aspx",'HindburnData.txt','HindburnVariables.txt','HindburnAll.pdf')
        #Rawthey
        CodeyStuff("http://rainchasers.com/river/rawthey/sedbergh-lune-confluence","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Sedbergh/14-Day-Forecast.aspx",'RawtheyData.txt','RawtheyVariables.txt','RawtheyAll.pdf')
        #Clough
        CodeyStuff("http://rainchasers.com/river/clough/bellow-end-road-bridge-sedbergh","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Garsdale/14-Day-Forecast.aspx",'CloughData.txt','CloughVariables.txt','CloughAll.pdf')
        #Swale
        CodeyStuff("http://rainchasers.com/river/swale/hoggarths-ivelet-bridge","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/West-Stonesdale/14-Day-Forecast.aspx",'SwaleData.txt','SwaleVariables.txt','SwaleAll.pdf')
        #Whitsundale
        CodeyStuff("http://rainchasers.com/river/whitsundale-beck/ravenseat-swale-confluence","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/West-Stonesdale/14-Day-Forecast.aspx",'WhitsundaleData.txt','WhitsundaleVariables.txt','WhitsundaleAll.pdf')
        #Stonedale
        CodeyStuff("http://rainchasers.com/river/stonesdale-beck/stonesdale-lane-bridge-swale-confluence","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/Keld/14-Day-Forecast.aspx",'StonedaleData.txt','StonedaleVariables.txt','StonedaleAll.pdf')
        #Wenning
        CodeyStuff("http://rainchasers.com/river/wenning/clapham-hornby","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/ChapelleDale/14-Day-Forecast.aspx",'WenningData.txt','WenningVariables.txt','WenningAll.pdf')
        #Ribble
        CodeyStuff("http://rainchasers.com/river/ribble/helwith-bridge-settle","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/High-Birkwith/14-Day-Forecast.aspx",'RibbleData.txt','RibbleVariables.txt','RibbleAll.pdf')
        #Wharfe
        CodeyStuff("http://rainchasers.com/river/wharfe/kettlewell-linton-falls","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/Hubberholme/14-Day-Forecast.aspx",'WharfeData.txt','WharfeVariables.txt','WharfeAll.pdf')
        #Cray
        CodeyStuff("http://rainchasers.com/river/cray-gill/cray-hubberholme","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/Buckden/14-Day-Forecast.aspx",'CrayData.txt','CrayVariables.txt','CrayAll.pdf')
        #Oughtershaw
        CodeyStuff("http://rainchasers.com/river/oughtershaw-beck/oughtershaw-beckermonds","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/Oughtershaw/14-Day-Forecast.aspx",'OughtershawData.txt','OughtershawVariables.txt','OughtershawAll.pdf')
        #Greenfield
        #CodeyStuff("http://rainchasers.com/river/green-field-beck/low-green-field-beckermonds","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/Oughtershaw/14-Day-Forecast.aspx",'GreenfieldData.txt','GreenfieldVariables.txt','GreenfieldAll.pdf')
        #Eden
        CodeyStuff("http://rainchasers.com/river/eden-lakes/lazonby-armathwaite","https://www.myweather2.com/City-Town/United-Kingdom/Cumbria/Temple-Sowerby/14-Day-Forecast.aspx",'EdenData.txt','EdenVariables.txt','EdenAll.pdf')
        #Ystwyth
        CodeyStuff("http://rainchasers.com/river/ystwyth/cwmystwyth-pont-rhyd-y-groes","https://www.myweather2.com/City-Town/United-Kingdom/Ceredigion/Cwmystwyth/14-Day-Forecast.aspx",'YstwythData.txt','YstwythVariables.txt','YstwythAll.pdf')
        #WyeDerbyshire
        CodeyStuff("http://rainchasers.com/river/wye-derbyshire/buxton-litton","https://www.myweather2.com/City-Town/United-Kingdom/Derbyshire/Buxton/14-Day-Forecast.aspx",'WyeDerbyshireData.txt','WyeDerbyshireVariables.txt','WyeDerbyshireAll.pdf')
        #Wenning
        CodeyStuff("http://rainchasers.com/river/wenning/clapham-hornby","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/Keasden/14-Day-Forecast.aspx",'WenningData.txt','WenningVariables.txt','WenningAll.pdf')
        #Wear
        CodeyStuff("http://rainchasers.com/river/wear/wearhead-stanhope","https://www.myweather2.com/City-Town/United-Kingdom/Northumberland/Wearhead/14-Day-Forecast.aspx",'WearData.txt','WearVariables.txt','WearAll.pdf')
        #Usway
        CodeyStuff("http://rainchasers.com/river/usway-burn/davidson-s-linn-coquet-confluence","https://www.myweather2.com/City-Town/United-Kingdom/Northumberland/Shillmoor/14-Day-Forecast.aspx",'UswayData.txt','UswayVariables.txt','UswayAll.pdf')
        #Ure
        CodeyStuff("http://rainchasers.com/river/ure/aysgarth-falls","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/Bainbridge/14-Day-Forecast.aspx",'UreData.txt','UreVariables.txt','UreAll.pdf')
        #Severn
        #CodeyStuff("http://rainchasers.com/river/severn/shrewsbury-weir","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/Bainbridge/14-Day-Forecast.aspx",'SevernData.txt','SevernVariables.txt','SevernAll.pdf')
        #Scalby
        #CodeyStuff("http://rainchasers.com/river/scalby-beck/mowthorpe-farm-sea","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/Hackness/14-Day-Forecast.aspx",'ScalbyData.txt','ScalbyVariables.txt','ScalbyAll.pdf')
        #Rye
        #CodeyStuff("http://rainchasers.com/river/rye/hawnby-helmsley","https://www.myweather2.com/City-Town/United-Kingdom/North-Yorkshire/Hawnby/14-Day-Forecast.aspx",'RyeData.txt','RyeVariables.txt','RyeAll.pdf')
        #Rookhope
        #CodeyStuff("","",'RookhopeData.txt','RookhopeVariables.txt','RookhopeAll.pdf')
        #
        #CodeyStuff("","",'Data.txt','Variables.txt','All.pdf')
        #
        #CodeyStuff("","",'Data.txt','Variables.txt','All.pdf')
        #
        #CodeyStuff("","",'Data.txt','Variables.txt','All.pdf')
        #dfgfdg
        #CodeyStuff("","",'Data.txt','Variables.txt','All.pdf')
        
        
        #Dartmoor
        #camel
        CodeyStuff("http://rainchasers.com/river/camel/trecarne-penrose-bridge","https://www.myweather2.com/City-Town/United-Kingdom/Cornwall/Camelford/14-Day-Forecast.aspx",'CamelData.txt','CamelVariables.txt','CamelAll.pdf')
        #Fowey
        CodeyStuff("http://rainchasers.com/river/fowey/golitha-falls-treverbyn","https://www.myweather2.com/City-Town/United-Kingdom/Cornwall/St-Cleer/14-Day-Forecast.aspx",'FoweyData.txt','FoweyVariables.txt','FoweyAll.pdf')
        #Tavy
        CodeyStuff("http://rainchasers.com/river/tavy/tavistock-denham-bridge","https://www.myweather2.com/City-Town/United-Kingdom/Devon/Cudlipptown/14-Day-Forecast.aspx",'TavyData.txt','TavyVariables.txt','TavyAll.pdf')
        #Walkham
        #CodeyStuff("http://rainchasers.com/river/walkham/bedford-bridge-tavy-confluence","https://www.myweather2.com/City-Town/United-Kingdom/Devon/Sampford-Spiney.aspx",'WalkhamData.txt','WalkhamVariables.txt','WalkhamAll.pdf')
        #Plym
        CodeyStuff("http://rainchasers.com/river/plym/shaugh-bridge-bickleigh-bridge","https://www.myweather2.com/City-Town/United-Kingdom/Devon/Shaugh-Prior/14-Day-Forecast.aspx",'Data.txt','Variables.txt','All.pdf')
        #Yealm
        CodeyStuff("http://rainchasers.com/river/yealm/bridge-mark-s-bridge","https://www.myweather2.com/City-Town/United-Kingdom/Devon/Cornwood/14-Day-Forecast.aspx",'YealmData.txt','YealmVariables.txt','YealmAll.pdf')
        #Erme
        CodeyStuff("http://rainchasers.com/river/erme/harford-bridge-ivybridge","https://www.myweather2.com/City-Town/United-Kingdom/Devon/Ivybridge/14-Day-Forecast.aspx",'ErmeData.txt','ErmeVariables.txt','ErmeAll.pdf')
        #EastLyn
        #CodeyStuff("http://rainchasers.com/river/east-lyn/brendon-watersmeet","https://www.myweather2.com/City-Town/United-Kingdom/Devon/Wilsham.aspx",'EastLynData.txt','EastLynVariables.txt','EastLynAll.pdf')
        print("Done")
        time.sleep(2400)

        
        
        
def CodeyStuff(WaterLevelWebsite,RainForcastWebsite,DataText,VariablesText,AllDataImage):
    from datetime import datetime  
    from datetime import timedelta 
    x = datetime.today()    
    print(x)
    link = WaterLevelWebsite
    try:
        print("start0")
        f = urllib.urlopen(link)
        print("end0")

        myfile = f.read()
        print("rainchasers open")
        #with open(WaterLevelWebsite, 'w') as wf:
        #    wf.write(myfile)
        
        currentlevelpos=myfile.find("@")
        leveltoend=myfile[currentlevelpos+1:currentlevelpos+20]
        endoflevel=leveltoend.find(" ")
        endoftimeago=leveltoend.find(" ",endoflevel+1)
        endofunits=leveltoend.find(" ",endoftimeago+1)
        currentlevel=leveltoend[0:endoflevel]
        timeunits=leveltoend[endoftimeago+1:endofunits]
        timeofcurrentlevel=leveltoend[endoflevel+1:endoftimeago]
        
        
        with open(DataText, 'r') as rf:
            f_contents = rf.read()
            if f_contents=="":
                date=x
                data=[[0] * 4] * 800
                n=0
                c=0
            else:
                data=[[0] * 4] * 800
                n=0
                c=f_contents.find("[[")
                d=f_contents.find(",")
                firstdate=f_contents[c+2:d+9]
                date=x             
        link = RainForcastWebsite

            
        #try:
        print("start")
        f = urllib.urlopen(link)

        print("end")
        
        myfile = f.read()
        print("weather forcast open")
        #with open(RainForcastWebsite, 'w') as wf:
        #    wf.write(myfile)
        
        daysahead=0
        
        oldtime="00"
        ang=myfile.find("00</td><td")
        rang=ang
        bang=myfile[ang-3:ang+5000]
        time=bang[0:5]
        
        if time[1]==":":
            time="0"+time
        a=time[0:2]
        b=oldtime[0:2]
        
        if a<b:
            daysahead=daysahead+1
            #search date (x) and time in text and overwrite
            date=datetime.today() + timedelta(days=daysahead)
        sang=bang.find("<div>Expect")
        
        #wang=bang[ang+11:ang+1000]
        wang=bang.find("&",sang)
        mm=bang[sang+11:wang]
        mm=str(float(mm)/3)
        ang=myfile.find("00</td><td",rang+5)
        myfile=myfile[ang-10:]
        date1=str(date)[0:10]
        if int(x.hour)==int(time[0:2]):
            data[n]=[date1,time,mm,currentlevel]
        elif data[n]==[0,0,0,0]:
            data[n]=[date1,time,mm,currentlevel]
        n=n+1
        LCDTV=int(time[0:2])+1
        if len(str(LCDTV))==1:
            LCDTV="0"+str(LCDTV)
        time=str(LCDTV)+time[2:]
        if int(x.hour)==int(time[0:2]):
            data[n]=[date1,time,mm,currentlevel]
        elif int(x.hour)<int(time[0:2]):
            data[n]=[date1,time,mm,0]
        elif data[n]==[0,0,0,0]:
            data[n]=[date1,time,mm,currentlevel]
        n=n+1
        data[n]=[date1,time,mm,currentlevel]
        LCDTV=int(time[0:2])+1
        if len(str(LCDTV))==1:
            LCDTV="0"+str(LCDTV)
        time=str(LCDTV)+time[2:]
        if int(x.hour)==int(time[0:2]):
            data[n]=[date1,time,mm,currentlevel]
        else:
            data[n]=[date1,time,mm,0]
        data[n]=[date1,time,mm,currentlevel]
        n=n+1
        oldtime=time
        dang=2
        
        while ang>1:
            print("find forcast")
            ang=myfile.find("00</td><td")
            rang=ang
            bang=myfile[ang-3:ang+5000]
            time=bang[0:5]
            if time[1]==":":
                time="0"+time
            a=time[0:2]
            b=oldtime[0:2]
            if a<b:
                daysahead=daysahead+1
                #search date (x) and time in text and overwrite
                date=datetime.today() + timedelta(days=daysahead)
            ang=bang.find("<div>Expect")
            if ang<1:
                ang=bang.find("&nbsp;mm")
                ang=ang-15
                wang=bang.find("&",ang)
                
            wang=bang.find("&",ang)
            if ang>1:
                mm=bang[ang+11:wang]
            while mm[0]==" ":
                mm=mm[1:]
            mm=str(float(mm)/3)
            dang=myfile.find("00</td><td",rang+5)
            myfile=myfile[dang-10:]
            date1=str(date)[0:10]
            if time[0]!="t":
                data[n]=[date1,time,mm,0]
                LCDTV=int(time[0:2])+1
                if len(str(LCDTV))==1:
                    LCDTV="0"+str(LCDTV)
                time=str(LCDTV)+time[2:]
                n=n+1
                data[n]=[date1,time,mm,0]
                LCDTV=int(time[0:2])+1
                if len(str(LCDTV))==1:
                    LCDTV="0"+str(LCDTV)
                time=str(LCDTV)+time[2:]
                n=n+1
                data[n]=[date1,time,mm,0]
                n=n+1
                oldtime=time


        if f_contents!="":
            starttime=(str(data[1][0:2])[1:-1])
            start=f_contents.find(starttime)
            g_contents=f_contents[0:start]
            data=str(data)
            data=data[2:]
            g_contents+=data
            with open(DataText, 'w') as wf:
                wf.write(g_contents)
        else:
            with open(DataText, 'w') as wf:
                wf.write(str(data))
            
        with open(DataText, 'r') as rf:
            f_contents = rf.read()

        with open(DataText, 'r') as rf:
            fb_contents = rf.read()
            f_contents=eval(fb_contents)
            g_contents='['
            for i in range(0,len(f_contents)-1):
                if (f_contents[i][1])!=f_contents[i+1][1]:
                    g_contents+=str(f_contents[i])
                    g_contents+=(', ')
                    
            g_contents+=str(f_contents[i])
            g_contents+=']'
       
        with open(DataText, 'w') as wf:
            wf.write(g_contents)
            
        import time
        BestFit(DataText,VariablesText,AllDataImage)
        
    except IOError:
        print('no internet connection')
    except ValueError:
        print('no value')
   ## except IOError:
   #     print('no internet connection')
   #     import time
   #     time.sleep(180)

    except IndexError:
        print('index error')
        print(time)
        
def BestFit(DataText,VariablesText,AllDataImage):
    print("bestfitstart")
    from matplotlib import pyplot as plt
    plt.clf()
    x=datetime.today()

    try:

        with open(VariablesText, 'r') as rf:
            testvariables = rf.read()
            nv=testvariables.find('.')
            nnv=testvariables.find('.',nv+1)
            GV1=float(testvariables[nv-1:nnv-1])
            nv=nnv
            nnv=testvariables.find('.',nv+1)
            GV2=float(testvariables[nv-1:nnv-1])
            nv=nnv
            nnv=testvariables.find('.',nv+1)
            GV3=float(testvariables[nv-1:nnv-1])
            nv=nnv
            nnv=testvariables.find('.',nv+1)
            GV4=float(testvariables[nv-1:nnv-1])
            nv=nnv
            nnv=testvariables.find('.',nv+1)
            GV5=float(testvariables[nv-1:nnv-1])
            nv=nnv
            nnv=testvariables.find('.',nv+1)
            GV6=float(testvariables[nv-1:nnv-1])
            nv=nnv
            nnv=testvariables.find('.',nv+1)
            GV7=float(testvariables[nv-1:nnv-1])
            nv=nnv
            nnv=testvariables.find('.',nv+1)
            GV8=float(testvariables[nv-1:nnv-1])
            nv=nnv
            nnv=testvariables.find('.',nv+1)
            GV9=float(testvariables[nv-1:nnv-1])
            nv=nnv
            nnv=testvariables.find('.',nv+1)
            GV10=float(testvariables[nv-1:nnv-1])


        with open(DataText, 'r') as rf:
                fb_contents = rf.read()
                f_contents=eval(fb_contents)
                dates=[0]*len(f_contents)
                times=[0]*len(f_contents)
                quantities=[0]*len(f_contents)
                levels=[0]*len(f_contents)
                #print(len(f_contents)-3)
                #print(f_contents[58])
                #print(f_contents[int(len(f_contents))])
                #lastrecordedtime=str((f_contents[(len(f_contents)-3)][0:2]))
                nows = datetime.today()
                now=(nows.strftime("%H"))



    #WHY MINUS 163??????????????????????????????????????

                
                for n in range(0,(len(f_contents)-1)):
                    d1=f_contents[n][0]
                    year1=d1[0:4]
                    month1=d1[5:7]
                    day1=d1[8:]
                    date1= datetime(int(year1),int(month1),int(day1))
                    step=date1-x
                    day2=step
                    k=str(day2)
                    found=k.find("d")
                    if found==-1:
                        l=0
                    else:
                        l=int(k[0:found])              
                    dates[n]=l
                    
                    times[n]=int((f_contents[n][1])[0:2])-int(now)
                    times[n]=times[n]+24*dates[n]+24
                    quantities[n]=float(f_contents[n][2])
                    levels[n]=float(f_contents[n][3])

        TimeConsidered=96

        trialequation=[0] * (len(levels))
        trialequation[0]=levels[1]
        prevrain=[0]*TimeConsidered
        prevrain[TimeConsidered-1]=quantities[(0)]
        trialatest=0 
        
        
        for i in range(1,len(levels)):
            ta=abs(trialequation[(i-1)]*GV1+GV3)**(GV2)
            tb=0
            for l in range(1,len(prevrain)):
                tb=tb+prevrain[len(prevrain)-l]*GV4/(GV5**(GV6*(GV7-l))+GV8**(GV9*(GV10+l)))
            trialequation[i]=ta+tb

            for n in range(0,TimeConsidered-1):
                prevrain[n]=prevrain[n+1]
            prevrain[TimeConsidered-1]=quantities[(i-1)]
            trialatest=trialatest+abs(trialequation[i]-levels[i])*(levels[i]/(levels[i]+0.01))
        GVA1=GV1
        GVA2=GV2
        GVA3=GV3
        GVA4=GV4
        GVA5=GV5
        GVA6=GV6
        GVA7=GV7
        GVA8=GV8
        GVA9=GV9
        GVA10=GV10

        trialequationc=trialequation
        print(trialatest)
        for l in range (0,300):
            print(l)

            try:
                    
                
                trialequationb=[0] * (len(levels))
                trialequationb[0]=levels[0]
                prevrain=[0]*TimeConsidered
                for n in range(0,TimeConsidered-1):
                    prevrain[n]=prevrain[n+1]
                prevrain[TimeConsidered-1]=quantities[(0)]
                trialbtest=0
                
                for i in range(1,len(levels)):
                    ta=abs(trialequationb[(i-1)]*GVA1+GVA3)**(GVA2)
                    tb=0
                    for f in range(1,len(prevrain)):
                        tb=tb+prevrain[len(prevrain)-f]*GVA4/(GVA5**(GVA6*(GVA7-f))+GVA8**(GVA9*(GVA10+f)))
                    trialequationb[i]=ta+tb
                    
                    for n in range(0,TimeConsidered-1):
                            prevrain[n]=prevrain[n+1]
                    prevrain[TimeConsidered-1]=quantities[(i-1)]
                    trialbtest=trialbtest+abs(trialequationb[i]-levels[i])*(levels[i]/(levels[i]+0.01))

                if trialbtest<trialatest:
                    GV1=GVA1
                    GV2=GVA2
                    GV3=GVA3
                    GV4=GVA4
                    GV5=GVA5
                    GV6=GVA6
                    GV7=GVA7
                    GV8=GVA8
                    GV9=GVA9
                    GV10=GVA10
                    print(trialbtest)
                    trialatest=trialbtest
                    trialequationc=trialequationb

                
                GVA1=GV1*(0.98+random()*0.04)
                GVA2=GV2*(0.98+random()*0.04)
                GVA3=GV3*(0.98+random()*0.04)
                GVA4=GV4*(0.98+random()*0.04)
                GVA5=GV5*(0.98+random()*0.04)
                GVA6=GV6*(0.98+random()*0.04)
                GVA7=GV7*(0.98+random()*0.04)
                GVA8=GV8*(0.98+random()*0.04)
                GVA9=GV9*(0.98+random()*0.04)
                GVA10=GV10*(0.98+random()*0.04)
                
            except OverflowError:
                GVA1=GV1
                GVA2=GV2
                GVA3=GV3
                GVA4=GV4
                GVA5=GV5
                GVA6=GV6
                GVA7=GV7
                GVA8=GV8
                GVA9=GV9
                GVA10=GV10
                    

        Low=[1.2,1.2]
        Med=[1.5,1.5]
        High=[2,2]
        StartEnd=[times[0],times[-5]]
        StartEnd[0] = [datetime.now() + timedelta(hours=times[0])]
        StartEnd[1] = [datetime.now() + timedelta(hours=times[-5])]
        

        xaxis = [datetime.now() + timedelta(hours=times[i]) for i in range(len(times)-2)]
        
        RiverNameEnd=AllDataImage.find('All')
        RiverName=AllDataImage[0:RiverNameEnd]
        plt.title(RiverName) 
        plt.xlabel("Time (month-day hour)")
        plt.ylabel("Rain (mm) and River levels (m)") 
        plt.plot(xaxis,quantities[0:len(xaxis)],'b')
        plt.plot(xaxis,levels[0:len(xaxis)],'black')
        plt.plot(xaxis,trialequationc[0:len(xaxis)],'c')
        plt.plot(StartEnd,Low,'y')
        plt.plot(StartEnd,Med,'#4CBF3F')
        plt.plot(StartEnd,High,'g')
        matplotlib.pyplot.subplots_adjust(left=0.09, bottom=0, right=0.99, top=0.94, wspace=None, hspace=None)
        #print(plt.get_backend())
        plt.gcf().autofmt_xdate()
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        plt.savefig(AllDataImage)
        #plt.axis([-750,-500,0,2.5])

        with open(VariablesText, 'w') as wf:
            wf.write(str(GV1))
            wf.write(str(GV2))
            wf.write(str(GV3))
            wf.write(str(GV4))
            wf.write(str(GV5))
            wf.write(str(GV6))
            wf.write(str(GV7))
            wf.write(str(GV8))
            wf.write(str(GV9))
            wf.write(str(GV10))
            
        #print(levels)
        #print(trialequationb)
        #print(len(levels))
        #print(len(trialequationb))
        StartLocation="C:\Users\Dr Blue\Documents\RainBot\ "
        StartLocation=StartLocation[0:35]+ AllDataImage
        EndLocation="C:\Users\Dr Blue\Dropbox\North Wales\ "
        EndLocation=EndLocation[0:37]+ AllDataImage
        print(EndLocation)
        shutil.copy(StartLocation,EndLocation)
        print("move")
        
    except OverflowError:
        print("Too large")


        






    
        
            
        

    
if __name__ == '__main__':
    main()

