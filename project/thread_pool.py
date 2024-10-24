from typing import Any, Callable, List
from threading import Thread, Condition

class Task:
    """
    Class to store result and status of function

    Atributes:
    _isDone (bool): a flag to indicate status of task
    _func (Callable): wrapped function
    _result (Any): result of function execution
    """
    def __init__(self, func: Callable) -> None:
        """
        Inizializing Task object
        """ 
        self._isDone: bool = False
        self._func: Callable = func
    
    def __call__(self, *args: Any, **kwargs: Any) -> None:
        """
        Calling a function, saving result of execution and marking that task was complited 
        """
        self._result: Any = self._func(*args, **kwargs)
        self._isDone = True
    
    def get_result(self) -> Any:
        """
        Returning result of function execution
        """
        while not self._isDone:
            pass
        return self._result

class ThreadPool:
    """
    Class for task completion via multiple threads

    Atributes:
    thread_num(int): number of threads
    isRunning(bool): a flag to indicate status of thread pool
    threads(list[threading.Thread]): a list of threads in pool
    tasks(list[Task]): a list of tasks
    condition(threading.Condition): a condition for tasks
    """
    def __init__(self, num: int = 1) -> None:
        """
        Inizializing Task object
        """
        if num < 1:
            raise ValueError("Number of threads can't be less then 1")
        self.thread_num = num
        self._isRunning = True
        self._threads: List[Thread] = []
        self._tasks: List[Task] = []
        self._condition = Condition()

    def _create_threads(self, num: int) -> None:
        """
        Creates and starts some number of threads
        """
        for _ in range(num):
            thread = Thread(target=self._thread_runner)
            thread.start()
            self._threads.append(thread)

    def _thread_runner(self) -> None:
        """
        Waits for task and execute it
        """
        while True:
            with self._condition:
                if not self._isRunning:
                    break
                elif len(self._tasks) == 0:
                    self._condition.wait()
                task = self._tasks.pop(0)
            task()

    def enqueue(self, func: Callable, *args: Any) -> Task:
        """
        Wrapping task and append in task queue
        """
        with self._condition:
            task = Task(func)
            task(*args)
            self._tasks.append(task)
            self._condition.notify()
            return task

    def dispose(self) -> None:
        """
        Stopping all threads and disposing thread pool
        """
        with self._condition:
            self._isRunning = False
            self._condition.notify_all()
        for thread in self._threads:
            thread.join()
