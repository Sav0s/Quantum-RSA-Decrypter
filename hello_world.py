import qsharp

from HelloWorld import SayHello
from qiskit import IBMQ

IBMQ.delete_account()

SayHello.simulate()
