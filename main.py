from rich.console import Console
import series_meter_bridge as Series
import parallel_meter_bridge as Parallel
import resistance_of_wire as ResistanceOfWire

class Main():
	def __init__(self):
		self.experiments = {}
		self.console = Console()
		self.number_of_experiment = 0
		self.importAllExperimentsWithPath()

	def importAllExperimentsWithPath(self):
		self.experiments[1] = ("To determine resistivity of two / three wires " +
		 " by plotting a graph for potential difference versus current.",'./resistivity_vi.py')
		self.experiments[2] = (("To find resistance of a given wire / standard resistor using metre bridge.",
			'./resistance_of_wire.py'))
		self.experiments[3] =("To verify the laws of combination (series) of resistances using a metre bridge.",
			'./series_meter_bridge.py')
		self.experiments[4] = ("To verify the laws of combination (parallel) of resistances using a metre bridge.",
			'./paralle_meter_bridge.py')


	def showOptions(self):
		self.console.print("Choose Experiment : ", style="red")
		for exp in self.experiments:
			self.console.print(str(exp) + " : ",end= '')
			self.console.print(self.experiments.get(exp)[0])
	def takeInput(self):
		input_experiment_number = int(input("Enter the experiment number : "))
		self.number_of_experiment = input_experiment_number
		print(input_experiment_number)
		

	def showTabulation(self,experiment_number):
		if experiment_number == 3:
			Series.Series().run()
		elif experiment_number == 4:
			Parallel.Parallel().run()
		elif experiment_number == 2:
			ResistanceOfWire.ResistanceOfWire().run()

	def test(self):
		for i in range(2):
			s = Series.Series()
			s.run()

main = Main()
main.showOptions()
main.takeInput()
main.showTabulation(main.number_of_experiment)
