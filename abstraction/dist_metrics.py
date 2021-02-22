import torch

class ACT_EMD:
	"""
	EMD stands for Earth Mover's Distance - Mallows distance or
	1st Wasserstein distance between the two distributions, is a 
	measure of the distance between two probability distributions.
	ACT or Approximate Constrained Transfers is a linear compelixty 
	approximation of the ICT or Iterative Constrained Transfers, which
	is a symmetric lower bound approximation of the Eath Mover's Distance
	Note that as the number of iterations of ACT approaches infinity, ACT
	becomes the same as ICT. For more, read - https://arxiv.org/pdf/1812.02091.pdf
	"""
	def __init__(self, histograms, use_gpu=True, cost_matrix=None):
        self.use_gpu = use_gpu

        # these are the histograms to which the distance must be calculated
        self.histograms = histograms

        # this is the cost matrix showing the cost of 
        # transporting one unit  of 'dirt' from coordinate i to j
        self.cost_matrix = cost_matrix

    def act(self):
    	# rename?
    	pass

