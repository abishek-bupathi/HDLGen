from PySide2.QtWidgets import *
import sys
sys.path.append("..")
from ProjectManager.project_manager import ProjectManager
from Generator.generator import Generator
from Help.help import Help
from HDLDesigner.hdl_designer import HDLDesigner


class Home(QMainWindow):

    def __init__(self, proj_dir=None):

        super().__init__()

        self.setWindowTitle("HDLGen")

        self.generate_btn = QPushButton("Generate")

        # Initializing UI Elements
        self.mainLayout = QVBoxLayout()

        self.tabs = QTabWidget()

        # Creating a container
        self.container = QWidget()

        self.proj_dir = proj_dir
        self.generator = Generator()

        self.setup_ui()


    def setup_ui(self):

        load_data = False

        if self.proj_dir is not None:
            load_data = True
        project_manager = ProjectManager(self.proj_dir, self)
        hdl_designer = HDLDesigner(self.proj_dir, load_data)

        print("Setting up UI")
        self.tabs.addTab(project_manager, "Project Manager")
        self.tabs.addTab(hdl_designer, "HDL Designer")
        self.tabs.addTab(Help(), "Help")
        self.generate_btn.clicked.connect(self.generate_btn_clicked)
        self.tabs.setCornerWidget(self.generate_btn)

        self.tabs.currentChanged.connect(hdl_designer.compDetails.update_comp_name)

        self.mainLayout.addWidget(self.tabs)
        self.setLayout(self.mainLayout)

        self.container.setLayout(self.mainLayout)

        self.setCentralWidget(self.container)


    def generate_btn_clicked(self):

        self.generator.generate_folders()
        self.generator.create_vhdl_file()
