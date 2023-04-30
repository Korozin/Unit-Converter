from PyQt5 import QtWidgets
from Classes import MainWindow, UnitValues, ErrorWindow


class UnitConverter_Main(QtWidgets.QMainWindow, MainWindow.UnitConverter_GUI):
    def __init__(self):
        super(UnitConverter_Main, self).__init__()

        # Set up base GUI parameters
        self.setupUi(self)
        self.Set_Functions()

        # Initialize ErrorWindow
        self.ErrorWindow = ErrorWindow.ErrorWindow()

    def Set_Functions(self):
        # Add items
        self.Mode_ComboBox.addItems(['Length', 'Mass', 'Temperature'])
        self.From_ComboBox.addItems(UnitValues.conversion_factors.keys())

        # Set TextBox state
        self.Output_TextEdit.setReadOnly(True)

        # Connect Functions
        self.Convert_Button.clicked.connect(self.Start_Conversion)
        self.Mode_ComboBox.currentIndexChanged.connect(self.update_comboboxes)
        self.update_comboboxes()

    def update_comboboxes(self):
        # Get current mode
        Current_Mode = self.Mode_ComboBox.currentText()

        # Clear "from" and "to" comboboxes
        self.From_ComboBox.clear()
        self.To_ComboBox.clear()

        # Update "from" and "to" comboboxes depending on the mode
        if Current_Mode == 'Length':
            self.From_ComboBox.addItems(['cm', 'inches', 'miles', 'feet', 'meters', 'kilometers'])
            self.To_ComboBox.addItems(['cm', 'inches', 'miles', 'feet', 'meters', 'kilometers'])
        elif Current_Mode == 'Mass':
            self.From_ComboBox.addItems(['grams', 'kilograms', 'pounds', 'ounces', 'metric_tonnes', 'short_tons', 'long_tons'])
            self.To_ComboBox.addItems(['grams', 'kilograms', 'pounds', 'ounces', 'metric_tonnes', 'short_tons', 'long_tons'])
        elif Current_Mode == 'Temperature':
            self.From_ComboBox.addItems(['Celsius', 'Fahrenheit', 'Kelvin'])
            self.To_ComboBox.addItems(['Celsius', 'Fahrenheit', 'Kelvin'])

    def Start_Conversion(self):
        # Get current mode and units
        Current_Mode = self.Mode_ComboBox.currentText()
        From_Unit = self.From_ComboBox.currentText()
        To_Unit = self.To_ComboBox.currentText()

        try:
            # Get input value
            Input_Value = float(self.Input_LineEdit.text())

            # Convert value
            if Current_Mode == 'Length' or Current_Mode == 'Mass':
                Output_Value = UnitValues.convert(From_Unit, To_Unit, Input_Value)
            elif Current_Mode == 'Temperature':
                Output_Value = round(UnitValues.convert(From_Unit, To_Unit, Input_Value), 2)

            # Update output
            Output_String = f"{Input_Value} {From_Unit} = {Output_Value} {To_Unit}"
            self.Output_TextEdit.clear()
            self.Output_TextEdit.insertPlainText(Output_String)
        except Exception as e:
            self.ErrorWindow.CreateWindow("Error!",
                                         f"{e}<br/><br/>Make sure Input Data is valid!",
                                         500, 200)
            self.ErrorWindow.show()


if __name__ == "__main__":
    import sys
    UnitConverter_App = QtWidgets.QApplication(sys.argv)
    UnitConverter_Var = UnitConverter_Main()
    UnitConverter_Var.show()
    sys.exit(UnitConverter_App.exec_())
