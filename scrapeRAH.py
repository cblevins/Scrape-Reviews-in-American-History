'''
Program to scrape reviews from a specific issue of Reviews in American History.
Note: requires browser access to Project MUSE
Created 9/25/2012 by Cameron Blevins
'''

import os, urllib2, urllib, re

def main():
    volume="41" #change volume number
    issue = "2" #change issue number
    volumeIssue = volume+"."+issue #concatenate vol and issue for a URL
        #make a directory for the volume you want to download
    newFolder=os.getcwd()+'/'+volumeIssue
    if volumeIssue not in os.listdir(os.getcwd()):
        os.mkdir(newFolder)
    os.chdir(newFolder)
        #download the pdfs of each article in the issue
    page = urllib2.urlopen("http://muse.jhu.edu/journals/reviews_in_american_history/toc/rah."+volumeIssue+".html")
    pageText= page.read()
        #identify links to pdfs
    findString= re.findall("<.*>Download PDF", pageText)
    for r in findString:
        fileName = re.findall("/journals/reviews_in_american_history/v0"+volume+"/"+volumeIssue+"."+"[a-z,-]+"+".pdf", r)
        for f in fileName:
                #isolate the name of the PDF file
            nameFile = re.findall("[a-z,-]+"+".pdf", f)
            nameFile= nameFile[0]
                #download the pdf file itself
            urllib.urlretrieve("http://muse.jhu.edu"+f, newFolder+'/'+nameFile)
            
main()

