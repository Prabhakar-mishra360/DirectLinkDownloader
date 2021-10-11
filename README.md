# DirectLinkDownloader

### Discription
- DirectLinkDownloader (GUI application) will allow you to get direct downloadable link (mega) to download movie/series from extramovies.
- Just give full link of movie or series from extramovies website and press Aabra ka dabra and you will get links in few seconds.
- A windows installable file also avaiable if you want to install software directly to your Windows machines (No need to install python).  

### Installation
- Without python installation:
  - Download DirectLinkDowloader.exe from 'Windows Executables 64bit'. Double click to install.
- With Python installation:
  - Download and install python 3
  - Clone/download project :   
  ```git clone https://github.com/Prabhakar-mishra360/DirectLinkDownloader.git```
  - Open command prompt with working directory DirectLinkDownloader folder present inside cloned/download project.
  - Then install all requirements:  
  ```pip install -r requirements.txt```
  - After proper installation of all requirement execute below command on same command prompt:  
  ```python DirectLinkDownloader.py```

### Usage
  - Search Tab
    - First tab is search tab, you need to give two input 1. Top level domain 2. Name of a movie or series you want to search.
    - Press on search, then wait for few seconds.
    - When success message popup and result count more than 0, you can select link from drop down and click on copy.
    - By clicking on copy, it will copy the selected text from dropdown to your system clipboard so you can directly paste on next tabs.
  - Movie Tab
    - If you are trying to download a movie press on movie tab, paste the link copied from seach tab if found, select resolution and press  
    Aabra ka dabra.
  - Series Tab
    - If you are trying to download a series press on series tab give link, select option torrent file or all episode links and press Aabra ka dabra and let the magic happen for you.
    - Torrent download option will only work for windows OS. 

### Tech
- DirectLinkDownloader uses python3 with PyQt5, BeautifulSoup, requests. 

### License
MIT
