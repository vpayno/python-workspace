"""AsyncIO Module Demo"""

import asyncio
from typing import Any, Coroutine

from icecream import ic  # type: ignore[import-untyped]
from rich import traceback

traceback.install(show_locals=True)

type task_delay_t = int  # type: ignore[valid-type]
type task_id_t = int  # type: ignore[valid-type]

type fetch_result_one_t = dict[str, str]  # type: ignore[valid-type]
type fetch_result_two_t = dict[str, str | int]  # type: ignore[valid-type]
type fetch_result_three_t = dict[str, str | int]  # type: ignore[valid-type]
type fetch_results_three_t = list[fetch_result_three_t]  # type: ignore[valid-type]
type fetch_results_four_t = tuple[fetch_result_two_t, fetch_result_two_t, fetch_result_two_t]  # type: ignore[valid-type]

type task_one_t = Coroutine[Any, Any, fetch_result_one_t]  # type: ignore[valid-type]

type task_two_t = Coroutine[Any, Any, fetch_result_two_t]  # type: ignore[valid-type]
type tasks_two_t = list[task_two_t]  # type: ignore[valid-type]

type task_three_t = asyncio.Task[fetch_result_three_t]  # type: ignore[valid-type]
type tasks_three_t = list[asyncio.Task[fetch_result_three_t]]  # type: ignore[valid-type]

type task_five_t = asyncio.Task[fetch_result_two_t]  # type: ignore[valid-type]
type tasks_five_t = list[task_five_t]  # type: ignore[valid-type]
type results_five_t = list[fetch_result_two_t]  # type: ignore[valid-type]

type future_t = asyncio.Future[Any]  # type: ignore[valid-type]
type future_data_t = str  # type: ignore[valid-type]
type async_loop_t = asyncio.AbstractEventLoop  # type: ignore[valid-type]

type semaphore_t = asyncio.Semaphore  # type: ignore[valid-type]
type resource_id_t = int  # type: ignore[valid-type]

type event_t = asyncio.Event # type: ignore[valid-type]


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def fetch_data_one(delay: task_delay_t) -> fetch_result_one_t:
    """define a coroutine that simulates a time-consuming task

    :param delay: in seconds
    :return: dictionary of fetch results
    """

    print("Fetching data one..")
    await asyncio.sleep(delay)

    print("Data fetched.")
    return {"data": "many things"}


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def fetch_data_two(delay: task_delay_t, id: task_id_t) -> fetch_result_two_t:
    """define a coroutine that simulates a time-consuming task

    :param delay: in seconds
    :param id: task id
    :return: dictionary of fetch results
    """

    print(f"Fetching data two... id: {id}")
    await asyncio.sleep(delay)

    print(f"Data fetched for id: {id}")
    return {"data": "many things", "id": id}


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def demo_one() -> None:
    print("\nDemo One\n")

    # create a place holder for the coroutine object
    task_one: task_one_t = fetch_data_one(2)

    # run the coroutine objects
    print("Scheduling task_one...")
    ic(task_one)
    result_one: fetch_result_one_t = await task_one
    print(f"Received results_one: {result_one}")

    print()


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def demo_two() -> None:
    print("\nDemo Two\n")

    # create a place holder for the coroutine object
    tasks_two: tasks_two_t = [
        fetch_data_two(2, 2),
        fetch_data_two(1, 1),
        fetch_data_two(4, 4),
        fetch_data_two(3, 3),
    ]

    print(f"Scheduling tasks: {tasks_two}")
    task_two: task_two_t
    for task_two in tasks_two:
        print("Scheduling task_two...")
        ic(task_two)
        result_two: fetch_result_two_t = await task_two
        print(f"Received result_two: {result_two}")

    print()


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def demo_three() -> None:
    """Async Demo Using asyncio.Task"""

    print("\nDemo Three\n")

    # create a place holder for the coroutine object
    # real tasks
    tasks_three: tasks_three_t = [
        asyncio.create_task(fetch_data_two(1, 1)),
        asyncio.create_task(fetch_data_two(2, 2)),
        asyncio.create_task(fetch_data_two(3, 3)),
        asyncio.create_task(fetch_data_two(4, 4)),
    ]

    print(f"Scheduling tasks: {tasks_three}")
    task_three: task_three_t
    results_three: fetch_results_three_t = []
    for task_three in tasks_three:
        print("Scheduling task_three...")
        ic(task_three)
        results_three.append(await task_three)
    print()

    result_three: fetch_result_three_t
    for result_three in results_three:
        print(f"Received result_three: {result_three}")

    print()


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def demo_four() -> None:
    """Async Demo Using asyncio.gather"""

    print("\nDemo Four\n")

    print("Gathering tasks...")
    results: fetch_results_four_t = await asyncio.gather(
        fetch_data_two(2, 2), fetch_data_two(1, 1), fetch_data_two(3, 3)
    )

    result: fetch_result_two_t
    for result in results:
        print(f"Received result: {result}")

    print()


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def demo_five() -> None:
    """Async Demo Using asyncio.TaskGroup"""

    print("\nDemo Five\n")

    tasks: tasks_five_t = []
    task: task_five_t

    # automatic error handling (aborts all tasks on 1st error)
    async with asyncio.TaskGroup() as tg:
        i: task_id_t
        sleep_time: task_delay_t
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data_two(i, sleep_time))
            tasks.append(task)

    results: results_five_t = [task.result() for task in tasks]

    result: fetch_result_two_t
    for result in results:
        print(f"Received result: {result}")

    print()


