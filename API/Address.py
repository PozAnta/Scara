from configparser import ConfigParser


class Address:
    def __init__(self):
        self.dict_obj = {}
        self.load_objects()

    def load_objects(self):
        config = ConfigParser()
        config.read('C:\\Python\\Robot\\Scara\\API\\SeleniumAddrs.ini')

        sections = config.sections()
        for section in sections:
            try:
                self.dict_obj[section] = config.get(section, 'AddressObject')
            except:
                print("exception on %s!" % section)
                self.dict_obj[section] = None

        # print(self.dict_obj)

    def obj_address(self, name_object):
        # print("Name: ", name_object)
        # print(self.dict_obj)
        return self.dict_obj.get(name_object)


class HomeSection(Address):

    def power_button_addr(self):
        return self.obj_address('PowerBtn')

    def write_terminal_addr(self):
        return self.obj_address('WriteTerminal')

    def read_terminal_addr(self):
        return self.obj_address('ReadTerminal')


class ProjectEditorSection(Address):

    def open_panel_terminal_addr(self):
        return self.obj_address('OpenPanelTerminal')

    def write_panel_terminal_addr(self):
        return self.obj_address('WritePanelTerminal')

    def press_close_terminal_addr(self):
        return self.obj_address('ClosePanelTerminal')

    def apps_folder_addr(self):
        return self.obj_address('AppsFolder')

    def adpt_folder_addr(self):
        return self.obj_address('AdeptFolder')

    def prog_adpt_folder_addr(self):
        return self.obj_address('ProgAdptFolder')

    def save_and_load_addr(self):
        return self.obj_address('SaveAndLoad')

    def run_programm_addr(self):
        return self.obj_address('RunProg')

    def kill_unload_addr(self):
        return self.obj_address('KillUnload')

    def project_editor_addr(self):
        return self.obj_address('ProjectEditor')

    def io_mapping_addr(self):
        return self.obj_address('IoMapping')

    def maxx_io_addr(self):
        return self.obj_address('MaxxIo')

    def maxx_inputs_addr(self):
        return self.obj_address('MaxxInputs')

    def maxx_outputs_addr(self):
        return self.obj_address('MaxxOutputs')


class Login(Address):
    def open_cs_addr(self):
        return self.obj_address('Login')


class SystemConfigurationSection(Address):
    def open_sys_configuration_addr(self):
        return self.obj_address('SystemConfiguration')

    def open_system_addr(self):
        return self.obj_address('System')

    def a1_offset_addr(self):
        return self.obj_address('MasterOffsetA1')

    def a2_offset_addr(self):
        return self.obj_address('MasterOffsetA2')

    def a3_offset_addr(self):
        return self.obj_address('MasterOffsetA3')

    def a4_offset_addr(self):
        return self.obj_address('MasterOffsetA4')
