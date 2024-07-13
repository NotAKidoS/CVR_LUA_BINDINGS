import os
import re
import sys

# very shit gpt'd script cause fuck you
# requires decompiling game in dnspy to project, then pass folder of scripting common
# python generate_docs.py "dnspy-export-scripting-wrappers\Assembly-CSharp\ABI\Scripting\CVRSTL\Common"

# shit that moonsharp auto converts or whatever https://www.moonsharp.org/mapping.html
simple_data_types = [
    'bool', 'int', 'float', 'string', 'double', 'long', 'short', 'byte', 'char', 'void', 'decimal', 'Table',
    'sbyte', 'byte', 'short', 'ushort', 'uint', 'ulong', 'System.StringBuilder', 'System.Text.StringBuilder',
    'MoonSharp.Interpreter.DynValue', 'System.SByte', 'System.Byte', 'System.Int16', 'System.UInt16',
    'System.Int32', 'System.UInt32', 'System.Int64', 'System.UInt64', 'System.Single', 'System.Decimal',
    'System.Double', 'System.Boolean', 'System.String', 'System.Text.StringBuilder', 'System.Char',
    'MoonSharp.Interpreter.Table', 'MoonSharp.Interpreter.CallbackFunction', 'System.Delegate',
    'System.Object', 'System.Type', 'MoonSharp.Interpreter.Closure', 'System.Reflection.MethodInfo',
    'System.Collections.IList', 'System.Collections.IDictionary', 'System.Collections.IEnumerable',
    'System.Collections.IEnumerator'
]

def log(message):
    print(message)
    with open("debug_log.txt", "a") as log_file:
        log_file.write(message + "\n")

def sanitize_name(name):
    return re.sub(r'_LUAINSTANCE_|_LUASTATIC_|_LUASTRUCT_|Scripted', '', name)

def is_invalid_type(type_name, known_wrappers, known_enums):
    type_name_cleaned = sanitize_name(type_name)
    
    # Check if type is in simple data types
    if type_name_cleaned in simple_data_types:
        return False
    
    # Check if type is an array
    if type_name_cleaned.endswith('[]'):
        array_type = type_name_cleaned[:-2]
        return is_invalid_type(array_type, known_wrappers, known_enums)
    
    # Check if type is a collection
    collection_match = re.match(r'(\w+)<(.+)>', type_name_cleaned)
    if collection_match:
        inner_type = collection_match.group(2)
        return is_invalid_type(inner_type, known_wrappers, known_enums)
    
    # Check if type is a known wrapper or enum
    if type_name_cleaned not in known_wrappers and type_name_cleaned not in known_enums:
        return True
    
    return False

def format_access(configs):
    return [config.split('.')[-1] for config in configs]

def parse_module_class(file_path):
    log(f"Parsing module class file: {file_path}")
    
    with open(file_path, 'r') as file:
        content = file.read()

    found_constructors = re.findall(r'public\s+_\w+_\w+\s+(\w+)\s*\(', content)
    enums = re.findall(r'public\s+DynValue\s+\w+\s*\{\s*get\s*\{\s*return\s+UserData\.CreateStatic\(typeof\(([^)]+)\)\)\.AsReadOnly\(\);', content)
    static_wrappers = re.findall(r'UserData\.RegisterType<([^>]+)>\(.*"([^"]+)"\);', content)
    instance_wrappers = re.findall(r'UserData\.RegisterProxyType<([^,]+),\s*([^)]+)>\(.*"([^"]+)"\);', content)
    struct_wrappers = re.findall(r'CVRUserData\.RegisterValueProxyType<([^,]+),\s*([^)]+)>\(.*"([^"]+)"\);', content)
    
    log(f"Found constructors: {found_constructors}")
    parsed_enums = [enum.split('.')[-1] for enum in enums]
    log(f"Found enums: {parsed_enums}")
    parsed_static_wrappers = {(sw[0].split('.')[-1], sw[1], 'static') for sw in static_wrappers}
    log(f"Found static wrappers: {parsed_static_wrappers}")
    parsed_instance_wrappers = {(iw[0].split('.')[-1], iw[1].split('.')[-1], 'instance') for iw in instance_wrappers}
    log(f"Found instance wrappers: {parsed_instance_wrappers}")
    parsed_struct_wrappers = {(sw[0].split('.')[-1], sw[1].split('.')[-1], 'struct') for sw in struct_wrappers}
    log(f"Found struct wrappers: {parsed_struct_wrappers}")

    # Collect known wrappers and enums for validation
    found_wrappers = {sanitize_name(w[0]) for w in parsed_static_wrappers}.union({sanitize_name(w[0]) for w in parsed_instance_wrappers}).union({sanitize_name(w[0]) for w in parsed_struct_wrappers})
    found_enums = set(parsed_enums)

    return found_constructors, found_wrappers, found_enums

