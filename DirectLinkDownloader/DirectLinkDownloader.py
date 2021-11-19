'''Icon used is made by Freepik (https://www.freepik.com) from www.flaticon.com '''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import logging
import requests
from bs4 import BeautifulSoup
from getpass import getuser
import threading
from pyperclip import copy

class CustomException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Ui_MainWindow(object):
    def __init__(self) -> None:
        super().__init__()
        
        self._messageBox:QMessageBox = None
        self._url:str = ""
        self._resolution:int = -1
        self._choice:int = -1
        self.linkProvider = ""
        self._LOG_FILE_PATH = "Log.log"
        logging.basicConfig(filename=self._LOG_FILE_PATH,level=logging.DEBUG, 
                format='%(asctime)s %(message)s')
        logging.info("****************Application started****************")

    def isUpdateAvailable(self):
        try:
            URL = "https://github.com/Prabhakar-mishra360/DirectLinkDownloader/tree/main/Windows%20Executables%2064bit"
            response = requests.get(URL)
            APPVERSION = "DirectLinkDownloader 3.0.exe"
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                ONLINE_APP_VERSION = soup.findAll(class_ = "js-navigation-open Link--primary")[0].get("title")
                
                if(len(ONLINE_APP_VERSION) > len(APPVERSION) or ONLINE_APP_VERSION > APPVERSION):
                    self.showPopUp()
            else:
                logging.info("isUpdateAvailable request failed: "+str(response.status_code))
        except Exception as e:
            logging.info("Is update error: "+str(e))

    def showPopUp(self):
        
        self._messageBox = QMessageBox()
        self._messageBox.setWindowTitle("Update Available")
        self._messageBox.setText("Do you want to download?")
        self._messageBox.setIcon(QMessageBox.Question)
        self._messageBox.setWindowIcon(QtGui.QIcon('icon.png'))
        self._messageBox.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
        self._messageBox.buttonClicked.connect(self._downloadUpdate)
        self._messageBox.exec()

    def _downloadUpdate(self,choice):
        
        if(choice.text() == "OK"):
            self._messageBox.setIcon(QMessageBox.Information)
            self._messageBox.setText("Please Wait Downloading!")
            self._messageBox.repaint()
            
            DOWNLOAD_LINK = "https://raw.githubusercontent.com/Prabhakar-mishra360/DirectLinkDownloader/main/Windows%20Executables%2064bit/DirectLinkDownloader.exe"
            PATH = "C:/Users/"+getuser()+"/Downloads/"+"DirectLinkDownloader.exe"
            response = requests.get(DOWNLOAD_LINK)
            if response.status_code == 200:
                with open(PATH,'wb') as f:
                    f.write(response.content)
                self.setStatusBarMsg("Downloaded: "+PATH,"green")

            else:
                logging.info("Download failed with: "+str(response.status_code))



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 250)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 801, 231))
        self.tabs.setObjectName("tabs")

        self.Search = QtWidgets.QWidget()
        self.Search.setObjectName("Search")

        self.title = QtWidgets.QLabel(self.Search)
        self.title.setGeometry(QtCore.QRect(190, 0, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.search = QtWidgets.QPushButton(self.Search)
        self.search.setGeometry(QtCore.QRect(610, 50, 111, 23))
        self.search.setObjectName("search")
        self.search.clicked.connect(self.searchMovies)

        self.domain = QtWidgets.QLabel(self.Search)
        self.domain.setGeometry(QtCore.QRect(70, 50, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.domain.setFont(font)
        self.domain.setObjectName("domain")

        self.name = QtWidgets.QLabel(self.Search)
        self.name.setGeometry(QtCore.QRect(330, 50, 91, 20))
        self.name.setObjectName("name")

        self.tDomain = QtWidgets.QLineEdit(self.Search)
        self.tDomain.setGeometry(QtCore.QRect(180, 50, 113, 20))
        self.tDomain.setObjectName("tDomain")

        self.movieInput = QtWidgets.QLineEdit(self.Search)
        self.movieInput.setGeometry(QtCore.QRect(400, 50, 171, 20))
        self.movieInput.setObjectName("movieInput")

        self.website = QtWidgets.QLabel(self.Search)
        self.website.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.website.setObjectName("website")

        self.progressBarSearch = QtWidgets.QProgressBar(self.Search)
        self.progressBarSearch.setGeometry(QtCore.QRect(10, 160, 771, 31))
        self.progressBarSearch.setProperty("value", 0)
        self.progressBarSearch.setObjectName("progressBarSearch")

        self.resultLable = QtWidgets.QLabel(self.Search)
        self.resultLable.setGeometry(QtCore.QRect(20, 80, 81, 20))
        self.resultLable.setObjectName("resultLable")

        self.linkList = QtWidgets.QComboBox(self.Search)
        self.linkList.setGeometry(QtCore.QRect(20, 110, 551, 22))
        self.linkList.setObjectName("linkList")

        self.copy = QtWidgets.QPushButton(self.Search)
        self.copy.setGeometry(QtCore.QRect(610, 110, 111, 23))
        self.copy.setObjectName("copy")
        self.copy.clicked.connect(self.copyLink)
        
        self.tabs.addTab(self.Search, "")

        self.movie = QtWidgets.QWidget()
        self.movie.setObjectName("movie")

        self.Title_2 = QtWidgets.QLabel(self.movie)
        self.Title_2.setGeometry(QtCore.QRect(10, 10, 771, 21))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.Title_2.setFont(font)
        self.Title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_2.setObjectName("Title_2")

        self.megaLink = QtWidgets.QLineEdit(self.movie)
        self.megaLink.setGeometry(QtCore.QRect(10, 130, 680, 21))
        self.megaLink.setReadOnly(True)
        self.megaLink.setObjectName("megaLink")

        self.copyMovieLink = QtWidgets.QPushButton(self.movie)
        self.copyMovieLink.setGeometry(QtCore.QRect(700, 130, 60, 22))
        self.copyMovieLink.setObjectName("copyMovieLink")
        self.copyMovieLink.clicked.connect(self.copyLink)

        self.progressBar = QtWidgets.QProgressBar(self.movie)
        self.progressBar.setGeometry(QtCore.QRect(10, 162, 771, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.url = QtWidgets.QLineEdit(self.movie)
        self.url.setGeometry(QtCore.QRect(10, 50, 751, 21))
        self.url.setToolTip("")
        self.url.setToolTipDuration(-1)
        self.url.setReadOnly(False)
        self.url.setObjectName("url")

        self.selectMovieSite = QtWidgets.QComboBox(self.movie)
        self.selectMovieSite.setGeometry(QtCore.QRect(240, 90, 80, 23))
        self.selectMovieSite.setObjectName("selectSite")
        self.selectMovieSite.addItems(["Mega","ExtraFiles","ShareDrive"])

        self.getLink = QtWidgets.QPushButton(self.movie)
        self.getLink.setGeometry(QtCore.QRect(340, 90, 421, 23))
        self.getLink.setObjectName("getLink")
        self.getLink.clicked.connect(self.doMagicForMovies)

        self.fullHD = QtWidgets.QRadioButton(self.movie)
        self.fullHD.setGeometry(QtCore.QRect(120, 90, 91, 17))
        self.fullHD.setObjectName("fullHD")
        self.fullHD.clicked.connect(self.selectFullHD)

        self.hd = QtWidgets.QRadioButton(self.movie)
        self.hd.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.hd.setObjectName("hd")
        self.hd.clicked.connect(self.selectHD)

        self.tabs.addTab(self.movie, "")

        self.series = QtWidgets.QWidget()
        self.series.setObjectName("series")
        

        self.getLinks = QtWidgets.QPushButton(self.series)
        self.getLinks.setGeometry(QtCore.QRect(270, 90, 491, 23))
        self.getLinks.setObjectName("getLinks")
        self.getLinks.clicked.connect(self.doMagicForSeries)

        self.Title = QtWidgets.QLabel(self.series)
        self.Title.setGeometry(QtCore.QRect(10, 10, 771, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")

        self.surl = QtWidgets.QLineEdit(self.series)
        self.surl.setGeometry(QtCore.QRect(10, 50, 751, 21))
        self.surl.setObjectName("surl")

        self.megaLinks = QtWidgets.QTextEdit(self.series)
        self.megaLinks.setGeometry(QtCore.QRect(10, 130, 751, 71))
        self.megaLinks.setObjectName("megaLinks")

        self.episodes = QtWidgets.QRadioButton(self.series)
        self.episodes.setGeometry(QtCore.QRect(120, 90, 131, 17))
        self.episodes.setObjectName("episodes")
        self.episodes.clicked.connect(self.selectEpisodesLink)

        self.torrent = QtWidgets.QRadioButton(self.series)
        self.torrent.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.torrent.setObjectName("torrent")
        self.torrent.clicked.connect(self.selectTorrent)

        self.tabs.addTab(self.series, "")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        self.tabs.currentChanged.connect(lambda x :self.statusbar.clearMessage() )
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.isUpdateAvailable()

    def clear(self,who:str):
        self.statusbar.clearMessage()
        self.statusbar.setStyleSheet('color:black')
        self.statusbar.repaint()
        if who == "movie":
            self.megaLink.setText("")
            self.progressBar.setProperty("value", 0)
        if who == "series":
            self.megaLinks.clear()
            self.megaLinks.repaint()
        if who == "search":
            self.progressBarSearch.setValue(0)
            self.linkList.clear()
        

    def setStatusBarMsg(self,msg:str,color:str = 'black'):
        self.statusbar.showMessage(msg)
        self.statusbar.setStyleSheet('color:'+color)
        self.statusbar.repaint()

    #For archieve links for series
    def getFirstStageLinkSeries(self,url: str)->str:
        logging.info("In first stage of series")
        response = requests.get(url)

        # Retrving archieve links
        if(response.status_code == 200):
            soup = BeautifulSoup(response.text, "html.parser")
            link = soup.find(class_ = 'dlbuttnn')
        logging.debug("link of first stage series: "+str(link))
        return "" if link == None else link.get("href")

    # this is used to get link of torrent download page of extramovies
    def secondStageTorrentUrl(self,url:str)->str:
        logging.info("Inside second stage of torrent download")
        response = requests.get(url)

        if(response.status_code == 200):
            soup = BeautifulSoup(response.text, "html.parser")
            link = soup.find(class_ = 'buttn torrent')
        return link.get("href")

    def multithreadLinks(self,url:str,linkList:list):
        response = requests.get(url)
        lock = threading.Lock()
        if(response.status_code == 200):
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.findAll('a')
            for link in links:
                if str(link.get('href')).__contains__("view"):
                    lock.acquire()
                    linkList.append(link.get('href'))
                    lock.release()
                    break

    # This is used to get link of page from where torrent can be downloaded
    def thirdStageTorrentUrl(self,url:str)->str:
        logging.info("Inside third stage of torrent download")
        
        response = requests.get(url)

        if(response.status_code == 200):
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.findAll('a')
            for link in links:
                if(str(link).__contains__("torrent")):
                    return link.get("href")

    # This will download torrent file 
    def downloadTorrent(self,url:str)->bool:
        logging.info("Inside downloading stage of torrent download")
        try:
            torrentUrl = url[0:36] + "torrent/" + url[36:] + ".torrent"
            response = requests.get(torrentUrl)
            PATH = "C:/Users/"+getuser()+"/Downloads/"+url[36:] + ".torrent"
            if response.status_code == 200:
                with open(PATH,"wb") as f:
                    f.write(response.content)
            logging.info("File downloaded at: "+PATH)
            self.megaLinks.setText("File downloaded at: "+PATH)
            self.setStatusBarMsg("Success!","green")
        except Exception as e:
            logging.debug(str(e))
            raise CustomException("Error in downloading torrent file")
    
    
    

    # This will retrive all links from archieve page
    def secondStageEpisodesUrls(self,url:str)->list:
        logging.info("Inside second stage of episodes download")
        response = requests.get(url)
        usefullLinks: list = []
        domain = url.split("/")[2]
        # Retrving archieve links
        if(response.status_code == 200):
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.findAll(class_ = "buttn blue")
            self.setStatusBarMsg("Please wait... 10%")
            for link in links:
                usefullLinks.append("https://"+domain+link.get("href"))
                
        return usefullLinks

    # This will takes all episode download page link and return extralinks for all episodes
    def thirdStageEpisodesUrls(self,urls:list)->list:
        logging.info("Inside third stage of episodes download")
        usefullLinks:list = []
        i:int = 0
        length = len(urls) 
        while i < length:
            self.setStatusBarMsg("Please wait... "+str(round((42/length)*(i+1),1))+"%")
            if i+4 < len(urls):
                t1 = threading.Thread(target=self.multithreadLinks,args=(urls[i],usefullLinks))
                t2 = threading.Thread(target=self.multithreadLinks,args=(urls[i+1],usefullLinks))
                t3 = threading.Thread(target=self.multithreadLinks,args=(urls[i+2],usefullLinks))
                t4 = threading.Thread(target=self.multithreadLinks,args=(urls[i+3],usefullLinks))
                t1.start()
                t2.start()
                t3.start()
                t4.start()

                t1.join()
                t2.join()
                t3.join()
                t4.join()
                i+=4
            elif(i+2 < len(urls)):
                t1 = threading.Thread(target=self.multithreadLinks,args=(urls[i],usefullLinks))
                t2 = threading.Thread(target=self.multithreadLinks,args=(urls[i+1],usefullLinks))

                t1.start()
                t2.start()

                t1.join()
                t2.join()

                i += 2
            else:
                self.multithreadLinks(urls[i],usefullLinks)
                i +=1

        return usefullLinks

    # This function will get all mega links
    def forthStageEpisodeUrls(self,urls:list)->list:
        logging.info("Inside fourth and final stage of episodes download")
        usefullLinks = []
        slot:int = 43/len(urls)
        i:int = 1
        for url in urls:
            response = requests.post(url)
            
            if(response.status_code == 200):
                self.setStatusBarMsg("Please wait... "+str(round(50+slot*i,1))+"%")
                i+=1
                soup = BeautifulSoup(response.text, "html.parser")
                links = soup.findAll('a')
                for link in links:
                    if str(link.get('href')).__contains__("mega.nz"):
                        usefullLinks.append(link.get('href'))
                        break
                    
        return usefullLinks

        # For archieve links
    def getFirstStageLink(self,url: str):
        logging.info("Started first stage")
        response = requests.get(url)
        usefullLinks: list = []
        self.progressBar.setProperty("value", 10)
        # Retrving archieve links
        if(response.status_code == 200):
            logging.info("Status code 200")
            self.progressBar.setProperty("value", 35)
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.findAll(class_='dlbuttnn')
            self.progressBar.setProperty("value", 40)
            for link in links:
                usefullLinks.append(str(link.get('href')))
            logging.info("First stage urls: "+str(usefullLinks))
            return usefullLinks
        else:
            raise CustomException("Unable to fetch link")

    # For mega download page link of extramovies
    def secondStageUrls(self,url: str):
        logging.info("Started second stage")
        response = requests.get(url)
        usefullLinks: list = []

        # Retrving archieve links
        if(response.status_code == 200):
            logging.info("Status code 200")
            self.progressBar.setProperty("value", 65)
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.findAll('a')
            self.progressBar.setProperty("value", 72)
            for link in links:
                if str(link).__contains__(self.selectMovieSite.currentText()):
                    usefullLinks.append(str(link.get('href')))
            logging.info("Second stage urls: "+str(usefullLinks))
            return usefullLinks
        else:
            raise CustomException("Unable to fetch link")

    def whichSourceForMovie(self):
        selectedOption = self.selectMovieSite.currentText()
        if selectedOption == "Mega":
            self.linkProvider = "mega.nz"
        elif selectedOption == "ExtraFiles":
            self.linkProvider = "extrafiles"
        elif selectedOption == "ShareDrive":
            self.linkProvider = "sharedrive"
    
    # For download page link of extramovies
    def thirdStageUrls(self,url: str):
        response = requests.get(url)
        logging.info("Started third stage")


        # Retriving mega link
        if(response.status_code == 200):
            logging.info("Status code 200")
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.findAll('a')
            self.progressBar.setProperty("value", 95)
            for link in links:
                if str(link.get('href')).__contains__(self.linkProvider):
                    logging.info("Third stage urls: "+str(link.get('href')))
                    return (str(link.get('href')))
        else:
            raise CustomException("Unable to fetch link")
    
    def selectHD(self):
        self._resolution = 1

    def selectFullHD(self):
        self._resolution = 2

    def selectTorrent(self):
        self._choice = 1
    
    def selectEpisodesLink(self):
        self._choice = 2

    # Return 1 if HD available, Return 2 if Full HD available
    def resolutionCheck(self,url:str)->None:
        resolution:int = -1
        if(url.__contains__("720p") and url.__contains__("1080p")):
            pass
        elif url.__contains__("720p"):
            resolution = 1
        elif url.__contains__("1080p"):
            resolution = 2
        
        if(self._resolution == 2 and resolution == 1):
            self.statusbar.showMessage("Full HD not present, fetching HD link")
        elif(self._resolution == 1 and resolution == 2):
            self.statusbar.showMessage("HD not present, fetching Full HD link")


    def doMagicForMovies(self):
        
        logging.info("Magic started for movie...")
        self.clear("movie")
        self.whichSourceForMovie()
        try:
            self._url = self.url.text()
            if(self._url.strip() == ""):
                raise CustomException("Requested Url is empty!")
            elif(self._resolution == -1):
                raise CustomException("Please select resolution!")
            else:
                domain = self._url.split("/")[2]
                logging.info("Site is: "+domain)
                self.resolutionCheck(self._url)
                firstStageUrls = self.getFirstStageLink(self._url)
                self.progressBar.setProperty("value", 45)

                if(len(firstStageUrls) == 0):
                    self._url = "https://"+domain+(self.secondStageUrls(self._url))[0]
                    logging.info("No url found in stage 1, seems old site. Going into stage 2")
                elif(len(firstStageUrls) == 1):
                    self._url = firstStageUrls[0]
                    self.progressBar.setProperty("value", 49)
                    self._url = "https://"+domain+(self.secondStageUrls(self._url))[0]
                else: 
                    if(self._resolution == 1):
                        self._url = firstStageUrls[0]
                        logging.info("User selected HD")
                    elif self._resolution == 2:
                        self._url = firstStageUrls[1]

                    self.progressBar.setProperty("value", 49)
                    self._url = "https://"+domain+(self.secondStageUrls(self._url))[0]

                self.progressBar.setProperty("value", 85)
                self.megaLink.setText(self.thirdStageUrls(self._url))

                self.progressBar.setProperty("value", 100)

                self.statusbar.showMessage("Success!")
                self.statusbar.setStyleSheet('color:green')

                logging.info("Success!")
        except CustomException as ce:
             self.statusbar.showMessage(str(ce))
             self.statusbar.setStyleSheet('color:red')
        except Exception as e:
             self.statusbar.showMessage("Something went wrong!")
             self.statusbar.setStyleSheet('color:red')
             logging.debug(str(e))

    def doMagicForSeries(self):
        logging.info("Magic started for series...")
        self.clear("series")
        try:
            self._url = self.surl.text()
            if(self._url.strip() == ""):
                raise CustomException("Requested Url is empty!")
            elif(self._choice == -1):
                raise CustomException("Please choose torrent/episode links!")
            else:
                domain = self._url.split("/")[2]
                logging.info("Site is: "+domain)
                self.resolutionCheck(self._url)
                firstStageUrls = self.getFirstStageLinkSeries(self._url)

                if(self._choice == 1):
                    logging.debug("inside torrent download file")
                    self.setStatusBarMsg("Please wait...","black")
                    if firstStageUrls.strip() == "":
                        logging.info("Not get any link from first stage might be old layout")
                        firstStageUrls = self.surl.text()

                    secondStageUrl = self.secondStageTorrentUrl(firstStageUrls)
                    logging.info("Second stage torrent links: "+str(secondStageUrl))
                    thirdStageurl = self.thirdStageTorrentUrl("https://"+domain+secondStageUrl)
                    logging.info("Third stage torrent links: "+str(thirdStageurl))
                    self.downloadTorrent(thirdStageurl)

                elif self._choice == 2:
                    self.setStatusBarMsg("Please wait... 0.0%")
                    logging.info("Inside episode download links")
                    if firstStageUrls.strip() == "":
                        logging.info("Not get any link from first stage might be old layout")
                        firstStageUrls = self._url
                        self.setStatusBarMsg("Please wait... 2.0%")
                   
                    secondStageUrls = self.secondStageEpisodesUrls(firstStageUrls)
                    logging.info("Second stage episodes links: "+str(secondStageUrls))
                    self.setStatusBarMsg("Please wait... 15.0%")

                    thirdStageUrls =  self.thirdStageEpisodesUrls(secondStageUrls)
                    logging.info("Third stage episodes links: "+str(thirdStageUrls))
                    self.setStatusBarMsg("Please wait... 50.0%")

                    megaLinks = self.forthStageEpisodeUrls(thirdStageUrls)
                    logging.info("Final stage episodes links: "+str(megaLinks))
                    self.setStatusBarMsg("Please wait... 95.0%")

                    for megaLink in megaLinks:
                        self.megaLinks.append(megaLink + "\n")
                    self.setStatusBarMsg("Please wait... 100%")
                    self.setStatusBarMsg("Success!","green")

                    logging.info("Success for series")
        except CustomException as ce:
            self.setStatusBarMsg(str(ce),"red")
            
        except Exception as e:
           self.setStatusBarMsg("Something went wrong!", "red")
           logging.debug(str(e))

    def searchMovies(self):
        try:
            self.clear("search")
            
            topLevelDomain = self.tDomain.text()
            if topLevelDomain.strip() == "":
                raise CustomException("Top Level domain required.")
            
            searchString = self.movieInput.text()
            if searchString.strip() == "":
                raise CustomException("Movie/Series name required.")

            self.progressBarSearch.setProperty("value", 10)
            url = "https://www.extramovies."+topLevelDomain+"?s="+searchString
            searchString = searchString.lower().replace(" ","-")
            qualifiedLinks = set([])
            response = requests.get(url)
            if(response.status_code == 200):
                soup = BeautifulSoup(response.text,"html.parser")
                links = soup.findAll('a')
                slot:int = 80//len(links)
                i:int = 1
                for link in links:
                    href = str(link.get("href"))
                    if(href.startswith("https") and href.__contains__(searchString) and not href.__contains__("login") 
                       and not href.__contains__("page")):
                        qualifiedLinks.add(href)
                    self.progressBarSearch.setValue(10+slot*i)
                    i += 1
                self.linkList.addItems(qualifiedLinks)
                self.setStatusBarMsg("Success. Number of links found: "+str(len(qualifiedLinks)),"green")
                self.progressBarSearch.setValue(100)
            else:
                raise CustomException("Could not able to get links, status code:",response.status_code)

        except CustomException as ce:
            self.setStatusBarMsg(str(ce),"red")
        except Exception as e:
            self.setStatusBarMsg("Something went wrong!", "red")
            logging.debug(str(e))
        
    def copyLink(self):
        tabIndex:int = self.tabs.currentIndex()
        if tabIndex == 0:    
            copy(self.linkList.currentText())
        elif tabIndex == 1:
            copy(self.megaLink.text())
        self.setStatusBarMsg("Copied!","green")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Search in Extramovies"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.domain.setText(_translate("MainWindow", "www.extramovies."))
        self.name.setText(_translate("MainWindow", "Movie/Series:"))
        self.tDomain.setPlaceholderText(_translate("MainWindow", "Top level domain"))
        self.movieInput.setPlaceholderText(_translate("MainWindow", "Movie/series name"))
        self.website.setText(_translate("MainWindow", "Website:"))
        self.resultLable.setText(_translate("MainWindow", "Search Results:"))
        self.copy.setText(_translate("MainWindow", "Copy"))
        self.Title_2.setText(_translate("MainWindow", "ExtraMovies Direct Downloader"))
        self.megaLink.setPlaceholderText(_translate("MainWindow", "Link will display here"))
        self.copyMovieLink.setText(_translate("MainWindow", "Copy"))
        self.url.setPlaceholderText(_translate("MainWindow", "Movie Link from Extramovies"))
        self.getLink.setText(_translate("MainWindow", "Aabra ka dabra"))
        self.fullHD.setText(_translate("MainWindow", "Full HD 1080p"))
        self.hd.setText(_translate("MainWindow", "HD 720p"))
        self.tabs.setTabText(self.tabs.indexOf(self.movie), _translate("MainWindow", "Movie"))
        self.getLinks.setText(_translate("MainWindow", "Aabra ka dabra"))
        self.Title.setText(_translate("MainWindow", "ExtraMovies Direct Downloader"))
        self.surl.setPlaceholderText(_translate("MainWindow", "Series Link from Extramovies"))
        self.megaLinks.setPlaceholderText(_translate("MainWindow", "Mega Links will appear here if selected All Episodes option"))
        self.episodes.setText(_translate("MainWindow", "All Episodes mega links"))
        self.torrent.setText(_translate("MainWindow", "Torrent File"))
        self.tabs.setTabText(self.tabs.indexOf(self.series), _translate("MainWindow", "Series"))
        self.tabs.setTabText(self.tabs.indexOf(self.Search), _translate("MainWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("DirectLinkDownloader")
    MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
    MainWindow.show()
    sys.exit(app.exec_())
