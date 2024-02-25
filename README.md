# python-workspace

Python workspace for experiments and tutorials.

## Topics

A "topic" may span more than one module.

### Dependencies

To install Python dependencies:

```bash { bacground=false category=dependency closeTerminalOnSuccess=false excludeFromRunAll=true interactive=true interpreter=bash name=install-dep-all promptEnv=true terminalRows=10 }
# Install/Update all project dependencies.

declare -a rf=( requirements-*.txt )

# don't quote the array, both the flag and file name will be treated as a single argument
echo Running: pip install --upgrade ${rf[@]//requirements-/--requirement requirements-}
time pip install --upgrade ${rf[@]//requirements-/--requirement requirements-}
```
