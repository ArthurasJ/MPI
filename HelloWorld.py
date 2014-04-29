from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
print ("Hello world! Best regards from " + str(rank) + "th process of " + str(size) + ".")