from qiskit import QuantumCircuit, BasicAer, execute

# 创建电路
qc = QuantumCircuit(1,1)
qc.h(0)
qc.measure_all()

backend = BasicAer.get_backend('qasm_simulator')
job = execute(qc, backend)
result = job.result()

print(qc.draw())
print(result.get_counts(qc))