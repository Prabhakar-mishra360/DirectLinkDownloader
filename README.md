# DirectLinkDownloader

### Discription
- DirectLinkDownloader (GUI application) will allow you to get direct downloadable link (mega) to download movie/series from extramovies.
- Just give full link of movie or series from extramovies website and press Aabra ka dabra and you will get links in few seconds.
- A windows installable file also avaiable if you want to install software directly to your Windows machines (No need to install python).  

### Usage
- Without python installation:
  - Download DirectLinkDowloader.exe from 'Windows Executables 64bit'. Double click to install.
- With Python installation:
  - Download and install python 3
  - Clone/download project : 
  ```git clone https://github.com/Prabhakar-mishra360/DirectLinkDownloader.git```
  - Open command prompt with working directory as cloned/downloaded project folder
  - Then install all requirements
  ```pip install -r requirement.txt```
  - After proper installation of all requirement execute below command on same command prompt
  ```python DirectLinkDownloader.py```
- After application opens:
  - If you are trying to download a movie press on movie tab (default) give link, select resolution and press Aabra ka dabra.
  - If you are trying to download a series press on series tab give link select option torrent file or all episode links and press Aabra ka dabra and let the magic happen for you.  

### Tech
- DirectLinkDownloader uses python3 with PyQt5, BeautifulSoup, requests. 

### License
MIT