def parse_wrapper(file_path):
    log(f"Parsing wrapper file: {file_path}")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    instance_properties = re.findall(r'public\s+([\w<>\[\]]+)\s+(\w+)\s*\{\s*get\s*\{[^}]*CheckIfCanAccessProperty\([^,]+,\s*[^,]+,\s*[^,]+,\s*CVRLuaEnvironmentContext\.(\w+),\s*CVRLuaObjectContext\.(\w+),\s*CVRLuaOwnerContext\.(\w+),\s*CVRLuaScopeContext\.(\w+)\);', content)
    static_properties = re.findall(r'public\s+static\s+([\w<>\[\]]+)\s+(\w+)\s*\{\s*get\s*\{[^}]*CheckIfCanAccessProperty\([^,]+,\s*[^,]+,\s*[^,]+,\s*CVRLuaEnvironmentContext\.(\w+),\s*CVRLuaObjectContext\.(\w+),\s*CVRLuaOwnerContext\.(\w+),\s*CVRLuaScopeContext\.(\w+)\);', content)
    instance_functions = re.findall(r'public\s+([\w<>\[\]]+)\s+(\w+)\s*\([^)]*\)\s*\{[^}]*CheckIfCanAccessMethod\([^,]+,\s*[^,]+,\s*CVRLuaEnvironmentContext\.(\w+),\s*CVRLuaObjectContext\.(\w+),\s*CVRLuaOwnerContext\.(\w+),\s*CVRLuaScopeContext\.(\w+)\);', content)
    static_functions = re.findall(r'public\s+static\s+([\w<>\[\]]+)\s+(\w+)\s*\([^)]*\)\s*\{[^}]*CheckIfCanAccessMethod\([^,]+,\s*[^,]+,\s*CVRLuaEnvironmentContext\.(\w+),\s*CVRLuaObjectContext\.(\w+),\s*CVRLuaOwnerContext\.(\w+),\s*CVRLuaScopeContext\.(\w+)\);', content)
    
    log(f"Found instance properties: {instance_properties}")
    log(f"Found instance functions: {instance_functions}")
    log(f"Found static properties: {static_properties}")
    log(f"Found static functions: {static_functions}")

    instance_properties = [(prop[0], prop[1], prop[2:]) for prop in instance_properties]
    static_properties = [(prop[0], prop[1], prop[2:]) for prop in static_properties]
    instance_functions = [(func[0], func[1], func[2:]) for func in instance_functions]
    static_functions = [(func[0], func[1], func[2:]) for func in static_functions]

    return instance_properties, instance_functions, static_properties, static_functions

def collect_wrapper_files(wrapper_folders):
    wrapper_files = []
    for wrapper_folder in wrapper_folders:
        for root, _, files in os.walk(wrapper_folder):
            for file in files:
                if file.endswith(".cs"):
                    wrapper_files.append(os.path.join(root, file))
    return wrapper_files

