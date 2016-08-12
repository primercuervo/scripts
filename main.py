from module.test import skycake
from optparse import OptionGroup

class ImportTest():
    """testing optparse as a plugin"""
    def __init__(self):
        ModTool.__init__(self)

    def setup_parser(self):
        """This mofo has to change with the plugin"""
        parser = OptionParser(self)
        parser.usage = '%prog nm [options]. \n Call %prog without any options to run it interactively.'
        ogroup.add_option("--awesome", type="string",
               help="this is fucking awesome.")
        parser.add_option_group(ogroup)
        return parser

    def setup_skycake(self):
        return skycake()

    def run(self):
        """override this. """
        pass

