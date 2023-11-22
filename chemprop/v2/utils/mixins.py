import inspect
from typing import Any


class ReprMixin:
    def __repr__(self) -> str:
        items = self.get_params().items()

        if len(items) > 0:
            keys, values = zip(*items)
            sig = inspect.signature(self.__class__)
            defaults = [sig.parameters[k].default for k in keys]
            items = [(k, v) for k, v, d in zip(keys, values, defaults) if v != d]

        argspec = ", ".join(f"{k}={repr(v)}" for k, v in items)

        return f"{self.__class__.__name__}({argspec})"

    def get_params(self, deep: bool = True) -> dict[str, Any]:
        return dict(self.__dict__.items())