async def set_future_result(future: future_t, value: future_data_t) -> None:
    """async function that returns a promised result

    :param future: promise
    :param value: promised data
    """

    await asyncio.sleep(2)

    future.set_result(value)
    print(f"Set the future's result to: {value}")


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
# a future is a promise of a future result
async def demo_six() -> None:
    """Async Demo Using futures"""

    print("\nDemo Six\n")

    # create future object
    loop: async_loop_t = asyncio.get_running_loop()
    future: future_t = loop.create_future()  # noqa: FURB184

    # schedule setting the future's result
    asyncio.create_task(set_future_result(future, "Future result is now!"))

    # wait for the future's result
    result: future_data_t = await future
    print(f"Received the future's result: {result}")

    print()


# shared variable
shared_resource: int = 0

# asyncio lock
lock: asyncio.Lock = asyncio.Lock()


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def modify_shared_resource() -> None:
    """Async Demo Using Locks"""
    global shared_resource

    # use global lock
    async with lock:
        # critical section start
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1
        await asyncio.sleep(1)
        print(f"Resource after modification: {shared_resource}")
        # critical section end


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def demo_seven() -> None:
    """Async Demo Seven Locks"""

    print("\nDemo Seven\n")

    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

    print()


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def access_resource(semaphore: semaphore_t, resource_id: resource_id_t) -> None:
    """Async Demo Using Semaphores

    :param semaphore: async semaphore
    :param resource_id: integer id
    """

    async with semaphore:
        print(f"Accessing limited resource {resource_id}")
        await asyncio.sleep(1)
        print(f"Releasing limited resource {resource_id}")


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def demo_eight() -> None:
    """Async Demo Eight Semaphores"""

    print("\nDemo Eight\n")

    concurrent_max_access: int = 2
    semaphore: semaphore_t = asyncio.Semaphore(concurrent_max_access)
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))

    print()


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def waiter(event: event_t) -> None:
    """Async event waiting"""

    print("waiting for the event to be set")
    await event.wait()
    print("event has been set , continuing execution")


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def setter(event: event_t) -> None:
    """Async event setting"""

    await asyncio.sleep(2)
    event.set()
    print("event has been set!")


# the function is of type Coroutine[Any, Any, None]
# the return type is None or whatever it returns via the `return` call.
async def demo_nine() -> None:
    """Async Demo Nine Wait/Set"""

    print("\nDemo Nine\n")

    event: event_t = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

    print()


def main() -> None:
    """Main Function"""

    print("Start of main coroutine...")

    # start event loops
    asyncio.run(demo_one())
    asyncio.run(demo_two())
    asyncio.run(demo_three())
    asyncio.run(demo_four())
    asyncio.run(demo_five())
    asyncio.run(demo_six())
    asyncio.run(demo_seven())
    asyncio.run(demo_eight())
    asyncio.run(demo_nine())

    print("End of main coroutine.")


if __name__ == "__main__":  # pragma: no cover
    main()
