from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def send(data, dest, tag):
	comm.send(data, dest = dest, tag = tag)
	print "Pranesimas is proceso %s issiustas i %s procesa kanalu %s" % (rank, dest, tag)

def receive(source, tag):
	data = comm.recv(source = source, tag = tag)
	print "Pranesimas: %s \n gautas is proceso %s kanalu %s" % (data, source, tag)


if rank == 0:
	data = {'a': 7, 'b': 3.14} #sukuriami fiktyvus duomenys
	data2 = {'c': 9, 'd': 69} #sukuriami fiktyvus duomenys nr. 2
	send(data, dest = 1, tag = 11) #dest - proceso numeris, kuriam siunciame pranesima #tag - "kanalo" numeris	
	send(data2, dest = 5, tag = 13) #siunciame pranesima i 5 procesa 13 kanalu

elif rank == 1:
	receive(source = 0, tag = 11) #paimame pranesima is 0 proceso, 11 kanalo

elif rank == 5:
	receive(source = 0, tag = 13) #paimame pranesima is 0 proceso, 13 kanalo