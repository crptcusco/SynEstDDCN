class DDCNModel(object):
    def __init__(self, number_of_rddas, number_of_variables_rdda, number_of_signals_rdda, number_exit_variables,
                 number_clauses_function):
        self.number_of_rddas = number_of_rddas  # number of rdds
        self.number_of_variables_rdda = number_of_variables_rdda  # number of variables for each rdd
        self.number_of_signals_rdda = number_of_signals_rdda  # number of signals who have each rdd
        self.number_exit_variables = number_exit_variables  # number of exit variables in the set of exit
        self.number_clauses_function = number_clauses_function  # number of clauses for each transition function
        self.list_of_rddas = []  # List of th object of each RDD
        self.l_rdda_permutation_attractors = []  # List who join RDD - Permutation - Attractors
        self.rddas_attractors = []  # List of attractors in form of key, Without RDD
        self.list_attractors_pairs = []  # List of attractors pairs in only one list without RDD
        self.group_signals_pairs = []  # List of attractors pairs group by relations between RDDs
        self.list_signal_pairs = []  # List of signal pairs group by relations,but without labels
        self.d_global_rdda_attractor = {}  # Dictionary for each attractor with his RDD
        self.attractor_fields = []  # The List of attractor fields in format of pair attractors
        # self.generateRDDAs()

        # Dictionary of RDD as key and Color as value
        self.d_rdd_color = {}
        # List of color for the graphics
        self.rdd_color_dict = {}
        list_colors = list(mcolors.CSS4_COLORS.keys())
        random.shuffle(list_colors)
        for i, color in enumerate(list_colors):
            self.rdd_color_dict[i] = color