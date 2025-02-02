from evox import pipelines, algorithms, problems
from evox.monitors import StdMOMonitor
from evox.metrics import IGD
import jax
import jax.numpy as jnp


N = 12
M = 3
POP_SIZE = 100
LB = 0
UB = 1
ITER = 10


def run_moea(algorithm, problem=problems.classic.DTLZ1(m=M)):
    key = jax.random.PRNGKey(42)
    monitor = StdMOMonitor(record_pf=False)
    # problem = problems.classic.DTLZ2(m=M)
    pipeline = pipelines.StdPipeline(
        algorithm=algorithm,
        problem=problem,
        fitness_transform=monitor.record_fit,
    )
    state = pipeline.init(key)
    true_pf, state = problem.pf(state)

    for i in range(ITER):
        state = pipeline.step(state)

    objs = monitor.get_last()


def test_ibea():
    algorithm = algorithms.IBEA(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
    )
    run_moea(algorithm)


def test_moead():
    algorithm = algorithms.MOEAD(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
        type=1,
    )
    run_moea(algorithm)


def test_nsga2():
    algorithm = algorithms.NSGA2(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
    )
    run_moea(algorithm)


def test_rvea():
    algorithm = algorithms.RVEA(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
    )
    run_moea(algorithm)


def test_nsga3():
    algorithm = algorithms.NSGA3(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
    )
    run_moea(algorithm)


def test_eagmoead():
    algorithm = algorithms.EAGMOEAD(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
    )
    run_moea(algorithm)


def test_hype():
    algorithm = algorithms.HypE(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
    )
    run_moea(algorithm)


def test_moeaddra():
    algorithm = algorithms.MOEADDRA(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
    )
    run_moea(algorithm)


def test_spea2():
    algorithm = algorithms.SPEA2(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
    )
    run_moea(algorithm)


def test_moeadm2m():
    algorithm = algorithms.MOEADM2M(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
    )
    run_moea(algorithm)


def test_knea():
    algorithm = algorithms.KnEA(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
    )
    run_moea(algorithm)


def test_bige():
    algorithm = algorithms.BiGE(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
    )
    run_moea(algorithm)


def test_gde3():
    algorithm = algorithms.GDE3(
        lb=jnp.full(shape=(N,), fill_value=LB),
        ub=jnp.full(shape=(N,), fill_value=UB),
        n_objs=M,
        pop_size=POP_SIZE,
    )
    run_moea(algorithm)
