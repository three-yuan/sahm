'''
Created on Sep 17, 2010

@author: talbertc
'''
from core.modules.vistrails_module import Module
from PyQt4 import QtCore, QtGui
import csv
from utils import dir_path_value, mktempfile, mktempdir, create_file_module
import shutil
import os
from core.system import execute_cmdline
import subprocess

#class SelectListWidget(QtGui.QTreeWidget):
#
#    def __init__(self, inputMDS, parent=None):
#        print inputMDS
#        QtGui.QTreeWidget.__init__(self, parent)
#        self.setColumnCount(1)
#        self.tree_items = {}
#        
#        csvfile = open(inputMDS, "r")
#        reader = csv.reader(csvfile)
#        header = reader.next() #store the header
#        header2 = reader.next() #the 2nd line of the mds with use/don't use
#        header3 = reader.next() #the 3rd line of the mds with the path
#        
#        headerList = []
#        for i in range(0, len(header)):
#            headerList.append([header[i], header2[i], header3[i]])
#        
#        for item in headerList:
#            print item
#            if item[2] <> '':
#                child_item = QtGui.QTreeWidgetItem([item[0],])
#                child_item.setFlags(QtCore.Qt.ItemIsUserCheckable |
#                                QtCore.Qt.ItemIsEnabled)
#                if int(item[1]) == 0:
#                    child_item.setCheckState(0, QtCore.Qt.Unchecked)
#                else:
#                    child_item.setCheckState(0, QtCore.Qt.Checked)
#                self.addTopLevelItem(child_item)
#                #self.tree_items[file] = child_item
#        csvfile.close()
#
#    def updateMDS_with_selected(self, inputMDS, outputMDS):
#        reader = csv.reader(open(inputMDS, "r"))
#        header = reader.next() #store the header
#        header2 = reader.next() #the 2nd line of the mds with use/don't use
#        header3 = reader.next() #the 3rd line of the mds with the path
#        
#        headerList = []
#        for i in range(0, len(header)):
#            headerList.append([header[i], header2[i], header3[i]])
#        
#        outHeader2 = []
#        for item in headerList:
#            if item[2] == '': #append our empty columns to header line 2
#                outHeader2.append('')
#                
#        
#        for file,item in self.tree_items.iteritems():
#            if item.checkState(0) == QtCore.Qt.Checked:
#                outHeader2.append("1")
#            else:
#                outHeader2.append("0")
#                
#        writer = csv.writer(open(outputMDS, "w"))
#        writer.writerow(header)
#        writer.writerow(outHeader2)
#        writer.writerow(header3)
#        for row in reader:
#            writer.writerow(row)
#        writer.close
#    
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class SelectListDialog(QtGui.QDialog):

    
    def __init__(self, inputMDS, outputMDS, rPath, modelsPath, parent=None):
        print inputMDS, outputMDS, rPath, modelsPath
        self.rPath = rPath
        self.modelsPath = modelsPath
        #print dir(self)
        
        QtGui.QDialog.__init__(self, parent)
        
        self.inputMDS = inputMDS
        self.outputMDS = outputMDS
        self.outputDir = os.path.split(outputMDS)[0]
        
        
        
        layout = QtGui.QVBoxLayout()
        ##begin  autogenerated code from QtDesigner
        self.resize(1017, 779)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setMargin(5)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(0, 0))
        self.splitter.setFrameShape(QtGui.QFrame.Box)
        self.splitter.setFrameShadow(QtGui.QFrame.Plain)
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(6, 6, 3, 3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.treeview = QtGui.QTreeWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeview.sizePolicy().hasHeightForWidth())
        self.treeview.setSizePolicy(sizePolicy)
        self.treeview.setMinimumSize(QtCore.QSize(75, 0))
        self.treeview.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeview.setSizeIncrement(QtCore.QSize(100, 0))
        self.treeview.setBaseSize(QtCore.QSize(0, 0))
        self.treeview.setObjectName(_fromUtf8("treeview"))
        self.verticalLayout.addWidget(self.treeview)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnRunR = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRunR.sizePolicy().hasHeightForWidth())
        self.btnRunR.setSizePolicy(sizePolicy)
        self.btnRunR.setObjectName(_fromUtf8("btnRunR"))
        self.horizontalLayout_3.addWidget(self.btnRunR)
        spacerItem = QtGui.QSpacerItem(10, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setText(_fromUtf8("0.7"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        
        self.scene = QtGui.QGraphicsScene() 
        self.view = QtGui.QGraphicsView(self.scene)
        self.view.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.view.sizePolicy().hasHeightForWidth())
        self.view.setSizePolicy(sizePolicy)
        self.view.setResizeAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.view.setObjectName(_fromUtf8("view"))
        
        self.splitter.addWidget(self.view)
        
        self.verticalLayout_3.addWidget(self.splitter)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 3, -1, 3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnOK = QtGui.QPushButton()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOK.sizePolicy().hasHeightForWidth())
        self.btnOK.setSizePolicy(sizePolicy)
        self.btnOK.setBaseSize(QtCore.QSize(100, 0))
        self.btnOK.setToolTip(_fromUtf8(""))
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.horizontalLayout.addWidget(self.btnOK)
        self.btnCancel = QtGui.QPushButton()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy)
        self.btnCancel.setBaseSize(QtCore.QSize(100, 0))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.setWindowTitle(_fromUtf8("Covariate Coorelation viewer"))
        self.label_2.setText(_fromUtf8("Covariates"))
        self.btnRunR.setText(_fromUtf8("Update"))
        self.label.setText(_fromUtf8("Threshold"))
        self.btnOK.setText(_fromUtf8("OK"))
        self.btnCancel.setText(_fromUtf8("Cancel"))
        
        
        ##End  autogenerated code from QtDesigner
        
        
        
        
        
        
        layout.addLayout(self.verticalLayout_3)
        
        
        self.btnCancel.setShortcut('Esc')
        self.connect(self.btnOK, QtCore.SIGNAL('clicked(bool)'),
                     self.okTriggered)
        self.connect(self.btnCancel, QtCore.SIGNAL('clicked(bool)'),
                     self.cancel)
        self.connect(self.btnRunR, QtCore.SIGNAL('clicked(bool)'),
                     self.updateROutput)
        
        self.scene.wheelEvent = self.wheel_event
        
        #code to populate the treeview with the contents of our MDS
        self.PopulateTreeview()
        
        self.setLayout(layout)
        
        #code to add in pictureviewer stuff
        outputPic = self.runR(self.inputMDS)
        self.setup_view()
        self.load_picture(outputPic)
        

    def okTriggered(self):
        self.SaveMDSFromTreeview()
        self.done(0)

    def cancel(self):
        shutil.copyfile(self.inputMDS, self.outputMDS)
        self.done(1)
    
    def PopulateTreeview(self):
        print self.inputMDS
        self.treeview.setColumnCount(1)
        
        csvfile = open(self.inputMDS, "r")
        reader = csv.reader(csvfile)
        header = reader.next() #store the header
        header2 = reader.next() #the 2nd line of the mds with use/don't use
        header3 = reader.next() #the 3rd line of the mds with the path
        
        headerList = []
        for i in range(0, len(header)):
            headerList.append([header[i], header2[i], header3[i]])
        
        for item in headerList:
            print item
            if item[2] <> '':
                child_item = QtGui.QTreeWidgetItem([item[0],])
                child_item.setFlags(QtCore.Qt.ItemIsUserCheckable |
                                QtCore.Qt.ItemIsEnabled)
                if int(item[1]) == 0:
                    child_item.setCheckState(0, QtCore.Qt.Unchecked)
                else:
                    child_item.setCheckState(0, QtCore.Qt.Checked)
                self.treeview.addTopLevelItem(child_item)
                #self.tree_items[file] = child_item
        csvfile.close()
        
    def SaveMDSFromTreeview(self):
        #updates the second header line on the input MDS file 
        #to reflect the checked items in the tree view 
        #and saves the results to the output MDS.
        
        reader = csv.reader(open(self.inputMDS, "r"))
        header = reader.next() #store the header
        header2 = reader.next() #the 2nd line of the mds with use/don't use
        header3 = reader.next() #the 3rd line of the mds with the path
        
        headerList = []
        for i in range(0, len(header)):
            headerList.append([header[i], header2[i], header3[i]])
        
        outHeader2 = []
        for item in headerList:
            if item[2] == '': #append our empty columns to header line 2
                outHeader2.append('0')
                
        treeviewIter = QtGui.QTreeWidgetItemIterator(self.treeview)
        while treeviewIter.value():
            if treeviewIter.value().checkState(0) == QtCore.Qt.Checked:
                outHeader2.append("1")
            else:
                outHeader2.append("0")
            treeviewIter += 1

        
        oFile = open(self.outputMDS, 'wb')
        writer = csv.writer(oFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(outHeader2)
        writer.writerow(header3)
        for row in reader:
            writer.writerow(row)
        oFile.close

    def updateROutput(self):
        self.SaveMDSFromTreeview()
        outputPic = self.runR(self.outputMDS)
        self.load_picture(outputPic)
        
    def runR(self, MDSfile):
        #layers_fname = os.path.join(os.path.dirname(__file__), 'layers.csv')
        print self.rPath, self.modelsPath
        #for now returning a random jpeg
        
        program = os.path.join(self.rPath, "i386", "Rterm.exe") #-q prevents program from running
        script = os.path.join(self.modelsPath, "PairsExplore.r")

        #output_dname =  #mktempdir(prefix='output_PE_')
        
#        threshold = unicode(self.lineEdit.text().toPlainText().toUtf)
        
        
#        arg_items = ["i=" + MDSfile, "o=" + output_dname, "m=" +  str(self.lineEdit.text())]
#        cmdline = [program, "--vanilla", "-f", script, "--args"] + arg_items
#        print 'running', cmdline
#        output = []
#        res = execute_cmdline(cmdline, output)
#        
#        print "res:", res
#        print "output:", output
        #    arg_items = list(itertools.chain(*args.items()))
#    output = []
#    jar_name = os.path.join(sahm_path, jar_name)
#    cmdline = ['java', '-jar', jar_name] + arg_items
#    print 'running', cmdline
#    res = execute_cmdline(['java', '-jar', jar_name] + arg_items, output)
#    return res, output


        args = "i=" + MDSfile + " o=" + self.outputDir + " m=" + str(self.lineEdit.text())

        command = program + " --vanilla -f " + script + " --args " + args
        p = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        # Second, use communicate to run the command; communicate() returns a
        #   tuple (stdoutdata, stderrdata)
        print "starting R Processing"

        ret = p.communicate()
        if ret[1]:
            print ret[1]
        del(ret)
        
        if os.path.exists(os.path.join(self.outputDir, "Predictor_Correlation.jpg")):
            return os.path.join(self.outputDir, "Predictor_Correlation.jpg")
        else:
            raise IOError

    def load_picture(self, strPicture):
        print "loading picture", strPicture
        self.l_pix = QtGui.QPixmap(strPicture) 
        self.c_view = self.l_pix.scaled(self.max_vsize, self.max_vsize, 
                                            QtCore.Qt.KeepAspectRatio, 
                                            QtCore.Qt.FastTransformation) 
        #change the previous line with QtCore.Qt.SmoothTransformation eventually 
        self.view_current()

    def setup_view(self):
            #print "setup_view" 
            self.zoom_step = 0.04 
            self.w_vsize = self.view.size().width() 
            self.h_vsize = self.view.size().height() 
            if self.w_vsize <= self.h_vsize: 
                self.max_vsize = self.w_vsize * 1.5
            else: 
                self.max_vsize = self.h_vsize * 1.5
            self.l_pix = "" 
    

#            self.load_current(r"C:\Users\Public\Pictures\Sample Pictures\Jellyfish.jpg") 
            
    def view_current(self):
        #print "view_current"
        size_img = self.c_view.size() 
        wth, hgt = QtCore.QSize.width(size_img), QtCore.QSize.height(size_img) 
        self.scene.clear() 
        self.scene.setSceneRect(0, 0, wth, hgt) 
        self.scene.addPixmap(self.c_view) 
        QtCore.QCoreApplication.processEvents() 
        
#    def load_current(self, filePath):
#        print "load_current" 
#        self.l_pix = QtGui.QPixmap(filePath) 
#        self.c_view = self.l_pix.scaled(self.max_vsize, self.max_vsize, 
#                                            QtCore.Qt.KeepAspectRatio, 
#                                            QtCore.Qt.FastTransformation) 
#        #change the previous line with QtCore.Qt.SmoothTransformation eventually 
#        self.view_current()

    def wheel_event (self, event):
        numDegrees = event.delta() / 8 
        numSteps = numDegrees / 15.0 
        self.zoom(numSteps) 
        event.accept() 

    def zoom(self, step):
        self.scene.clear() 
        w = self.c_view.size().width() 
        h = self.c_view.size().height() 
        w, h = w * (1 + self.zoom_step*step), h * (1 + self.zoom_step*step) 
        self.c_view = self.l_pix.scaled(w, h, 
                                            QtCore.Qt.KeepAspectRatio, 
                                            QtCore.Qt.FastTransformation) 
        self.view_current() 