def generate_docs(common_folder):
    log("Starting documentation generation")

    modules_folder = os.path.join(common_folder, "Modules")
    wrapper_folders = [os.path.join(common_folder, folder) for folder in os.listdir(common_folder) if folder != "Modules" and os.path.isdir(os.path.join(common_folder, folder))]

    wrapper_files = collect_wrapper_files(wrapper_folders)

    module_constructors = {}
    module_wrappers = {}
    module_enums = {}

    known_wrappers = set()
    known_enums = set()

    # First pass: Collect known wrappers and enums
    for module_file in os.listdir(modules_folder):
        module_file_path = os.path.join(modules_folder, module_file)
        if os.path.isfile(module_file_path):
            module_name = os.path.splitext(module_file)[0]
            found_constructors, found_wrappers, found_enums = parse_module_class(module_file_path)

            # Associate with module dicts
            module_constructors[module_name] = found_constructors
            module_wrappers[module_name] = found_wrappers
            module_enums[module_name] = found_enums

            # Complete sets of everything bound so we can verify invalid bindings
            known_wrappers.update(found_wrappers)
            known_enums.update(found_enums)

    docs = ""
    toc = "## Table of Contents\n\n"

    # Generate documentation using parsed data
    for module_name, wrappers in module_wrappers.items():
        toc += f"- [{module_name}](#{module_name.lower()})\n"
        docs += f"# {module_name}\n\n"

        # Constructors
        docs += "## Constructors:\n"
        for constructor in module_constructors[module_name]:
            docs += f"- {constructor}()\n"

        # Enums
        docs += "\n## Enums:\n"
        for enum in module_enums[module_name]:
            docs += f"- {enum}\n"

        # Wrappers
        docs += "\n## Wrappers:\n"
        for wrapper in wrappers:
            toc += f"  - [{sanitize_name(wrapper)}](#{sanitize_name(wrapper).lower()})\n"
            docs += f"### {sanitize_name(wrapper)}\n"

            instance_file = None
            static_file = None
            struct_file = None

            for wrapper_file in wrapper_files:
                if f"_LUAINSTANCE_Scripted{wrapper}.cs" in wrapper_file:
                    instance_file = wrapper_file
                if f"_LUASTATIC_Scripted{wrapper}.cs" in wrapper_file:
                    static_file = wrapper_file
                if f"_LUASTRUCT_Scripted{wrapper}.cs" in wrapper_file:
                    struct_file = wrapper_file
                if f"_LUAINSTANCE_{wrapper}.cs" in wrapper_file:
                    instance_file = wrapper_file
                if f"_LUASTATIC_{wrapper}.cs" in wrapper_file:
                    static_file = wrapper_file
                if f"_LUASTRUCT_{wrapper}.cs" in wrapper_file:
                    struct_file = wrapper_file

            log(f"Instance file {'found' if instance_file else 'not found'}: {wrapper}")
            log(f"Static file {'found' if static_file else 'not found'}: {wrapper}")
            log(f"Struct file {'found' if struct_file else 'not found'}: {wrapper}")

            if static_file:
                _, _, static_props, static_funcs = parse_wrapper(static_file)
                if static_props:
                    docs += "#### Static Properties\n"
                    docs += "| Name | Return Type | Environment | Object | Owner | Scope |\n"
                    docs += "|------|-------------|-------------|--------|-------|-------|\n"
                    for prop in static_props:
                        type_name = prop[0]
                        if is_invalid_type(type_name, known_wrappers, known_enums):
                            type_name += " (invalid)"
                        env, obj, owner, scope = format_access(prop[2])
                        docs += f"| `{prop[1]}` | `{sanitize_name(type_name)}` | `{env}` | `{obj}` | `{owner}` | `{scope}` |\n"
                if static_funcs:
                    docs += "#### Static Functions\n"
                    docs += "| Name | Return Type | Environment | Object | Owner | Scope |\n"
                    docs += "|------|-------------|-------------|--------|-------|-------|\n"
                    for func in static_funcs:
                        type_name = func[0]
                        if is_invalid_type(type_name, known_wrappers, known_enums):
                            type_name += " (invalid)"
                        env, obj, owner, scope = format_access(func[2])
                        docs += f"| `{func[1]}` | `{sanitize_name(type_name)}` | `{env}` | `{obj}` | `{owner}` | `{scope}` |\n"

            if instance_file:
                instance_props, instance_funcs, _, _ = parse_wrapper(instance_file)
                if instance_props:
                    docs += "#### Instance Properties\n"
                    docs += "| Name | Return Type | Environment | Object | Owner | Scope |\n"
                    docs += "|------|-------------|-------------|--------|-------|-------|\n"
                    for prop in instance_props:
                        type_name = prop[0]
                        if is_invalid_type(type_name, known_wrappers, known_enums):
                            type_name += " (invalid)"
                        env, obj, owner, scope = format_access(prop[2])
                        docs += f"| `{prop[1]}` | `{sanitize_name(type_name)}` | `{env}` | `{obj}` | `{owner}` | `{scope}` |\n"
                if instance_funcs:
                    docs += "#### Instance Functions\n"
                    docs += "| Name | Return Type | Environment | Object | Owner | Scope |\n"
                    docs += "|------|-------------|-------------|--------|-------|-------|\n"
                    for func in instance_funcs:
                        type_name = func[0]
                        if is_invalid_type(type_name, known_wrappers, known_enums):
                            type_name += " (invalid)"
                        env, obj, owner, scope = format_access(func[2])
                        docs += f"| `{func[1]}` | `{sanitize_name(type_name)}` | `{env}` | `{obj}` | `{owner}` | `{scope}` |\n"

            if struct_file:
                struct_props, struct_funcs, _, _ = parse_wrapper(struct_file)
                if struct_props or struct_funcs:
                    docs += "#### Struct\n"
                    docs += "| Name | Return Type | Environment | Object | Owner | Scope |\n"
                    docs += "|------|-------------|-------------|--------|-------|-------|\n"
                    for prop in struct_props:
                        type_name = prop[0]
                        if is_invalid_type(type_name, known_wrappers, known_enums):
                            type_name += " (invalid)"
                        env, obj, owner, scope = format_access(prop[2])
                        docs += f"| `{prop[1]}` | `{sanitize_name(type_name)}` | `{env}` | `{obj}` | `{owner}` | `{scope}` |\n"
                    for func in struct_funcs:
                        type_name = func[0]
                        if is_invalid_type(type_name, known_wrappers, known_enums):
                            type_name += " (invalid)"
                        env, obj, owner, scope = format_access(func[2])
                        docs += f"| `{func[1]}` | `{sanitize_name(type_name)}` | `{env}` | `{obj}` | `{owner}` | `{scope}` |\n"

        docs += "\n"

    with open("autogenerated_docs.md", "w") as output_file:
        output_file.write(toc + "\n" + docs)

    log("Documentation generation complete")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_docs.py <common_folder>")
        sys.exit(1)

    common_folder_path = sys.argv[1]
    generate_docs(common_folder_path)
