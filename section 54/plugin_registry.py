"""Explicit class-decorator registry with lightweight signature checks."""
import inspect

class Registry:
    def __init__(self):
        self.plugins = {}
    def register(self, name):
        def decorate(cls):
            if name in self.plugins:
                raise ValueError(f"duplicate plugin: {name}")
            inspect.signature(cls.run).bind(None, "sample")
            self.plugins[name] = cls
            return cls
        return decorate
    def run(self, name, text):
        return self.plugins[name]().run(text)

registry = Registry()

@registry.register("upper")
class Upper:
    def run(self, text):
        return text.upper()

@registry.register("strip")
class Strip:
    def run(self, text):
        return text.strip()

if __name__ == "__main__":
    for name, cls in sorted(registry.plugins.items()):
        print(name, inspect.signature(cls.run))
    print(registry.run("upper", "Signals"))
