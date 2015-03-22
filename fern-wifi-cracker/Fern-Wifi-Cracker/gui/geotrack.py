import os
from main_window import font_size
from PyQt4 import QtCore, QtGui

font_setting = font_size()


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_fern_geotrack(object):
    def setupUi(self, fern_geotrack):
        fern_geotrack.setObjectName(_fromUtf8("fern_geotrack"))
        fern_geotrack.resize(823, 630)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/map.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fern_geotrack.setWindowIcon(icon)
        self.verticalLayout_5 = QtGui.QVBoxLayout(fern_geotrack)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem = QtGui.QSpacerItem(207, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(15, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.target_combo = QtGui.QComboBox(fern_geotrack)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.target_combo.sizePolicy().hasHeightForWidth())
        self.target_combo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.target_combo.setFont(font)
        self.target_combo.setEditable(False)
        self.target_combo.setObjectName(_fromUtf8("target_combo"))
        self.horizontalLayout_2.addWidget(self.target_combo)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(248, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.database_radio = QtGui.QRadioButton(fern_geotrack)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.database_radio.setFont(font)
        self.database_radio.setChecked(True)
        self.database_radio.setObjectName(_fromUtf8("database_radio"))
        self.horizontalLayout_4.addWidget(self.database_radio)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.insert_mac_radio = QtGui.QRadioButton(fern_geotrack)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.insert_mac_radio.setFont(font)
        self.insert_mac_radio.setChecked(False)
        self.insert_mac_radio.setObjectName(_fromUtf8("insert_mac_radio"))
        self.horizontalLayout_4.addWidget(self.insert_mac_radio)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem6 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem6)
        self.map_viewer = QtWebKit.QWebView(fern_geotrack)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.map_viewer.setFont(font)
        self.map_viewer.setUrl(QtCore.QUrl(_fromUtf8("")))
        self.map_viewer.setObjectName(_fromUtf8("map_viewer"))
        self.verticalLayout_5.addWidget(self.map_viewer)
        self.groupBox = QtGui.QGroupBox(fern_geotrack)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mac_address_label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.mac_address_label.setFont(font)
        self.mac_address_label.setObjectName(_fromUtf8("mac_address_label"))
        self.verticalLayout.addWidget(self.mac_address_label)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.country_label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.country_label.setFont(font)
        self.country_label.setObjectName(_fromUtf8("country_label"))
        self.verticalLayout.addWidget(self.country_label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem9 = QtGui.QSpacerItem(29, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.latitude_label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.latitude_label.setFont(font)
        self.latitude_label.setObjectName(_fromUtf8("latitude_label"))
        self.verticalLayout_4.addWidget(self.latitude_label)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.city_label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.city_label.setFont(font)
        self.city_label.setObjectName(_fromUtf8("city_label"))
        self.verticalLayout_4.addWidget(self.city_label)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem11 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.longitude_label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.longitude_label.setFont(font)
        self.longitude_label.setObjectName(_fromUtf8("longitude_label"))
        self.verticalLayout_3.addWidget(self.longitude_label)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)
        self.street_label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.street_label.setFont(font)
        self.street_label.setObjectName(_fromUtf8("street_label"))
        self.verticalLayout_3.addWidget(self.street_label)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem13 = QtGui.QSpacerItem(29, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem13)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.accuracy_label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.accuracy_label.setFont(font)
        self.accuracy_label.setObjectName(_fromUtf8("accuracy_label"))
        self.verticalLayout_2.addWidget(self.accuracy_label)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        self.country_code_label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.country_code_label.setFont(font)
        self.country_code_label.setObjectName(_fromUtf8("country_code_label"))
        self.verticalLayout_2.addWidget(self.country_code_label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label = QtGui.QLabel(fern_geotrack)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem16 = QtGui.QSpacerItem(220, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.track_button = QtGui.QPushButton(fern_geotrack)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.track_button.sizePolicy().hasHeightForWidth())
        self.track_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.track_button.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("world.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.track_button.setIcon(icon1)
        self.track_button.setIconSize(QtCore.QSize(24, 29))
        self.track_button.setObjectName(_fromUtf8("track_button"))
        self.horizontalLayout_3.addWidget(self.track_button)
        spacerItem17 = QtGui.QSpacerItem(19, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem17)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem18 = QtGui.QSpacerItem(277, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem18)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.retranslateUi(fern_geotrack)
        QtCore.QMetaObject.connectSlotsByName(fern_geotrack)

    def retranslateUi(self, fern_geotrack):
        fern_geotrack.setWindowTitle(QtGui.QApplication.translate("fern_geotrack", "Fern - Mac Geolocatory Tracker", None, QtGui.QApplication.UnicodeUTF8))
        self.database_radio.setText(QtGui.QApplication.translate("fern_geotrack", "Use Database addresses", None, QtGui.QApplication.UnicodeUTF8))
        self.insert_mac_radio.setText(QtGui.QApplication.translate("fern_geotrack", "Insert Mac Address", None, QtGui.QApplication.UnicodeUTF8))
        self.mac_address_label.setText(QtGui.QApplication.translate("fern_geotrack", "Mac Address: ", None, QtGui.QApplication.UnicodeUTF8))
        self.country_label.setText(QtGui.QApplication.translate("fern_geotrack", "Country: ", None, QtGui.QApplication.UnicodeUTF8))
        self.latitude_label.setText(QtGui.QApplication.translate("fern_geotrack", "Latitude: ", None, QtGui.QApplication.UnicodeUTF8))
        self.city_label.setText(QtGui.QApplication.translate("fern_geotrack", "City: Lagos", None, QtGui.QApplication.UnicodeUTF8))
        self.longitude_label.setText(QtGui.QApplication.translate("fern_geotrack", "Longitude: ", None, QtGui.QApplication.UnicodeUTF8))
        self.street_label.setText(QtGui.QApplication.translate("fern_geotrack", "Street: ", None, QtGui.QApplication.UnicodeUTF8))
        self.accuracy_label.setText(QtGui.QApplication.translate("fern_geotrack", "Accuracy: ", None, QtGui.QApplication.UnicodeUTF8))
        self.country_code_label.setText(QtGui.QApplication.translate("fern_geotrack", "Country Code: ", None, QtGui.QApplication.UnicodeUTF8))
        self.track_button.setText(QtGui.QApplication.translate("fern_geotrack", "Track", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit