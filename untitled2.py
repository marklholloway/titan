# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 18:29:00 2018

@author: Mark
"""




import win32gui
import pyautogui
import win32com.client

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 2.5



class Windowparser(object):
    #class needs to be cleaned up to remove self calls#
    def __init__(self,appId):
        self.appId = appId
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0 
        try:
            self.updateWindowDimensions()            
        except  ValueError:
            print ("Incorrect appID passed to window parser")
                       
    def updateWindowDimensions(self):
        self.hwndMain = win32gui.FindWindow(self.appId,None)
        rect = win32gui.GetWindowRect(self.hwndMain)
        self.x = rect[0]
        self.y = rect[1]
        self.w = rect[2] - self.x
        self.h = rect[3] - self.y

    def PrintDimensions(self):
            print ("Window %s:" % win32gui.GetWindowText(self.hwndMain))
            print ("\tLocation: (%d, %d)" % (self.x, self.y))
            print ("\t    Size: (%d, %d)" % (self.w, self.h))
    
    def BringForward(self): #this function should belong to another class#
         shell = win32com.client.Dispatch("WScript.Shell")
         shell.SendKeys('%')
         win32gui.SetForegroundWindow(self.hwndMain)
        


def main():
    
    parser = Windowparser("MSPaintApp")    
    parser.updateWindowDimensions()
    parser.PrintDimensions()        
    parser.BringForward()

if __name__ == '__main__':
    main()
   



