import contextlib
import inspect
import os
import importlib
import typing

# TODO make support dicts

def get_docs():
    """Custom typehint/docstring extractor"""
    directory_path = "\\".join(__file__.split("\\")[:-1])+"\\objects"
    documentation = []
    relative = directory_path.replace(os.getcwd(), "").replace("\\", ".")[1:]
    for filename in os.listdir(directory_path):
        if filename.endswith(".py") and filename != "__init__.py" and not filename.startswith("_"):
            module_name = filename[:-3]
            module_path = f"{relative}.{module_name}"
            module = importlib.import_module(module_path)

            class_name = module_name.capitalize()  # Class name is the capitalized filename

            object_class = getattr(module, class_name)
            object_data = {"name": object_class.__name__, "docstring": object_class.__doc__,
                           "attributes": []}

            for x in [a for a in object_class.__dict__ if not a.startswith('_')]:
                attr_obj = getattr(object_class, x)
                attr_data = {"name": x, "doc": attr_obj.__doc__, "type": ""}

                if isinstance(attr_obj, property):

                    attr_data["type"] = typing.get_type_hints(attr_obj.fget).get("return", None)
                    if attr_data["type"] is not None:
                        try:
                            attr_data["type"] = attr_data["type"].__name__
                        except Exception:
                            pass
                else:
                    params = inspect.signature(attr_obj).parameters
                    if len(params) > 1:
                        args = []
                        for x in params:
                            if x == "self":
                                continue
                            print(x,"-", inspect.signature(attr_obj).parameters[x].annotation, inspect.signature(attr_obj).parameters[x].default)
                            param_data = {"name": inspect.signature(attr_obj).parameters[x].name,
                                         "type": inspect.signature(attr_obj).parameters[x].annotation,
                                         "required": True
                                         }
                            if str(inspect.signature(attr_obj).parameters[x].default) != "<class 'inspect._empty'>":
                                param_data["required"] = False
                        attr_data["args"] = args
                    with contextlib.suppress(Exception):
                        attr_data["type"] = typing.get_type_hints(attr_obj)["return"]





                object_data["attributes"].append(attr_data)
            documentation.append(object_data)
    return documentation

if __name__ == "__main__":
    print(get_docs())