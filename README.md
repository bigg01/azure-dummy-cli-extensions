# azure-dummy-cli-extensions

## build
```sh
python setup.py bdist_wheel
```
## add extension
```sh
az extension add --source dist/tipsextension-0.0.1-py2.py3-none-any.whl                                  
Are you sure you want to install this extension? (y/n): y
The extension is invalid. Use --debug for more information.
```
##run command
```sh
az gimme -h

Group
    az gimme

Commands:
    tips : Points you to a world of Azure Tips and Tricks.

For more specific examples, use: az find "az gimme"

Please let us know how we are doing: https://aka.ms/azureclihats
```

## find cli extensions location 
```sh
file $HOME/.azure/cliextensions/tipsextension/tipsextension-0.0.1-py2.py3-none-any.whl
```

ref: https://microsoft.github.io/AzureTipsAndTricks/blog/tip200.html