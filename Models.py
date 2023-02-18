#-----------------------------------------------------------------------------------
# Part of the initial source code for primitive Shape (c) 2018 fieldOfView and CalibrationShapes (c) 2020-2022 5@xes
#
# The 3D-Models plugin is released under the terms of the AGPLv3 or higher.
# Modifications M4L 2023
#-----------------------------------------------------------------------------------
#
# V1.0.0 Initial Release
#-------------------------------------------------------------------------------------------

VERSION_QT5 = False
try:
    from PyQt6.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, QUrl
    from PyQt6.QtGui import QDesktopServices
except ImportError:
    from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, QUrl
    from PyQt5.QtGui import QDesktopServices
    VERSION_QT5 = True
    
# Imports from the python standard library to build the plugin functionality
import os

from UM.Extension import Extension
from UM.PluginRegistry import PluginRegistry
from UM.Application import Application
from cura.CuraApplication import CuraApplication

from UM.Resources import Resources
from UM.Settings.SettingInstance import SettingInstance

from cura.CuraVersion import CuraVersion  # type: ignore
from UM.Version import Version

from UM.Logger import Logger
from UM.Message import Message

from UM.i18n import i18nCatalog

i18n_cura_catalog = i18nCatalog("cura")
i18n_catalog = i18nCatalog("fdmprinter.def.json")
i18n_extrud_catalog = i18nCatalog("fdmextruder.def.json")

Resources.addSearchPath(
    os.path.join(os.path.abspath(os.path.dirname(__file__)))
)  # Plugin translation file import

catalog = i18nCatalog("models")

if catalog.hasTranslationLoaded():
    Logger.log("i", "Search 3D-Models loaded!")

#This class is the extension and doubles as QObject to manage the qml    
class Models(QObject, Extension):
    #Create an api
    from cura.CuraApplication import CuraApplication
    api = CuraApplication.getInstance().getCuraAPI()
    
    
    def __init__(self, parent = None) -> None:
        QObject.__init__(self, parent)
        
        self._controller = CuraApplication.getInstance().getController()
        self._message = None
                
        self.setMenuName(catalog.i18nc("@item:inmenu", "Search 3D-Model"))
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Thingiverse Homepage"), self.gotoThingiverse)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Cults Homepage"), self.gotoCults)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Printables Homepage"), self.gotoPrintables)  
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open MyMiniFactory Homepage"), self.gotoMyMiniFactory)          
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Pinshape Homepage"), self.gotoPinshape)           
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open YouMagine Homepage"), self.gotoYouMagine)         
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Threeding Homepage"), self.gotoThreeding)     
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open redpath Homepage"), self.gotoredpath)          
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Fab365 Homepage"), self.gotofab)    
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open CGTrader Homepage"), self.gotoCGTrader)  
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open TurboSquid Homepage"), self.gotoTurboSquid)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open 3DExport Homepage"), self.gotoExport)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Free3D Homepage"), self.gotoFree)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Instructables Homepage"), self.gotoInstructables)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open NIH 3D Print Exchange Homepage"), self.gotoExchange)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Smithsonian Homepage"), self.gotoSmithsonian)        
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open African Fossils Homepage"), self.gotoAfricanFossils)         
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open NASA 3D Resources Homepage"), self.gotoNASA)          
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Dremel Lesson Plans Homepage"), self.gotoDremel)     
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Creality Cloud Homepage"), self.gotoCreality)     
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open 3DSets Homepage"), self.gotoSets)  
        self.addMenuItem("   ", lambda: None)        
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Search at Yeggi"), self.gotoYeggi)         
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Search at STLFinder"), self.gotoSTLFinder)    
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Search at Thangs"), self.gotoThangs)   
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Search at 3dmdb"), self.gotomdb) 
        self.addMenuItem("     ", lambda: None)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Help"), self.gotoHelp)
  
    def gotoThingiverse(self) -> None:
        QDesktopServices.openUrl(QUrl("https://www.thingiverse.com/"))
        
    def gotoCults(self) -> None:
        QDesktopServices.openUrl(QUrl("https://cults3d.com/"))
     
    def gotoPrintables(self) -> None:
        QDesktopServices.openUrl(QUrl("https://www.printables.com/")) 

    def gotoMyMiniFactory(self) -> None:
        QDesktopServices.openUrl(QUrl("https://www.myminifactory.com/")) 
     
    def gotoPinshape(self) -> None:
        QDesktopServices.openUrl(QUrl("https://pinshape.com/"))      
     
    def gotoYouMagine(self) -> None:
        QDesktopServices.openUrl(QUrl("https://www.youmagine.com/"))      
     
    def gotoThreeding(self) -> None:
        QDesktopServices.openUrl(QUrl("https://www.threeding.com/"))        

    def gotoredpath(self) -> None:
        QDesktopServices.openUrl(QUrl("https://www.redpah.com/"))         

    def gotofab(self) -> None:
        QDesktopServices.openUrl(QUrl("https://fab365.net/"))     
        
    def gotoCGTrader(self) -> None:
        QDesktopServices.openUrl(QUrl("https://www.cgtrader.com/"))         

    def gotoTurboSquid(self) -> None:
        QDesktopServices.openUrl(QUrl("https://www.turbosquid.com/"))  

    def gotoExport(self) -> None:
        QDesktopServices.openUrl(QUrl("https://de.3dexport.com/")) 

    def gotoFree(self) -> None:
        QDesktopServices.openUrl(QUrl("https://free3d.com/")) 
  
    def gotoInstructables(self) -> None:
        QDesktopServices.openUrl(QUrl("https://www.instructables.com/"))   

    def gotoExchange(self) -> None:
        QDesktopServices.openUrl(QUrl("https://3dprint.nih.gov/"))    

    def gotoSmithsonian(self) -> None:
        QDesktopServices.openUrl(QUrl("https://3d.si.edu/")) 

    def gotoAfricanFossils(self) -> None:
        QDesktopServices.openUrl(QUrl("https://africanfossils.org/")) 

    def gotoNASA(self) -> None:
        QDesktopServices.openUrl(QUrl("https://nasa3d.arc.nasa.gov/models/printable")) 

    def gotoDremel(self) -> None:
        QDesktopServices.openUrl(QUrl("https://3pitech.com/pages/dremel-lesson-plans")) 
        
    def gotoCreality(self) -> None:
        QDesktopServices.openUrl(QUrl("https://m.crealitycloud.com/en/3d-models")) 
        
    def gotoSets(self) -> None:
        QDesktopServices.openUrl(QUrl("https://3dsets.com/")) 
        
    def gotoYeggi(self) -> None:
        QDesktopServices.openUrl(QUrl("https://www.yeggi.com/"))        
        
    def gotoSTLFinder(self) -> None:
        QDesktopServices.openUrl(QUrl("https://www.stlfinder.com/"))          
        
    def gotoThangs(self) -> None:
        QDesktopServices.openUrl(QUrl("https://thangs.com/"))        
        
    def gotomdb(self) -> None:
        QDesktopServices.openUrl(QUrl("https://3dmdb.com/"))   
  
    def gotoHelp(self) -> None:
        QDesktopServices.openUrl(QUrl("http://www.x40-community.org/index.php/9-cura-workflow/89-cura-idex-calibration-parts-plugin"))

   
